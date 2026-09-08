# -*- coding: utf-8 -*-
"""
Screen content for the signed-in console.

Structure — routes, sidebar groups, screen titles, table columns, filter sets,
counts and status vocabularies — was read off the real console at
open.fusionconnectgroup.com on 8 September 2026, in both the developer and the
platform-admin views.

Two rules about data:

* **Developer screens render their real state, which is empty.** A new
  developer's first hour is entirely empty states, so those are the design
  surface and they are shown honestly.
* **Admin screens carry SYNTHETIC rows.** The live admin view holds real
  customer names, companies, emails and phone numbers. None of it appears here.
  Every developer handle, company, ticket subject and trace ID below is
  invented; volumes are shaped to look like the real ones so the layout is
  tested at realistic density.
"""

ARROW = '<iconify-icon icon="solar:arrow-right-linear" aria-hidden="true"></iconify-icon>'

# ------------------------------------------------------------------ helpers

def chiprow(items):
    """The strip of context chips today's console puts above a screen title —
    scope, environment, template source. Dropping it lost real information."""
    out = "".join(pill(lb, k) for lb, k in items)
    return f'      <div class="band-top" style="margin-bottom:16px;gap:8px">{out}</div>'


def phead(h1, lede="", actions="", crumb=None):
    c = ""
    if crumb:
        parts = [f'<a href="{h}">{t}</a>' if h else f"<span>{t}</span>" for t, h in crumb]
        c = f'      <p class="pcrumb">{" <i aria-hidden=\"true\">/</i> ".join(parts)}</p>\n'
    l = f'          <p class="lede">{lede}</p>\n' if lede else ""
    a = f'        <div class="phead-a">{actions}</div>\n' if actions else ""
    return f"""{c}      <div class="phead">
        <div class="phead-t">
          <h1>{h1}</h1>
{l}        </div>
{a}      </div>"""


def kpi(label, value, unit="", foot="", icon="solar:chart-square-linear", lead=False):
    u = f"<u>{unit}</u>" if unit else ""
    return f"""        <div class="kpi{' kpi--lead' if lead else ''}">
          <p class="kpi-k">{label}<iconify-icon icon="{icon}" aria-hidden="true"></iconify-icon></p>
          <p class="kpi-v">{value}{u}</p>
          <p class="kpi-f">{foot}</p>
        </div>"""


def kpis(items):
    """The first tile in a row leads: it is the only one whose unit takes the
    accent. Four orange units in a row of four reads as a colour wash."""
    if items:
        # lead with the first tile that actually carries a unit — a bare integer
        # gives the accent nothing to colour, which is why no orange was landing
        i = next((n for n, it in enumerate(items) if "<u>" in it), 0)
        items = list(items)
        items[i] = items[i].replace('class="kpi"', 'class="kpi kpi--lead"', 1)
    return '      <div class="kpis">\n' + "\n".join(items) + "\n      </div>"


def pnl(title, body, sub="", right="", flush=False):
    s = f'<span class="sub">{sub}</span>' if sub else ""
    r = f'<span class="r">{right}</span>' if right else ""
    cls = "pnl-b pnl-b--flush" if flush else "pnl-b"
    head = f'        <div class="pnl-h"><h2>{title}</h2>{s}{r}</div>\n' if title else ""
    return f"""      <section class="pnl">
{head}        <div class="{cls}">
{body}
        </div>
      </section>"""


def sel(label, *options):
    opts = "".join(f"<option>{o}</option>" for o in options)
    return f"""          <div class="fgrp"><label>{label}</label>
            <select class="sel" aria-label="{label}">{opts}</select></div>"""


def rail(items, active):
    out = "".join(
        f'<a{" class=\"on\"" if i == active else ""} href="#">{i}</a>' for i in items
    )
    return f'<nav class="rail" aria-label="Time range">{out}</nav>'


def counts(items):
    out = "".join(
        f'<a{" class=\"on\"" if on else ""} href="#">{lb}<span class="n">{n}</span></a>'
        for lb, n, on in items
    )
    return f'<nav class="counts" aria-label="Filter by status">{out}</nav>'


