#!/usr/bin/env python3
"""
Build the side-by-side approval page: today's console against the redesign.

One self-contained HTML file with every screenshot inlined as base64, so it can
be hosted or emailed as a single attachment with nothing to load.

    python3 build-compare.py

Screens are captured at 1440x1000, first viewport only, because the real console
scrolls inside its own pane rather than the page.

ponytail: no framework, no image host, two tabs and a <details>-free toggle.
"""

import base64
from pathlib import Path

HERE = Path(__file__).parent
JPG = HERE / "jpg"
OUT = HERE / "console-redesign-review.html"

# tab, (today's file, redesign file, screen name, what changed)
SCREENS = [
    ("dev", "console", "new-index", "Console", "The orange banner and rocket go. Empty states become the design, since a new developer sees nothing else for their first hour."),
    ("dev", "getting-started", "new-getting-started", "Getting Started", "Same five-step debug flow, rebuilt on the brand's panels and mono type. Credentials stay masked until revealed."),
    ("dev", "app-management", "new-app-management", "App Management", "Three products, three credential sets, one card each. Production access is a link, not a coloured button."),
    ("dev", "sandbox", "new-sandbox", "Sandbox Environment", "Status moves into chips. The empty test log gains a route into Getting Started."),
    ("dev", "trace", "new-trace", "Request Trace", "Nine filters in one pill row, four counters above the table, and an empty state that says what fills it."),
    ("dev", "coverage", "new-coverage", "Coverage Map", "Density legend keeps the three bands. Counters carry the catalogue state."),
    ("dev", "hotel-mapping", "new-hotel-mapping", "Hotel Mapping", "The three-step CSV pipeline reads as three steps. Batch history keeps its columns."),
    ("dev", "hotel-orders", "new-hotel-orders", "Hotel Orders", "Sandbox and production as a segmented control rather than two buttons."),
    ("dev", "flight-orders", "new-flight-orders", "Flight Orders", "Same columns, same environment switch, brand table."),
    ("dev", "tmc-builder", "new-tmc-builder", "Build My TMC", "The four white-label templates become four selectable cards instead of one button."),
    ("dev", "sdk-assistant", "new-sdk", "SDK", "Eight SDKs as one sortable table rather than eight stacked cards. Install command stays copyable."),
    ("dev", "skills", "new-skills", "Skills", "Three packages, install command in the terminal block, tool support stated once."),
    ("dev", "ai-assistant", "new-ai-assistant", "AI Assistant", "Conversation list beside the thread. The floating orange bubble is gone."),
    ("dev", "tickets", "new-tickets", "My Tickets", "Counters, status chips, and an empty state that explains when to raise one."),
    ("admin", "adm-dashboard", "new-admin-dashboard", "Dashboard", "The blue-to-orange gradient banner goes. Charts are orange on white; the donut no longer reads 'No data 100%'."),
    ("admin", "adm-user-list", "new-admin-user-list", "User List", "Onboarding and access state as chips, so a pending account is findable down a 60-row list."),
    ("admin", "adm-app-review", "new-admin-app-review", "App Review", "Six state counts as one strip. 122 requests, same columns, same actions."),
    ("admin", "adm-ticket-list", "new-admin-ticket-list", "Ticket List", "Response-time counter added. Status chips replace coloured text."),
    ("admin", "adm-trace", "new-admin-trace", "Request Trace", "The admin view of the same table: developer account filter, latency band, export."),
    ("admin", "adm-sdk-management", "new-admin-sdk-management", "SDK Management", "Publish, version and retire in one row per package."),
    ("admin", "adm-docs-management", "new-admin-docs-management", "Docs Management", "Swagger versions and guide pages as two counts on one table."),
]


def b64(name):
    f = JPG / f"{name}.jpg"
    if not f.exists():
        raise SystemExit(f"missing screenshot: {f}")
    return "data:image/jpeg;base64," + base64.b64encode(f.read_bytes()).decode()


