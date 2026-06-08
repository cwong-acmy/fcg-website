# FCG Open Design System Prompt

**Date:** 2026-06-05
**Use:** Drop into Open Design (or any equivalent design-system generator — Claude Code, v0, Lovable, Bolt, Galileo) to spin up FCG-aligned UI.
**Source:** `reference/DESIGN.md` (designlang v12.15.0 extract from hostmyclaudehtml.com/p/nF8CHUnIEL) + `reference/brand-voice.md` + `assets/css/fcg-brand-theme.css`.

---

## The Prompt

```
Create a design system for FCG Group.

The connection-layer infrastructure for travel — supply, distribution, booking, and financial operations across Asian and Western markets, used by 100+ enterprise TMCs, platforms, and hotel groups.

Brand personality: declarative, authoritative, infrastructure-native.

Primary color: ink (#080805) — the dark canvas dominating 70–80% of any surface, with elevated card ink (#111827) for raised product surfaces and a near-white foreground (#f7f7f2) for body copy on dark.

Accent color: orange (#f97316) — the single spark, 10–15% of any surface, hover (#ea580c), with cyan (#0ea5e9) reserved for hero glow gradients only. Neutrals: (#a1a1aa) for secondary text on dark, (#6b7280) muted-2 for body on light cards, (#e5e7eb) for card outlines, (#f3f4f6) bg-soft for icon tiles and diagram backdrops. Secondary accent spectrum is intentionally narrow — orange is the identity; cyan and yellow appear only inside the hero glow gradient, never as standalone surfaces.

Font feel: infrastructure-doc precision. Inter as the primary typeface across display, body, and UI — weights 300–600, tight letter-spacing on headlines (-0.025em to -0.05em), generous line-height on body (1.55–1.65). JetBrains Mono reserved for meta — eyebrows (mono 11/500 uppercase), captions, stat units (99.9%, 14 / DAYS), counter strips (01 / 04), and code blocks.

Button style: pill — 999px radius on every CTA, badge, nav pill, and chip. 32px radius on primary product cards (75 instances), 8px on icon tiles and meta strips, 2px on inputs. Primary buttons are orange-filled (#f97316) on white text with a 14px orange glow shadow rgba(249,115,22,0.22); secondary buttons are ghost — transparent with a thin white border on dark, white-fill with subtle (#d9dee7) border on light. Never replace pill with 24px on buttons — the brand reads off-shape.

Mode: dark first — ink (#080805) as the canvas, orange (#f97316) as the spark, near-white (#f7f7f2) as the breathing room. Light mode inverts to (#f7f8fa) canvas with (#0f1114) text and the same orange accent. Light product cards on the dark canvas appear as deliberate contrast moments (the 75 product card instances, the bento white tiles, the chat user bubble) — not the default. Code blocks, console strips, and the dark accent rail run on (#121212) inside light cards. The canvas never lightens to grey on its own; light surfaces are always cards.
```

---

## Notes (supplementary context for the generator)

```
Visual style sits in Linear / Stripe / Cloudflare infrastructure-doc territory: geometric precision, angular cuts, forward momentum, large pill geometry, asymmetric bento grids. Card-based layouts on a dark canvas — 32px-radius product cards padded 40px, pill nav with shadow-xl, pill CTAs, soft glassmorphic surfaces with hairline borders. Flat material — no skeuomorphism, no neumorphism — with subtle 24px/80px shadows and a tight orange glow on accent moments only. Stat tiles use a big mono numeral with the unit as an accent `<em>` (`300<em>+</em>`, `99.9<em>%</em>`). Three sanctioned in-card surfaces: bg-soft (#f3f4f6) for SVG routing diagrams, dark (#121212) for console/code, and white with 1px border for stacked mono key/value data. Not Notion soft, not Wise warm, not Vercel monochrome — closer to a control-room aesthetic with one bright signal color.

Voice is confident, declarative, infrastructure-flexing — neutral on emotion, heavy on authority. Speak about the system, not to the reader. "The infrastructure behind how travel actually works," not "we help you connect." No "you" in hero or section heads; "we" only permitted in the about/origin slot and rationed to one sentence per block. Sentence case everywhere except proper nouns and product names (G-Link, F-Link, AgreeEase, Atlas TMC OS, Travakey, Contrabook, Allbon, Akrapay). CTAs are verb-first, ≤4 words, sales-led: "Book a demo," "Schedule a call," "Request sandbox access," "See the connections." Rhythm signature is stacked period-fragments ("Asia-native. Globally connected."), middot triads ("Connect · Operate · Experience"), `>` arrow section-end prompts, and range-closers ("from a single API call to the largest TMC migration") used at most once per page. Em-dashes only for range-closers; never as a general rhythm device. Banned: seamless, frictionless, intuitive, beautiful, magical, revolutionary, empower, unlock, supercharge, AI-powered, journey, solution-as-noun, "Learn more," "Get started," "Click here." Short over long — every word earns its place. Specific over vague — "300+ travel brands already connected" beats "trusted by industry leaders."

Photography is documentary and infrastructural — operations rooms, server racks, airport control rooms, real hotel exteriors at dawn, network-equipment macros, transit infrastructure. Wide format, available light, no posed models. No stock travel cliches: no smiling business travelers, no sunset airplane wings, no rolling suitcase in a hotel lobby, no handshake-over-laptop, no team-around-a-screen shot.

Illustration is minimal and diagrammatic. When used: routing diagrams, supply-path graphs, node-and-arrow networks rendered on the bg-soft (#f3f4f6) backdrop with thin orange-accent edges and JetBrains Mono labels. Never illustrative characters, mascots, scenes, or anthropomorphised technology. Decorative concentric rings (three rings, 280px, 50% opacity) appear on product cards ≥360px wide and are suppressed entirely below — rings are decoration, not signal.

Iconography is outlined, single-weight, thin-stroke, square-cap — Iconify or equivalent. 16px default, 12px JetBrains Mono glyphs for meta strips and chevrons. Active, selected, and hover states pick up the orange accent; everything else stays in muted (#a1a1aa) on dark or muted-2 (#6b7280) on light. Never filled icons in body content, never multicolor icon sets, never duotone.

The FCG wordmark — geometric, set in Ethnocentric (Typodermic), with parallelogram-shaped negative space inside the F, C, and G and diagonal slashes binding the letterforms — is the hero on every brand surface. Four sanctioned lockups: black-on-light, white-on-dark, white-on-orange, white-on-image. It must read from 16px favicon to billboard scale and stands alone — never lock it up with the tagline "Where East meets West in travel" inside the mark itself.

Tone reference brands for voice (not visuals): Stripe (clarity, range-closers, sentence-case headings — borrowed without the "you" intimacy), Linear (terse infrastructure-doc voice), Cloudflare (network-as-protagonist framing), AWS docs (specific over vague), Vercel (verb-first CTAs), Anthropic (calm authority), Plaid (B2B infrastructure register), Notion API docs (system-described product copy).
```

---

## Completeness score

10 / 10 — project name, one-sentence what it does, 3-word personality, primary hex, accent hex(es) with cascade, narrow secondary spectrum with hexes, typeface named with weights and rules, button radius numerics per component, dark-first mode declared with cascade rules, 1+ visual reference brand, 8 voice reference brands.
