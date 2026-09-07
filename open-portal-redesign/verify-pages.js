// Observation check for the Direction B portal pages.
//
// Attaches to the always-on Chrome for Testing on :9222 (never launches one),
// loads every page at 1280 and 375, forces the scroll-reveal animations to their
// end state so full-page captures are not blank, and asserts the brand rules that
// a screenshot alone will not tell you about.
//
// Usage: NODE_PATH=$(npm root -g) node verify-pages.js [pageName ...]

const puppeteer = require("puppeteer-core");
const path = require("path");

const DIR = path.join(__dirname, "variant-b-impeccable");
const OUT = path.join(__dirname, "shots", "b-pages");
const ALL = [
  "index", "app-management", "api-docs-hotel", "api-docs-hotel-process",
  "api-docs-hotel-apis", "api-docs-flink", "api-docs-errors", "sdk",
  "skills", "ai-assistant", "login", "register",
];

const pages = process.argv.slice(2).length ? process.argv.slice(2) : ALL;

function audit() {
  const surf = [], smallOrange = [], overlap = [], misalign = [], fonts = new Set();

  document.querySelectorAll("body *").forEach((e) => {
    const cs = getComputedStyle(e);
    // the accent must never be a surface: only dots, dashes, arcs, cursor, focus ring
    if (cs.backgroundColor === "rgb(249, 115, 22)") {
      const r = e.getBoundingClientRect();
      if (r.width > 16 || r.height > 16) surf.push(e.className || e.tagName);
    }
    // #F97316 on white is 2.80:1 — never legal below 18px
    if (cs.color === "rgb(249, 115, 22)" && parseFloat(cs.fontSize) < 18 && e.textContent.trim()) {
      smallOrange.push(e.tagName + "." + e.className);
    }
  });

  document
    .querySelectorAll("h1,h2,h3,h4,p,a,button,code,pre,td,th,li,label,input,select,span")
    .forEach((e) => fonts.add(getComputedStyle(e).fontFamily.split(",")[0].replace(/"/g, "")));

  // sibling boxes in a grid/flex track must not intersect
  document.querySelectorAll(".mini,.steps,.cards,.iopts,.fields--2").forEach((g) => {
    const k = [...g.children].map((x) => x.getBoundingClientRect());
    for (let i = 0; i < k.length; i++)
      for (let j = i + 1; j < k.length; j++)
        if (k[i].left < k[j].right - 1 && k[j].left < k[i].right - 1 &&
            k[i].top < k[j].bottom - 1 && k[j].top < k[i].bottom - 1)
          overlap.push(g.className);
  });

  // within one visual row of cards, the meta blocks must start at the same y
  document.querySelectorAll(".cards").forEach((g) => {
    const rows = {};
    [...g.children].forEach((c) => {
      const t = Math.round(c.getBoundingClientRect().top / 5) * 5;
      (rows[t] = rows[t] || []).push(c);
    });
    Object.values(rows).forEach((row) => {
      const ys = row
        .map((c) => c.querySelector(":scope > .card-meta"))
        .filter(Boolean)
        .map((x) => Math.round(x.getBoundingClientRect().top));
      if (ys.length > 1 && Math.max(...ys) - Math.min(...ys) > 2) misalign.push(JSON.stringify(ys));
    });
  });

  const hs = [...document.querySelectorAll("h1,h2,h3,h4,h5,h6")].map((e) => +e.tagName[1]);
  let skip = null;
  for (let i = 1; i < hs.length; i++)
    if (hs[i] - hs[i - 1] > 1) { skip = "h" + hs[i - 1] + "->h" + hs[i]; break; }

  return {
    sw: document.documentElement.scrollWidth,
    cw: document.documentElement.clientWidth,
    surf: [...new Set(surf)],
    smallOrange: [...new Set(smallOrange)],
    overlap: [...new Set(overlap)],
    misalign,
    skip,
    badFont: [...fonts].filter((f) => !["Inter", "ui-monospace", "Iconify"].includes(f)),
    h1: document.querySelectorAll("h1").length,
    deadHref: document.querySelectorAll('a[href="#"]').length,
  };
}

(async () => {
  const browser = await puppeteer.connect({ browserURL: "http://localhost:9222" });
  const page = await browser.newPage();
  const errors = [];
  page.on("pageerror", (e) => errors.push("pageerror: " + e.message));
  page.on("console", (m) => { if (m.type() === "error") errors.push("console: " + m.text()); });

  let failing = 0;
  for (const w of [1280, 375]) {
    await page.setViewport({ width: w, height: 900 });
    for (const name of pages) {
      // domcontentloaded, not networkidle2 — the Google Fonts / Iconify CDN stalls
      await page.goto("file://" + path.join(DIR, name + ".html"), {
        waitUntil: "domcontentloaded", timeout: 20000,
      });
      await page.evaluate(async () => {
        // force reveal animations to their end state, or a full-page shot comes out blank
        document.querySelectorAll(".rv").forEach((e) => {
          e.classList.add("in");
          e.style.transition = "none";
          e.style.opacity = 1;
          e.style.transform = "none";
        });
        try { await document.fonts.ready; } catch (_) {}
      });
      await new Promise((r) => setTimeout(r, 900));

      const m = await page.evaluate(audit);
      const f = [];
      if (m.sw > m.cw + 1) f.push(`H-SCROLL ${m.sw}>${m.cw}`);
      if (m.overlap.length) f.push("OVERLAP " + m.overlap);
      if (m.surf.length) f.push("ACCENT-SURFACE " + m.surf);
      if (m.smallOrange.length) f.push("SMALL-ORANGE " + m.smallOrange);
      if (m.badFont.length) f.push("FONT " + m.badFont);
      if (m.h1 !== 1) f.push("H1=" + m.h1);
      if (m.skip) f.push("HEADING-SKIP " + m.skip);
      if (m.deadHref) f.push("DEAD-HREF x" + m.deadHref);
      if (w === 1280 && m.misalign.length) f.push("META-MISALIGN " + m.misalign);

      if (f.length) failing++;
      console.log(`${w} ${name.padEnd(26)}${f.length ? " FAIL " + f.join(" | ") : " ok"}`);
      await page.screenshot({ path: path.join(OUT, `${name}-${w}.png`), fullPage: true });
    }
  }

  console.log(`\nJS errors: ${errors.length ? JSON.stringify([...new Set(errors)].slice(0, 6)) : "none"}`);
  console.log(`Failing checks: ${failing} / ${pages.length * 2}`);
  await page.close();
  browser.disconnect();
  process.exit(failing || errors.length ? 1 : 0);
})();
