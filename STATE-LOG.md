# STATE-LOG — FCG Website

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