def rows(tab):
    out = []
    for i, (t, old, new, title, note) in enumerate([s for s in SCREENS if s[0] == tab], 1):
        out.append(f"""    <section class="row" id="{tab}-{i}">
      <div class="row-h">
        <span class="num">{i:02d}</span>
        <div><h3>{title}</h3><p>{note}</p></div>
      </div>
      <div class="pair">
        <figure><figcaption><span class="tag tag--old">Today</span></figcaption>
          <img loading="lazy" src="{b64(old)}" alt="{title}, the console today"></figure>
        <figure><figcaption><span class="tag tag--new">Proposed</span></figcaption>
          <img loading="lazy" src="{b64(new)}" alt="{title}, redesigned"></figure>
      </div>
    </section>""")
    return "\n".join(out)


def nav(tab):
    items = [s for s in SCREENS if s[0] == tab]
    return "".join(f'<a href="#{tab}-{i}">{s[3]}</a>' for i, s in enumerate(items, 1))


HTML = f"""<!DOCTYPE html>
<html lang="en-GB"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Open Developer Platform — console redesign for review</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
:root{{--ink:#0F1114;--muted:#6B7280;--muted-card:#5A6069;--card:#F3F4F6;--line:#D1D5DB;
 --hair:rgba(15,17,20,.08);--shell:rgba(15,17,20,.04);--accent:#F97316;--accent-ink:#EA580C;
 --sans:"Inter",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
 --mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;}}
*{{margin:0;padding:0;box-sizing:border-box}}
html{{scroll-behavior:smooth;scroll-padding-top:132px}}
body{{font-family:var(--sans);color:var(--ink);background:#fff;-webkit-font-smoothing:antialiased}}
img{{max-width:100%;display:block}}
a{{color:inherit;text-decoration:none}}
.wrap{{max-width:1560px;margin:0 auto;padding:0 32px}}

header{{padding:52px 0 30px}}
.eyebrow{{display:flex;align-items:center;gap:10px;font-size:11px;font-weight:500;letter-spacing:.18em;
 text-transform:uppercase;color:var(--accent-ink);margin-bottom:18px}}
.eyebrow::before{{content:"";width:12px;height:1.5px;background:currentColor}}
h1{{font-size:clamp(32px,4vw,54px);font-weight:500;letter-spacing:-.032em;line-height:1.04;max-width:20ch}}
.lede{{font-size:16.5px;line-height:27px;color:var(--muted);max-width:70ch;margin-top:18px}}
.meta{{display:flex;flex-wrap:wrap;gap:10px;margin-top:24px}}
.chip{{display:inline-flex;align-items:center;gap:8px;height:30px;padding:0 14px;border:1px solid var(--line);
 border-radius:999px;font-size:12.5px;color:var(--muted-card)}}
.chip b{{color:var(--ink);font-weight:500}}

.bar{{position:sticky;top:0;z-index:30;background:rgba(255,255,255,.92);
 backdrop-filter:saturate(180%) blur(10px);border-bottom:1px solid var(--hair)}}
.bar-in{{display:flex;align-items:center;gap:18px;padding:12px 32px;max-width:1560px;margin:0 auto;flex-wrap:wrap}}
.tabs{{display:flex;gap:3px;padding:3px;background:var(--shell);border:1px solid var(--hair);border-radius:999px}}
.tabs button{{height:38px;padding:0 22px;border:0;border-radius:999px;background:transparent;cursor:pointer;
 font:inherit;font-size:14px;color:var(--ink);display:inline-flex;align-items:center;gap:9px;
 transition:background 160ms ease}}
.tabs button .n{{font-family:var(--mono);font-size:11px;color:var(--muted)}}
.tabs button:hover{{background:#fff}}
.tabs button[aria-selected="true"]{{background:#fff;font-weight:500}}
.tabs button[aria-selected="true"] .n{{color:var(--ink)}}
.jump{{display:flex;gap:14px;overflow-x:auto;scrollbar-width:none;font-size:12.5px;color:var(--muted);
 padding:2px 0;flex:1 1 320px;min-width:0}}
.jump::-webkit-scrollbar{{height:0}}
.jump a{{white-space:nowrap;padding-bottom:2px;border-bottom:1px solid transparent}}
.jump a:hover{{color:var(--ink);border-bottom-color:var(--line)}}

.row{{padding:44px 0;border-top:1px solid var(--hair)}}
.row-h{{display:flex;gap:16px;align-items:flex-start;margin-bottom:22px;max-width:96ch}}
.num{{font-family:var(--mono);font-size:11px;color:var(--muted);padding-top:5px;flex:none}}
.row-h h3{{font-size:21px;font-weight:500;letter-spacing:-.02em}}
.row-h p{{font-size:14px;line-height:23px;color:var(--muted);margin-top:7px}}
.pair{{display:grid;grid-template-columns:1fr 1fr;gap:20px}}
figure{{min-width:0}}
figcaption{{margin-bottom:10px}}
.tag{{display:inline-flex;align-items:center;gap:8px;height:26px;padding:0 13px;border-radius:999px;
 font-size:11px;font-weight:500;letter-spacing:.14em;text-transform:uppercase}}
.tag--old{{background:var(--card);color:var(--muted-card)}}
.tag--new{{background:#111;color:#fff}}
figure img{{border:1px solid var(--line);border-radius:14px;width:100%}}

footer{{padding:56px 0 80px;border-top:1px solid var(--hair);margin-top:20px}}
footer p{{font-size:13.5px;line-height:23px;color:var(--muted);max-width:80ch}}
footer b{{color:var(--ink);font-weight:500}}
.hide{{display:none}}
@media (max-width:1080px){{ .pair{{grid-template-columns:1fr}} .wrap,.bar-in{{padding-left:20px;padding-right:20px}} }}
</style></head>
<body>

<div class="wrap"><header>
  <p class="eyebrow">Open Developer Platform</p>
  <h1>The signed-in console, today and proposed</h1>
  <p class="lede">Every screen behind the login, captured from the live platform on 8 September 2026 and
  rebuilt in the FCG brand. Nothing has been removed: same routes, same columns, same filters, same
  actions. What changes is how it looks and how the empty and failure states read.</p>
  <div class="meta">
    <span class="chip"><b>21</b> screens</span>
    <span class="chip"><b>14</b> developer view</span>
    <span class="chip"><b>7</b> platform admin</span>
    <span class="chip">Captured at <b>1440&times;1000</b></span>
    <span class="chip">English only, for now</span>
  </div>
</header></div>

<div class="bar"><div class="bar-in">
  <div class="tabs" role="tablist">
    <button role="tab" aria-selected="true" data-tab="dev">Developer view <span class="n">14</span></button>
    <button role="tab" aria-selected="false" data-tab="admin">Platform admin <span class="n">7</span></button>
  </div>
  <nav class="jump" id="jump-dev">{nav("dev")}</nav>
  <nav class="jump hide" id="jump-admin">{nav("admin")}</nav>
</div></div>

<div class="wrap">
  <div id="panel-dev">
{rows("dev")}
  </div>
  <div id="panel-admin" class="hide">
{rows("admin")}
  </div>

  <footer>
    <p><b>What is not settled.</b> The console is English only; the Simplified and Traditional Chinese
    editions follow once the design is approved. Small orange labels sit at 3.56:1, below the 4.5:1
    accessibility threshold, which is a recorded brand decision rather than an oversight. Admin rows are
    sample data.</p>
    <p style="margin-top:14px"><b>How to give feedback.</b> Quote the screen number and the view, for
    example &ldquo;admin 03&rdquo;, so a comment lands on one screen rather than the set.</p>
  </footer>
</div>

<script>
(function(){{
  var btns = document.querySelectorAll('.tabs button');
  btns.forEach(function(b){{
    b.addEventListener('click', function(){{
      var t = b.dataset.tab;
      btns.forEach(function(o){{ o.setAttribute('aria-selected', String(o === b)); }});
      ['dev','admin'].forEach(function(k){{
        document.getElementById('panel-' + k).classList.toggle('hide', k !== t);
        document.getElementById('jump-' + k).classList.toggle('hide', k !== t);
      }});
      window.scrollTo({{top: 0, behavior: 'instant'}});
    }});
  }});
}})();
</script>
</body></html>
"""

OUT.write_text(HTML, encoding="utf-8")
print(f"{OUT.name}  {OUT.stat().st_size/1048576:.1f} MB  ({len(SCREENS)} screens)")
