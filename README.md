# FCG Website

This folder contains the working copy of the FCG marketing website.

## Folder Structure

- Top-level `.html` files are the current live website pages.
- `drafts/` contains the newest active draft versions that are not live yet.
- `working-versions/` contains older saved versions and reference experiments.
- `assets/` contains shared CSS, images, logos, and product visuals.
- `components/` contains reusable section and component experiments.
- `reference/` contains brand, product, design, and positioning notes.
- `design-archive/` contains historical design extraction and comparison files.
- `outputs/` contains generated review files, reports, and supporting scripts.

## Current Live Pages

The 4-item nav (Products · Network · Developer · About) links these root pages. All page copy/figures are aligned to the company deck (the source of truth — see `reference/FCG_Knowledge_Base.md`).

- `index.html` — home
- `about.html`
- Products: `corporate-booking-tool.html`, `ai-booking-tool.html`, `agreeease.html`, `atlas.html`, `glink.html`, `flink.html`
- Network: `addn.html`, `payment.html`
- `developer.html` — Developer Platform (canon; the old `api-access.html` is archived)
- `components.html` — shared component reference

Archived (in `archive/`, not deployed): `api-access.html`, `whitelabel.html`, `agent-booking-tool.html`, `advisory-implementation.html`, `ai-mapping.html`, `bts.html` (Business Travel Show London event page, June 2026; HubSpot embed removed with the HubSpot exit).

## Draft Workflow

Keep only the latest active draft for each page in `drafts/`. Move older draft versions into the matching folder inside `working-versions/`.

## Working Workflow

1. Ask Codex to make a small website change.
2. Preview the site locally.
3. Approve the change if it looks right.
4. Ask Codex to commit the change.
5. Ask Codex to push the change to GitHub only when ready.

The GitHub repository should stay private until explicitly approved for public release.
