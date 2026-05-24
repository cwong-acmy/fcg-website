# FCG — Brand voice guidelines

_Voice fingerprint and writing rules for the FCG marketing site._
_Structure modelled on designlang's brand-book voice chapter; populated from `index.html`, `about.html`, and product pages as of 2026-05-23._

---

## 01 · Voice fingerprint at a glance

| Dimension | Value |
|---|---|
| **Tone** | Confident, declarative, infrastructure-flexing — neutral on emotion, heavy on authority |
| **Pronoun posture** | Third-person / system-described. The network speaks, not the salesperson |
| **Heading style** | Sentence case (target state); mixed in current site — to be normalised |
| **Heading length class** | Mixed — short label fragments next to long value-prop sentences |
| **Rhythm signature** | Dot-separated fragments, middot (·) triads, `>` arrow prompts |
| **Sentence shape** | Short declarative fragments stacked; range-closer sentences for scale claims |
| **Register** | B2B infrastructure documentation, not B2B SaaS marketing |

One-line summary: **FCG sells the inevitability of the network.** Stripe says *you* can do this; FCG says *this exists, and the players that matter are already on it.*

---

## 02 · Pronoun posture

**Rule:** Speak about the system, not to the reader. The reader is a witness joining something that already works — not a protagonist being onboarded.

- ✅ "The infrastructure behind how travel actually works."
- ✅ "300+ travel brands, TMCs, and hotel groups. Already connected."
- ✅ "The inventory that everything connects to."
- ❌ "We help you connect your platform to..."
- ❌ "You can accept bookings from any source."
- ❌ "Get your team onboarded in minutes."

**When "you" is permitted:** secondary product-page body copy where a concrete capability is being explained ("Four engagement types, mapped to where you are." — acceptable because "you" describes *where the reader stands in the system*, not what they personally do). Never use "you" in hero copy or top-level section heads.

**About / origin slot exception:**

The about/origin section is the *only* place "we" is permitted. Even then, ration it: one "we" sentence per origin block, and only when describing the company's posture or commitment — never the product's capabilities.

- ✅ "We don't sell software to TMCs that need strategy first."
- ✅ "We built FCG because the connection layer was the bottleneck."
- ❌ "We help you connect your platform." _(product capability — use system-described voice)_
- ❌ "We offer four engagement models." _(catalog — name the models, drop the "we")_

Audience-routing cards on the about page revert to system-described voice ("Built for TMCs," not "We serve TMCs").

---

## 03 · Heading style

**Rule:** Sentence case everywhere. Title Case is reserved for proper nouns and product names.

| Use sentence case | Use Title Case |
|---|---|
| All H1, H2, H3 section heads | Product names: G-Link, F-Link, Atlas TMC OS, AgreeEase |
| Value-prop statements | City labels: Hong Kong SAR, Kuala Lumpur Malaysia |
| Audience cohort labels ("For builders & platforms") | Capitalised acronyms: TMC, APAC, API |

**Fixes to make:**

| Current | Target |
|---|---|
| Connected Across Every Market That Matters | Connected across every market that matters |
| Asia-Native, Globally-Ready | Asia-native. Globally connected. |
| Operational Audit / Deployment Strategy / Implementation Support / Ongoing Advisory | Operational audit / Deployment strategy / Implementation support / Ongoing advisory |
| Three triggers that start an advisory conversation. | _(already sentence case — keep)_ |

---

## 04 · Heading patterns — what good looks like

These existing headings are the canonical voice. New copy should pattern-match these:

**Authority + opposition (the FCG signature):**
- Open connections, not locked platforms.
- Asia-native. Globally connected.
- Scale that earns the claim.
- We don't sell software to TMCs that need strategy first.

**Stat-as-headline (proof-led):**
- 4.3M+ hotels. 24.9M+ room types. Every major airline. One connection to all of it.
- 300+ travel brands, TMCs, and hotel groups. Already connected.

**Three-beat tagline (rhythm-led):**
- Connect · Operate · Experience
- Connect to the supply infrastructure behind travel.

**System-described value prop:**
- The infrastructure behind how travel actually works.
- The inventory that everything connects to.
- Modernize the right part of the stack first.

**Audience routing (always sentence case, always parallel):**
- For builders & platforms
- For TMCs & Travel Programs
- For Operators

---

## 05 · Sentence shape

**Default mode:** short declarative fragments separated by periods. Stack three or four for a hero or claim.

