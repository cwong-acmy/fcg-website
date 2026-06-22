# FCG Site Redo — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship the restructured, redesigned, rewritten FCG site — 12 pages on a new 4-item nav — before BTS London (Jun 24 2026).

**Architecture:** Hand-written static HTML (no framework/SSG), Tailwind-CDN + GSAP + Iconify + occasional React/Babel islands. No shared-include mechanism exists — nav/footer are inlined per page. Phase 0 produces one canonical **page shell** (head + new nav + footer); Phase 1 builds all 12 pages in parallel from that shell. The golden look is `drafts/index-v4.html` (Home) and `drafts/flink-v7.html` / `glink-v7.html` / `tmc-api-v7.html` (products).

**Tech Stack:** Static HTML5, Tailwind (CDN), GSAP, Iconify, vanilla JS. Verification is visual (preview) + structural (grep/link checks), not unit tests.

**Spec:** `docs/superpowers/specs/2026-06-22-fcg-site-redo-design.md`

**Nav decision (ponytail):** Nav/footer stay *inlined per page*, copied from the canonical shell — matches the existing pattern, no new JS include. `ponytail: inlined nav; extract to nav.js include only if post-BTS maintenance hurts.`

---

## File Structure

| File | Responsibility | Phase |
|---|---|---|
| `_shell/nav.html` | Canonical new 4-item nav markup (new file, reference only) | 0 |
| `_shell/footer.html` | Canonical single footer markup (new file, reference only) | 0 |
| `_shell/head.html` | Canonical `<head>` (CDN scripts, theme CSS, meta) | 0 |
| `archive/` | Destination for the 4 removed pages | 0 |
| `index.html` | Home — rebuilt from `drafts/index-v4.html` + shell | 1 |
| `about.html` | About — rebuilt + shell | 1 |
| `corporate-booking-tool.html` | CBT (Front) | 1 |
| `ai-booking-tool.html` | AI-BT (Front) | 1 |
| `agreeease.html` | RFP (Front) | 1 |
| `atlas.html` | AtlasOS (Mid) | 1 |
| `glink.html` | G-Link (Back) — from `drafts/glink-v7.html` | 1 |
| `flink.html` | F-Link (Back) — from `drafts/flink-v7.html` | 1 |
| `addn.html` | ADDN (Network) — new | 1 |
| `developer.html` | Developer — from `api-access.html` | 1 |
| `payment.html` | Payment (Network) — new, gap analysis §4 | 1 |
| `bts.html` | BTS landing — new, standalone, gap analysis §3 | 1 |

`_shell/` holds reference snippets only — it is not served. Pages paste from it.

---

## Phase 0 — Foundation (critical path, do first, single session)

### Task 1: Extract the canonical head + footer into `_shell/`

**Files:**
- Create: `_shell/head.html`, `_shell/footer.html`
- Source: `drafts/index-v4.html` (head: lines 1–~60; footer: `2441-2504`, the first/primary footer — discard the duplicate `2508-2548`)

- [ ] **Step 1:** Read `drafts/index-v4.html` lines 1–60 and `2441-2548`. Copy the `<head>` block (CDN scripts, theme CSS link, meta) verbatim into `_shell/head.html`.

- [ ] **Step 2:** Copy the primary footer (`2441-2504`) into `_shell/footer.html`. Do NOT copy the second footer (`2508-2548`) — it is the duplicate to be dropped.

- [ ] **Step 3: Verify** — both files non-empty, head contains `fcg-brand-theme` CSS link, footer contains the contact block.

Run: `grep -l fcg-brand-theme _shell/head.html && grep -c "footer" _shell/footer.html`
Expected: prints the head path, then a count ≥ 1.

- [ ] **Step 4: Commit**

```bash
git add _shell/head.html _shell/footer.html
git commit -m "Add canonical head + footer shell snippets"
```

### Task 2: Author the new 4-item nav into `_shell/nav.html`

**Files:**
- Create: `_shell/nav.html`
- Style base: `drafts/index-v4.html:1262-1379` (existing nav — copy its classes/markup, restructure contents)

The base nav carries the OLD IA (Products / Solutions / About with Whitelabel). Transform to the new IA below, keeping the existing Tailwind classes, dropdown JS hooks, theme toggle, and logo lockup.

