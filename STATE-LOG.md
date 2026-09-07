# STATE-LOG — FCG Website

## 2026-09-07 (later) — Direction B built out to 12 pages, then an orange pass

### What changed

**Built the eleven remaining portal pages in Direction B**, plus the homepage, at
[open-portal-redesign/variant-b-impeccable/](open-portal-redesign/variant-b-impeccable): app management,
G-Link docs (overview, integration flow, API reference), F-Link docs, error codes, SDK, Skills,
AI Assistant, login, register.

**One shell source.** [build-pages.py](open-portal-redesign/variant-b-impeccable/build-pages.py) lifts the
head, token block and behaviour script verbatim out of `index.html` and generates nav and footer from one
list, writing them back into `index.html` too. Tokens are byte-identical across all twelve files, checked.
Page content is in [pages_content.py](open-portal-redesign/variant-b-impeccable/pages_content.py).

**Content came off the live portal**, read on 7 September 2026: endpoint paths, methods, SDK versions and
install commands, error codes, rate limits. Nothing invented; copy rewritten into FCG's declarative voice
in British English.

**Then Crystal asked for more orange**, against three screenshots of the marketing site's own treatment.
Applied: orange eyebrow labels, an orange second clause on a headline, an orange lead-in phrase on a lede,
a tinted status chip (orange dot + orange label on a pale orange pill), orange mono card labels, and one
filled orange circular arrow on tertiary links. Buttons and panels stay ink.

### Decisions

- **Small orange text is now intended, and sits behind one token.** `--accent-ink` carries every orange
  label under 18px. `#F97316` on white is 2.80:1 and fails AA, which is what the earlier open question was
  about; Crystal chose to match the marketing site. Switching that single token to `#C2410C` (4.6:1) makes
  every small orange label pass without touching anything else. The required-field asterisk on the auth
  forms is ink, not orange, because it is the only visual marker of a required field.
- **Three copy rules, each enforced by the build rather than remembered.** `build-pages.py` refuses to
  build if any of them break, and each was tested by deliberately breaking it:
  1. An orange `<em>` clause must follow a comma. A headline with no comma stays entirely ink.
  2. An `<h1>` is a page title and never ends in a full stop. Section headings are sentences and keep theirs.
  3. One orange emphasis per block: if a heading carries an orange clause, its lede does not also get an
     orange lead-in.
- **The orange clause is block-level**, so a comma can never leave an orphan word at the end of the ink line.
- **Chips must add information the page does not already carry.** Seven band chips were removed for
  restating the heading or lede immediately below them. Eight remain: the Sandbox/Production ready badges on
  the Skills cards (the live portal's own treatment), `Online` on the AI Assistant, `New` on Skills. Chips
  ride the eyebrow line, never the CTA row.
- **Mobile buttons size to content with the label flush left.** Full-bleed pills read as banners on a phone
  and centre their label away from the text column. The form submit stays full width, as forms conventionally do.
- **Header keeps Register; the drawer carries Login as a full-width button** and a three-way
  ENG / 简体 / 繁體 control as a segmented row.
- **Did not extend the chooser.** Its job (pick a direction) is done, and its base64 `srcdoc` embedding
  would break the new cross-page links.

### Bugs found and fixed, all by measuring rather than reading code

- **`td class="path"` collided with the homepage's unscoped `.path` closing card** (`border-radius:24px`,
  `padding:40px 38px`, `display:flex`), rendering every path cell as an overflowing rounded panel. Table cell
  classes now carry a `t-` prefix. A sweep for classes styled in both CSS blocks showed `.path` was the only
  genuine collision; the rest are scoped or deliberate shared components.
- **The tab rail was clipped, not scrolling, below about 585px.** `.band-foot` sizes to content in a column
  flex container and `min-width:auto` stopped it shrinking, so `max-width:100%` on the rail never bit.
  `body{overflow-x:hidden}` meant no document scrollbar appeared and the horizontal-scroll check passed while
  content was silently cut off.
- **The donor script crashed on the auth pages** — the reduced header has no burger, and the unguarded
  `addEventListener` also killed the scroll-reveal observer on those two pages.
- **`.mnav a` was unscoped**, so `display:block` plus vertical padding flattened the drawer's CTA pills and
  pushed their labels outside. Now `.mnav ul a`.
- **`code.inl` was scoped to `.docs-main`**, so instances in chat bubbles and section ledes fell back to the
  browser's default monospace.
- **`min-height` for card-row alignment was hitting `.card-k`** (also a `<p>`), inflating the eyebrow and
  never touching the description.
- **The docs column had a flat 26px between every sibling**, giving a heading the same weight as a paragraph
  break. Now has real rhythm: open above a heading, tight beneath it.
- **Nav `<h4>` labels and the auth aside's `<h2>` sat before the `<h1>`** in the heading outline. They are
  navigation labels, not document headings, so they became `<p>` with `aria-labelledby` on a `<nav>`.

### Verified

