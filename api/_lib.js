/**
 * Shared code for the two form endpoints (api/book-demo.js, api/subscribe.js).
 * Ported from accomy.com (accomy-astro/src/lib/server/*.ts): the Supabase insert is the write
 * that must succeed; the Lark Base row and chat card are a best-effort copy for the team.
 * FCG keeps its own schema, Base tables and chat, so FCG leads never land in Accomy's pipeline.
 * Files starting with "_" are not routes on Vercel.
 */
const FEISHU = "https://open.feishu.cn";
const SITE = "https://www.fusionconnectgroup.com";

// Same lists as the <select>s in contact.html (tools/test-forms.js fails if they drift).
const OPTIONS = {
  companyType: ["Travel management company (TMC)", "Online travel agency (OTA)", "Travel agency", "Corporate travel team",
    "Airline, hotel or supplier", "Developer or technology partner", "Other"],
  region: ["Greater China", "Southeast Asia", "Japan and Korea", "South Asia", "Middle East", "Europe", "Americas", "Other"],
  product: ["corporate-booking-tool", "ai-booking-tool", "agreeease", "atlas", "glink", "flink", "addn", "payment", "developer", "not-sure"],
};
const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

const str = (v, max = 200) => (typeof v === "string" ? v.trim().slice(0, max) : "");

// ---------- rate limit ----------
// ponytail: in-memory per warm instance, caps a burst from one client, not a distributed flood.
// Durable fix: a Vercel Firewall rate-limit rule on /api/*.
const hits = new Map();
const RATE_LIMIT = { limit: 8, windowMs: 10 * 60 * 1000 };
function rateLimited(req, route, now = Date.now()) {
  const ip = String(req.headers["x-forwarded-for"] || "").split(",")[0].trim();
  if (!ip) return false;
  const key = `${route}:${ip}`;
  const recent = (hits.get(key) || []).filter((t) => now - t < RATE_LIMIT.windowMs);
  const limited = recent.length >= RATE_LIMIT.limit;
  if (!limited) recent.push(now);
  hits.set(key, recent);
  if (hits.size > 5000) for (const [k, ts] of hits) if (!ts.some((t) => now - t < RATE_LIMIT.windowMs)) hits.delete(k);
  return limited;
}

// ---------- Supabase (PostgREST, plain fetch) ----------
async function insertRow(table, row, env = process.env, fetchImpl = fetch) {
  const { SUPABASE_URL: url, SUPABASE_SECRET_KEY: key } = env;
  if (!url || !key) throw new Error("SUPABASE_URL/SUPABASE_SECRET_KEY missing");
  const res = await fetchImpl(`${url}/rest/v1/${table}`, {
    method: "POST",
    headers: {
      apikey: key, Authorization: `Bearer ${key}`, "Content-Type": "application/json",
      "Content-Profile": env.FCG_DB_SCHEMA || "fcg_website", Prefer: "return=representation",
    },
    body: JSON.stringify(row),
    signal: AbortSignal.timeout(4000),
  });
  const text = await res.text().catch(() => "");
  // Only the email unique index means "already subscribed"; any other conflict must surface.
  if (res.status === 409 && text.includes("subscribers_email_key")) return null;
  if (!res.ok) throw new Error(`Supabase insert failed (${res.status}): ${text.slice(0, 300)}`);
  try {
    return JSON.parse(text)[0].id || "";
  } catch {
    console.error("[forms] insert.unconfirmed", { table, status: res.status });
    return ""; // committed but no readable id: still a success for the visitor
  }
}

// ---------- Lark (Feishu open API) ----------
let token = null;
async function tenantToken(env, fetchImpl) {
  if (token && token.expiresAt > Date.now()) return token.value;
  const res = await fetchImpl(`${FEISHU}/open-apis/auth/v3/tenant_access_token/internal`, {
    method: "POST", headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ app_id: env.LARK_APP_ID, app_secret: env.LARK_APP_SECRET }),
    signal: AbortSignal.timeout(2500),
  });
  const data = await res.json();
  if (!res.ok || data.code !== 0 || !data.tenant_access_token) throw new Error(`Lark token error ${data.code}: ${data.msg}`);
  token = { value: data.tenant_access_token, expiresAt: Date.now() + Math.max((data.expire || 0) * 1000 - 60000, 0) };
  return token.value;
}

async function larkPost(path, body, env, fetchImpl) {
  const t = await tenantToken(env, fetchImpl);
  const res = await fetchImpl(`${FEISHU}${path}`, {
    method: "POST", headers: { Authorization: `Bearer ${t}`, "Content-Type": "application/json" },
    body: JSON.stringify(body), signal: AbortSignal.timeout(2500),
  });
  const data = await res.json().catch(() => ({}));
  // A 91403 on the Base write means the app is not a collaborator on that Base (document ACL), not a missing scope.
  if (!res.ok || data.code !== 0) throw new Error(`Lark ${path} error ${res.status}/${data.code}: ${data.msg}`);
}

/** Collapse newlines (a value must never start a new lark_md line), drop < > so no <at> tag can ping the chat, escape markdown. */
const escMd = (v) => String(v).replace(/[\r\n]+/g, " ").replace(/[<>]/g, "").replace(/[\\`*_~[\]()|]/g, (c) => `\\${c}`);

/**
 * Best-effort copy to a Base table and a chat card. Never throws; the two writes are separate
 * failure domains so one failing does not swallow the other. Awaited by callers on purpose:
 * Vercel may stop un-awaited work after the response is sent.
 */
async function mirrorToLark({ title, tableEnv, fields, lines }, env = process.env, fetchImpl = fetch) {
  if (!env.LARK_APP_ID || !env.LARK_APP_SECRET) return console.error("[forms] lark config missing");
  const base = async () => {
    try {
      const app = env.LARK_LEADS_BASE_APP_TOKEN, table = env[tableEnv];
      if (!app || !table) return console.error("[forms] lark.base.skipped", { reason: `missing base token or ${tableEnv}` });
      await larkPost(`/open-apis/bitable/v1/apps/${encodeURIComponent(app)}/tables/${encodeURIComponent(table)}/records`, { fields }, env, fetchImpl);
    } catch (e) { console.error("[forms] lark.base.failed", { error: e.message }); }
  };
  const card = async () => {
    try {
      if (!env.LARK_LEADS_CHAT_ID) return console.error("[forms] LARK_LEADS_CHAT_ID missing");
      const content = { config: { wide_screen_mode: true }, header: { title: { tag: "plain_text", content: title }, template: "orange" },
        elements: [{ tag: "div", text: { tag: "lark_md", content: lines.join("\n") } }] };
      await larkPost("/open-apis/im/v1/messages?receive_id_type=chat_id",
        { receive_id: env.LARK_LEADS_CHAT_ID, msg_type: "interactive", content: JSON.stringify(content) }, env, fetchImpl);
    } catch (e) { console.error("[forms] lark.card.failed", { error: e.message }); }
  };
  await Promise.all([base(), card()]);
}

module.exports = { SITE, OPTIONS, EMAIL_RE, str, rateLimited, insertRow, mirrorToLark, escMd, RATE_LIMIT };
