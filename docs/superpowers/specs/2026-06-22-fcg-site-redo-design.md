# FCG Website Redo — Design Spec

**Date:** 2026-06-22
**Status:** Approved (design) — pending written-spec review
**Scope:** Full site — restructure + visual redesign + copy rewrite + BTS event pages
**Hard deadline:** Before BTS London, Jun 24 2026 (~2 days from spec date)

---

## Goal

Restructure, redesign, and rewrite the FCG marketing site onto a new 4-item
navigation and the codified FCG design system, AND ship the two BTS event pages
(China-supply landing + Payment) — all before BTS London (Jun 24). This is a
**rollout**, not a visual exploration — the design direction is already locked
(design-system doc + the in-progress golden draft). Copy is rewritten to the FCG
brand voice (`docs/FCG Open Design System Prompt.md`, voice section).

## One deadline, all 12 equal

Everything ships before BTS. No tiering — once the template is locked, all 12
pages fan out in parallel at equal priority for maximum throughput.

**Risk (accepted by Crystal):** with ~2 days and no tiering, if the window runs
short the shortfall lands on an arbitrary page rather than a back-of-house one —
including, potentially, an event-facing page (BTS landing / Payment).

## Locked navigation IA

Top-level: **Products · Network · Developer · About**
(the old "Solutions" dropdown is removed entirely.)

| Tab | Behaviour | Contents |
|---|---|---|
| **Products** | Mega-menu, grouped *Front / Mid / Back* (group name TBD) | Front → CBT, AI-BT, RFP · Mid → AtlasOS · Back → G-Link, F-Link |
| **Network** | Dropdown → 2 separate pages | ADDN, Payment *(Payment page = Track A)* |
| **Developer** | Direct link, no dropdown | repurposed from `api-access.html` |
| **About** | Direct link, no dropdown | Corporate intro · FCG [second item TBD] |

## Page inventory (this build)

| Action | Page | Source |
|---|---|---|
| Keep → redesign + rewrite | Home | `index.html` |
| Keep → redesign + rewrite | About | `about.html` |
| Keep → redesign + rewrite | CBT (Front) | `corporate-booking-tool.html` |
| Keep → redesign + rewrite | AI-BT (Front) | `ai-booking-tool.html` |
| Keep → redesign + rewrite | RFP (Front) | `agreeease.html` |
| Keep → redesign + rewrite | AtlasOS (Mid) | `atlas.html` |
| New | G-Link (Back) | `drafts/glink-*` |
| New | F-Link (Back) | `drafts/flink-*` |
| New | ADDN (Network) | — |
| Repurpose | Developer | `api-access.html` |
| New | Payment (Network) | gap analysis §4 |
| New | BTS landing (standalone, not in main nav) | gap analysis §3 |
| Remove (archive, do not delete) | Whitelabel | `whitelabel.html` |
| Remove (archive, do not delete) | Advisory & Implementation | `advisory-implementation.html` |
| Remove (archive, do not delete) | AI Mapping | `ai-mapping.html` |
| Remove (archive, do not delete) | Agent Booking Tool | `agent-booking-tool.html` |
| Internal, untouched | Components library | `components.html` |

**Ships 12 pages:** Home, About, CBT, AI-BT, RFP, AtlasOS, G-Link, F-Link, ADDN,
Developer, Payment, BTS landing.

## Plan — deadline-driven, template-then-fan-out

The template is the critical path; everything else parallelises behind it.

| Phase | Scope | Depends on |
|---|---|---|
| **0 — Foundation (critical path, do first)** | Resolve the open items below; pin the golden reference page; build the new 4-item nav (Products mega-menu w/ Front/Mid/Back; Network dropdown; Developer + About direct links); extract shared header/footer as one reusable template; archive the 4 removed pages. | — |
| **1 — Parallel fan-out** | All 12 pages built against the locked template, in parallel at equal priority. Each page = redesign to golden + copy rewrite. | Phase 0 |

**Why template-first:** front-loads the one decision every page copies, so the
fan-out is mechanical and the header/nav isn't rebuilt 12 times.

## Open items (resolve at Phase 0 start — non-blocking for this spec)

1. ~~Golden reference page.~~ **RESOLVED:** `index-v4.html` for Home;
   `flink-v7` / `glink-v7` / `tmc-api-v7` for product pages. The v6 edits from
   Jun 22 are not the template.
2. **Front / Mid / Back group name** — placeholder; needs a nicer label.
3. **`O-T` / `O-G` / `O-F` tags** — "open platform … API" (O-T = open platform
   TMC API). Decide how/where these surface (likely Developer + product pages).
4. **Red double-underlines** on the sketch (CBT, "Open") — priority markers?
5. **About second item** ("FCG [?]") — confirm label.

## Success criteria

- Every shipped page links the same shared header/footer/nav template — change
  the nav once, it changes everywhere.
- Nav matches the locked IA exactly (4 tabs; removed pages gone from nav).
- Copy on every shipped page follows the FCG voice rules (no banned words; voice
  per design-system doc).
- The 4 removed pages are archived (not deleted) and unlinked from nav.
- Each page visually matches the pinned golden reference.

## Out of scope

- Re-architecture (stays hand-written static HTML — no framework/SSG).
- New visual direction (the design system is the answer).
- Whitelabel, Advisory, AI Mapping, Agent Booking Tool, and the former
  gap-analysis Solutions pages (Sourcing in China, Global Sourcing, Property
  Hosting) — all out of this build.
- Product videos and the physical flyer (gap analysis §5) — separate deliverables.