[verify-pages.js](open-portal-redesign/verify-pages.js) attaches to Chrome for Testing on `:9222`, loads all
twelve pages at 1280 and 375, forces the reveal animations to their end state so full-page captures are not
blank, and asserts: no console or page errors, no horizontal scroll, nothing clipped by its `.wrap`, the
accent never filling anything at button scale, Inter throughout, one `h1` per page with no heading skips, no
dead `href="#"`, no table cell inheriting panel styling, card meta rows aligned within a visual row, and
`--accent-ink` holding an approved value. **24 / 24 pass, no JS errors.** Screenshots in
[shots/b-pages/](open-portal-redesign/shots/b-pages).

Static checks alongside it: every internal link resolves, and the `:root` token block plus the nav and footer
markup are byte-identical across all twelve files.

### Still open

- **Nothing is deployed.** The live marketing site is served from OneDrive `07 Website` on nginx, not this
  repo and not Vercel, so nothing here changes anything live. The portal redesign has no deployment target
  agreed yet.
- **The AA call on small orange text** is Crystal's, and reversible in one token if she wants `#C2410C`.
- **Image generation still blocked** — both Google AI Studio keys return `429 free_tier limit 0`; Higgsfield
  needs an interactive `hf auth login` from Crystal. Brand-kit raster boards remain unbuilt, prompts stored.
- **Six duplicate full-tree folders** (`about/`, `whitelabel/`, `atlas/`, `agreeease/`,
  `corporate-booking-tool/`, `advisory-implementation/`) are untracked junk from an old copy operation.
  Deleting them needs Crystal's approval. `.vercel/` and `.claude/` also left untracked.
- **This work is on branch `portal-redesign-direction-b`**, not `main`, and is not pushed.

### Learnings

**Problem.** Build eleven pages that must match one existing page exactly, then restyle all twelve to a
moving brief, without drift.

**Approach.** Make the existing page the shell donor rather than a thing to copy: lift its head, token block
and script verbatim at build time and generate nav and footer from one list, writing them back into the donor
too. Then, as each style rule arrives, encode it as a build assertion instead of applying it by hand, and
prove the assertion by deliberately breaking it.

**Judgment calls — what was NOT done, and why.**
- Did not hand-write twelve copies of a 450-line token block. Duplication is how "byte-identical" quietly
  becomes false three edits later.
- Did not trust the horizontal-scroll check. `body{overflow-x:hidden}` converts overflow into silent
  clipping, so a passing scroll check proved nothing; comparing each child against its `.wrap` content box
  found the real bug.
- Did not guess at the rounded-panel table cells from the screenshot. Reading the computed style named the
  colliding class in one query, and a sweep for classes defined in both stylesheets showed it was the only one.
- Did not fix the card-alignment defect by nudging a magic number after each failure. Measuring the actual
  boxes revealed the `min-height` was landing on the wrong element entirely.
- Did not add a "learn more" orange circle to primary CTAs, and did not let orange fill a button or panel,
  even while adding orange everywhere else it was asked for.
- Did not extend the chooser to the new pages. It had already served its purpose, and its embedding method
  is incompatible with cross-page links.

**Reusable rule.** When a brief arrives in pieces, turn each accepted rule into a build-time assertion and
break it once to prove it fires — otherwise rule five silently undoes rule two. And when a symptom is
visual, read the computed style before reading the source; the collision is usually a class name, not logic.

## 2026-09-07 — Live-source audit, brand kit, developer-portal redesign directions

### What changed

**1. Established what actually serves the live site.** `fusionconnectgroup.com` is **not** built from this
repo. Verified by byte-hashing every live page against every local candidate.

- Live host: nginx at `43.135.32.47` (Tencent Cloud range). **Not Vercel**, despite `.vercel/project.json`
  (`prj_bIBO2PVjRM052GwQXYZN0ZxoPCWB`, work team `team_SyKixqrcZUCIGFNYQC13rwVl`) sitting in this repo.
- Live source of truth: `~/Library/CloudStorage/OneDrive-SharedLibraries-FusionConnectGroup/FCG Marketing - Documents/07 Website/`.
  Every live page matches a file there byte-for-byte, except that the deployer stripped the space out of
  the `* _crystal-denzel-edit.html` filenames and rewrote the `%20` hrefs. Uploaded 20 July 2026.
- Only `components.html` in this repo matches live. Everything else is a stale May-2026 "Full Website V8"
  generation: `4.3M+` / `300+ partners` / US spelling, and pages (`whitelabel`, `advisory-implementation`,
  `api-access`, `ai-mapping`, `agent-booking-tool`) that were never live.
- **nginx serves the homepage as a catch-all for unknown paths**, so a 200 does not prove a page exists.
  Compare bytes, never status codes.

**2. Built the FCG brand kit** → [brandkit/](brandkit). `designlang` v12.15.0 full extraction plus a written
spec, with every token cross-checked against the live page's own inline `<style>` block.

