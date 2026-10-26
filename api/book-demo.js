/**
 * POST /api/book-demo: the contact.html form. Validates on the server against the same option
 * lists as the form, saves an fcg_website.leads row, then mirrors it to Lark (Base row + card).
 * The visitor sees success only after the Supabase insert.
 */
const lib = require("./_lib.js");

const PAGE_RE = /^\/contact(\.html)?(\?product=[a-z-]+)?$/; // the only page with this form; nothing else is echoed into Lark

function validate(b) {
  const v = {
    firstname: lib.str(b.firstname, 100), lastname: lib.str(b.lastname, 100), email: lib.str(b.email, 254),
    company: lib.str(b.company), jobtitle: lib.str(b.jobtitle), companyType: lib.str(b.companyType),
    region: lib.str(b.region), product: lib.str(b.product), message: lib.str(b.message, 2000),
  };
  if (lib.str(b.website)) return { bot: true }; // honeypot
  for (const k of ["firstname", "lastname", "company", "jobtitle"]) if (!v[k]) return { error: "Please fill in every required field." };
  if (!lib.EMAIL_RE.test(v.email)) return { error: "Please enter a valid work email." };
  for (const k of ["companyType", "region", "product"]) if (!lib.OPTIONS[k].includes(v[k])) return { error: "Please choose an option from each list." };
  const page = lib.str(b.page);
  v.page = lib.SITE + (PAGE_RE.test(page) ? page : "/contact.html");
  return { value: v };
}

const deps = { insertRow: lib.insertRow, mirrorToLark: lib.mirrorToLark };

async function handler(req, res) {
  if (req.method !== "POST") return res.status(405).json({ error: "Method not allowed." });
  if (lib.rateLimited(req, "book-demo")) {
    return res.status(429).json({ error: "Too many requests from your network. Please try again in a few minutes, or email hello@fusionconnectgroup.com." });
  }
  const { value: v, error, bot } = validate(req.body && typeof req.body === "object" ? req.body : {});
  if (bot) return res.status(200).json({ ok: true }); // tell a bot nothing
  if (error) return res.status(400).json({ error });
  try {
    const row = {
      form: "book_demo", page_uri: v.page, name: `${v.firstname} ${v.lastname}`, email: v.email.toLowerCase(),
      company: v.company, job_title: v.jobtitle, message: v.message || null,
      details: { company_type: v.companyType, region: v.region, product: v.product },
    };
    const id = await deps.insertRow("leads", row);
    const shownId = id || "unconfirmed (see function logs)";
    await deps.mirrorToLark({
      title: "New FCG demo request",
      tableEnv: "LARK_LEADS_DEMO_TABLE_ID",
      fields: { Name: row.name, Email: row.email, Company: row.company, "Job title": row.job_title, "Company type": v.companyType,
        Region: v.region, Product: v.product, Message: row.message || "", Page: row.page_uri, "Submitted at": Date.now(), "Supabase id": shownId },
      lines: [
        `**Name:** ${lib.escMd(row.name)}`, `**Email:** ${lib.escMd(row.email)}`, `**Company:** ${lib.escMd(row.company)}`,
        `**Job title:** ${lib.escMd(row.job_title)}`, `**Company type:** ${lib.escMd(v.companyType)}`, `**Region:** ${lib.escMd(v.region)}`,
        `**Product:** ${lib.escMd(v.product)}`,
        ...(row.message ? [`**Message:** ${lib.escMd([...row.message].slice(0, 500).join(""))}`] : []),
        `**Supabase id:** ${shownId}`,
      ],
    });
    return res.status(200).json({ ok: true });
  } catch (e) {
    console.error("[book-demo] request.failed", { error: e.message });
    return res.status(502).json({ error: "We couldn't send your request. Please try again or email hello@fusionconnectgroup.com." });
  }
}

module.exports = handler;
module.exports.deps = deps;
module.exports.validate = validate;
