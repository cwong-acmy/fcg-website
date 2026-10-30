# FCG Ad Studio (standalone)

The team's place to make on-brand FCG posts, blog covers and video stills, and export PNGs.
Design rules: the FCG design bible (FCG Internal Wiki, "Design bible (creative direction)").

- No outside requests: fonts (Inter, Caveat), the export library (modern-screenshot 4.7.0) and the Calendly reference frames ship in this folder.
- Export uses the browser's own renderer (SVG foreignObject), checks Inter has loaded, then downloads the PNG.
- Work autosaves to the browser (localStorage). "Copy link" shares one template's setup without photos; links are validated on load.
- Deploy: work Vercel team, project `fcg-ad-studio`, static, no build step.
  `VERCEL_TOKEN` from 1Password `op://LLM Automations/g2zgsv4azlxe7kiz7oewvogevy/credential`, then `vercel deploy --prod --yes` from this folder.
- Source of record is this folder. `02.FCG/03.Brand Assets/06.Ad Templates/fcg-ad-studio.html` is the older single-file version.