**3. Built two developer-portal homepage directions** → [open-portal-redesign/](open-portal-redesign),
realigning `open.fusionconnectgroup.com/home` to the marketing brand. Direction A via `huashu-design`,
Direction B via `impeccable`, both assembled into a self-contained tabbed chooser.

### Decisions

- **The brand kit's authority is the live HTML, not designlang.** designlang's heuristics rank CSS
  frequency, not brand intent. It was right that Inter carries everything (Sora is loaded in the live
  `<head>` and never applied — do not reintroduce it), but its `foreground: #000000` and "Title Case"
  voice call both contradict the source (`#0F1114`; sentence case with a terminal full stop).
- **The accent rule is the whole system.** `#F97316` appears 49 times against ink's 188 and is never a
  surface — only status dots, section-eyebrow dashes, statistic unit suffixes, thin arcs, focus rings.
  The current portal breaks this with orange button and panel fills; both directions fix it.
- **Raster brand boards deliberately not faked.** The `brandkit` skill is image generation and every
  model refused on quota. Built the board in code from the real tokens and the real wordmark instead —
  more accurate than a model's approximation, and editable. Prompts stored for later.
- **Did not polish the losing variant.** Two known cosmetic defects in Direction A (faint partner-grid
  crosshairs, orange arcs spilling outside the globe) are logged, not fixed, until a direction is chosen.

### Blockers

- **Image generation: BLOCKED.** Both Google AI Studio keys in 1Password return
  `429 … free_tier_requests, limit: 0` for every Gemini image model — no billing on either project.
  Higgsfield returns `Not authenticated` and needs an interactive `hf auth login` from Crystal.
- **Open question for Crystal — small orange text.** `#F97316` on white is 2.80:1 and fails AA; it is one
  of the three contrast failures designlang flagged on the live site. Both directions independently set
  the eyebrow label in ink and kept only the dash orange. Recommended resolution: `#C2410C` (4.6:1) for
  small orange text, `#F97316` retained at display size. Awaiting her call.
- **External publication not done.** The chooser is local only; hosting it publicly needs her approval.
- **`brandkit` skill is not session-registered.** It lives at `Desktop/Claude/.claude/skills/brandkit`,
  one level above this project, so `Skill(brandkit)` fails with "Unknown skill". Read and followed the
  SKILL.md directly. Its `.agents/skills/brandkit` twin is byte-identical.

### Next actions

1. Crystal picks Direction A or B from [open-portal-redesign/choose.html](open-portal-redesign/choose.html).
2. Apply the small-orange-text decision to the chosen direction.
3. Build the remaining portal pages in the chosen direction: `/home/app-management`,
   `/home/api-docs/detail/hotel` (+ `/apis`, `/integration/process`), `/home/api-docs/detail/flink`,
   `/home/api-docs/errors`, `/home/sdk-assistant`, `/home/skills`, `/home/ai-assistant`, `/login`, `/register`.
4. Decide what to do about this repo being stale — reconcile the live OneDrive generation in as the new
   baseline, or retire the repo as a historical checkpoint.
5. Six duplicate full-tree copies (`about/`, `whitelabel/`, `atlas/`, `agreeease/`,
   `corporate-booking-tool/`, `advisory-implementation/`) are untracked junk from an earlier copy
   operation. Deleting them needs Crystal's approval; do not commit them.

### Learnings

**Problem.** Work out which of ~150 local HTML files serves a live site, then realign a sibling portal to
that site's design language.

**Approach.** Hash the live bytes against every local candidate before reading a single file — identity
first, similarity second. When nothing matched, extract the live page's *link graph* rather than its
content: filenames the live homepage referenced (`*_crystal-denzel-edit.html`, `glink`, `addn`) existed
nowhere in the repo or its git history, which located the real source in one Spotlight query. For the
design language, treat the live page's own inline `<style>` block as authority and the extraction tool as
a corroborating witness.

**Judgment calls — what was NOT done, and why.**
- Did not trust `designlang`'s token report, and did not discard it either. Used it for screenshots,
  scale measurement and structure; overrode it on foreground colour and voice where the source disagreed.
- Did not probe live pages by status code. nginx's catch-all returns 200 for everything, so
  `whitelabel.html` and `api-access.html` both looked real at 164,654 bytes — the homepage.
- Did not generate the raster brand boards with a fallback model or a stock stand-in. A board with an
  invented wordmark would have been worse than no board and would have propagated into the redesign.
- Did not accept either subagent's self-report. Direction B's accent check was a false pass on method —
  it grepped the literal hex, missing `var(--accent)`. The conclusion happened to hold; the method
  would not have caught a violation.
- Did not fix the losing variant's cosmetic defects. Polish before selection is work thrown away.

**Reusable rule.** For "which file is live", compare bytes and follow the live page's own link graph —
never filenames, mtimes, or HTTP status codes. For "match this design", the target's own stylesheet
outranks any extraction tool, and the tool's job is screenshots and measurement.
