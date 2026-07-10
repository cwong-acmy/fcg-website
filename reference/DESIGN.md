# FCG Design System

Reproduced from the `hostmyclaudehtml.com` design extract (`03.Code Projects/design lang/hostmyclaudehtml-com/`). Live preview: [components.html](components.html).

**Library:** shadcn/ui (0.65 confidence) · **Material:** flat · **Voice:** neutral, you-only, Title Case, tight

---

## 1. Tokens

### Color

| Role | Hex | Use |
|---|---|---|
| `primary` | `#111827` | Buttons, headings, dark surfaces |
| `accent` | `#f97316` | Emphasis spans, hover, glow, status dots |
| `fg` | `#0f1114` | Body text on light |
| `bg` | `#ffffff` | Default page background |
| `bg-soft` | `#f3f4f6` | Icon tiles, soft cards |
| `card-dark` | `#121212` | Dark cards |
| `muted` | `#6b7280` | Secondary text, links |
| `muted-2` | `#4b5563` | Body copy on light cards |
| `border` | `#e5e7eb` | Card outlines, dividers |
| `border-dark` | `#2a2a2a` | Outlines on dark cards |

> ⚠️ `#6b7280` on `#f3f4f6` fails WCAG AA (4.39:1). Avoid that pairing for body text.

### Type — Inter (primary), JetBrains Mono (meta)

| Token | Size | Weight | LH | Tracking |
|---|---|---|---|---|
| Display H1 | 96px | 500 | 1.0 | -0.05em |
| Headline H2 | 72px | 500 | 1.0 | -0.05em |
| Section H3 | 48px | 500 | 1.0 | -0.025em |
| Subsection H4 | 30px | 500 | 1.2 | -0.025em |
| Body lg | 18px | 300 | 1.55 | 0 |
| Body | 14px | 400 | 1.5 | 0 |
| Mono | 12px | 400 | 1.3 | 0.05em (uppercase) |

Hero scales mobile→desktop: `48 → 72 → 96`.

### Spacing — base 2px

`1, 16, 24, 32, 40, 48, 64, 80, 96, 128, 136, 160, 192, 256`. Cards pad **40px**, soft cards pad **16px**, nav pads **16/32**.

### Radius

| Token | Value | Used on |
|---|---|---|
| xs | 2px | Inputs, fine details |
| md | 8px | Icon tiles, meta strips |
| xl | 24px | Mid containers |
| 2xl | **32px** | **Primary card** (75 instances) |
| pill | 9999px | **Buttons, nav, badges** (92 instances) |

### Elevation — flat material

```css
--shadow-card: rgba(0,0,0,0.15) 0px 0px 10px 0px;
--shadow-xl:   rgba(0,0,0,0.10) 0px 20px 25px -5px,
               rgba(0,0,0,0.08) 0px 8px 10px -6px;
--shadow-glow-accent: rgba(249,115,22,0.4) 0px 0px 8px 0px;
```

### Motion

- Ease: `cubic-bezier(0.4, 0, 0.2, 1)` (94 uses)
- Durations: `instant 75 · xs 100 · sm 200 · md 300 · lg 500`
- Button hover: scale `1.004` + bg lighten, 150ms
- Link hover: color → accent, 150ms

---

## 2. Components

### Button

Three observed variants. All pill-shaped (`9999px`), Inter 14/500.

| Variant | Bg | Color | Padding | Use |
|---|---|---|---|---|
| **Primary** | `#111827` | `#ffffff` | `16px 32px` | "Book a demo" — single CTA per section |
| **Primary sm** | `#111827` | `#ffffff` | `14px 32px` | In-line repeat CTA |
| **Secondary** | `rgba(0,0,0,0.06)` | `#111827` | `14px 28px` | "Schedule a Call" — soft alt |
| **Ghost** | transparent | `#111827` | `12px 20px` | Tertiary, hover → accent |
| **Accent** | `#f97316` | `#ffffff` | `14px 28px` + glow | High-emphasis (rare) |

**Hover:** `bg → #141b2b`, `transform: scale(1.004)`.
**Focus:** `outline: 2px #e9f1fb`, offset 2px.

```html
<button class="btn btn-primary">Book a demo <svg>→</svg></button>
<button class="btn btn-secondary"><code>&lt;/&gt;</code> Schedule a Call</button>
```

### Card

Most-used component (75 instances). Three flavors:

| Variant | Bg | Border | Radius | Padding | Shadow |
|---|---|---|---|---|---|
| **Product (light)** | `#ffffff` | none | 32px | 40px | `shadow-xl` |
| **Soft (inline)** | `rgba(0,0,0,0.05)` | `rgba(0,0,0,0.12)` | 16px | 16px | none |
| **Dark** | `#121212` | `#2a2a2a` | 32px | 40px | none |

