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

# The globe on the Coverage Map is the marketing site's globe, not a new one:
# the Cobe library and its FCG configuration are lifted verbatim out of the
# repo-root index.html, the same way the CSS is lifted out of the portal donor.
# Marker colour there is already [0.97, 0.45, 0.09] — #F97316.
_SITE = HERE.parent.parent / "index.html"
_src = _SITE.read_text(encoding="utf-8")
_a = _src.index("var createGlobe=function(){")
_b = _src.index("</script>", _a)
GLOBE_LIB = "<script>\n" + _src[_a:_b].strip() + "\n</script>"
assert "createGlobe" in GLOBE_LIB and len(GLOBE_LIB) > 10000, "globe not found in the marketing index.html"


# ------------------------------------------------------------------ console CSS

CONSOLE_CSS = """<style>
/* ============================================================
   CONSOLE SHELL — the same tokens at app density.
   Sidebar + topbar + scrolling page. No scroll reveal: a screen
   opened forty times a day must not fade in.
   ============================================================ */
:root{
  /* Status colour, Stripe-bright. Two tokens per state, for the same reason
     --accent and --accent-ink are split: the DOT wants the vivid hue, the
     LABEL wants a hue you can actually read at 13px.
       dot  — vivid, no contrast requirement, it is a shape
       ink  — the same hue carried down to at least 4.5:1 on white
     Never fill a button or a panel with either. */
  --ok-bg:#CBF4C9;   --ok:#0E6245;     /* 6.07:1 on its own ground */
  --warn-bg:#F8E5B9; --warn:#983705;   /* 5.86:1 */
  --bad-bg:#FDE2DD;  --bad:#A41C4E;    /* 5.99:1 */
  --neu-bg:#E3E8EE;  --neu:#4F566B;    /* 5.93:1 */
  --info-bg:#D7EDFB; --info:#0B5A9E;   /* 5.86:1 — scope, environment, informational */
  --vio-bg:#E6E6FC;  --vio:#4B3FA8;    /* 6.63:1 — HTTP methods that write */
  --side:252px;
}

body{overflow-x:visible}
.app{display:grid;grid-template-columns:var(--side) 1fr;min-height:100vh;align-items:start}

/* ---------- sidebar ---------- */
.side{position:sticky;top:0;height:100vh;overflow-y:auto;overscroll-behavior:contain;
  border-right:1px solid var(--line);background:#fff;padding:0 12px 32px;scrollbar-width:thin}
.side-brand{position:sticky;top:0;z-index:2;background:#fff;display:flex;align-items:center;gap:9px;
  height:64px;padding:0 8px;margin-bottom:14px;border-bottom:1px solid transparent}
.side-brand .sub{font-size:10.5px;font-weight:500;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);white-space:nowrap}
.side-brand .div{width:1px;height:16px;background:var(--line)}
.side-grp{margin-top:20px;padding:0 10px 8px;display:flex;align-items:center;gap:7px}
.side-grp span{font-size:10.5px;font-weight:600;letter-spacing:.18em;text-transform:uppercase;color:var(--muted-card)}
.side-grp i{display:block;width:10px;height:1.5px;background:var(--accent);flex:none}
.side a{display:flex;align-items:center;gap:10px;height:36px;padding:0 10px;border-radius:999px;
  font-size:13.5px;color:var(--ink);transition:background var(--hover) ease,transform var(--press) var(--ease-out)}
.side a iconify-icon{font-size:17px;color:var(--muted);flex:none}
.side a:active{transform:scale(.985)}
@media (hover:hover) and (pointer:fine){ .side a:hover{background:var(--shell)} }
/* the current screen is the one place the sidebar earns colour: a light
   accent wash rather than the neutral --card fill, so it reads at a glance
   down a 16-item rail. Label stays ink; the wash carries the state. */
.side a.on{background:rgba(249,115,22,.11);font-weight:500}
.side a.on iconify-icon{color:var(--accent-ink)}
.side a .tag{margin-left:auto;font-family:var(--mono);font-size:10.5px;color:var(--muted)}
.side a.on .dot,.side a .dot{margin-left:auto}

/* ---------- topbar ---------- */
.main{min-width:0}
.top{position:sticky;top:0;z-index:20;display:flex;align-items:center;gap:16px;height:64px;padding:0 28px;
  background:rgba(255,255,255,.9);backdrop-filter:saturate(180%) blur(10px);border-bottom:1px solid var(--hair)}
.srch{flex:1 1 auto;min-width:0;max-width:520px;display:flex;align-items:center;gap:9px;height:36px;padding:0 14px;
  background:var(--shell);border:1px solid transparent;border-radius:999px;color:var(--muted);font-size:13.5px;
  transition:background var(--hover) ease,border-color var(--hover) ease}
@media (hover:hover) and (pointer:fine){ .srch:hover{background:#fff;border-color:var(--line)} }
.srch iconify-icon{font-size:16px;flex:none}
.srch span{min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
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
.stack{display:flex;flex-direction:column;gap:20px;min-width:0}
.stack > *{min-width:0}

/* ---------- panel ---------- */
.pnl{border:1px solid var(--line);border-radius:20px;background:#fff;overflow:hidden;
  display:flex;flex-direction:column}
.pnl-h{display:flex;flex-wrap:wrap;align-items:center;gap:12px;padding:16px 20px;border-bottom:1px solid var(--hair)}
.pnl-h h2{font-size:14.5px;font-weight:500;letter-spacing:-.01em}
.pnl-h .sub{font-size:12.5px;color:var(--muted)}
.pnl-h .r{margin-left:auto;display:flex;align-items:center;gap:8px;flex-wrap:wrap}
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
.kpi--lead .kpi-v u{color:var(--accent-ink)}
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
/* Status is a chip, not a dot beside grey text: a filled ground is findable
   in a hundred-row table in a way a 6px dot is not. Ground and label are a
   matched pair, every one of them above 5.8:1. */
.st{display:inline-flex;align-items:center;gap:6px;height:24px;padding:0 11px;border-radius:999px;
  font-size:12px;font-weight:500;letter-spacing:-.005em;white-space:nowrap;
  background:var(--neu-bg);color:var(--neu)}
.st b{width:5px;height:5px;border-radius:50%;background:currentColor;flex:none;opacity:.85}
.st--ok{background:var(--ok-bg);color:var(--ok)}
.st--warn{background:var(--warn-bg);color:var(--warn)}
.st--bad{background:var(--bad-bg);color:var(--bad)}
.st--live{background:var(--ok-bg);color:var(--ok)}
.st--info{background:var(--info-bg);color:var(--info)}
.st--vio{background:var(--vio-bg);color:var(--vio)}
.pill{display:inline-flex;align-items:center;gap:7px;height:24px;padding:0 10px;border:1px solid var(--line);
  border-radius:999px;font-size:11.5px;color:var(--ink);background:#fff;white-space:nowrap}
.pill--q{background:var(--card);border-color:transparent;color:var(--muted-card)}
.pill b{width:5px;height:5px;border-radius:50%;background:currentColor;flex:none;opacity:.85}
/* the same chip vocabulary, so a status reads the same wherever it appears */
.pill--ok{background:var(--ok-bg);color:var(--ok);border-color:transparent}
.pill--warn{background:var(--warn-bg);color:var(--warn);border-color:transparent}
.pill--bad{background:var(--bad-bg);color:var(--bad);border-color:transparent}
.pill--info{background:var(--info-bg);color:var(--info);border-color:transparent}
.pill--vio{background:var(--vio-bg);color:var(--vio);border-color:transparent}
/* HTTP method, coloured the way an API reference colours it: read is green,
   write is violet, destructive is red. */
.pill--method{font-family:var(--mono);font-size:10.5px;letter-spacing:.08em;font-weight:600}

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
.chart .bar{fill:var(--accent)}
.chart .bar--q{fill:#FBD3B4}
.chart .ln{fill:none;stroke:var(--accent);stroke-width:2;stroke-linejoin:round;stroke-linecap:round}
.chart .ln--q{stroke:#FBD3B4;stroke-dasharray:3 3}
.chart .area{fill:rgba(249,115,22,.10)}
.chart .pt{fill:var(--ink)}
.chart text{font-family:var(--mono);font-size:9px;fill:var(--muted);letter-spacing:.06em}
.legend{display:flex;flex-wrap:wrap;gap:16px;margin-top:12px}
.legend span{display:inline-flex;align-items:center;gap:7px;font-size:11.5px;color:var(--muted)}
.legend i{width:14px;height:2px;background:var(--accent);border-radius:2px}
.legend i.q{background:#FBD3B4}
.ring{display:flex;align-items:center;gap:22px;flex-wrap:wrap}
/* the ring is a fixed 128px dial; .chart{width:100%} would blow it up to the panel width */
.ring svg.chart{flex:none;width:128px;height:128px}
.ring .seg-a{stroke:var(--accent)}
.ring .seg-b{stroke:#FBD3B4}
.ring .seg-0{stroke:var(--card)}

/* ---------- callout ----------
   In the console a .note is advice you are meant to notice, so it takes the
   same light accent wash the chips use. Scoped here: the marketing pages keep
   the neutral --card note they were approved with. */
.page .note{background:rgba(249,115,22,.09);border-color:rgba(249,115,22,.22);color:var(--muted-card)}
.page .note iconify-icon{color:var(--accent-ink)}
.page .note strong{color:var(--ink)}

/* ---------- coverage: globe and table are two views of one dataset ---------- */
.viewsw{display:flex;gap:2px;padding:3px;background:var(--shell);border:1px solid var(--hair);border-radius:999px}
.viewsw button{display:inline-flex;align-items:center;gap:7px;height:32px;padding:0 15px;border:0;border-radius:999px;
  background:transparent;font:inherit;font-size:13px;color:var(--ink);cursor:pointer;transition:background var(--hover) ease}
.viewsw button iconify-icon{font-size:15px;color:var(--muted)}
@media (hover:hover) and (pointer:fine){ .viewsw button:hover{background:#fff} }
.viewsw button[aria-selected="true"]{background:#fff;font-weight:500}
.viewsw button[aria-selected="true"] iconify-icon{color:var(--accent-ink)}
.globe-stage{position:relative;display:grid;place-items:center;padding:26px 20px 34px;min-height:520px;overflow:hidden}
.globe-stage canvas{width:min(560px,86%);aspect-ratio:1;opacity:0;transition:opacity 1.2s ease;cursor:grab;touch-action:none}
.globe-stage canvas:active{cursor:grabbing}
.globe-legend{position:absolute;top:20px;right:24px;display:flex;flex-direction:column;gap:9px;
  padding:14px 16px;background:rgba(255,255,255,.86);backdrop-filter:blur(8px);border:1px solid var(--line);border-radius:14px}
.globe-legend p{font-size:10.5px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--muted-card)}
.globe-legend span{display:flex;align-items:center;gap:9px;font-size:12.5px;color:var(--muted-card)}
.globe-legend i{width:7px;height:7px;border-radius:50%;background:var(--accent);flex:none}
.globe-legend i.s{width:5px;height:5px;opacity:.55}
.globe-search{position:absolute;top:20px;left:24px;display:flex;align-items:center;gap:9px;height:36px;padding:0 15px;
  background:#fff;border:1px solid var(--line);border-radius:999px;font-size:13px;color:var(--muted)}
.globe-search iconify-icon{font-size:15px}
.is-hidden{display:none !important}

/* ---------- ranking list ---------- */
.rank{display:flex;flex-direction:column}
.rank li{display:flex;align-items:center;gap:12px;padding:11px 20px;border-top:1px solid var(--hair-soft);font-size:13px}
.rank li:first-child{border-top:0}
.rank .i{font-family:var(--mono);font-size:11px;color:var(--muted);width:16px;flex:none}
.rank .p{font-family:var(--mono);font-size:12px;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.rank .v{margin-left:auto;font-family:var(--mono);font-size:12px;color:var(--muted-card);flex:none}
.rank .track{flex:0 0 96px;height:3px;border-radius:2px;background:var(--card);overflow:hidden}
.rank .track i{display:block;height:100%;background:var(--accent)}

/* ---------- console tables ---------- */
.pnl table.tbl th{background:#fff;font-size:10.5px}
.pnl table.tbl td{font-size:13px;padding:13px 20px}
.pnl table.tbl th{padding:12px 20px}
.tfoot{margin-top:auto;display:flex;flex-wrap:wrap;align-items:center;gap:12px;padding:13px 20px;border-top:1px solid var(--hair);
  font-size:12.5px;color:var(--muted)}
.tfoot .r{margin-left:auto;display:flex;align-items:center;gap:8px}
.pg{display:flex;gap:2px;padding:3px;background:var(--shell);border-radius:999px}
.pg a{display:grid;place-items:center;min-width:28px;height:28px;padding:0 9px;border-radius:999px;font-size:12.5px;
  font-family:var(--mono)}
.pg a.on{background:#fff;color:var(--ink)}
.tact{display:flex;gap:14px;white-space:nowrap}
.tact a{font-size:12.5px;color:var(--ink);border-bottom:1px solid var(--line);padding-bottom:1px}
.tact a.q,.tact button.q{color:var(--muted)}
.tact .danger{color:var(--bad)}
/* row actions act, so they are buttons; they keep the link's look */
.tact button{border:0;background:transparent;font:inherit;font-size:12.5px;color:var(--ink);
  border-bottom:1px solid var(--line);padding:0 0 1px;cursor:pointer}
@media (hover:hover) and (pointer:fine){ .tact button:hover{border-bottom-color:currentColor} }
@media (hover:hover) and (pointer:fine){ .tact a:hover{border-bottom-color:var(--ink)} }

/* ---------- two and three column layouts ---------- */
.g2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px}
.g3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}
.g-side{display:grid;grid-template-columns:minmax(0,340px) minmax(0,1fr);gap:20px;align-items:start}
.g-side--r{grid-template-columns:minmax(0,1fr) minmax(0,340px)}
.g2 > *,.g3 > *,.g-side > *{min-width:0}

/* ---------- step list (getting started) ---------- */
.slist{display:flex;flex-direction:column;gap:8px;padding:20px}
.slist a{display:flex;align-items:center;gap:13px;padding:12px 14px;border:1px solid var(--line);border-radius:14px;
  transition:background var(--hover) ease,border-color var(--hover) ease}
@media (hover:hover) and (pointer:fine){ .slist a:hover{background:var(--card);border-color:var(--card)} }
.slist a.on{background:rgba(249,115,22,.11);border-color:transparent}
.slist a.on .n{border-color:var(--accent-ink);color:var(--accent-ink)}
.slist .n{display:grid;place-items:center;width:26px;height:26px;border-radius:999px;border:1px solid var(--line);
  font-family:var(--mono);font-size:11.5px;color:var(--muted);flex:none;background:#fff}
.slist a.on .n{border-color:var(--ink);color:var(--ink)}
.slist a.done .n{background:var(--ink);border-color:var(--ink);color:#fff}
.slist .t{min-width:0}
.slist .t b{display:block;font-size:13.5px;font-weight:500}
.slist .t code{display:block;font-family:var(--mono);font-size:11.5px;color:var(--muted);
  overflow-wrap:anywhere;line-height:1.45}

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
/* A secret is retrieved, not read. Copy works while the value is still masked;
   the eye reveals one field and puts it back on its own. */
.kv .v.secret{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.kv .v.secret span{font-family:var(--mono);font-size:12px;letter-spacing:.06em}
.kv-act{display:inline-flex;align-items:center;justify-content:center;width:28px;height:28px;border:1px solid var(--line);
  border-radius:999px;background:#fff;color:var(--muted-card);cursor:pointer;flex:none;
  transition:color var(--hover) ease,background var(--hover) ease,transform var(--press) var(--ease-out)}
.kv-act iconify-icon{font-size:14px}
.kv-act:active{transform:scale(.94)}
.kv-act.done{color:var(--ok);border-color:var(--ok-bg);background:var(--ok-bg)}
@media (hover:hover) and (pointer:fine){ .kv-act:hover{color:var(--ink);background:var(--card)} }

/* ---------- chat workspace ----------
   The assistant is an app screen, not a document: a conversation rail, a
   thread that owns the remaining height, and a composer pinned to the floor.
   Laying it out as stacked cards made a chat look like a report. */
.page--full{padding:0;max-width:none;height:calc(100vh - 64px);min-height:520px}
.wsp{display:grid;grid-template-columns:264px minmax(0,1fr);height:100%}
.wsp-side{display:flex;flex-direction:column;min-height:0;border-right:1px solid var(--hair);background:#fff}
.wsp-side-h{display:flex;align-items:center;gap:10px;padding:15px 16px;border-bottom:1px solid var(--hair)}
.wsp-side-h p{font-size:10.5px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--muted-card)}
.wsp-side-h .btn{margin-left:auto}
.convs{flex:1;overflow-y:auto;padding:11px;display:flex;flex-direction:column;gap:4px}
.conv-item{display:flex;flex-direction:column;gap:3px;padding:11px 13px;border-radius:13px;cursor:pointer;
  transition:background var(--hover) ease}
@media (hover:hover) and (pointer:fine){ .conv-item:hover{background:var(--shell)} }
.conv-item.on{background:rgba(249,115,22,.11)}
.conv-item b{font-size:13.5px;font-weight:500}
.conv-item span{font-family:var(--mono);font-size:11px;color:var(--muted)}
.wsp-main{display:flex;flex-direction:column;min-width:0;min-height:0}
.wsp-h{display:flex;align-items:center;gap:12px;padding:14px 24px;border-bottom:1px solid var(--hair)}
.wsp-h h1{font-size:16px;font-weight:500;letter-spacing:-.012em}
.wsp-h p{font-size:12.5px;color:var(--muted)}
.wsp-h .r{margin-left:auto;display:flex;align-items:center;gap:8px}
.thread{flex:1;min-height:0;overflow-y:auto;padding:28px 24px;display:flex;flex-direction:column;gap:16px}
.thread-empty{margin:auto;text-align:center;max-width:46ch;display:flex;flex-direction:column;gap:8px;
  padding:34px 26px;background:var(--card);border-radius:18px}
.thread-empty h2{font-size:14.5px;font-weight:500}
.thread-empty p{font-size:13.5px;line-height:22px;color:var(--muted-card)}
.wsp-f{border-top:1px solid var(--hair);padding:14px 24px 16px;background:#fff}
.wsp-f .disclaim{font-size:11.5px;color:var(--muted);margin-top:10px;text-align:center}
.wsp-f .disclaim a{border-bottom:1px solid var(--line)}
.conv{display:flex;flex-direction:column;gap:16px;padding:20px;min-height:320px}
.bub{max-width:74%;padding:13px 16px;border-radius:16px;font-size:13.5px;line-height:22px}
.bub--ai{background:var(--card);border-bottom-left-radius:6px}
.bub--me{margin-left:auto;background:var(--ink);color:#fff;border-bottom-right-radius:6px}
.composer{display:flex;gap:10px;align-items:center}
.composer input{flex:1;height:40px;padding:0 16px;font:inherit;font-size:13.5px;border:1px solid var(--line);
  border-radius:999px;background:#fff;color:var(--ink)}
.composer input::placeholder{color:var(--muted)}

/* ---------- responsive ---------- */
@media (max-width:1180px){ .kpis{grid-template-columns:repeat(2,minmax(0,1fr))} .g3{grid-template-columns:1fr} }
@media (max-width:1080px){ .g-side,.g-side--r{grid-template-columns:1fr} }
.side-burger{display:none;margin-left:auto;width:36px;height:36px;border:1px solid var(--line);border-radius:999px;
  background:#fff;color:var(--ink);cursor:pointer;align-items:center;justify-content:center}
.side-burger iconify-icon{font-size:18px}
@media (max-width:900px){
  .app{grid-template-columns:1fr}
  .side{position:sticky;top:0;z-index:25;height:auto;overflow:visible;border-right:0;
    border-bottom:1px solid var(--line);padding:0 14px}
  .side-brand{position:static;margin-bottom:0;border-bottom:0}
  .side-burger{display:inline-flex}
  /* the rail is closed by default: on a phone the screen you opened matters
     more than the sixteen you did not. */
  .side-nav{display:none;padding-bottom:16px}
  .side.is-open .side-nav{display:block}
  .side-grp{margin-top:14px}
  .g2{grid-template-columns:1fr}
  .page{padding:22px 16px 72px}
  .page--full{height:auto}
  .wsp{grid-template-columns:1fr}
  .wsp-side{border-right:0;border-bottom:1px solid var(--hair)}
  .top{padding:0 16px;gap:10px}
  .srch{max-width:none}
  .srch span{display:none}
  .kbd{display:none}
  .rail,.counts,.viewsw{border-radius:18px;flex-wrap:wrap}
  .globe-legend,.globe-search{position:static;margin-bottom:14px}
  .globe-stage{min-height:0;padding:18px 14px 26px}
  /* 44px targets on touch. Left at 36/40 for a mouse, where they are correct. */
  .side a{height:44px}
  .iconbtn{width:42px;height:42px}
  .pg a{min-width:38px;height:38px}
  .btn--sm{height:44px}
  .rail a,.rail button,.counts a{height:40px}
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
<script>
(function(){{
  "use strict";
  var b = document.getElementById('side-burger'), s = document.querySelector('.side');
  if (!b || !s) return;
  b.addEventListener('click', function(){{
    var open = s.classList.toggle('is-open');
    b.setAttribute('aria-expanded', String(open));
    b.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
  }});
}})();
</script>
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
    <button class="side-burger" type="button" id="side-burger" aria-expanded="false"
      aria-controls="side-nav" aria-label="Open navigation">
      <iconify-icon icon="solar:hamburger-menu-linear" aria-hidden="true"></iconify-icon>
    </button>
    <div class="side-nav" id="side-nav">
{body}
    </div>
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


def build(slug, title, desc, body, nav, active, who, initials, role, home="../index.html", page_cls="", extra=""):
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
    if page_cls:
        html = html.replace('<main class="page" id="main">', f'<main class="page {page_cls}" id="main">')
    if extra:
        html = html.replace("</body>", extra + "\n</body>")
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