> 4.3M+ hotels. 24.9M+ room types. Every major airline. One connection to all of it.

**Range-closer mode (borrowed from Stripe):** end a capability list with a scale clause that establishes the upper and lower bound.

> Accept payments, offer financial services and implement custom revenue models — from your first transaction to your billionth.  _(Stripe)_

> Connect supply, deduplicate content, and route bookings — from a single API call to the largest TMC migration.  _(FCG application)_

Use range-closers sparingly — at most once per page, on the hero or a major section opener. Overuse turns the rhythm soft.

**Range-closer scope:** sanctioned slots are (1) the hero, (2) a major section opener (H2 with its clarifier line). **Not sanctioned:** inside a product card, in a bento cell, beneath a feature illustration, or in a pull-quote. Range-closers earn their weight by being rare — overuse at card scale softens the cadence to marketing prose.

**Stat-fragment headlines:** small-cell stat tiles ("1 contract," "300+ brands," "14 days") read as verbless fragments by design. The fragment rule overrides the "complete claim" rule when:
1. The stat is the headline of a tile ≤ 1 grid column wide, and
2. A mono caption beneath supplies the verb context ("PER MIGRATION," "ALREADY CONNECTED," "FROM CONTRACT TO LIVE").

In every other slot, headlines remain complete claims.