**New IA (build exactly this):**
- **Products** — mega-menu, three groups:
  - *Front* → CBT (`corporate-booking-tool.html`), AI-BT (`ai-booking-tool.html`), RFP (`agreeease.html`)
  - *Mid* → AtlasOS (`atlas.html`)
  - *Back* → G-Link (`glink.html`), F-Link (`flink.html`)
- **Network** — dropdown → ADDN (`addn.html`), Payment (`payment.html`)
- **Developer** — direct link → `developer.html` (no dropdown)
- **About** — direct link → `about.html` (no dropdown)

Removed from nav entirely: Solutions group, Whitelabel, Advisory & Implementation, AI Mapping, Agent Booking Tool.

- [ ] **Step 1:** Copy `drafts/index-v4.html:1262-1379` into `_shell/nav.html`.

- [ ] **Step 2:** Delete the Solutions dropdown and every Whitelabel/Advisory/AI-Mapping/Agent-Booking link/entry.

- [ ] **Step 3:** Restructure the Products dropdown into the three groups above (Front / Mid / Back), with the six links. Keep the existing dropdown markup/classes; only the group labels and `<a href>` items change.

- [ ] **Step 4:** Add the **Network** dropdown (ADDN, Payment) and the **Developer** + **About** direct links, reusing the same pill/link classes as existing top-level items.

- [ ] **Step 5: Verify** — nav contains exactly the new top-level items and no removed items.

Run: `grep -oE ">(Products|Network|Developer|About|Solutions|Whitelabel)<" _shell/nav.html | sort | uniq -c`
Expected: Products, Network, Developer, About present; Solutions and Whitelabel absent (count 0).

- [ ] **Step 6: Verify links resolve to intended targets** —

Run: `grep -oE 'href="[a-z-]+\.html"' _shell/nav.html | sort -u`
Expected: includes `corporate-booking-tool.html ai-booking-tool.html agreeease.html atlas.html glink.html flink.html addn.html payment.html developer.html about.html` — and none of `whitelabel/advisory-implementation/ai-mapping/agent-booking-tool`.

- [ ] **Step 7: Commit**

```bash
git add _shell/nav.html
git commit -m "Author new 4-item nav (Products/Network/Developer/About) shell"
```

### Task 3: Archive the 4 removed pages

**Files:**
- Move: `whitelabel.html`, `advisory-implementation.html`, `ai-mapping.html`, `agent-booking-tool.html` → `archive/`

Per project rule: archive, never delete; only after Crystal's approval (granted in spec).

- [ ] **Step 1:** `mkdir -p archive`

- [ ] **Step 2:** `git mv whitelabel.html advisory-implementation.html ai-mapping.html agent-booking-tool.html archive/`

- [ ] **Step 3: Verify** — files gone from root, present in archive.

Run: `ls archive/ && ls whitelabel.html 2>&1 | grep -q "No such" && echo "removed from root OK"`
Expected: the four files listed under archive/, then "removed from root OK".

- [ ] **Step 4: Commit**

```bash
git add -A
git commit -m "Archive removed pages (Whitelabel, Advisory, AI Mapping, Agent Booking)"
```

---

## Phase 1 — Parallel page fan-out (12 pages, all equal priority)

Once Phase 0 is committed, build all 12 pages in parallel — one subagent per page. **Every page follows the same recipe.** Pages are independent (no shared state), so dispatch them concurrently.

**Content source of truth (overrides everything):** `reference/FCG_Company_Deckpptx.pptx`. Extract the deck first (pptx skill) and treat it as authoritative over the knowledge-base MD, the gap analysis, and existing page copy where they conflict. Group names in nav/footer are locked: **book** (For travel programs & TMCs), **core** (For travel operators), **engine** (For builders & platforms). ADDN uses its official name: "AI-Powered Decentralized Distribution Network".

### Per-page recipe (apply to each of the 12)

**Inputs per page:** target file, golden source draft (or nearest), the page's product/content brief.

