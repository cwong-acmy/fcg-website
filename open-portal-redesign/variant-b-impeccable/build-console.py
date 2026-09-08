#!/usr/bin/env python3
"""
Build the signed-in console screens in Direction B.

The console is the same design system as the twelve public pages, at app
density: sidebar instead of a marketing nav, 40px section gaps instead of 128px,
no scroll reveal. Tokens, wordmark and copy rules are lifted from build-pages.py
so nothing can drift between the public site and the console.

Screens mirror the real console captured on 8 September 2026 — same routes, same
groups, same columns. Dev screens render their real first-run state, which is
empty. Admin screens carry SYNTHETIC rows: no real developer, company, email or
phone from the live platform appears here.

ponytail: one CSS block, one shell function, no template engine.
Run:  python3 build-console.py
"""

import importlib.util
import re
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE / "console"

# build-pages.py is the token authority; a hyphen keeps it out of `import`.
_spec = importlib.util.spec_from_file_location("bp", HERE / "build-pages.py")
bp = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(bp)

ARROW = '<iconify-icon icon="solar:arrow-right-linear" aria-hidden="true"></iconify-icon>'

from console_nav import DEV_NAV, ADMIN_NAV  # noqa: F401

# ------------------------------------------------------------------ console CSS

CONSOLE_CSS = """<style>
/* ============================================================
   CONSOLE SHELL — the same tokens at app density.
   Sidebar + topbar + scrolling page. No scroll reveal: a screen
   opened forty times a day must not fade in.
   ============================================================ */
:root{
  /* Status is the one place the console needs colour the marketing site
     does not have. Desaturated so they read as state, never as brand, and
     all three clear 4.5:1 on white. Orange stays brand-only. */
  --ok:#1F7A5C;
  --warn:#946200;
  --bad:#B3261E;
  --side:252px;
}

body{overflow-x:visible}
.app{display:grid;grid-template-columns:var(--side) 1fr;min-height:100vh;align-items:start}

/* ---------- sidebar ---------- */
.side{position:sticky;top:0;height:100vh;overflow-y:auto;overscroll-behavior:contain;
  border-right:1px solid var(--line);background:#fff;padding:0 12px 32px;scrollbar-width:thin}
.side-brand{position:sticky;top:0;z-index:2;background:#fff;display:flex;align-items:center;gap:9px;
  height:64px;padding:0 8px;margin-bottom:14px;border-bottom:1px solid transparent}
.side-brand .sub{font-size:9.5px;font-weight:500;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);white-space:nowrap}
.side-brand .div{width:1px;height:16px;background:var(--line)}
.side-grp{margin-top:20px;padding:0 10px 8px;display:flex;align-items:center;gap:7px}
.side-grp span{font-size:9.5px;font-weight:600;letter-spacing:.18em;text-transform:uppercase;color:var(--muted-card)}
.side-grp i{display:block;width:10px;height:1.5px;background:var(--accent);flex:none}
.side a{display:flex;align-items:center;gap:10px;height:36px;padding:0 10px;border-radius:999px;
  font-size:13.5px;color:var(--ink);transition:background var(--hover) ease,transform var(--press) var(--ease-out)}
.side a iconify-icon{font-size:17px;color:var(--muted);flex:none}
.side a:active{transform:scale(.985)}
@media (hover:hover) and (pointer:fine){ .side a:hover{background:var(--shell)} }
.side a.on{background:var(--card);font-weight:500}
.side a.on iconify-icon{color:var(--ink)}
.side a .tag{margin-left:auto;font-family:var(--mono);font-size:10.5px;color:var(--muted)}
.side a.on .dot,.side a .dot{margin-left:auto}

/* ---------- topbar ---------- */
.main{min-width:0}
.top{position:sticky;top:0;z-index:20;display:flex;align-items:center;gap:16px;height:64px;padding:0 28px;
  background:rgba(255,255,255,.9);backdrop-filter:saturate(180%) blur(10px);border-bottom:1px solid var(--hair)}
.srch{flex:1 1 auto;max-width:520px;display:flex;align-items:center;gap:9px;height:36px;padding:0 14px;
  background:var(--shell);border:1px solid transparent;border-radius:999px;color:var(--muted);font-size:13.5px;
  transition:background var(--hover) ease,border-color var(--hover) ease}
@media (hover:hover) and (pointer:fine){ .srch:hover{background:#fff;border-color:var(--line)} }
.srch iconify-icon{font-size:16px}
.kbd{margin-left:auto;font-family:var(--mono);font-size:10.5px;letter-spacing:.04em;color:var(--muted);
  border:1px solid var(--line);border-radius:6px;padding:2px 6px;background:#fff}
.top-r{margin-left:auto;display:flex;align-items:center;gap:8px}
.iconbtn{display:inline-flex;align-items:center;justify-content:center;width:34px;height:34px;border:0;background:transparent;
  border-radius:999px;color:var(--ink);cursor:pointer;transition:background var(--hover) ease}
.iconbtn iconify-icon{font-size:18px}
@media (hover:hover) and (pointer:fine){ .iconbtn:hover{background:var(--shell)} }
.who{display:flex;align-items:center;gap:9px;height:34px;padding:0 12px 0 4px;border:1px solid var(--line);
  border-radius:999px;font-size:13px;background:#fff}
.who .av{width:24px;height:24px;border-radius:999px;background:var(--card);display:grid;place-items:center;
  font-size:10.5px;font-weight:600;letter-spacing:.02em;color:var(--ink)}
.who .role{font-family:var(--mono);font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}

/* ---------- page ---------- */
.page{padding:30px 28px 88px;max-width:1360px}
.phead{display:flex;flex-wrap:wrap;align-items:flex-end;gap:16px;margin-bottom:26px}
.phead-t{min-width:0;display:flex;flex-direction:column;gap:9px}
.phead h1{font-size:29px;font-weight:500;letter-spacing:-.028em;line-height:1.1}
.phead .lede{font-size:14.5px;line-height:23px;max-width:74ch}
.phead-a{margin-left:auto;display:flex;flex-wrap:wrap;gap:9px;align-items:center}
.pcrumb{display:flex;align-items:center;gap:8px;color:var(--muted);font-family:var(--mono);font-size:10.5px;
  letter-spacing:.14em;text-transform:uppercase;margin-bottom:14px}
.pcrumb i{font-style:normal;color:var(--line)}
.stack{display:flex;flex-direction:column;gap:20px}

/* ---------- panel ---------- */
.pnl{border:1px solid var(--line);border-radius:20px;background:#fff;overflow:hidden}
.pnl-h{display:flex;flex-wrap:wrap;align-items:center;gap:12px;padding:16px 20px;border-bottom:1px solid var(--hair)}
.pnl-h h2{font-size:14.5px;font-weight:500;letter-spacing:-.01em}
.pnl-h .sub{font-size:12.5px;color:var(--muted)}
.pnl-h .r{margin-left:auto;display:flex;align-items:center;gap:8px}
.pnl-b{padding:20px}
.pnl-b--flush{padding:0}

/* ---------- KPI tiles: value in ink, unit in orange (the site's statistic) ---------- */
.kpis{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px}
.kpi{border:1px solid var(--line);border-radius:18px;background:#fff;padding:17px 19px 19px;display:flex;flex-direction:column;gap:7px}
.kpi-k{display:flex;align-items:center;gap:8px;font-size:11px;font-weight:500;letter-spacing:.12em;
  text-transform:uppercase;color:var(--muted-card)}
.kpi-k iconify-icon{font-size:15px;color:var(--muted);margin-left:auto}
.kpi-v{font-size:34px;font-weight:500;letter-spacing:-.035em;line-height:1}
.kpi-v u{text-decoration:none;font-style:normal;color:var(--muted)}
/* one orange unit per row, on the tile that leads. Four orange units in a
   row of four tiles reads as a colour wash, which is what the accent law
   is there to prevent. */
.kpi--lead .kpi-v u{color:var(--accent)}
.kpi-f{font-size:12.5px;color:var(--muted)}

/* ---------- filter bar ---------- */
.fbar{display:flex;flex-wrap:wrap;gap:14px;align-items:flex-end;padding:18px 20px}
.fgrp{display:flex;flex-direction:column;gap:7px;min-width:0;flex:1 1 168px;max-width:230px}
.fgrp label{font-size:10px;font-weight:500;letter-spacing:.16em;text-transform:uppercase;color:var(--muted-card)}
.sel{appearance:none;-webkit-appearance:none;width:100%;height:38px;padding:0 34px 0 14px;font:inherit;font-size:13.5px;
  color:var(--ink);background:#fff;border:1px solid var(--line);border-radius:999px;cursor:pointer;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='none' stroke='%236B7280' stroke-width='1.4'><path d='M4 6.5 8 10.5 12 6.5'/></svg>");
  background-repeat:no-repeat;background-position:right 13px center;background-size:15px}
.fbar .rail{flex:0 0 auto;align-self:flex-end}
.fbar-a{margin-left:auto;display:flex;gap:9px;align-self:flex-end}

/* ---------- status ---------- */
.st{display:inline-flex;align-items:center;gap:7px;font-size:13px;white-space:nowrap}
.st b{width:6px;height:6px;border-radius:50%;background:var(--line);flex:none}
.st--ok b{background:var(--ok)}
.st--warn b{background:var(--warn)}
.st--bad b{background:var(--bad)}
.st--bad{color:var(--bad)}
.st--live b{background:var(--ok);box-shadow:0 0 0 3px rgba(31,122,92,.14)}
.pill{display:inline-flex;align-items:center;gap:7px;height:24px;padding:0 10px;border:1px solid var(--line);
  border-radius:999px;font-size:11.5px;color:var(--ink);background:#fff;white-space:nowrap}
.pill--q{background:var(--card);border-color:transparent;color:var(--muted-card)}
.pill b{width:6px;height:6px;border-radius:50%;background:var(--line);flex:none}
.pill--ok b{background:var(--ok)} .pill--warn b{background:var(--warn)} .pill--bad b{background:var(--bad)}

/* ---------- counts strip (All 122 / Pending 10 / …) ---------- */
.counts{display:flex;flex-wrap:wrap;gap:2px;padding:3px;background:var(--shell);border:1px solid var(--hair);
  border-radius:999px;overflow-x:auto;scrollbar-width:none}
.counts::-webkit-scrollbar{width:0;height:0}
.counts a{display:inline-flex;align-items:center;gap:8px;height:32px;padding:0 14px;border-radius:999px;
  font-size:13px;white-space:nowrap;transition:background var(--hover) ease}
.counts a .n{font-family:var(--mono);font-size:11px;color:var(--muted)}
@media (hover:hover) and (pointer:fine){ .counts a:hover{background:#fff} }
.counts a.on{background:#fff;font-weight:500}
.counts a.on .n{color:var(--ink)}

/* ---------- empty state: the console's most-seen screen ---------- */
.empty{display:flex;flex-direction:column;align-items:center;text-align:center;gap:9px;padding:54px 24px;
  background:var(--card);border-radius:16px;margin:20px}
.empty--flat{background:transparent;border:1px dashed var(--line)}
.empty iconify-icon{font-size:24px;color:var(--muted-card)}
.empty h3{font-size:14.5px;font-weight:500}
.empty p{font-size:13.5px;line-height:22px;color:var(--muted-card);max-width:52ch}
.empty .btn{margin-top:7px}

/* ---------- charts: ink first, one orange highlight, never a colour wheel ---------- */
.chart{width:100%;height:auto;display:block;overflow:visible}
.chart .grid{stroke:var(--hair);stroke-width:1}
.chart .bar{fill:var(--ink)}
.chart .bar--q{fill:#C9CDD3}
.chart .ln{fill:none;stroke:var(--ink);stroke-width:1.6;stroke-linejoin:round;stroke-linecap:round}
.chart .ln--q{stroke:#C9CDD3;stroke-dasharray:3 3}
.chart .area{fill:rgba(15,17,20,.05)}
.chart .pt{fill:var(--accent)}
.chart text{font-family:var(--mono);font-size:9px;fill:var(--muted);letter-spacing:.06em}
.legend{display:flex;flex-wrap:wrap;gap:16px;margin-top:12px}
.legend span{display:inline-flex;align-items:center;gap:7px;font-size:11.5px;color:var(--muted)}
.legend i{width:14px;height:2px;background:var(--ink);border-radius:2px}
.legend i.q{background:#C9CDD3}
.ring{display:flex;align-items:center;gap:22px;flex-wrap:wrap}
/* the ring is a fixed 128px dial; .chart{width:100%} would blow it up to the panel width */
.ring svg.chart{flex:none;width:128px;height:128px}
.ring .seg-a{stroke:var(--ink)}
.ring .seg-b{stroke:#C9CDD3}
.ring .seg-0{stroke:var(--card)}

/* ---------- ranking list ---------- */
.rank{display:flex;flex-direction:column}
.rank li{display:flex;align-items:center;gap:12px;padding:11px 20px;border-top:1px solid var(--hair-soft);font-size:13px}
.rank li:first-child{border-top:0}
.rank .i{font-family:var(--mono);font-size:11px;color:var(--muted);width:16px;flex:none}
.rank .p{font-family:var(--mono);font-size:12px;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.rank .v{margin-left:auto;font-family:var(--mono);font-size:12px;color:var(--muted-card);flex:none}
.rank .track{flex:0 0 96px;height:3px;border-radius:2px;background:var(--card);overflow:hidden}
.rank .track i{display:block;height:100%;background:var(--ink)}

/* ---------- console tables ---------- */
.pnl table.tbl th{background:#fff}
.pnl table.tbl td{font-size:13px;padding:13px 20px}
.pnl table.tbl th{padding:12px 20px}
.tfoot{display:flex;flex-wrap:wrap;align-items:center;gap:12px;padding:13px 20px;border-top:1px solid var(--hair);
  font-size:12.5px;color:var(--muted)}
.tfoot .r{margin-left:auto;display:flex;align-items:center;gap:8px}
.pg{display:flex;gap:2px;padding:3px;background:var(--shell);border-radius:999px}
.pg a{display:grid;place-items:center;min-width:28px;height:28px;padding:0 9px;border-radius:999px;font-size:12.5px;
  font-family:var(--mono)}
.pg a.on{background:#fff;color:var(--ink)}
.tact{display:flex;gap:14px;white-space:nowrap}
.tact a{font-size:12.5px;color:var(--ink);border-bottom:1px solid var(--line);padding-bottom:1px}
.tact a.q{color:var(--muted)}
@media (hover:hover) and (pointer:fine){ .tact a:hover{border-bottom-color:var(--ink)} }

/* ---------- two and three column layouts ---------- */
.g2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px}
.g3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}
.g-side{display:grid;grid-template-columns:minmax(0,340px) minmax(0,1fr);gap:20px;align-items:start}
.g-side--r{grid-template-columns:minmax(0,1fr) minmax(0,340px)}

/* ---------- step list (getting started) ---------- */
.slist{display:flex;flex-direction:column;gap:8px;padding:20px}
.slist a{display:flex;align-items:center;gap:13px;padding:12px 14px;border:1px solid var(--line);border-radius:14px;
  transition:background var(--hover) ease,border-color var(--hover) ease}
@media (hover:hover) and (pointer:fine){ .slist a:hover{background:var(--card);border-color:var(--card)} }
.slist a.on{background:var(--card);border-color:transparent}
.slist .n{display:grid;place-items:center;width:26px;height:26px;border-radius:999px;border:1px solid var(--line);
  font-family:var(--mono);font-size:11.5px;color:var(--muted);flex:none;background:#fff}
.slist a.on .n{border-color:var(--ink);color:var(--ink)}
.slist a.done .n{background:var(--ink);border-color:var(--ink);color:#fff}
.slist .t{min-width:0}
.slist .t b{display:block;font-size:13.5px;font-weight:500}
.slist .t code{display:block;font-family:var(--mono);font-size:11.5px;color:var(--muted);overflow:hidden;
  text-overflow:ellipsis;white-space:nowrap}

/* ---------- progress ---------- */
.prog{height:4px;border-radius:2px;background:var(--card);overflow:hidden}
.prog i{display:block;height:100%;background:var(--ink);border-radius:2px}

/* ---------- code / request panes ---------- */
.pane{font-family:var(--mono);font-size:12px;line-height:20px;white-space:pre;overflow:auto;padding:16px 18px;
  background:var(--card);border-radius:14px;min-height:190px;color:var(--ink)}
.pane--q{color:var(--muted-card)}
.pane--dark{background:var(--dark);color:var(--dark-fg)}
.kv{display:flex;flex-direction:column}
.kv div{display:flex;gap:14px;align-items:baseline;padding:11px 0;border-top:1px solid var(--hair-soft)}
.kv div:first-child{border-top:0}
.kv .k{font-size:11px;font-weight:500;letter-spacing:.12em;text-transform:uppercase;color:var(--muted-card);flex:0 0 132px}
.kv .v{font-size:13px;min-width:0;overflow-wrap:anywhere}
.kv .v.mono{font-family:var(--mono);font-size:12px}

/* ---------- chat ---------- */
.conv{display:flex;flex-direction:column;gap:16px;padding:20px;min-height:320px}
.bub{max-width:74%;padding:13px 16px;border-radius:16px;font-size:13.5px;line-height:22px}
.bub--ai{background:var(--card);border-bottom-left-radius:6px}
.bub--me{margin-left:auto;background:var(--ink);color:#fff;border-bottom-right-radius:6px}
.composer{display:flex;gap:10px;align-items:center;padding:14px 20px;border-top:1px solid var(--hair)}
.composer input{flex:1;height:40px;padding:0 16px;font:inherit;font-size:13.5px;border:1px solid var(--line);
  border-radius:999px;background:#fff;color:var(--ink)}
.composer input::placeholder{color:var(--muted)}

/* ---------- responsive ---------- */
@media (max-width:1180px){ .kpis{grid-template-columns:repeat(2,minmax(0,1fr))} .g3{grid-template-columns:1fr} }
@media (max-width:1080px){ .g-side,.g-side--r{grid-template-columns:1fr} }
@media (max-width:900px){
  .app{grid-template-columns:1fr}
  .side{position:static;height:auto;border-right:0;border-bottom:1px solid var(--line);padding-bottom:18px}
  .side-brand{position:static}
  .g2{grid-template-columns:1fr}
  .page{padding:24px 18px 72px}
  .top{padding:0 18px}
  .srch{max-width:none}
}
@media (max-width:620px){ .kpis{grid-template-columns:1fr} .who .role{display:none} }
</style>"""

