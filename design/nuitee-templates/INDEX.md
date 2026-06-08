# Nuitee layout library → FCG templates

A catalog of the layout/section patterns nuitee.com uses, deduplicated across page types,
mapped to FCG's existing component system and brand voice. Use it to assemble lean,
un-wordy FCG pages without inventing new structures or copy.

**Source pages indexed (2026-06-08):** `/` · `/connect` · `/connect/liteapi-enterprise` · `/solutions/independent-hotels` · `/about-us` · `/insights`

**The nuitee discipline (what we're borrowing — layout only, not their copy or colour):**
- Headlines 4–7 words. One clarifier line per section, never a paragraph.
- 60–70% whitespace. Icon + short label + one line carries meaning; structure does the explaining.
- Card-and-grid modularity over narrative flow.
- One primary action per section.

> **FCG styling rule for every template:** tokens from [DESIGN.md](../../reference/DESIGN.md) + the live [fcg-brand-theme.css](../../assets/css/fcg-brand-theme.css) (dark-first: `#080805` bg, `#f7f7f2` fg, `#f97316` accent — rare). Voice from [brand-voice.md](../../reference/brand-voice.md): sentence case, system-described (no "you" in heads), pill buttons, banned-word list, run the §12 checklist before any copy ships. Templates are **greyboxed** — structure + labelled copy slots, no real copy or fake assets.

---

## Section archetypes

Each row → one greyboxed template file in `sections/`. Status: ✅ built · ⬜ pending sign-off.

| # | Template | What it is (structure) | Copy density | FCG component / class analog | Status |
|---|---|---|---|---|---|
| 01 | `hero-centered` | Single column, centered. Pill + short headline + 1 clarifier + 2 CTAs (+ optional product shot) | ~30% text | `.fcg-default-hero` | ✅ |
| 02 | `hero-split` | Copy left, product visual right | ~35% text | `.fcg-hero2` / `.fcg-tailark-hero` | ✅ |
| 03 | `logo-strip` | Row of 5 trust logos, ~1 line label | ~5% text | `.partner-grid-section` / `.partner-logo-card` | ✅ |
| 04 | `pathway-cards-3up` | Section head + 3 cards (icon + 1–3 word title + one line + see-link) | ultra-lean | `.product-card` grid | ✅ |
| 05 | `value-grid-2x2` | 2×2 value props, icon + headline + short copy | ~40% text | `.product-card` / `.fcg-bento-card` | ✅ |
| 06 | `feature-tabs` | Chip/tab rail drives one rotating viewport (deep-dive) | ~35% text | `.fcg-feature108` / `.fcg-showcase` tabs | ✅ |
| 07 | `feature-split` | Image one side, stacked feature list the other | moderate | `.fcg-showcase` split | ✅ |
| 08 | `stats-band` | Row of KPI numerals + mono captions | moderate | `.about3-stat` / stat tile | ✅ |
| 09 | `statement-band` | One centered outcome/claim, heavy whitespace | minimal | `.fcg-marketing-section` | ✅ |
| 10 | `steps-howitworks` | Sequential numbered steps (3–4), stacked | high whitespace | `.fcg-flow-step` | ✅ |
| 11 | `solutions-tile-grid` | Dense segment tiles (icon + 2–3 word title + one line) | sparse | `.product-card` dense grid | ✅ |
| 12 | `testimonial-quote` | Logo + pull-quote + attribution | high whitespace | pull-quote card | ✅ |
| 13 | `faq-accordion` | Stacked Q&A, single-open | moderate | `.accordion` | ✅ |
| 14 | `article-card-grid` | Featured article + category sections of cards | low/card | case-study / card | ✅ |
| 15 | `final-cta-band` | Closing `>` prompt + headline + primary/secondary CTA | minimal | `.fcg-final-cta` | ✅ |

Nav and footer are **not** templated here — reuse the existing site's nav/footer markup so they stay consistent.

---

## Page-type recipes

How nuitee composes each page type, as an FCG section stack. Build a new page by stacking these templates in order.

**Homepage** (`/`)
`hero-centered` → `logo-strip` → `pathway-cards-3up` → `feature-tabs` → `solutions-tile-grid` → `testimonial-quote` → `final-cta-band`

**Product hub** (`/connect`, `/cloud`, `/cupid` → FCG: G-Link / Atlas / api-access landing)
`hero-centered` → `logo-strip` → `value-grid-2x2` → `feature-tabs` → `pathway-cards-3up` (sub-products) → `final-cta-band`

**Product detail** (`/connect/liteapi-enterprise` → FCG: a single product page)
`hero-split` → `value-grid-2x2` → `statement-band` → `feature-split` ×N (alternating) → `final-cta-band`

**Segment / audience landing** (`/solutions/*` → FCG: For TMCs / For builders / For operators)
`hero-centered` → `statement-band` (outcome) → `value-grid-2x2` (pain points) → `feature-split` (recommended bundle) → `steps-howitworks` → `stats-band` (outcomes) → `testimonial-quote` → `faq-accordion` → `final-cta-band`

**About / company** (`/about-us`)
`hero-centered` (mission) → `stats-band` (origins) → `value-grid-2x2` (core values) → `steps-howitworks` (milestones timeline) → `statement-band` (culture) → `final-cta-band`

**Insights / content listing** (`/insights`)
`hero-centered` (page title) → `article-card-grid` (featured + category sections) → `final-cta-band`

---

## How to use

1. Pick a page-type recipe above.
2. Copy the listed section templates from `sections/` into a new page, in order.
3. Wire in the real nav + footer from an existing live page.
4. Fill copy against [brand-voice.md](../../reference/brand-voice.md) — replace every `[slot]`, keep one clarifier per section.
5. Swap greybox `.gb` boxes for **real** product screenshots / the FCG logo — never CSS/SVG fakes.
6. Run the §12 voice checklist + anti-slop guardrails before it leaves draft.

_Each `sections/*.html` previews standalone via `template-shell.css`. The shell mirrors the live theme tokens so greyboxes read in true FCG dark-first style._