- [ ] **Step 1:** Start the page from the canonical shell — paste `_shell/head.html`, `_shell/nav.html`, `_shell/footer.html` into the page skeleton.
- [ ] **Step 2:** Port the page body from its golden source (e.g. `index.html` ← `drafts/index-v4.html`; `glink.html` ← `drafts/glink-v7.html`; `flink.html` ← `drafts/flink-v7.html`). For pages with no v7 golden (CBT, AI-BT, RFP, AtlasOS, Developer), match the golden's section structure and visual system.
- [ ] **Step 3:** For net-new pages (ADDN, Payment, BTS landing), build sections from the gap analysis (`proposals/bts-website-gap-analysis.md` §3 BTS, §4 Payment) and the knowledge base (`reference/FCG_Knowledge_Base.md`).
- [ ] **Step 4:** Rewrite all copy to the FCG voice — no banned words (seamless, frictionless, intuitive, beautiful, magical, revolutionary, empower, unlock, supercharge, AI-powered, journey, "Learn more", "Get started", "Click here"); sentence case; verb-first CTAs ≤4 words; declarative/infrastructure register. Rules: `docs/FCG Open Design System Prompt.md` (voice section).
- [ ] **Step 5: Verify (structural)** — page links the theme CSS, contains the canonical nav (4 items, no removed items), single footer, no broken internal links.

Run (per page `X.html`):
```bash
grep -q fcg-brand-theme X.html \
 && grep -qE ">Products<" X.html && grep -qE ">Network<" X.html \
 && ! grep -qE ">Solutions<|>Whitelabel<" X.html \
 && echo "STRUCTURE OK"
```
Expected: `STRUCTURE OK`.

- [ ] **Step 6: Verify (banned words)** —

Run: `grep -vi "AI-Powered Decentralized Distribution Network" X.html | grep -inE "seamless|frictionless|intuitive|magical|revolutionary|empower|unlock|supercharge|AI-powered|learn more|get started|click here" || echo "VOICE CLEAN"`
Expected: `VOICE CLEAN` (no matches). NOTE: ADDN's official name "AI-Powered Decentralized Distribution Network" is the ONE sanctioned exception to the AI-powered ban — keep it verbatim (it's in the shell nav/footer); the grep above excludes that line. Never reword it.

- [ ] **Step 7: Verify (visual)** — preview the page (preview_start once, then preview_snapshot / preview_screenshot per page). Confirm it renders, nav works, matches the golden look.

- [ ] **Step 8: Commit** the page.

```bash
git add X.html
git commit -m "Rebuild X on new nav + golden design + rewritten copy"
```

### Page-to-source map for the fan-out

| Page | File | Golden source | Notes |
|---|---|---|---|
| Home | `index.html` | `drafts/index-v4.html` | exercises the shell first |
| About | `about.html` | match golden | confirm second nav-item label |
| CBT | `corporate-booking-tool.html` | `drafts/tmc-api-v7.html` (nearest) | Front |
| AI-BT | `ai-booking-tool.html` | match golden | Front |
| RFP | `agreeease.html` | match golden | Front |
| AtlasOS | `atlas.html` | match golden | Mid |
| G-Link | `glink.html` | `drafts/glink-v7.html` | Back; new filename |
| F-Link | `flink.html` | `drafts/flink-v7.html` | Back; new filename |
| ADDN | `addn.html` | knowledge base | Network; net-new |
| Developer | `developer.html` | `api-access.html` body | repurpose api-access |
| Payment | `payment.html` | gap analysis §4 | net-new; name Confirma |
| BTS landing | `bts.html` | gap analysis §3 | standalone, not in nav |

---

## Open items to settle during execution (non-blocking)

1. **Front / Mid / Back group label** — placeholder; pick a nicer name when authoring `_shell/nav.html` (Task 2). Default to keeping Front/Mid/Back if undecided.
2. **`O-T` / `O-G` / `O-F` "open platform … API" tags** — surface on `developer.html` and the relevant product pages; decide presentation during those page builds.
3. **About second nav-item label** ("FCG …") — confirm when building About.

---

## Self-Review

**Spec coverage:** nav IA (Task 2), all 12 pages (Phase 1 map), 4 removals (Task 3), single footer (Task 1), voice rewrite (Step 4/6), golden match (Step 7) — all mapped. ✓
**Placeholders:** none — every step has a concrete action + runnable check. Open items are explicitly parked, not hidden TODOs. ✓
**Consistency:** new filenames (`glink.html`, `flink.html`, `developer.html`, `addn.html`, `payment.html`, `bts.html`) used consistently in File Structure, nav links (Task 2 Step 6), and the fan-out map. ✓