**Product card anatomy** (from screenshots):
- `num` — top-right, mono-styled big number (`01`, `02`, `03`) in `--border` color
- `icon-tile` — 48×48, `bg-soft`, 8px radius, primary-color icon
- `rings` — three concentric circles centered, 50% opacity (decoration)
- **Ring scale rule:** rings render at 280px when card width ≥ 360px. Below 360px (narrow grid cells, bento small cells), suppress rings entirely — do not shrink. Rings are decoration, not signal.
- `h3` — 24px / 600
- `body` — 14px / `muted-2`. Inline `<em>` switches to accent color, weight 500 (e.g. _"Live in days, not quarters."_)
- `meta` — mono strip at bottom, `border`-outlined, uppercase

### Nav

Pill-shaped container, white bg, `shadow-xl`. Three regions: brand · links pill (subtle gray bg) · actions (icon buttons + CTA).

Sticky `z-50`. Hover state: link color → accent.

### Badge

Pill, mono 11px uppercase, optional accent dot with glow. Two themes: white-on-light or `card-dark`.

### Input

Underline-only. No radius. 16px Inter. Border `#0f1114`, hover/focus → accent.

### Link

Body: 10.4px / 400 / `#6b7280`. Hover → `#f97316`.

### Accordion

Single-open shell by default. Container is a product card; rows are 1px dividers, no inner padding on the card itself.

| Token | Value |
|---|---|
| Trigger padding | `28px 0` |
| Trigger type | Body lg (18/300), `fg` on hover → `accent` |
| Chevron | 16px mono glyph, `muted`, rotates 180° on `[data-state="open"]` |
| Panel padding | `0 0 28px` |
| Panel body | Body (14/400), `muted-2` |
| Transition | `max-height` + `opacity`, 300ms `--ease` |
| ARIA | `aria-expanded` on trigger, `aria-controls` on panel |

**Variants:** `single` (default — opening a row closes the others) and `multi` (independent). Set via `data-mode="multi"` on the container.

```html
<div class="accordion" data-mode="single">
  <details class="accordion-item">
    <summary class="accordion-trigger">Topic label <span class="chevron">▾</span></summary>
    <div class="accordion-panel">Panel copy in fragments.</div>
  </details>
</div>
```

### Chat bubble

Used in AI-mediated feature blocks. Two roles: `user` (soft card, left) and `system` (dark card, right). Avatar chip is 32×32 mono initial.

| Token | Value |
|---|---|
| Bubble radius | `--r-lg` 15px (inside `--r-xl` 24px container) |
| Bubble padding | `16px 20px` |
| Avatar chip | 32×32, `bg-soft`, mono 12/500, primary |
| Composer bg | `card-dark` |
| Send button | Accent pill, 36×36 |
| Row gap | 16px |
| Container | Soft card or dark card, 24px padding |

### Tabs / Carousel (chip-driven)

Pill rail (left or top) drives a single viewport on the right. Active chip uses the primary button treatment; inactive chips use soft-card bg with `muted-2` text.

| Token | Value |
|---|---|
| Chip (active) | `primary` bg, white text, pill radius |
| Chip (inactive) | `rgba(0,0,0,0.06)` bg, `muted-2` text |
| Counter | Mono 11/500 uppercase, format `01 / 04` (forward slash, no spaces around) |
| Pagination dots | 8px circle, `border` default, `accent` active, 12px gap |
| Slide transition | 300ms opacity + 8px translateY |
| Viewport | Product card |

### Bento grid

Asymmetric primitive. Use `grid-template-areas` to compose. Cells inherit product-card geometry; padding scales with cell size.

| Cell size | Padding | Radius |
|---|---|---|
| ≥ 2-column wide | 40px | 32px |
| 1×1, sub-200px | 24px | 32px |

```css
.bento {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: repeat(4, minmax(140px, auto));
  gap: 24px;
  grid-template-areas:
    "stat stat glink glink"
    "stat stat glink glink"
    "flink flink flink atlas"
    "small1 small2 small3 atlas";
}
```

Reserve the tall dark rail for one product anchor per bento.

### Stat / metric tile

Used inside bento cells, case-study headers, and section openers. Tile is a product card; numeral is H3 (48/500) with accent `<em>` for the unit suffix.

| Unit | Treatment | Example |
|---|---|---|
| `+` | Accent `<em>`, no space | `300<em>+</em>` |
| `%` | Mono 24/500, accent, same baseline | `99.9<em>%</em>` |
| `M` / `K` / `B` | Inline at H3 weight, no `<em>` | `4.3M` |
| `d` / `h` / time | Mono 14/500, uppercase, separate line below numeral | `14` / `DAYS` |

