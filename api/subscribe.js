/**
 * POST /api/subscribe: the blog newsletter box. One fcg_website.subscribers row per address;
 * a repeat sign-up is a plain 200 with nothing stored or mirrored, so nobody can probe the list.
 *
 * ponytail: single opt-in. consent_at records the submission under the fine print on blog.html.
 * Add a confirmation email (double opt-in) before this list is ever mailed.
 */
const lib = require("./_lib.js");

const deps = { insertRow: lib.insertRow, mirrorToLark: lib.mirrorToLark };

async function handler(req, res) {
  if (req.method !== "POST") return res.status(405).json({ error: "Method not allowed." });
  if (lib.rateLimited(req, "subscribe")) return res.status(429).json({ error: "Too many sign-ups from your network. Please try again in a few minutes." });
  const b = req.body && typeof req.body === "object" ? req.body : {};
  const email = lib.str(b.email, 254).toLowerCase();
  if (lib.str(b.website)) return res.status(200).json({ ok: true }); // honeypot: tell a bot nothing
  if (!lib.EMAIL_RE.test(email)) return res.status(400).json({ error: "Enter a valid work email." });
  try {
    const row = { email, source: "blog_newsletter", page_uri: `${lib.SITE}/blog.html` };
    const id = await deps.insertRow("subscribers", row);
    if (id === null) return res.status(200).json({ ok: true }); // already subscribed
    const shownId = id || "unconfirmed (see function logs)";
    await deps.mirrorToLark({
      title: "New FCG newsletter subscriber",
      tableEnv: "LARK_LEADS_SUBSCRIBERS_TABLE_ID",
      fields: { Email: email, Source: row.source, Page: row.page_uri, "Submitted at": Date.now(), "Supabase id": shownId },
      lines: [`**Email:** ${lib.escMd(email)}`, `**Page:** ${lib.escMd(row.page_uri)}`, `**Supabase id:** ${shownId}`],
    });
    return res.status(200).json({ ok: true });
  } catch (e) {
    console.error("[subscribe] request.failed", { error: e.message });
    return res.status(502).json({ error: "We couldn't sign you up. Please try again or email hello@fusionconnectgroup.com." });
  }
}

module.exports = handler;
module.exports.deps = deps;