# ------------------------------------------------------------------- shell

PAGE = """<!DOCTYPE html>
{head}<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<script src="https://code.iconify.design/iconify-icon/1.0.7/iconify-icon.min.js"></script>
<script>document.documentElement.classList.add('js');</script>
{css}
{pagecss}
{consolecss}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{symbol}
<div class="app">
{side}
  <div class="main">
{top}
    <main class="page" id="main">
{body}
    </main>
  </div>
</div>
</body>
</html>
"""


def sidebar(nav, active, home):
    rows = []
    for group, items in nav:
        rows.append(f'    <p class="side-grp"><i aria-hidden="true"></i><span>{group}</span></p>')
        rows.append('    <nav aria-label="' + re.sub("&amp;", "and", group) + '">')
        for key, label, icon, href in items:
            on = ' class="on"' if key == active else ""
            cur = ' aria-current="page"' if key == active else ""
            tag = ' <span class="tag">0/5</span>' if key == "getting-started" else ""
            rows.append(
                f'      <a{on}{cur} href="{href}">'
                f'<iconify-icon icon="{icon}" aria-hidden="true"></iconify-icon>{label}{tag}</a>'
            )
        rows.append("    </nav>")
    body = "\n".join(rows)
    return f"""  <aside class="side">
    <a class="side-brand" href="{home}" aria-label="Open Developer Platform — console home">
      {bp.LOGO.format(h=22)}
      <span class="div" aria-hidden="true"></span>
      <span class="sub">Console</span>
    </a>
{body}
  </aside>"""


