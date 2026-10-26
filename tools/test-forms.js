// node --test tools/test-forms.js : the two form endpoints, with Supabase and Lark mocked out.
const test = require("node:test");
const assert = require("node:assert");
const fs = require("node:fs");
const path = require("node:path");
const lib = require("../api/_lib.js");
const demo = require("../api/book-demo.js");
const sub = require("../api/subscribe.js");

function call(handler, body, headers = {}) {
  return new Promise((resolve) => {
    const res = { status(c) { this.code = c; return this; }, json(b) { resolve({ code: this.code, body: b }); } };
    handler({ method: "POST", headers, body }, res);
  });
}
const good = { firstname: "Ada", lastname: "Lim", email: "Ada@Example.com", company: "Acme Travel", jobtitle: "Head of Ops",
  companyType: "Travel agency", region: "Southeast Asia", product: "atlas", message: "Hi", page: "/contact.html?product=atlas", website: "" };

test("form option lists match contact.html", () => {
  const html = fs.readFileSync(path.join(__dirname, "..", "contact.html"), "utf8");
  for (const [name, values] of Object.entries(lib.OPTIONS)) {
    const block = html.match(new RegExp(`name="${name}"[^>]*>([\\s\\S]*?)</select>`))[1];
    const opts = [...block.matchAll(/<option(?: value="([^"]*)")?>([^<]*)</g)].map((m) => m[1] ?? m[2]).filter(Boolean);
    assert.deepStrictEqual(opts, values, name);
  }
});

test("book-demo saves first, then mirrors, and lowercases the email", async () => {
  const calls = [];
  demo.deps.insertRow = async (t, row) => { calls.push(["insert", t, row]); return "id-1"; };
  demo.deps.mirrorToLark = async (m) => { calls.push(["mirror", m]); };
  const r = await call(demo, good);
  assert.strictEqual(r.code, 200);
  assert.deepStrictEqual(calls.map((c) => c[0]), ["insert", "mirror"]);
  assert.strictEqual(calls[0][2].email, "ada@example.com");
  assert.strictEqual(calls[0][2].page_uri, "https://www.fusionconnectgroup.com/contact.html?product=atlas");
  assert.match(calls[1][1].lines.join("\n"), /id-1/);
});

test("book-demo rejects honeypot, off-list values, bad email and a foreign page", async () => {
  demo.deps.insertRow = async () => assert.fail("must not insert");
  assert.strictEqual((await call(demo, { ...good, website: "x" })).code, 200, "honeypot answers like success");
  for (const bad of [{ product: "spam" }, { email: "nope" }, { firstname: "" }]) {
    assert.strictEqual((await call(demo, { ...good, ...bad })).code, 400, JSON.stringify(bad));
  }
  assert.strictEqual(demo.validate({ ...good, page: "/x\n**evil**" }).value.page, "https://www.fusionconnectgroup.com/contact.html");
  assert.strictEqual(demo.validate({ ...good, page: "\n/contact.html" }).value.page, "https://www.fusionconnectgroup.com/contact.html");
  assert.strictEqual(lib.escMd("<at id=all></at> *x*"), "at id=all/at \\*x\\*");
});

test("book-demo returns 502 when the save fails, and never mirrors", async () => {
  demo.deps.insertRow = async () => { throw new Error("down"); };
  demo.deps.mirrorToLark = async () => assert.fail("must not mirror");
  const orig = console.error; console.error = () => {};
  assert.strictEqual((await call(demo, good)).code, 502);
  console.error = orig;
});

test("subscribe: new address mirrors, repeat address is a quiet 200", async () => {
  let mirrored = 0;
  sub.deps.mirrorToLark = async () => { mirrored++; };
  sub.deps.insertRow = async () => "id-2";
  assert.strictEqual((await call(sub, { email: "a@b.co", source: "blog_newsletter" })).code, 200);
  sub.deps.insertRow = async () => null;
  assert.strictEqual((await call(sub, { email: "a@b.co" })).code, 200);
  assert.strictEqual(mirrored, 1);
  assert.strictEqual((await call(sub, { email: "bad" })).code, 400);
});

test("insertRow maps the unique-email 409 to null and other errors to a throw", async () => {
  const env = { SUPABASE_URL: "https://x", SUPABASE_SECRET_KEY: "k" };
  const f = (status, text) => async () => ({ status, ok: status < 300, text: async () => text });
  assert.strictEqual(await lib.insertRow("subscribers", {}, env, f(409, 'duplicate key "subscribers_email_key"')), null);
  await assert.rejects(lib.insertRow("leads", {}, env, f(409, "other")));
  assert.strictEqual(await lib.insertRow("leads", {}, env, f(201, '[{"id":"z"}]')), "z");
});

test("rate limit: 8 per 10 minutes per address", () => {
  const req = { headers: { "x-forwarded-for": "9.9.9.9" } };
  for (let i = 0; i < lib.RATE_LIMIT.limit; i++) assert.strictEqual(lib.rateLimited(req, "t", 1000), false);
  assert.strictEqual(lib.rateLimited(req, "t", 1000), true);
});
