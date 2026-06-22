# FCG Website Redo — Design Spec

**Date:** 2026-06-22
**Status:** Approved (design) — pending written-spec review
**Scope:** Track B — main-site restructure + visual redesign + copy rewrite

---

## Goal

Restructure, redesign, and rewrite the FCG marketing site onto a new 4-item
navigation and the codified FCG design system. This is a **rollout**, not a
visual exploration — the design direction is already locked (design-system doc +
the in-progress golden draft). Copy is rewritten to the FCG brand voice
(`docs/FCG Open Design System Prompt.md`, voice section).

## Two-track context

This site work splits into two tracks on different clocks. This spec covers
**Track B only**.

- **Track A** — BTS London event pages (BTS China-supply landing + Payment),
  deadline Jun 24–25 2026. Specced separately, built after Track B per the
  decided order (B then A). The **Payment** nav slot exists in Track B's nav,
  but the Payment page itself is a Track A deliverable.
- **Track B** — this spec.

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
| Deferred (Track A) — nav slot only | Payment (Network) | — |
| Remove (archive, do not delete) | Whitelabel | `whitelabel.html` |
| Remove (archive, do not delete) | Advisory & Implementation | `advisory-implementation.html` |
| Remove (archive, do not delete) | AI Mapping | `ai-mapping.html` |
| Remove (archive, do not delete) | Agent Booking Tool | `agent-booking-tool.html` |
| Internal, untouched | Components library | `components.html` |

**Track B ships 10 pages:** Home, About, CBT, AI-BT, RFP, AtlasOS, G-Link,
F-Link, ADDN, Developer. (Payment nav slot present; page built in Track A.)

## Phased plan

Each phase = its own plan → build → review.

| Phase | Scope | Depends on |
|---|---|---|
| **0 — Foundation** | Pin the golden reference page; build the new 4-item nav (Products mega-menu w/ Front/Mid/Back; Network dropdown; Developer + About direct links); extract shared header/footer as one reusable template; archive the 4 removed pages. | — |
| **1 — Spine** | Home + About → golden quality + copy rewrite. | Phase 0 template |
| **2 — Products** | CBT, AI-BT, RFP, AtlasOS, G-Link, F-Link → each to golden + rewrite. | Phase 0 template |
| **3 — Network + Developer** | ADDN page; Developer hub (from api-access); Payment nav slot wired (page deferred to Track A). | Phase 0 nav |

**Why spine-first:** front-loads the one decision everything copies (the
template), so Phase 2 is mechanical and the header isn't rebuilt 10 times.

## Open items (resolve at Phase 0 start — non-blocking for this spec)

1. **Golden reference page.** Version numbers aren't chronological: freshest
   work (Jun 22) is on `flink-v6`, `glink-v6`, `whitelabel-v2/v3`; the `v7`
   files are untouched since Jun 9. Pick the approved template before rollout.
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
- Track A pages (BTS landing, Payment page build).
- Whitelabel, Advisory, AI Mapping, Agent Booking Tool, and the former
  gap-analysis Solutions pages (Sourcing in China, Global Sourcing, Property
  Hosting) — all out of this build.