def topbar(who, initials, role):
    return f"""    <header class="top">
      <div class="srch" role="search">
        <iconify-icon icon="solar:magnifer-linear" aria-hidden="true"></iconify-icon>
        <span>Search screens, API docs, orders, tickets</span>
        <span class="kbd">Ctrl K</span>
      </div>
      <div class="top-r">
        <button class="iconbtn" type="button" aria-label="Notifications">
          <iconify-icon icon="solar:bell-linear" aria-hidden="true"></iconify-icon>
        </button>
        <button class="iconbtn" type="button" aria-label="Language: English">
          <iconify-icon icon="solar:global-linear" aria-hidden="true"></iconify-icon>
        </button>
        <span class="who"><span class="av" aria-hidden="true">{initials}</span>{who}<span class="role">{role}</span></span>
      </div>
    </header>"""


def build(slug, title, desc, body, nav, active, who, initials, role, home="../index.html"):
    html = PAGE.format(
        head=bp.HEAD_OPEN,
        title=title,
        desc=desc,
        css=bp.CSS,
        pagecss=bp.PAGE_CSS,
        consolecss=CONSOLE_CSS,
        symbol=bp.SYMBOL,
        side=sidebar(nav, active, home),
        top=topbar(who, initials, role),
        body=body.strip("\n"),
    )
    bp.check_h1_rule(html, slug)
    bp.check_em_rule(html, slug)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{slug}.html").write_text(html, encoding="utf-8")
    return len(html)