Caption beneath the numeral: mono 12/500 uppercase, `muted`.

### Pull-quote (card variant)

Long-form quote rendered as a light product card. No accent `<em>`. Attribution is a two-row mono strip.

| Token | Value |
|---|---|
| Quote type | Body lg (18/300), `fg` |
| Open glyph | Decorative `"` in `--border`, 96px, top-left, mono |
| Attribution name | Mono 12/600, uppercase, `fg` |
| Attribution role | Mono 11/400, uppercase, `muted` |
| Avatar (optional) | 40×40 mono-initial circle, `bg-soft`, primary |

Pull-quote cards never carry a CTA — they close a section, not start one.

---

## 3. Layout

- **Container:** 1280–1600px max, padded 24–48px
- **Grid:** 12-column desktop, 4-column mobile
- **Gaps:** 24px (cards), 32px (sections), 96/128px (hero stacking)
- **Breakpoints:** `sm 640 · md 768 · lg 1024`

### Section-head CTA pair

When a section header carries CTAs, pair them on the right edge of the header row, baseline-aligned with the H2.

- **Primary** + **Secondary**, in that order. Never two primaries.
- Secondary CTA omits the icon prefix when sitting next to a primary.
- On `< md` breakpoint: stack below the header, primary first. Full-width is forbidden — keep pill geometry.

### `>` block treatment

The `>` arrow prompt is a section-close pattern, not an inline glyph.

| Token | Value |
|---|---|
| Glyph | Mono 14/500, `muted` |
| Spacing | 96px top margin from prior block, 24px from CTA pair below |
| Alignment | Left-aligned with section gutter; CTA pair sits in the next row |
| Border | Optional 1px top divider in `border`, 32px above the prompt |

Pair the `>` prompt with a primary + secondary CTA below it — never with a primary alone.

### In-card visual surfaces

Inside a light product card, three visual surfaces are sanctioned:

| Surface | Bg | Border | Use |
|---|---|---|---|
| **Diagram backdrop** | `bg-soft` | none | SVG routing diagrams, node/arrow graphs |
| **Console block** | `card-dark` | none | Code samples, terminal output, log strips |
| **Data stack** | `#ffffff` | 1px `border` | Stacked rows of mono key/value pairs |

All three inherit `--r-md` (8px) radius and 24px internal padding. They never bleed to the card edge — keep a 16px inset minimum from the card border.

---

## 4. Voice in components

- CTA verbs: **book**, **schedule** (in that order)
- Address the reader as **you** only — never "we" in copy on buttons or H tags
- Headings: Title Case, tight (rarely > 8 words)
- Inline accent emphasis uses orange `<em>` spans inside body copy

---

## 5. Don'ts

- Don't ship the `#6b7280` on `#f3f4f6` pairing for any reading copy
- Don't reach past 14px for button text — pill geometry was tuned for that scale
- Don't add a third button variant when "Schedule a Call" can carry the secondary slot
- Don't replace pill `9999` with `xl 24` on buttons — the brand reads off-shape

---

_Source: `03.Code Projects/design lang/hostmyclaudehtml-com/hostmyclaudehtml-com-DESIGN.md` · generated by designlang v12.15.0._

---

# 6. Deck / slide system

_Design contract for FCG presentation decks (1920×1080 HTML slides). Added 2026-06-08. Reusable template lives at `design/deck-template/`._

> **Theme note — this section is dark-first.** Sections 1–5 above document the **light** web extract (`#ffffff` bg, `#111827` primary). The shipped site theme (`assets/css/fcg-brand-theme.css`) and these decks are **dark-first** (`#080805` bg, `#f7f7f2` text). Same brand, inverted surface. When `DESIGN.md` §1 and the live CSS disagree, the live CSS is current — reconcile when there's time.

## 6.1 Slide tokens

Brand hue is unchanged; only the surface inverts. Pulled from `assets/css/fcg-brand-theme.css`.

| Role | Hex / value | Use |
|---|---|---|
| `bg` | `#080805` | Slide background (near-black, matches logo fill) |
| `fg` | `#f7f7f2` | Headlines, primary text |
| `muted` | `#a1a1aa` | Body copy, clarifiers |
| `soft` | `#71717a` | Eyebrows, captions, meta |
| `accent` | `#f97316` | Emphasis `<em>`, stat units, index numerals, primary CTA |
| `accent-strong` | `#ea580c` | CTA hover |
| `border` | `rgba(255,255,255,0.10)` | Card outlines, dividers, hairlines |
| `card` | `linear-gradient(180deg, rgba(255,255,255,0.065), rgba(255,255,255,0.025))` | Stat / product / point card fill |