**Avoid:**
- Comma-stacked compound sentences as the dominant rhythm (that's Stripe's signature, not FCG's).
- Adjective-heavy phrasing ("powerful," "seamless," "world-class," "cutting-edge").
- Storytelling preambles ("In a world where...", "We started FCG because...").

---

## 06 · CTAs and button copy

**Rule:** Verb-first, zero adjectives, ≤4 words. No exclamation marks.

**Primary CTAs (sales-led — keep these):**
- Book a demo
- Schedule a call
- Request a demo
- Request sandbox access
- Get sandbox access
- Get connected

**Secondary CTAs (quieter, observational — push these further):**
- See how it works
- See the supply paths
- See engagement models
- Explore the architecture
- View the connection

**Discovery/process labels:**
- Discovery call
- Operational audit
- Deployment plan
- Start a conversation

**Top CTA verbs in current use:** see, book, request, explore, view, get, schedule, talk, start, join.

**Replace these (too marketing-y or off-register):**

| Replace | With |
|---|---|
| `> Ready to modernize?` | Canonical replacements (pick by section context): `> See the connections` (network / G-Link) · `> Read the architecture` (technical / builder) · `> Start a conversation` (TMC / advisory) · `> See engagement models` (operator / services). The `>` glyph stays; the prompt verb shifts to match the section's audience. |
| "Learn more" (anywhere) | A specific verb: `See pricing`, `View integrations`, `Read the spec` |
| "Get started" (self-serve framing) | `Book a demo` or `Request sandbox access` — FCG is sales-led, not self-serve |
| "Click here" | Never — always describe the destination |

**Do not borrow** Stripe's "Read the story" pattern — FCG is not a brand-storytelling company.

---

## 07 · Punctuation and typographic signature

These are FCG's typographic fingerprint. Preserve them; do not replace with Stripe's em-dashes.

| Mark | When to use | Example |
|---|---|---|
| **Middot (·)** | Three-beat taglines, capability triads | Connect · Operate · Experience |
| **Period between fragments** | Stacked stat or claim fragments | Asia-native. Globally connected. |
| **`>` arrow** | Section-end prompts, transitions | `> Ready to modernize?` (replace the text — keep the arrow convention) |
| **Em-dash (—)** | Sparingly, only for range-closers | …from a single API call to the largest TMC migration. |
| **Ampersand (&)** | Audience cohort labels only | For builders & platforms |
| **Plus sign (+)** | Stat callouts | 4.3M+ hotels, 300+ brands |
| **Forward slash (/)** | Counter separators (`01 / 04`), unit/measure pairs (`14 / DAYS`). Never as "and/or." | `01 / 04` |
| **Stat unit `%`** | Inline, mono, accent, no space before | `99.9%` |
| **Stat unit `d` / `h` / time** | Mono uppercase, one line below the numeral | `14` / `DAYS` |
| **Eyebrow triad (` · `)** | Three-part eyebrow: `Category · Subcategory · Index`. Space-middot-space. Categories sentence case, index mono numeral. | `Capabilities · Connection · 03` |

**Avoid:** semicolons, exclamation marks, ellipses, em-dashes as a rhythm device. The slash as a coordinator ("hotels/airlines" → use "hotels, airlines, and GDS"). The `&` outside cohort labels — never in body copy, headings, or CTAs.

**Eyebrow concatenation grammar:**

Eyebrows are mono 11/500 uppercase. Three patterns are canonical:

| Pattern | Use | Example |
|---|---|---|
| Single label | Section type | `CASE STUDY` |
| Pair (` / `) | Section + slot | `COMPONENTS / REGISTRY` |
| Triad (` · `) | Category + scope + index | `CAPABILITIES · CONNECTION · 03` |

Never mix separators in one eyebrow. Never end an eyebrow with punctuation. Indices are mono numerals (`03`), not words ("third").

---

## 07b · Shortened-form policy

FCG prefers the full form. Shortened forms are permitted only when the constraint is real (mono caption width, badge geometry, table column) and the full form has already appeared on the same page.

| Full form | Shortened (constrained slots only) |
|---|---|
| deduplicate | dedup |
| infrastructure | infra |
| implementation | impl |
| operational | ops |
| Asia-Pacific | APAC |

Never shorten in headings, hero copy, or running body. Never invent new shortenings — if it isn't on this list, write the full form.

---

## 08 · Subheads and section structure

**Rule:** Every section head gets exactly **one** clarifying line beneath it. Not a paragraph.

**Pattern:**
```
[Bold sentence-case claim]
[One-line clarifier that says what the section will show, in ≤20 words]
```

**Example (good):**
> Scale that earns the claim.
> 4.3M+ hotels, 24.9M+ room types, every major airline — connected through one open layer.

**Example (current — too much):**
> The Core
> [paragraph of marketing copy]

**Example (current — too little):**
> Connected Volume
> _(no clarifier at all)_

Tightening every section to **bold claim → one-line clarifier** makes the site feel denser and more confident, matching FCG's existing terseness.

---

## 09 · What to borrow from Stripe (and what to leave alone)

Imported as a working reference from the Stripe ↔ FCG voice comparison. Goal: borrow Stripe's **clarity** without importing Stripe's **intimacy**.

### Safe to borrow (reinforces FCG)

**1. Sentence-case headings as the default**
Stripe is rigorously sentence case. FCG is mixed — "Connected Across Every Market That Matters" (Title Case) sits next to "Open connections vs. closed platforms" (sentence case). Standardising on sentence case makes FCG read more like infrastructure documentation and less like a marketing site — which fits its "we are the layer underneath" claim.
**Apply to:** every H2/H3. Keep Title Case only for proper nouns and product names ("G-Link," "Atlas TMC OS").

**2. The capability-stacking compound sentence**
Stripe's hero: *"Accept payments, offer financial services and implement custom revenue models — from your first transaction to your billionth."* Three capabilities in one breath, then a range claim.
FCG already does this with stat fragments (*"4.3M+ hotels. 24.9M+ room types. Every major airline. One connection to all of it."*). Borrow the **range-closer** move — end a capability list with a scale clause: *"...from a single API call to the largest TMC migration."* This reinforces FCG's authority without softening it.

**3. Verb-first, ego-less CTAs**
Stripe's "Read the story," "Continue," "Get started" — every CTA starts with a verb and contains zero adjectives. FCG's "Book a demo" and "Schedule a Call" already do this. Where to push it: secondary CTAs and section ends. Replace `> Ready to modernize?` with `See the connections` or `Read the architecture` — quieter, verb-led, less salesy.

**4. The "what it does, what it produces" two-line subhead**
After every Stripe section head there's a single short clarifying line. FCG sometimes has this, sometimes has a paragraph. Tightening every section to **bold claim → one-line clarifier** would make the site feel denser and more confident, matching FCG's existing terseness.

### Do NOT borrow (would dilute FCG)

- **The "you" pronoun in hero/section heads.** Stripe addresses the reader directly; FCG addresses the system. Importing "you" collapses FCG's gravitational posture.
- **Em-dashes as a primary rhythm device.** Stripe's signature is em-dash and comma. FCG's signature is middot, period, and `>` arrow — keep those.
- **Self-serve framing on primary CTAs.** "Get started" / "Sign up" implies frictionless solo onboarding. FCG is sales-led and consultative.
- **"Story" and "Watch" language.** FCG is a connection-layer company, not a brand-storytelling company.

### The one rule

> Borrow Stripe's **clarity** (sentence case, verb-led CTAs, compound capability sentences with range closers). Reject Stripe's **intimacy** (you-pronoun, self-serve CTAs, storytelling vocabulary).

---

## 10 · Vocabulary — words and phrases

**Preferred verbs:** connect, operate, route, deduplicate, modernize, layer, deploy, audit, implement, advise, see, request, schedule, book.

**Preferred nouns:** infrastructure, layer, stack, supply, inventory, connection, network, content, route, engagement, deployment, audit.

**Preferred adjectives (used sparingly):** open, connected, deduplicated, live, native, global, independent, operational.

**Banned vocabulary:**
- _seamless, frictionless, intuitive, beautiful, delightful, magical_ (SaaS marketing clichés)
- _revolutionary, game-changing, cutting-edge, next-gen_ (hype)
- _empower, unlock, supercharge_ (verb hype)
- _solution_ as a generic noun ("our solution does X") — name the product
- _journey, experience_ when used emotionally ("your travel journey")
- _AI-powered, AI-driven_ as a standalone claim — say what it does

**Phrases that are core to FCG (preserve):**
- "Open connections, not locked platforms"
- "Asia-native. Globally connected."
- "Scale that earns the claim"
- "The infrastructure behind how travel actually works"
- "Connect · Operate · Experience"
- "Already connected"

---

## 11 · Audience posture

| Cohort | How to address them | What lands |
|---|---|---|
| **Builders & platforms** | Technical, API-first, range claims | "From a single API call to the largest deployment" |
| **TMCs & travel programs** | Strategic, operational, consultative | "We don't sell software to TMCs that need strategy first" |
| **Operators** | Stack-level, modernisation-framed | "Modernize the right part of the stack first" |

Never collapse the three into a single voice — keep audience-specific entry pages distinct in their emphasis (technical / strategic / operational) even though the underlying tone is identical.

---

## 11b · AI-feature copy patterns

When describing AI-mediated UI (AgreeEase contract mapping, agent-assisted booking, AI search), describe **what the system does to specific inputs**, not the technology behind it.

**Sanctioned patterns:**
- "AgreeEase maps clauses to fields."
- "The agent reads the contract and writes to the booking record."
- "Routes the request to the right supply path."
- "Reconciles two PNRs into one."

**Banned (re-stated from §10 for AI context):**
- "AI-powered," "AI-driven," "intelligent," "smart" — adjective hype, no signal.
- "Magical," "delightful," "seamless" experience claims around the AI.
- "Our AI does X" — name the product (AgreeEase, the agent, the router); never abstract it to "our AI."
- "Understands," "learns," "knows" — anthropomorphic verbs. Use what the system *does* to the input: maps, extracts, routes, reconciles, deduplicates, normalises.

**Default verb stack for AI features:** map, extract, route, reconcile, deduplicate, normalise, classify, match, resolve.

---

## 12 · Application checklist (use before publishing any new page)

- [ ] All H1/H2/H3 in sentence case (except proper nouns and product names)
- [ ] Hero or major claim uses stacked fragments or a range-closer — not comma-compound sentence
- [ ] No use of "you" in hero or top-level section heads
- [ ] Every section has exactly one clarifying line beneath the head (no paragraphs)
- [ ] Primary CTA is verb-first, ≤4 words, sales-led ("Book a demo" / "Request sandbox access")
- [ ] Secondary CTAs use observational verbs ("See," "View," "Read," "Explore")
- [ ] No banned vocabulary (seamless, revolutionary, empower, etc.)
- [ ] Middot (·), periods, and `>` arrows used as rhythm — em-dashes reserved for range-closers
- [ ] Audience cohort labels parallel ("For X & Y" structure)
- [ ] No storytelling preamble — page opens on the claim, not the backstory
- [ ] No range-closer below hero or major-section-opener scope (no card-level range-closers)
- [ ] Counter format uses ` / ` separator with mono numerals (`01 / 04`)
- [ ] Eyebrows follow single / pair / triad pattern with no mixed separators
- [ ] Stat units render per §07 table (`%` inline accent, `d`/time mono below)
- [ ] No "we" outside the about/origin slot — and ≤ 1 "we" sentence even there
- [ ] AI-feature copy describes what the system does to inputs, not "our AI"
- [ ] No invented shortenings — full form unless slot is constrained

---

_Source data: voice extraction performed via `designlang brand https://stripe.com` (v12.15.0), May 2026; FCG site signals extracted from `index.html`, `about.html`, and product pages across the repo._