def tbl(cols, rows, minw=760):
    ths = "".join(f"<th>{c}</th>" for c in cols)
    if rows:
        trs = "\n".join("        <tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
        body = f"<tbody>\n{trs}\n      </tbody>"
    else:
        body = "<tbody></tbody>"
    return f"""<div class="tblwrap" style="border:0;border-radius:0"><div class="tblscroll">
    <table class="tbl" style="min-width:{minw}px">
      <thead><tr>{ths}</tr></thead>
      {body}
    </table>
  </div></div>"""


def empty(title, text, icon="solar:inbox-linear", cta=""):
    c = f'\n          <a class="btn btn--sm" href="#">{cta} {ARROW}</a>' if cta else ""
    return f"""          <div class="empty">
            <iconify-icon icon="{icon}" aria-hidden="true"></iconify-icon>
            <h3>{title}</h3>
            <p>{text}</p>{c}
          </div>"""


def st(label, kind=""):
    k = f" st--{kind}" if kind else ""
    return f'<span class="st{k}"><b aria-hidden="true"></b>{label}</span>'


def pill(label, kind=""):
    k = f" pill--{kind}" if kind else ""
    b = '<b aria-hidden="true"></b>' if kind in ("ok", "warn", "bad") else ""
    return f'<span class="pill{k}">{b}{label}</span>'


def tfoot(shown, total, per_page=10):
    """Derive the pager from the numbers on the page. Hardcoding it produced
    'Showing 7 of 122' over six page chips at ten per page — wrong twice."""
    pages = max(1, -(-total // per_page))
    nums = list(range(1, min(pages, 5) + 1))
    pgs = "".join(f'<a href="#"{" class=\"on\"" if i == 1 else ""}>{i}</a>' for i in nums)
    if pages > 5:
        pgs += f'<span class="pg-gap">…</span><a href="#">{pages}</a>'
    return f"""          <div class="tfoot">Showing {shown} of {total:,}
            <span class="r"><span class="pg">{pgs}</span>{per_page} / page</span>
          </div>"""


def bars(values, labels, w=560, h=168):
    """Ink bars, quiet grid. The tallest bar is the only one that gets a label."""
    if not values:
        return ""
    top = max(values) or 1
    n = len(values)
    gap, pad = 18, 22
    bw = (w - pad - gap * (n - 1)) / n
    out = [f'<svg class="chart" viewBox="0 0 {w} {h}" role="img" aria-label="Endpoint call volume">']
    for i in range(4):
        y = 8 + (h - 40) * i / 3
        out.append(f'<line class="grid" x1="{pad}" y1="{y:.0f}" x2="{w}" y2="{y:.0f}"/>')
    for i, (v, lb) in enumerate(zip(values, labels)):
        bh = (h - 48) * v / top
        x = pad + i * (bw + gap)
        y = h - 30 - bh
        out.append(f'<rect class="bar" x="{x:.0f}" y="{y:.0f}" width="{bw:.0f}" height="{bh:.0f}" rx="3"/>')
        out.append(f'<text x="{x + bw / 2:.0f}" y="{h - 14}" text-anchor="middle">{lb}</text>')
    out.append("</svg>")
    return "".join(out)


def line(series, labels, w=560, h=168):
    """Two series: primary ink, secondary grey dashed. Last point takes the
    orange dot — the only accent a chart gets."""
    top = max(max(s) for s in series) or 1
    n = len(labels)
    pad, base = 26, h - 30
    def pts(s):
        return [(pad + (w - pad - 6) * i / (n - 1), base - (base - 12) * v / top) for i, v in enumerate(s)]
    out = [f'<svg class="chart" viewBox="0 0 {w} {h}" role="img" aria-label="Requests and failures, last seven days">']
    for i in range(4):
        y = 12 + (base - 12) * i / 3
        out.append(f'<line class="grid" x1="{pad}" y1="{y:.0f}" x2="{w}" y2="{y:.0f}"/>')
    for idx, s in enumerate(series):
        p = pts(s)
        d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in p)
        if idx == 0:
            out.append(f'<path class="area" d="{d} L{p[-1][0]:.1f} {base} L{p[0][0]:.1f} {base} Z"/>')
        out.append(f'<path class="ln{" ln--q" if idx else ""}" d="{d}"/>')
    lastx, lasty = pts(series[0])[-1]
    out.append(f'<circle class="pt" cx="{lastx:.1f}" cy="{lasty:.1f}" r="3.4"/>')
    for i, lb in enumerate(labels):
        out.append(f'<text x="{pad + (w - pad - 6) * i / (n - 1):.0f}" y="{h - 12}" text-anchor="middle">{lb}</text>')
    out.append("</svg>")
    return "".join(out)


def ring(pct, label, sub):
    """A share ring. With no data it draws one flat --card ring and says so,
    rather than a full-circle 'No data 100%'."""
    r, c = 52, 2 * 3.14159 * 52
    if pct is None:
        arc = f'<circle class="seg-0" cx="64" cy="64" r="{r}" fill="none" stroke-width="16"/>'
        mid = '<text x="64" y="68" text-anchor="middle" style="font-size:11px">no data</text>'
    else:
        dash = c * pct / 100
        arc = (f'<circle class="seg-b" cx="64" cy="64" r="{r}" fill="none" stroke-width="16"/>'
               f'<circle class="seg-a" cx="64" cy="64" r="{r}" fill="none" stroke-width="16" '
               f'stroke-dasharray="{dash:.1f} {c - dash:.1f}" stroke-linecap="butt" transform="rotate(-90 64 64)"/>')
        mid = f'<text x="64" y="69" text-anchor="middle" style="font-size:15px;fill:var(--ink)">{pct}%</text>'
    return f"""<div class="ring">
            <svg class="chart" width="128" height="128" viewBox="0 0 128 128" role="img" aria-label="{label}">{arc}{mid}</svg>
            <div><p style="font-size:13.5px;font-weight:500">{label}</p>
            <p style="font-size:12.5px;color:var(--muted);margin-top:4px">{sub}</p>
            <div class="legend"><span><i></i>Succeeded</span></div></div>
          </div>"""


def rank(rows):
    if not rows:
        return empty("No ranking data yet", "Rankings appear once the selected range contains successful calls.",
                     "solar:ranking-linear")
    top = max(v for _, v in rows) or 1
    out = []
    for i, (path, v) in enumerate(rows, 1):
        out.append(f'            <li><span class="i">{i:02d}</span><span class="p">{path}</span>'
                   f'<span class="track"><i style="width:{100 * v / top:.0f}%"></i></span>'
                   f'<span class="v">{v:,}</span></li>')
    return '          <ul class="rank">\n' + "\n".join(out) + "\n          </ul>"


# ============================================================ DEVELOPER SCREENS

FILTERS_DEV = f"""          <div class="fbar">
{sel("Environment", "All environments", "Sandbox", "Production")}
{sel("Application", "All applications", "G-Link Hotel API", "F-Link Flight API", "TMC API")}
            <div class="fgrp" style="flex:0 0 auto;max-width:none"><label>Time range</label>
              {rail(["Today", "Last 7 days", "Last 30 days"], "Last 7 days")}</div>
            <span class="fbar-a"><a class="btn btn--ghost btn--sm" href="#">Reset</a>
              <a class="btn btn--sm" href="#">Apply {ARROW}</a></span>
          </div>"""

CONSOLE = f"""
{phead("Console", "Request volume, success rate and search-to-booking ratio across every application on this account.",
       f'<a class="btn btn--sm" href="../api-docs-hotel.html">View API docs {ARROW}</a>'
       f'<a class="btn btn--ghost btn--sm" href="getting-started.html">Getting started {ARROW}</a>')}
      <div class="stack">
        <section class="pnl">{FILTERS_DEV}</section>
{kpis([
    kpi("Successful requests", "0", "", "Nothing recorded in this range", "solar:check-circle-linear"),
    kpi("Success rate", "0.0", "%", "0 of 0 calls", "solar:graph-up-linear"),
    kpi("Search to booking", "0.0", "%", "0 bookings / 0 searches", "solar:cart-check-linear"),
    kpi("Average latency", "0", "ms", "Current filter scope", "solar:clock-circle-linear"),
])}
        <div class="g2">
{pnl("Calls by endpoint", empty("No calls in this range", "Run the first-order flow in Getting Started and this fills within a minute.", "solar:chart-square-linear", "Open Getting Started"), sub="Current filter range", flush=True)}
{pnl("Successful call trend", empty("No trend yet", "Seven days of history appear here once the first sandbox call succeeds.", "solar:graph-linear"), sub="Last 7 days", flush=True)}
        </div>
        <div class="g2">
{pnl("Request outcome", "          " + ring(None, "Succeeded against failed", "No calls in the selected range."))}
{pnl("Popular endpoints", rank([]), sub="Current range", flush=True)}
        </div>
{pnl("Recent requests",
     tbl(["Request ID", "Endpoint", "Status", "Duration", "Time"], []) +
     empty("No requests recorded", "Every sandbox and production call lands here within a few seconds of completing.", "solar:inbox-linear"),
     right='<a class="tlink" href="trace.html">Open request trace ' + ARROW + '</a>', flush=True)}
{pnl("Announcements", empty("Nothing to read", "Platform notices, breaking changes and maintenance windows appear here.", "solar:bell-linear"), flush=True)}
      </div>
"""

GETTING_STARTED_STEPS = [
    ("Destination query", "/openapi/v1/glink/search/destination"),
    ("Hotel list query", "/openapi/v1/glink/search/hotelList"),
    ("Real-time product query", "/openapi/v1/glink/booking/productDetails"),
    ("Availability check", "/openapi/v1/glink/booking/availabilityCheck"),
    ("Create order", "/openapi/v1/glink/booking/createOrder"),
]

_steps = "\n".join(
    f'            <a{" class=\"on\"" if i == 1 else ""} href="#step-{i}">'
    f'<span class="n">{i}</span><span class="t"><b>{t}</b><code>{p}</code></span></a>'
    for i, (t, p) in enumerate(GETTING_STARTED_STEPS, 1)
)

GETTING_STARTED = f"""
{chiprow([("Sandbox available", "ok"), ("G-Link only", "info"), ("Template: default_template", "")])}
{phead("Getting Started",
       "The five calls that take a G-Link integration from nothing to a first sandbox booking. Each step sends a real request against your sandbox credentials.",
       f'<a class="btn btn--ghost btn--sm" href="#">Refresh</a><a class="btn btn--sm" href="#">Run the full flow {ARROW}</a>',
       crumb=[("Sandbox", "sandbox.html"), ("G-Link first-order debug", None)])}
      <div class="stack">
        <div class="g-side">
          <div class="stack">
{pnl("Integration progress",
     '          <p style="font-size:12.5px;color:var(--muted);margin-bottom:10px">0 of 5 endpoints connected</p>'
     + chr(10) + '          <div class="prog"><i style="width:0%"></i></div>')}
{pnl("First booking path", '          <div class="slist">' + chr(10) + _steps + chr(10) + "          </div>", flush=True)}
{pnl("Sandbox credentials",
     '''          <div class="kv">
            <div><span class="k">Open app ID</span><span class="v mono">oapp_&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;</span></div>
            <div><span class="k">Open secret</span><span class="v mono">enc:&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;</span></div>
            <div><span class="k">Environment</span><span class="v">''' + pill("Sandbox", "ok") + '''</span></div>
          </div>
          <div class="note" style="margin-top:16px"><iconify-icon icon="solar:info-circle-linear"></iconify-icon>
            <span>G-Link does not create supplier accounts automatically, so these credentials reuse the activated sandbox mapping. Reveal them from App Management.</span></div>''',
     right='<a class="tlink" href="app-management.html">App management ' + ARROW + '</a>')}
          </div>
          <div class="stack">
            <section class="pnl" id="step-1">
              <div class="pnl-h">
                {pill("POST", "vio method")}
                <h2>Destination query</h2>
                {pill("Not connected")}
                <span class="r"><a class="btn btn--ghost btn--sm" href="../api-docs-hotel-apis.html">Endpoint docs</a>
                <a class="btn btn--sm" href="#">Send sandbox request {ARROW}</a></span>
              </div>
              <div class="pnl-b">
                <p style="font-family:var(--mono);font-size:12px;color:var(--muted);margin-bottom:6px">/openapi/v1/glink/search/destination</p>
                <p style="font-size:13.5px;color:var(--muted);line-height:22px;max-width:70ch">Returns the destinations available to your account. The hotel list call in step two reuses the destination ID this returns.</p>
                <div class="g2" style="margin-top:18px">
                  <div>
                    <p class="kpi-k" style="margin-bottom:9px">Request body</p>
                    <div class="pane">{{
  "keyWord": "Shanghai"
}}</div>
                  </div>
                  <div>
                    <p class="kpi-k" style="margin-bottom:9px">Response</p>
                    <div class="pane pane--q">Send the request and the response
appears here, with the destination ID
carried into step two.</div>
                  </div>
                </div>
              </div>
            </section>
{pnl("What connecting a step means",
     '''          <p style="font-size:13.5px;line-height:23px;color:var(--muted);max-width:74ch">A step counts as connected once it returns a 200 with a usable payload from your own credentials. Marking a step by hand is for endpoints you have already wired outside this console; it changes the progress figure and nothing else.</p>''')}
          </div>
        </div>
      </div>
"""

APPS = [
    ("G-Link Hotel API", "glink-hotel", "Hotel search, booking, payment and cancellation workflows.", "28 April 2026", ""),
    ("F-Link Flight API", "flink-flight", "Flight search, ticketing, refunds and changes.", "28 April 2026", ""),
    ("TMC API", "tmc-api", "Rapid deployment of corporate travel platforms.", "28 April 2026",
     "The TMC API sandbox settles in USD only."),
]

def secret_row(label, kind):
    """Masked by default. Copy works without revealing; the eye reveals this one
    field and re-masks itself. A developer wants the value in the clipboard, not
    on a shared screen."""
    return (f'              <div><span class="k">{label}</span><span class="v secret">'
            f'<span>&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;</span>'
            f'<button class="kv-act" type="button" aria-label="Copy {label.lower()}">'
            f'<iconify-icon icon="solar:copy-linear" aria-hidden="true"></iconify-icon></button>'
            f'<button class="kv-act" type="button" aria-expanded="false" aria-label="Reveal {label.lower()}">'
            f'<iconify-icon icon="solar:eye-linear" aria-hidden="true"></iconify-icon></button>'
            f'</span></div>')


_appcards = "\n".join(f"""        <section class="pnl">
          <div class="pnl-h"><h2>{n}</h2>{pill("Sandbox enabled", "ok")}</div>
          <div class="pnl-b">
            <p style="font-size:13.5px;color:var(--muted);line-height:22px">{d}</p>
            <div class="kv" style="margin-top:14px">
              <div><span class="k">App code</span><span class="v secret"><span>{c}</span>
                <button class="kv-act" type="button" aria-label="Copy app code">
                <iconify-icon icon="solar:copy-linear" aria-hidden="true"></iconify-icon></button></span></div>
{secret_row("App key", "key")}
{secret_row("App secret", "secret")}
              <div><span class="k">Created</span><span class="v">{cr}</span></div>
            </div>
            {'<div class="note" style="margin-top:14px"><iconify-icon icon="solar:info-circle-linear"></iconify-icon><span>' + note + "</span></div>" if note else ""}
          </div>
          <div class="tfoot"><a class="btn btn--ghost btn--sm" href="#">Apply for production {ARROW}</a>
            <span class="r"><a class="tlink" href="../api-docs-hotel.html">Product docs {ARROW}</a></span></div>
        </section>""" for n, c, d, cr, note in APPS)

APP_MANAGEMENT = f"""
{phead("App Management",
       "One credential set per product, so a hotel key never unlocks a flight endpoint and a sandbox key never reaches production.",
       f'<a class="btn btn--sm" href="#">Create an application {ARROW}</a>')}
      <div class="stack">
        <div class="g3">
{_appcards}
        </div>
{pnl("Traveller-facing client example",
     '''          <p style="font-size:13.5px;line-height:23px;color:var(--muted);max-width:74ch">A complete client wired to G-Link hotel and F-Link flight real-time inventory. Open it, read it, then take the source and start building.</p>
          <div class="kv" style="margin-top:14px">
            <div><span class="k">Inventory</span><span class="v">G-Link and F-Link, live sandbox</span></div>
            <div><span class="k">Environment</span><span class="v">''' + pill("Sandbox", "ok") + '''</span></div>
          </div>''',
     right='<a class="btn btn--sm" href="#">Open full client ' + ARROW + '</a><a class="tlink" href="sdk.html">Download source</a>')}
      </div>
"""

SANDBOX = f"""
{phead("Sandbox Environment",
       "Validate integration logic against real API behaviour without touching production data or incurring cost.")}
      <div class="stack">
        <div class="g3">
{pnl("G-Link Hotel sandbox", '          <p style="font-size:13.5px;color:var(--muted);line-height:22px">Hotel search, booking, payment and cancellation.</p>', right=pill("Active", "ok"))}
{pnl("F-Link Flight sandbox", '          <p style="font-size:13.5px;color:var(--muted);line-height:22px">Flight search, ticketing, refunds and changes.</p>', right=pill("Active", "ok"))}
{pnl("TMC API sandbox", '          <p style="font-size:13.5px;color:var(--muted);line-height:22px">Corporate travel platform deployment. Settles in USD only.</p>', right=pill("Active", "ok"))}
        </div>
{pnl("Recent test records",
     empty("No test records yet", "Requests sent from Getting Started or from your own client appear here with their full payloads.",
           "solar:test-tube-linear", "Run the first-order flow"),
     right='<a class="tlink" href="getting-started.html">Getting started ' + ARROW + '</a>', flush=True)}
      </div>
"""

TRACE_FILTERS = f"""          <div class="fbar">
{sel("Application", "Select application", "G-Link Hotel API", "F-Link Flight API", "TMC API")}
{sel("Environment", "All environments", "Sandbox", "Production")}
{sel("Time range", "All time", "Last hour", "Last 24 hours", "Last 7 days")}
{sel("Product", "Select product", "G-Link", "F-Link", "TMC")}
{sel("Endpoint", "Select a product first")}
{sel("Status", "All statuses", "Success", "Failed", "Timeout")}
{sel("Latency", "All latencies", "Under 200ms", "200ms to 1s", "Over 1s")}
            <span class="fbar-a"><a class="btn btn--ghost btn--sm" href="#">Reset</a>
              <a class="btn btn--sm" href="#">Search {ARROW}</a></span>
          </div>"""

TRACE = f"""
{phead("Request Trace", "Every API call your applications make, with its payload, timing and failure reason.",
       f'<a class="btn btn--ghost btn--sm" href="#">Export CSV</a>')}
      <div class="stack">
        <section class="pnl">{TRACE_FILTERS}</section>
{kpis([
    kpi("Total requests", "0", "", "All time", "solar:routing-2-linear"),
    kpi("Failures", "0", "", "0.0% of calls", "solar:danger-triangle-linear"),
    kpi("Timeouts", "0", "", "No timeouts recorded", "solar:clock-circle-linear"),
    kpi("Successes", "0", "", "All time", "solar:check-circle-linear"),
])}
{pnl("Requests",
     tbl(["Trace ID", "Env", "Path", "Status", "Duration", "Application", "Time"], [], 900) +
     empty("No requests to inspect", "Traces are retained for 30 days. Send a sandbox request and it appears here within seconds.",
           "solar:routing-2-linear", "Open Getting Started"),
     sub="0 total", flush=True)}
      </div>
"""

COVERAGE_MARKERS = [
    ("Bangkok", 13.7563, 100.5018, .05), ("Tokyo", 35.6762, 139.6503, .05),
    ("Shanghai", 31.2304, 121.4737, .05), ("Hong Kong", 22.3193, 114.1694, .05),
    ("Singapore", 1.3521, 103.8198, .05), ("Dubai", 25.2048, 55.2708, .04),
    ("London", 51.5074, -0.1278, .05), ("Paris", 48.8566, 2.3522, .04),
    ("New York", 40.7128, -74.0060, .05), ("Los Angeles", 33.9425, -118.4081, .04),
    ("Miami", 25.7617, -80.1918, .035), ("Mexico City", 19.4326, -99.1332, .035),
    ("São Paulo", -23.5505, -46.6333, .035), ("Sydney", -33.8688, 151.2093, .04),
]

COVERAGE = f"""
{phead("Coverage Map", "Bookable properties by country and region, plotted on WGS84 coordinates.",
       '<div class="viewsw" role="tablist" id="cov-switch">'
       '<button role="tab" aria-selected="true" data-view="globe">'
       '<iconify-icon icon="solar:global-linear" aria-hidden="true"></iconify-icon>Globe</button>'
       '<button role="tab" aria-selected="false" data-view="table">'
       '<iconify-icon icon="solar:list-linear" aria-hidden="true"></iconify-icon>Table</button>'
       '</div>'
       f'<a class="btn btn--ghost btn--sm" href="#">Refresh properties</a>',
       crumb=[("Hotel catalogue", None), ("Coverage map", None)])}
      <div class="stack">
{kpis([
    kpi("Total properties", "0", "", "Awaiting first catalogue sync", "solar:buildings-2-linear"),
    kpi("Countries and regions", "0", "", "Awaiting first catalogue sync", "solar:global-linear"),
    kpi("Properties in view", "0", "", "Pan or zoom to change", "solar:map-point-linear"),
    kpi("Catalogue source", "Mock", "", "Switches to live on production access", "solar:database-linear"),
])}
        <section class="pnl" id="cov-globe-view">
          <div class="pnl-h"><h2>Coverage</h2><span class="sub">Drag to spin</span>
            <span class="r">{pill("Mock provider", "info")}</span></div>
          <div class="globe-stage">
            <span class="globe-search"><iconify-icon icon="solar:magnifer-linear" aria-hidden="true"></iconify-icon>Search for a place</span>
            <div class="globe-legend">
              <p>Density</p>
              <span><i style="width:9px;height:9px"></i>Over 30 properties</span>
              <span><i></i>10 to 30 properties</span>
              <span><i class="s"></i>Under 10 properties</span>
            </div>
            <canvas id="cov-globe" aria-label="Coverage globe. The same globe as the FCG website."></canvas>
          </div>
          <div class="tfoot">Gateway cities shown while the catalogue is on the mock provider.
            <span class="r">WGS84</span></div>
        </section>
        <section class="pnl is-hidden" id="cov-table-view">
          <div class="pnl-h"><h2>Properties</h2><span class="sub">0 records</span>
            <span class="r">{pill("Mock provider", "info")}</span></div>
{tbl(["Property ID", "Name", "City", "Country", "Coordinates", "Chain", "Rating"], [], 900)}
{empty("No properties to list", "The catalogue populates both views at once. Sync a property set and the globe plots it and the table lists it.", "solar:buildings-2-linear", "Read the catalogue guide")}
        </section>
      </div>
"""

COVERAGE_JS = """<script>
(function(){
  "use strict";
  var sw = document.getElementById('cov-switch');
  if (sw) {
    sw.addEventListener('click', function(e){
      var b = e.target.closest('button'); if (!b) return;
      sw.querySelectorAll('button').forEach(function(o){ o.setAttribute('aria-selected', String(o === b)); });
      document.getElementById('cov-globe-view').classList.toggle('is-hidden', b.dataset.view !== 'globe');
      document.getElementById('cov-table-view').classList.toggle('is-hidden', b.dataset.view !== 'table');
    });
  }

  // The FCG website's globe, same library and same orange marker colour,
  // in the light configuration the site uses for its light theme.
  var canvas = document.getElementById('cov-globe');
  if (!canvas || typeof createGlobe !== 'function') return;
  var phi = 3.2, down = false, startX = 0, drag = 0;
  var markers = MARKERS;

  canvas.addEventListener('pointerdown', function(e){ down = true; startX = e.clientX; });
  window.addEventListener('pointerup', function(){ down = false; phi += drag; drag = 0; }, {passive:true});
  window.addEventListener('pointermove', function(e){ if (down) drag = (e.clientX - startX) / 200; }, {passive:true});

  function draw(){
    var w = canvas.offsetWidth;
    if (!w) { requestAnimationFrame(draw); return; }
    var dpr = Math.min(2, window.devicePixelRatio || 1);
    createGlobe(canvas, {
      devicePixelRatio: dpr, width: w * dpr, height: w * dpr,
      phi: 0, theta: 0.2,
      dark: 0, diffuse: 2, mapSamples: 16000, mapBrightness: 2,
      baseColor: [0.95, 0.95, 0.95],
      markerColor: [0.97, 0.45, 0.09],
      glowColor: [0.92, 0.92, 0.92],
      markers: markers,
      onRender: function(state){
        if (!down) phi += 0.003;
        state.phi = phi + drag;
        state.width = canvas.width; state.height = canvas.height;
      }
    });
    canvas.style.opacity = '1';
  }
  draw();
})();
</script>""".replace("MARKERS", str([{"location": [la, ln], "size": sz} for _, la, ln, sz in COVERAGE_MARKERS]).replace("'", '"'))

MAPPING = f"""
{phead("Hotel Mapping", "Match your own property inventory to platform hotel IDs by uploading a CSV.",
       f'<a class="btn btn--ghost btn--sm" href="#">Download CSV template</a><a class="btn btn--sm" href="#">Upload CSV {ARROW}</a>',
       crumb=[("Hotel catalogue", None), ("Hotel mapping", None)])}
      <div class="stack">
        <div class="g3">
{pnl("Step one", '          <p style="font-size:13.5px;line-height:22px;color:var(--muted)">Download the template. It carries the columns the matcher expects: property ID and name, address, country, city, coordinates, chain, type, rating and postal code.</p>', sub="Download the template")}
{pnl("Step two", '          <p style="font-size:13.5px;line-height:22px;color:var(--muted)">Upload the completed file under your distributor code. The platform opens a batch and processes it asynchronously, so a large file does not block the page.</p>', sub="Upload your file")}
{pnl("Step three", '          <p style="font-size:13.5px;line-height:22px;color:var(--muted)">Review matched, needs-review, unmatched and invalid rows. Cancel an incorrect mapping, or export the finished result as CSV.</p>', sub="Review and export")}
        </div>
{pnl("Mapping history",
     tbl(["Batch", "File", "Status", "Progress", "Uploaded", ""], []) +
     empty("No batches yet", "Upload a mapping file and its batch appears here with a live progress figure.",
           "solar:upload-linear", "Upload CSV"),
     sub="Local batch index", right='<a class="tlink" href="#">Refresh</a>', flush=True)}
      </div>
"""

HOTEL_ORDERS = f"""
{phead("Hotel Orders", "Every hotel booking made through your applications, in sandbox and in production.",
       f'<a class="btn btn--ghost btn--sm" href="#">Refresh</a>',
       crumb=[("My orders", None), ("Hotel orders", None)])}
      <div class="stack">
        <section class="pnl">
          <div class="fbar">
            <div class="fgrp" style="flex:0 0 auto;max-width:none"><label>Environment</label>
              {rail(["Sandbox", "Production"], "Sandbox")}</div>
{sel("Payment method", "All methods", "Prepay", "Credit line", "Card")}
            <span class="fbar-a"><a class="btn btn--sm" href="#">Search {ARROW}</a></span>
          </div>
        </section>
{pnl("Orders",
     tbl(["Order no.", "Customer ref.", "Check-in", "Check-out", "Nights", "Rooms", "Guest", "Amount", "Payment", ""], [], 1080) +
     empty("No hotel orders yet", "Bookings created through the G-Link booking endpoints appear here immediately, sandbox included.",
           "solar:bed-linear", "Open the booking flow"),
     flush=True)}
      </div>
"""

FLIGHT_ORDERS = f"""
{phead("Flight Orders", "Every ticket issued through your applications, with passenger and contact details.",
       f'<a class="btn btn--ghost btn--sm" href="#">Refresh</a>',
       crumb=[("My orders", None), ("Flight orders", None)])}
      <div class="stack">
        <section class="pnl">
          <div class="fbar">
            <div class="fgrp" style="flex:0 0 auto;max-width:none"><label>Environment</label>
              {rail(["Sandbox", "Production"], "Sandbox")}</div>
            <span class="fbar-a"><a class="btn btn--sm" href="#">Search {ARROW}</a></span>
          </div>
        </section>
{pnl("Orders",
     tbl(["Order no.", "Passenger", "Contact", "Phone", "Amount", "Created"], [], 860) +
     empty("No flight orders yet", "Tickets issued through the F-Link ticketing endpoints appear here, sandbox included.",
           "solar:plane-linear", "Open the F-Link docs"),
     flush=True)}
      </div>
"""

def _wire(rows):
    """A wireframe of the template, not a grey rectangle with a generic icon.
    A chooser where every option looks identical is not a chooser."""
    out, y = [], 10
    for w, h in rows:
        out.append(f'<rect x="{(100 - w) / 2:.0f}" y="{y}" width="{w}" height="{h}" rx="2" fill="#D8DBE0"/>')
        y += h + 5
    return ('<svg viewBox="0 0 100 74" width="100%" height="104" role="img" aria-hidden="true" '
            'style="display:block;background:var(--card);border-radius:12px">'
            '<rect x="6" y="5" width="88" height="4" rx="2" fill="#B9BEC6"/>' + "".join(out) + "</svg>")


# name, description, wireframe row spec (width, height)
TMC_TEMPLATES = [
    ("Corporate", "A booking-first homepage for a managed travel programme, with policy and approval surfaced up front.",
     [(88, 18), (42, 12), (88, 8)]),
    ("Agency", "A margin-first layout for a travel agency reselling to corporate clients.",
     [(88, 10), (88, 10), (88, 10), (40, 8)]),
    ("Marketplace", "A search-led homepage for a multi-supplier marketplace.",
     [(60, 8), (88, 26), (88, 8)]),
    ("Minimal", "A single-column layout for embedding inside an existing intranet.",
     [(52, 8), (52, 8), (52, 8)]),
]

_tmc = "\n".join(f"""        <section class="pnl">
          <div class="pnl-h"><h2>{n}</h2></div>
          <div class="pnl-b">
            {_wire(rows)}
            <p style="font-size:13px;line-height:21px;color:var(--muted);margin-top:13px">{d}</p>
          </div>
          <div class="tfoot"><a class="tlink" href="#">Preview {ARROW}</a>
            <span class="r"><button class="btn btn--sm" type="button">Select</button></span></div>
        </section>""" for n, d, rows in TMC_TEMPLATES)

TMC_BUILDER = f"""
{phead("Build My TMC", "Pick a white-label homepage template, then configure brand, policy and suppliers in the white-label system.",
       f'<a class="btn btn--sm" href="../../whitelabel.html">Open the white-label system {ARROW}</a>')}
      <div class="stack">
        <div class="g2">
{_tmc}
        </div>
      </div>
"""

SDKS = [
    ("G-Link Hotel", "Python", "glink-sdk-python", "2.5.3", "13 July 2026", "pip install glink-sdk-python"),
    ("G-Link Hotel", "Java", "glink-sdk-java", "2.5.3", "13 July 2026", "mvn install glink-sdk-java"),
    ("G-Link Hotel", "Go", "open-platform-go-sdk", "2.5.3", "13 July 2026", "go get open-platform/sdk/glink"),
    ("F-Link Flight", "Python", "flink-sdk-python", "1.4.0", "29 April 2026", "pip install flink-sdk-python"),
    ("F-Link Flight", "Java", "flink-sdk-java", "1.4.0", "29 April 2026", "mvn install flink-sdk-java"),
    ("TMC API", "Python", "tmc-sdk-python", "1.0.0", "30 July 2026", "pip install tmc-sdk-python"),
    ("TMC API", "Java", "tmc-sdk-java", "1.0.0", "30 July 2026", "mvn install tmc-sdk-java"),
    ("TMC API", "Go", "tmc-go-sdk", "1.0.0", "30 July 2026", "go get open-platform/sdk/tmc"),
]

SDK = f"""
{phead("SDK", "Eight published SDKs across three products, each with an install command, a changelog and a checksum.")}
      <div class="stack">
        <section class="pnl">
          <div class="fbar">
            <div class="fgrp" style="flex:0 0 auto;max-width:none"><label>Product</label>
              {rail(["All", "G-Link Hotel", "F-Link Flight", "TMC API"], "All")}</div>
            <div class="fgrp" style="flex:0 0 auto;max-width:none"><label>Language</label>
              {rail(["All", "Go", "Java", "Python"], "All")}</div>
          </div>
        </section>
{pnl("Published SDKs",
     tbl(["Product", "Language", "Package", "Version", "Published", "Install", ""],
         [[p, l, f'<span class="mono">{pk}</span>', f'<span class="mono">v{v}</span>', d,
           f'<span class="v secret"><span style="font-size:11.5px">{cmd}</span>'
           f'<button class="kv-act" type="button" aria-label="Copy install command">'
           f'<iconify-icon icon="solar:copy-linear" aria-hidden="true"></iconify-icon></button></span>',
           '<span class="tact"><a href="#">Docs</a><a class="q" href="#">Download</a></span>']
          for p, l, pk, v, d, cmd in SDKS], 1000),
     sub="8 packages", flush=True)}
{pnl("Node.js SDK", '          <p style="font-size:13.5px;line-height:22px;color:var(--muted);max-width:74ch">A Node.js SDK is in progress across all three products. Until it ships, call the REST endpoints directly; the request signing rules are identical.</p>', right=pill("In progress", "warn"))}
      </div>
"""

SKILL_PKGS = [
    ("G-Link Hotel API Skills", "G-Link", "2.0.0", "Auth, search, booking, payment, order management, webhooks and troubleshooting.", "npx @mongoui/skills install glink-hotel-api --tool codex"),
    ("F-Link Flight API Skills", "F-Link", "2.0.0", "Auth, flight search, booking, ticketing, changes, refunds, webhooks and troubleshooting.", "npx @mongoui/skills install flink-flight-api --tool codex"),
    ("TMC API Skills", "TMC", "1.0.0", "Auth, flight and hotel booking, approvals, travel policy, organisation hierarchy and webhooks.", "npx @mongoui/skills install tmc-api --tool codex"),
]

_skills = "\n".join(f"""        <section class="pnl">
          <div class="pnl-h"><h2>{n}</h2>{pill(f"v{v}")}<span class="r">{pill("Sandbox ready", "ok")}{pill("Production ready", "ok")}</span></div>
          <div class="pnl-b">
            <p style="font-size:13.5px;line-height:22px;color:var(--muted);max-width:74ch">{d}</p>
            <div class="cmd" style="margin-top:14px"><code>{c}</code><button type="button" aria-label="Copy command"><iconify-icon icon="solar:copy-linear" aria-hidden="true"></iconify-icon></button></div>
            <p style="font-size:12px;color:var(--muted);margin-top:12px">Works with Codex, Cursor, Claude Code, Kiro and Gemini CLI.</p>
          </div>
          <div class="tfoot"><a class="tlink" href="#">Package detail {ARROW}</a>
            <span class="r"><a class="btn btn--sm" href="#">Download SKILL.md {ARROW}</a></span></div>
        </section>""" for n, p, v, d, c in SKILL_PKGS)

SKILLS = f"""
{phead("Skills", "Official skill packages that teach an AI coding assistant how this platform's APIs actually behave.")}
      <div class="stack">
{kpis([
    kpi("Skill packages", "3", "", "One per product", "solar:magic-stick-3-linear"),
    kpi("Integration coverage", "100", "%", "Auth through to webhooks", "solar:check-circle-linear"),
    kpi("Supported tools", "5", "", "Codex, Cursor, Claude Code, Kiro, Gemini CLI", "solar:cpu-linear"),
    kpi("Install routes", "2", "", "Remote command or SKILL.md download", "solar:download-minimalistic-linear"),
])}
{_skills}
      </div>
"""

AI_ASSISTANT = f"""
      <div class="wsp">
        <aside class="wsp-side">
          <div class="wsp-side-h">
            <p>Conversation history</p>
            <a class="btn btn--sm" href="#">New</a>
          </div>
          <div class="convs">
            <div class="conv-item on"><b>New conversation</b><span>08 Sept &middot; 04:19</span></div>
          </div>
        </aside>
        <section class="wsp-main">
          <div class="wsp-h">
            <div><h1>AI Assistant</h1>
              <p>Answers on API integration, signing, orders, webhooks and MCP.</p></div>
            <span class="r">{pill("Reads your app context", "ok")}</span>
          </div>
          <div class="thread">
            <div class="thread-empty">
              <h2>A new conversation has started</h2>
              <p>Type your question below. The assistant can read your application list, your sandbox
                 credential scope and the published API docs, so questions about your own integration
                 work without pasting anything in.</p>
            </div>
          </div>
          <div class="wsp-f">
            <div class="composer">
              <input type="text" aria-label="Message"
                placeholder="Enter your question and press Enter to send. Shift and Enter starts a new line.">
              <button class="btn btn--sm" type="button">Send {ARROW}</button>
            </div>
            <p class="disclaim">Answers are guidance, not a commitment. Refunds, billing and contractual
              questions need a <a href="tickets.html">ticket</a>.</p>
          </div>
        </section>
      </div>
"""

TICKETS = f"""
{phead("My Tickets", "Technical and commercial requests, tracked to resolution with a named assignee.",
       f'<a class="btn btn--sm" href="#">Create a ticket {ARROW}</a>')}
      <div class="stack">
{kpis([
    kpi("Pending", "0", "", "Awaiting first response", "solar:hourglass-linear"),
    kpi("Processing", "0", "", "With the platform team", "solar:refresh-linear"),
    kpi("Resolved", "0", "", "Last 90 days", "solar:check-circle-linear"),
    kpi("Median first response", "0", "h", "No tickets raised yet", "solar:clock-circle-linear"),
])}
{pnl("Tickets",
     '          ' + counts([("All", 0, True), ("Pending", 0, False), ("Processing", 0, False), ("Resolved", 0, False)]) +
     tbl(["Ticket no.", "Title", "Type", "Status", "Assignee", "Created"], [], 860) +
     empty("No tickets raised", "Raise one for anything the AI assistant cannot settle: refunds, billing, contract terms or a suspected platform fault.",
           "solar:ticket-linear", "Create a ticket"),
     flush=True)}
      </div>
"""

# =============================================================== ADMIN SCREENS
# Every row below is synthetic. See the module docstring.

ADMIN_FILTERS = f"""          <div class="fbar">
{sel("Environment", "All environments", "Sandbox", "Production")}
{sel("Developer account", "All developers", "northwind-ota", "voyage-labs", "meridian-tmc")}
{sel("Application", "All applications", "G-Link Hotel API", "F-Link Flight API", "TMC White Label")}
            <div class="fgrp" style="flex:0 0 auto;max-width:none"><label>Time range</label>
              {rail(["Today", "Last 7 days", "Last 30 days"], "Last 7 days")}</div>
            <span class="fbar-a"><a class="btn btn--ghost btn--sm" href="#">Reset</a>
              <a class="btn btn--sm" href="#">Search {ARROW}</a></span>
          </div>"""

ADMIN_DASHBOARD = f"""
{phead("Dashboard", "Requests, failure rate, search-to-booking ratio and slow endpoints across every developer on the platform.",
       f'<a class="btn btn--ghost btn--sm" href="admin-trace.html">Open request trace {ARROW}</a>')}
      <div class="stack">
        <section class="pnl">{ADMIN_FILTERS}</section>
{kpis([
    kpi("Total requests", "48,912", "", "312 failed in range", "solar:routing-2-linear"),
    kpi("Active developers", "23", "", "Of 60 registered", "solar:users-group-rounded-linear"),
    kpi("Active apps", "38", "", "Of 122 provisioned", "solar:widget-5-linear"),
    kpi("Search to booking", "2.4", "%", "1,174 bookings / 48,912 searches", "solar:cart-check-linear"),
])}
        <div class="g2">
{pnl("Calls by endpoint", "          " + bars([9200, 7400, 6100, 4800, 3900, 2600], ["search", "list", "detail", "avail", "order", "cancel"]), sub="Last 7 days")}
{pnl("Request volume", "          " + line([[5100, 6400, 7200, 6800, 8100, 7600, 7700]], ["09-02", "09-03", "09-04", "09-05", "09-06", "09-07", "09-08"]) + '<div class="legend"><span><i></i>Requests, all products</span></div>', sub="Last 7 days")}
        </div>
        <div class="g2">
{pnl("Request outcome", "          " + ring(99, "Succeeded against failed", "312 failures in 48,912 calls."))}
{pnl("Busiest endpoints", rank([("/openapi/v1/glink/search/hotelList", 9204), ("/openapi/v1/flink/flight/search", 7411), ("/openapi/v1/glink/booking/productDetails", 6088), ("/openapi/v1/tmc/employees/certificates", 4832), ("/openapi/v1/glink/booking/availabilityCheck", 3907)]), sub="Last 7 days", flush=True)}
        </div>
        <div class="g2">
{pnl("Slowest endpoints", rank([("/openapi/v1/glink/hotel/lowestPrice", 2140), ("/openapi/v1/flink/flight/search", 1680), ("/openapi/v1/glink/search/hotelList", 940)]), sub="Median milliseconds", flush=True)}
{pnl("Busiest developers", rank([("northwind-ota", 18420), ("voyage-labs", 11207), ("meridian-tmc", 8814), ("harbourline-travel", 6033)]), sub="Last 7 days", flush=True)}
        </div>
{pnl("Recent failures",
     tbl(["Request ID", "Endpoint", "Status", "Duration", "Time"],
         [[f'<span class="mono" style="font-size:11.5px">req_8f2c41d9</span>', '<span class="mono" style="font-size:11.5px">/openapi/v1/flink/flight/search</span>', st("Failed", "bad"), "51ms", "11:02"],
          [f'<span class="mono" style="font-size:11.5px">req_6b19ae02</span>', '<span class="mono" style="font-size:11.5px">/openapi/v1/glink/hotel/lowestPrice</span>', st("Failed", "bad"), "206ms", "10:20"],
          [f'<span class="mono" style="font-size:11.5px">req_2d70c5f4</span>', '<span class="mono" style="font-size:11.5px">/openapi/v1/glink/order/checkoutRequest</span>', st("Timeout", "warn"), "5,001ms", "09:48"]], 820),
     right='<a class="tlink" href="admin-trace.html">All traces ' + ARROW + '</a>', flush=True)}
      </div>
"""

USERS = [
    ("northwind-ota", "Northwind OTA", "Completed", "Approved", "8 Sept 2026"),
    ("voyage-labs", "Voyage Labs", "Completed", "Approved", "4 Sept 2026"),
    ("harbourline-travel", "Harbourline Travel", "Skipped", "Approved", "2 Sept 2026"),
    ("meridian-tmc", "Meridian TMC", "Completed", "Approved", "2 Sept 2026"),
    ("kestrel-holidays", "Kestrel Holidays", "Not completed", "Pending", "1 Sept 2026"),
    ("solstice-group", "Solstice Travel Group", "Not completed", "Pending", "31 Aug 2026"),
    ("atlas-corporate", "Atlas Corporate Travel", "Skipped", "Pending", "25 Aug 2026"),
]

ADMIN_USERS = f"""
{phead("User List", "Every registered developer account, its onboarding state and its access decision.",
       f'<a class="btn btn--ghost btn--sm" href="#">Refresh</a><a class="btn btn--sm" href="#">Export {ARROW}</a>')}
      <div class="stack">
{kpis([
    kpi("Registered", "60", "", "Developers and administrators", "solar:users-group-rounded-linear"),
    kpi("Pending review", "3", "", "Awaiting an access decision", "solar:hourglass-linear"),
    kpi("Approved", "56", "", "Sandbox or production", "solar:check-circle-linear"),
    kpi("Setup completed", "18", "", "Finished the onboarding questions", "solar:clipboard-check-linear"),
])}
{pnl("Accounts",
     '          ' + counts([("All users", 60, True), ("Pending", 3, False), ("Approved", 56, False), ("Rejected", 1, False)]) +
     tbl(["Account", "Company", "Onboarding", "Status", "Registered", ""],
         [[f'<span class="mono">{a}</span>', c,
           st(s, "ok" if s == "Completed" else ("warn" if s == "Skipped" else "")),
           pill(d, "ok" if d == "Approved" else "warn"), r,
           '<span class="tact"><button type="button">Open</button>'
           '<button type="button" class="danger">Disable</button></span>']
          for a, c, s, d, r in USERS], 940),
     sub="60 records", right='<span class="pill pill--q">Developers</span><span class="pill pill--q">Administrators</span>', flush=True)}
{tfoot(7, 60)}
      </div>
"""

# app, developer, provider, environment, status, kind, applied, waiting
REVIEWS = [
    ("G-Link Hotel API", "northwind-ota", "GLINK", "Production", "Production live", "ok", "8 Sept", "—"),
    ("F-Link Flight API", "northwind-ota", "FLINK", "Sandbox", "Sandbox enabled", "ok", "8 Sept", "—"),
    ("TMC White Label", "meridian-tmc", "TMC", "Sandbox", "Sandbox enabled", "ok", "4 Sept", "—"),
    ("G-Link Hotel API", "kestrel-holidays", "GLINK", "Sandbox", "Pending sandbox", "warn", "1 Sept", "7 days"),
    ("F-Link Flight API", "solstice-group", "FLINK", "Sandbox", "Pending sandbox", "warn", "31 Aug", "8 days"),
    ("G-Link Hotel API", "voyage-labs", "GLINK", "Production", "Pending production approval", "warn", "4 Sept", "4 days"),
    ("TMC White Label", "atlas-corporate", "TMC", "Sandbox", "Frozen", "bad", "25 Aug", "—"),
]

ADMIN_REVIEW = f"""
{phead("App Review", "Access requests across all three products, from first sandbox key through to production sign-off.",
       f'<a class="btn btn--ghost btn--sm" href="#">Upload customer info form</a><a class="btn btn--sm" href="#">Review queue {ARROW}</a>')}
      <div class="stack">
{kpis([
    kpi("Access requests", "122", "", "All products, all states", "solar:clipboard-list-linear"),
    kpi("Pending sandbox", "10", "", "Waiting on activation", "solar:hourglass-linear"),
    kpi("Pending production", "4", "", "Waiting on approval", "solar:shield-check-linear"),
    kpi("Production live", "7", "", "Billed on usage", "solar:check-circle-linear"),
])}
{pnl("Access requests",
     '          ' + counts([("All", 122, True), ("Pending sandbox", 10, False), ("Sandbox enabled", 101, False),
                            ("Pending production", 4, False), ("Production live", 7, False), ("Frozen", 0, False)]) +
     tbl(["App", "Developer", "Provider", "Environment", "Status", "Applied", "Waiting", ""],
         [[f'{a}<br><span class="mono" style="font-size:11px;color:var(--muted)">{a.lower().replace(" ", "-")}</span>',
           f'<span class="mono">{d}</span>', f'<span class="mono">{p}</span>', e, st(s, k), ap,
           f'<span class="mono"{" style=\"color:var(--warn)\"" if w != "—" else ""}>{w}</span>',
           '<span class="tact"><button type="button">Edit credentials</button>'
           + ('<button type="button" class="danger">Freeze</button>' if k == "ok"
              else '<button type="button">Unfreeze</button>' if s == "Frozen"
              else '<button type="button">Approve</button>') + "</span>"]
          for a, d, p, e, s, k, ap, w in REVIEWS], 1120),
     sub="122 records", flush=True)}
{tfoot(7, 122)}
      </div>
"""

TICKET_ROWS = [
    ("TK20260904784409", "Sandbox flight search returns success with a null payload on every route", "Technical", "Processing", "warn"),
    ("TK20260826499187", "Flight results appear intermittently, is there a maintenance window", "Technical", "Processing", "warn"),
    ("TK20260825063142", "Lowest-price response is empty for future dates", "Technical", "Processing", "warn"),
    ("TK20260812820215", "Two callback URLs on one application", "Commercial", "Pending", ""),
    ("TK20260731820378", "Standardised field and enum definitions across TMC endpoints", "Technical", "Resolved", "ok"),
]

ADMIN_TICKETS = f"""
{phead("Ticket List", "Every developer ticket on the platform. Open one to reply, reassign or resolve it.",
       f'<a class="btn btn--ghost btn--sm" href="#">Export</a>')}
      <div class="stack">
{kpis([
    kpi("Pending", "3", "", "No first response yet", "solar:hourglass-linear"),
    kpi("Processing", "6", "", "Assigned and in progress", "solar:refresh-linear"),
    kpi("Resolved", "7", "", "Last 90 days", "solar:check-circle-linear"),
    kpi("Median first response", "4.2", "h", "Against a 8h target", "solar:clock-circle-linear"),
])}
{pnl("Tickets",
     '          ' + counts([("All tickets", 16, True), ("Pending", 3, False), ("Processing", 6, False), ("Resolved", 7, False)]) +
     tbl(["Ticket no.", "Title", "Type", "Status", "Assignee", ""],
         [[f'<span class="mono" style="font-size:11.5px">{no}</span>', t, ty, st(s, k), "admin",
           '<span class="tact"><button type="button">Open</button>'
           '<button type="button" class="q">Transfer</button></span>']
          for no, t, ty, s, k in TICKET_ROWS], 980),
     sub="16 tickets", flush=True)}
{tfoot(5, 16)}
      </div>
"""

TRACE_ROWS = [
    ("trc_9a41c0e2", "Sandbox", "/openapi/v1/tmc/employees/870/certificates", "Success", "ok", "66ms", "tmc-white-label", "12:20:52"),
    ("trc_9a41bd77", "Sandbox", "/openapi/v1/tmc/employees/981/certificates", "Success", "ok", "67ms", "tmc-white-label", "12:20:52"),
    ("trc_9a41b902", "Production", "/openapi/v1/glink/search/hotelList", "Success", "ok", "412ms", "glink-hotel", "12:19:03"),
    ("trc_9a41a5be", "Production", "/openapi/v1/glink/hotel/lowestPrice", "Failed", "bad", "206ms", "glink-hotel", "12:18:44"),
    ("trc_9a419f10", "Sandbox", "/openapi/v1/flink/flight/search", "Timeout", "warn", "5,001ms", "flink-flight", "12:17:59"),
]

ADMIN_TRACE = f"""
{phead("Request Trace", "Every call on the platform, filterable down to one developer, one endpoint and one latency band.",
       f'<a class="btn btn--ghost btn--sm" href="#">Export CSV</a>')}
      <div class="stack">
        <section class="pnl">
          <div class="fbar">
{sel("Developer account", "All developers", "northwind-ota", "voyage-labs", "meridian-tmc")}
{sel("Application", "All applications", "glink-hotel", "flink-flight", "tmc-white-label")}
{sel("Environment", "All environments", "Sandbox", "Production")}
{sel("Product", "All products", "G-Link", "F-Link", "TMC")}
{sel("Status", "All statuses", "Success", "Failed", "Timeout")}
{sel("Latency", "All latencies", "Under 200ms", "200ms to 1s", "Over 1s")}
            <span class="fbar-a"><a class="btn btn--ghost btn--sm" href="#">Reset</a>
              <a class="btn btn--sm" href="#">Search {ARROW}</a></span>
          </div>
        </section>
{kpis([
    kpi("Total requests", "48,912", "", "Last 7 days", "solar:routing-2-linear"),
    kpi("Failures", "312", "", "0.6% of calls", "solar:danger-triangle-linear"),
    kpi("Timeouts", "27", "", "Over the 5s ceiling", "solar:clock-circle-linear"),
    kpi("Median latency", "148", "ms", "Across all endpoints", "solar:graph-linear"),
])}
{pnl("Requests",
     tbl(["Trace ID", "Env", "Path", "Status", "Duration", "Application", "Time"],
         [[f'<span class="mono" style="font-size:11.5px">{i}</span>', e,
           f'<span class="mono" style="font-size:11.5px">{p}</span>', st(s, k), f'<span class="mono">{d}</span>',
           f'<span class="mono" style="font-size:11.5px">{a}</span>', f'<span class="mono">{t}</span>']
          for i, e, p, s, k, d, a, t in TRACE_ROWS], 1040),
     sub="100 loaded", flush=True)}
{tfoot(5, 100)}
{pnl("Request detail",
     f'''          <div class="kv" style="margin-bottom:18px">
            <div><span class="k">Trace</span><span class="v mono">trc_9a41a5be</span></div>
            <div><span class="k">Endpoint</span><span class="v mono">POST /openapi/v1/glink/hotel/lowestPrice</span></div>
            <div><span class="k">Outcome</span><span class="v">{st("Failed", "bad")} <span style="color:var(--muted)">422 after 206ms</span></span></div>
            <div><span class="k">Developer</span><span class="v mono">northwind-ota &middot; glink-hotel &middot; production</span></div>
          </div>
          <div class="note"><iconify-icon icon="solar:danger-triangle-linear"></iconify-icon>
            <span><strong>Check-in date is in the past.</strong> The lowest-price endpoint rejects a stay that
            has already started. Error <span class="mono">GL-1042</span>; the caller should validate the date
            against the property time zone, not the server clock.</span></div>
          <div class="g2" style="margin-top:18px">
            <div><p class="kpi-k" style="margin-bottom:9px">Request</p>
              <div class="pane">{{
  "hotelId": "GL-88213",
  "checkIn": "2026-09-01",
  "checkOut": "2026-09-03",
  "rooms": 1
}}</div></div>
            <div><p class="kpi-k" style="margin-bottom:9px">Response</p>
              <div class="pane">{{
  "code": "GL-1042",
  "message": "checkIn must be a future date",
  "traceId": "trc_9a41a5be"
}}</div></div>
          </div>''',
     sub="The row selected above",
     right='<a class="tlink" href="../api-docs-errors.html">Error code reference ' + ARROW + '</a>')}
      </div>
"""

SDK_MGMT_ROWS = [
    ("Tmc Java SDK", "tmc-sdk-java", "tmc-white-label", "Java", "30 July 2026"),
    ("Tmc Python SDK", "tmc-sdk-python", "tmc-white-label", "Python", "30 July 2026"),
    ("Open Platform Go SDK", "tmc-go-sdk", "tmc-white-label", "Go", "30 July 2026"),
    ("Glink Hotel Python SDK", "glink-sdk-python", "glink-hotel", "Python", "13 July 2026"),
    ("Glink Hotel Java SDK", "glink-sdk-java", "glink-hotel", "Java", "13 July 2026"),
    ("Open Platform Go SDK", "open-platform-go-sdk", "glink-hotel", "Go", "13 July 2026"),
    ("Flink Flight Python SDK", "flink-sdk-python", "flink-flight", "Python", "29 April 2026"),
    ("Flink Flight Java SDK", "flink-sdk-java", "flink-flight", "Java", "29 April 2026"),
]

ADMIN_SDK = f"""
{phead("SDK Management", "Publish, version and retire the SDK packages developers install.",
       f'<a class="btn btn--ghost btn--sm" href="#">Refresh</a><a class="btn btn--sm" href="#">Create a package {ARROW}</a>')}
      <div class="stack">
{pnl("SDK packages",
     tbl(["Package", "Identifier", "Product", "Language", "Status", "Updated", ""],
         [[n, f'<span class="mono">{i}</span>', f'<span class="mono">{p}</span>', l, st("Active", "ok"), u,
           '<span class="tact"><button type="button">Edit</button><button type="button">Upload version</button>'
           '<button type="button" class="q">Versions</button></span>']
          for n, i, p, l, u in SDK_MGMT_ROWS], 1060),
     sub="8 packages", flush=True)}
      </div>
"""

DOCS_ROWS = [
    ("v1.0.9", "glink-api.en-US.json", "glink-hotel", "en-US", 28, "8 July 2026"),
    ("v1.0.9", "glink-api.zh-CN.json", "glink-hotel", "zh-CN", 28, "8 July 2026"),
    ("v1.0.9", "glink-api.zh-TW.json", "glink-hotel", "zh-TW", 28, "8 July 2026"),
    ("v1.0.0", "tmc-api.en-US.json", "tmc-api", "en-US", 95, "7 August 2026"),
    ("v1.0.0", "tmc-api.zh-CN.json", "tmc-api", "zh-CN", 95, "7 August 2026"),
    ("v1.0.0", "tmc-api.zh-TW.json", "tmc-api", "zh-TW", 95, "7 August 2026"),
]

ADMIN_DOCS = f"""
{phead("Docs Management", "Import a Swagger file to generate API reference pages, then publish them to the live docs.",
       f'<a class="btn btn--ghost btn--sm" href="#">Create a guide page</a><a class="btn btn--sm" href="#">Upload Swagger {ARROW}</a>')}
      <div class="stack">
{kpis([
    kpi("Swagger versions", "37", "", "Across three products", "solar:file-check-linear"),
    kpi("Guide pages", "55", "", "Hand-written, three locales", "solar:documents-linear"),
    kpi("Endpoints documented", "218", "", "Generated from Swagger", "solar:code-square-linear"),
    kpi("Locales", "3", "", "en-US, zh-CN, zh-TW", "solar:global-linear"),
])}
{pnl("Swagger versions",
     '          ' + counts([("Swagger versions", 37, True), ("Guide pages", 55, False)]) +
     tbl(["Version", "File", "Product", "Locale", "Endpoints", "Status", "Uploaded", ""],
         [[f'<span class="mono">{v}</span>', f'<span class="mono" style="font-size:11.5px">{f}</span>',
           f'<span class="mono">{p}</span>', f'<span class="mono">{l}</span>', str(e), st("Published", "ok"), u,
           '<span class="tact"><button type="button">Update</button><button type="button">Detail</button>'
           '<button type="button" class="q">Publish</button></span>']
          for v, f, p, l, e, u in DOCS_ROWS], 1100),
     sub="37 versions", flush=True)}
{tfoot(6, 37)}
      </div>
"""

# ------------------------------------------------------------------ registry

from console_nav import DEV_NAV, ADMIN_NAV  # noqa: E402
from build_console_globe import GLOBE_LIB  # noqa: E402

_D = dict(nav=DEV_NAV, who="developer", initials="D", role="Sandbox")
_A = dict(nav=ADMIN_NAV, who="admin", initials="C", role="Platform admin")

SCREENS = [
    dict(slug="index", active="console", title="Console — Open Developer Platform",
         desc="Request volume, success rate and search-to-booking ratio across your applications.", body=CONSOLE, **_D),
    dict(slug="getting-started", active="getting-started", title="Getting Started — Open Developer Platform",
         desc="The five G-Link calls that take an integration from nothing to a first sandbox booking.", body=GETTING_STARTED, **_D),
    dict(slug="app-management", active="apps", title="App Management — Open Developer Platform",
         desc="One credential set per product, sandbox and production kept separate.", body=APP_MANAGEMENT, **_D),
    dict(slug="sandbox", active="sandbox", title="Sandbox Environment — Open Developer Platform",
         desc="Validate integration logic against real API behaviour without touching production data.", body=SANDBOX, **_D),
    dict(slug="trace", active="trace", title="Request Trace — Open Developer Platform",
         desc="Every API call your applications make, with payload, timing and failure reason.", body=TRACE, **_D),
    dict(slug="coverage", active="coverage", title="Coverage Map — Open Developer Platform",
         desc="Bookable properties by country and region, plotted on WGS84 coordinates.",
         body=COVERAGE, extra=GLOBE_LIB + COVERAGE_JS, **_D),
    dict(slug="hotel-mapping", active="mapping", title="Hotel Mapping — Open Developer Platform",
         desc="Match your own property inventory to platform hotel IDs by uploading a CSV.", body=MAPPING, **_D),
    dict(slug="hotel-orders", active="horders", title="Hotel Orders — Open Developer Platform",
         desc="Every hotel booking made through your applications, sandbox and production.", body=HOTEL_ORDERS, **_D),
    dict(slug="flight-orders", active="forders", title="Flight Orders — Open Developer Platform",
         desc="Every ticket issued through your applications, with passenger and contact details.", body=FLIGHT_ORDERS, **_D),
    dict(slug="tmc-builder", active="tmc", title="Build My TMC — Open Developer Platform",
         desc="Pick a white-label homepage template, then configure brand, policy and suppliers.", body=TMC_BUILDER, **_D),
    dict(slug="sdk", active="sdk", title="SDK — Open Developer Platform",
         desc="Eight published SDKs across three products, with install commands and changelogs.", body=SDK, **_D),
    dict(slug="skills", active="skills", title="Skills — Open Developer Platform",
         desc="Official skill packages that teach an AI coding assistant how these APIs behave.", body=SKILLS, **_D),
    dict(slug="ai-assistant", active="ai", title="AI Assistant — Open Developer Platform",
         desc="Ask about signing, pagination, order state machines, webhooks and error codes.",
         body=AI_ASSISTANT, page_cls="page--full", **_D),
    dict(slug="tickets", active="tickets", title="My Tickets — Open Developer Platform",
         desc="Technical and commercial requests, tracked to resolution with a named assignee.", body=TICKETS, **_D),

    dict(slug="admin-dashboard", active="dashboard", title="Admin Dashboard — Open Developer Platform",
         desc="Requests, failure rate and slow endpoints across every developer on the platform.", body=ADMIN_DASHBOARD, **_A),
    dict(slug="admin-user-list", active="users", title="User List — Open Developer Platform",
         desc="Every registered developer account, its onboarding state and its access decision.", body=ADMIN_USERS, **_A),
    dict(slug="admin-app-review", active="review", title="App Review — Open Developer Platform",
         desc="Access requests from first sandbox key through to production sign-off.", body=ADMIN_REVIEW, **_A),
    dict(slug="admin-ticket-list", active="atickets", title="Ticket List — Open Developer Platform",
         desc="Every developer ticket on the platform, with assignee and response time.", body=ADMIN_TICKETS, **_A),
    dict(slug="admin-trace", active="atrace", title="Platform Request Trace — Open Developer Platform",
         desc="Every call on the platform, filterable by developer, endpoint and latency band.", body=ADMIN_TRACE, **_A),
    dict(slug="admin-sdk-management", active="asdk", title="SDK Management — Open Developer Platform",
         desc="Publish, version and retire the SDK packages developers install.", body=ADMIN_SDK, **_A),
    dict(slug="admin-docs-management", active="adocs", title="Docs Management — Open Developer Platform",
         desc="Import Swagger to generate API reference pages, then publish them to the live docs.", body=ADMIN_DOCS, **_A),
]