Accent glow (cover, closing): `radial-gradient(circle, rgba(249,115,22,0.16), transparent 62%)`, blurred.

## 6.2 Type — Inter (matches live site)

The shipped theme forces Inter on all text (the §1 JetBrains-Mono-for-meta rule is overridden in production). Decks follow the live site: **Inter everywhere**, with uppercase + wide tracking for the "documentation" texture on eyebrows/meta.

| Token | Size | Weight | Tracking | Use |
|---|---|---|---|---|
| Cover / closing H1 | 104–118px | 600 | -0.03em | Big statement slides |
| Section title | 104px | 600 | -0.03em | Dividers |
| Slide H2 | 64–72px | 600 | -0.025em | Content / stat / product heads |
| Stat numeral | 84px | 600 | -0.03em | Proof tiles, `tabular-nums` |
| Card H3 | 30–34px | 600 | -0.01em | Point / product card titles |
| Body / clarifier | 19–26px | 300 | 0 | One-line clarifiers, card copy |
| Eyebrow / meta | 14–16px | 500 | 0.24em, UPPERCASE | `Category · Scope · 0N`, accent index |

## 6.3 Archetypes (8)

Each is a self-contained 1920×1080 HTML file under `design/deck-template/slides/`. Aggregated by `index.html` (the huashu `deck_index.html` wrapper: 3D overview wall + full-screen present + print-to-PDF).

| # | File | Role |
|---|---|---|
| 01 | `01-cover.html` | Logo + eyebrow + display headline + middot triad + clarifier |
| 02 | `02-section.html` | Ghost index numeral, accent bar eyebrow, sentence-case section title |
| 03 | `03-stat.html` | 4-up stat tiles, big numeral + accent unit `<em>` + mono caption |
| 04 | `04-content.html` | Claim → one-line clarifier → 3 supporting point cards |
| 05 | `05-two-column.html` | Text + accent bullets · right = sanctioned visual surface (swap in a real screenshot/diagram) |
| 06 | `06-product.html` | Product cards (G-Link / Atlas / AgreeEase) + section-head CTA pair |
| 07 | `07-quote.html` | Full-bleed pull-quote, ghost quote mark, mono attribution |
| 08 | `08-closing.html` | `>` arrow prompt + display headline + primary/secondary CTA pair |

## 6.4 Reused component rules

- **Buttons** — pill (`9999px`), Inter 15–19px/500. Primary = accent fill + `0 14px 34px rgba(249,115,22,0.22)` glow; secondary = `rgba(255,255,255,0.04)` fill + `border`. Never two primaries; secondary drops the icon.
- **Stat tile** — `card` fill, `border`, 26px radius, 44px pad. Unit (`M+`, `%`, `+`) is an accent `<em>`, no space before. Caption = mono-style uppercase `soft`.
- **Product card** — 30px radius, faint corner index numeral (`rgba(255,255,255,0.10)`), 54px icon tile, mono meta strip with top divider.
- **Eyebrow** — `Category · Scope · 0N` triad, space-middot-space, index in accent. Section divider variant uses a 54px accent bar prefix.
- **Emphasis** — orange `<em>` spans, `font-style:normal; font-weight:500` (never italic).

## 6.5 Voice in decks

Follows `brand-voice.md` in full. Decks specifically:
- Headlines sentence case; product nouns keep Title Case (`G-Link`, `Atlas TMC OS`, `AgreeEase`).
- Triads use middot (`Connect · Operate · Experience`); stat fragments stack with periods.
- Section-end and closing slides carry the `>` arrow prompt + a verb-first CTA — never a bare statement.
- Range-closer allowed once, on cover or a major section opener only.

## 6.6 Deck don'ts

- Don't switch decks to light mode silently — it contradicts the live site. If a light deck is needed, flip the token block per slide and note it.
- Don't add a second accent colour for "variety" — orange carries all emphasis; everything else is the neutral ramp.
- Don't let a single slide carry its own page number — the `deck_index.html` wrapper owns the counter.
- Don't fill a content slide to the edges — keep the 96–120px gutter; whitespace is the format's main compositional tool.
- Don't fake product UI with CSS shapes on the two-column slide — drop in a real screenshot or leave the honest placeholder.

---

_Source: FCG deck template (`design/deck-template/`), tokens from `assets/css/fcg-brand-theme.css` + `assets/images/fcg-logo.svg`, built via huashu-design 2026-06-08._