def contact_sheet(screens):
    """A flat list of every screen. The dev and admin sidebars cannot reach each
    other, so without this there is no way to review both sets in one sitting."""
    def col(title, rows):
        li = "\n".join(
            f'        <li><a href="{sl}.html">{ti.split(" — ")[0]}</a>'
            f'<span>{de}</span></li>' for sl, ti, de in rows)
        return f'      <div><p class="side-grp"><i></i><span>{title}</span></p>\n<ul class="sheet">\n{li}\n</ul></div>'

    dev = [(s["slug"], s["title"], s["desc"]) for s in screens if not s["slug"].startswith("admin-")]
    adm = [(s["slug"], s["title"], s["desc"]) for s in screens if s["slug"].startswith("admin-")]
    body = f"""      <div class="phead"><div class="phead-t">
        <h1>Console screens</h1>
        <p class="lede">Every screen in the signed-in console, in Direction B. Developer screens show their
        real first-run state, which is empty. Admin screens carry synthetic rows.</p>
      </div></div>
      <div class="g2">
{col("Developer view — 14 screens", dev)}
{col("Platform admin view — 7 screens", adm)}
      </div>"""
    extra = """<style>
.sheet{display:flex;flex-direction:column;border:1px solid var(--line);border-radius:20px;background:#fff;overflow:hidden}
.sheet li{display:flex;flex-direction:column;gap:3px;padding:14px 20px;border-top:1px solid var(--hair-soft)}
.sheet li:first-child{border-top:0}
.sheet a{font-size:14px;font-weight:500}
.sheet span{font-size:12.5px;color:var(--muted);line-height:19px}
</style>"""
    html = PAGE.format(head=bp.HEAD_OPEN, title="Console screens — Open Developer Platform",
                       desc="Contact sheet for the signed-in console screens.",
                       css=bp.CSS, pagecss=bp.PAGE_CSS, consolecss=CONSOLE_CSS + extra, symbol=bp.SYMBOL,
                       side="", top=topbar("review", "R", "Contact sheet"), body=body)
    html = html.replace('<div class="app">', '<div class="app" style="grid-template-columns:1fr">')
    (OUT / "_screens.html").write_text(html, encoding="utf-8")


if __name__ == "__main__":
    import console_content as cc

    total = 0
    for spec in cc.SCREENS:
        total += build(**spec)
    contact_sheet(cc.SCREENS)
    print(f"console: {len(cc.SCREENS)} screens  {total/1024:.0f} KB  →  {OUT.relative_to(HERE.parent)}")
    print("review them all from console/_screens.html")
