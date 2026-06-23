# FCG Supply Network — The Real Moat

**Purpose:** Deep-dive on what sits *behind* the API. This is the asset competitors cannot replicate. Used for internal training, sales enablement, and external-facing materials.

> "Customers don't want the API. They want what's behind it. The API is just an integration method." — Elaine Wan

---

## 1. Why the Supply Network Is the Product

When a TMC integrates with FCG, what they are actually buying is **access to a curated, multi-source, corporate-travel-grade supply chain** that took years to build. The API is the door. The supply network is the room.

This matters because every competitor — whether a B2B wholesaler or a same-category TMC platform — can say "we connect to many hotels." Anyone can claim 1 million, 4 million, 10 million hotels. That number alone is meaningless. What matters is **the composition, the relationship depth, the geographic spread, and the rate-type coverage** behind the number.

FCG's supply network is differentiated on four dimensions:

| Dimension | What it means | Why competitors can't match |
|---|---|---|
| **Source diversity** | Four structurally different supply types (GDS, direct-hotel/NDC, bedbank aggregators, regional direct) | Each source type requires its own integration discipline, commercial relationship, and operational capability. Most platforms specialize in one or two. |
| **Rate-type coverage** | Public rates + RFP/corporate-negotiated rates + wholesale rates, all in one pipe | Corporate rates are only available through GDS or direct hotel channels — wholesalers structurally cannot deliver them |
| **Geographic depth** | Asia and China supply at a depth global competitors cannot match | Requires being physically based in the region. Years of in-market relationships. |
| **Operational reliability** | Bookings stay accountable end-to-end; cancellations, holds, changes are honored | Wholesale re-routing chains (A→B→C→D) drop accountability. Our model is direct-where-possible. |

---

## 2. The Four Supply Buckets

FCG aggregates four structurally different types of supply. Each plays a distinct role. The combination is the moat.

### 2.1 Bucket A — GDS Direct

**What it is:** Direct integrations with Global Distribution Systems.

**Live connections (from G-link supplier list):**
- **Sabre** — Live
- **SabreABC** — Live

*Note: Amadeus was discussed during the internal walkthrough as part of the strategic GDS stack. It is not currently on the active G-link supplier list and should be treated as a roadmap / strategic mention rather than a live integration until confirmed otherwise.*

**Why this bucket exists in our stack:**
- **GDS is the only channel that carries corporate negotiated rates.** This is the single most important point in our entire supply story. Bedbanks and B2B aggregators physically cannot push corporate-negotiated rates through their channel because hotels do not pass those rates out via wholesale.
- For any large corporate, ~70% of bookings are RFP / corporate-negotiated rates. A TMC without GDS supply cannot serve large corporates properly.
- GDS also carries the published-rate inventory that anchors comparison and policy enforcement.

**What competitors get wrong here:**
- B2B wholesalers (Didatravel, HeyTrip, Hotelbeds, etc.) do not connect to GDS for corporate rates. They distribute their own marked-up inventory and call that "TMC distribution," but it's the wrong rate type for the buyer.
- Some same-category players cover GDS but in regions where their relationships are thin — particularly Asia.

**What's hard about it:**
- GDS is an old, slow-moving ecosystem. New integrations take 180+ days minimum.
- GDS itself rarely improves. Anything modern (AI, agentic flows) has to be built around it.
- We've done the integration work so our customers don't have to.

---

### 2.2 Bucket B — Direct Hotel / NDC / Channel Managers / Hotel Chain Deployments

**What it is:** Direct hotel contracts and channel-manager connections, plus direct G-link deployments inside major Chinese hotel chains. This is where corporate negotiated rates flow when they don't come through GDS, and where Chinese chain inventory is sourced at scale.

**Pure Resource / B2B Direct Platforms — Live:**
- **HyperGuest** — Israel-based; B2B direct-connect marketplace between hotels and distributors

**Pure Resource / B2B Direct Platforms — Contracted or In Development:**
- **Shiji 石基** — contract signed, in development (gateway to multiple hotel-chain integrations)
- **德比 (Derbisoft)** — channel manager; coming soon
- **iOL X** — contract in review

**Chinese Hotel Chains — G-link Deployed Directly:**
- **锦江国际 (Jin Jiang International)** — one of the largest Chinese hotel groups
- **锦江 (Jin Jiang)** — G-link deployed
- **亚朵 (Atour)** — G-link deployed; premium Chinese chain
- **如家 (Home Inns)** — G-link deployed; major economy chain

**Chinese Platforms Going Abroad — Coming Soon:**
- **携程国际 (Trip.com International, indirect)** — via domestic third-party partnership, used to source international content back

**Why this bucket matters:**
- **Most reliable channel in the entire stack.** A booking made through a direct hotel relationship has the shortest chain of accountability — there is no re-router in the middle.
- This is the second path for corporate negotiated rates, alongside GDS. For hotels not covered by GDS corporate-rate flows, the direct channel-manager path is how we deliver them.
- Channel managers (like Derbisoft) and aggregation platforms (Shiji) let us connect to many hotels through one integration, instead of one-by-one.
- **Direct G-link deployment inside Chinese hotel chains** is the deepest possible integration — G-link is literally embedded in the chain's distribution stack.

**Strategic note:** The Chinese hotel chain deployments (Jin Jiang, Atour, Home Inns) are a special category — these are not just connections, they are G-link installations inside hotel-chain operations. This is a moat that compounds: as more Chinese chains run on G-link, the platform becomes the default infrastructure for Chinese-chain distribution.

---

### 2.3 Bucket C — Bedbank Aggregators (B2B Wholesalers)

**What it is:** Third-party hotel content aggregators. These give us breadth — long tail coverage, leisure-style inventory, exotic destinations — but not corporate-rate access.

**International Tier-1 Wholesalers — Live:**
- **RateHawk Global** — direct contracts + supplier aggregation; strong in Middle East, Europe, Asia-Pacific
- **Expedia EPS** — global breadth
- **MIKI** — UK-based since 1967; veteran European B2B wholesaler, global direct-contract coverage
- **Hotelbeds** — the global benchmark bedbank
- **Bedsonline** — Hotelbeds' agency-distribution arm
- **HyperGuest** — Israel-based; B2B hotel-to-distributor direct connectivity marketplace

**International Tier-1 Wholesalers — Contracted, Pending Activation:**
- **Agoda** — contract signed, awaiting deployment slot
- **Webbeds / DOTW** — second-largest global B2B hotel distribution platform after Hotelbeds; 500K+ hotels, 30K+ direct contracts
- **Restel Hotels** — Spanish; Hotusa Group; 100+ country coverage; contract in review
- **Veturis 维途** — Spanish; strong in Southern Europe and Latin America; contract signed
- **Nuitee** — contract signed, awaiting deployment

**Chinese Top-Tier B2B Wholesalers — Live:**
- **Heytrip 喜玩** — China leading B2B wholesaler
- **Huitravel 汇智** — China leading B2B wholesaler
- **Meituan 美团 (Overseas Account)** — major Chinese hotel and lifestyle platform
- **Dida Travel 道旅** — China leading B2B wholesaler

**Chinese Top-Tier B2B Wholesalers — Contracted, Pending:**
- **Tourmind 途灵** — Shenzhen-based; direct contracts + resource aggregation; tier-1 domestic B2B

**Specialty / Regional B2B — Live:**
- **Mengtu 萌兔** — niche route specialty

**Specialty / Regional B2B — Contracted or Negotiating:**
- **TBO** — India (Gurugram); 1M+ rooms, 50K+ direct contracts; coming soon
- **YALAGO** — Dubai; Emirates Airlines Group subsidiary; strong in Middle East / Southeast Asia; in review
- **Pax2Night** — Turkey (Istanbul, Yuppi Group); strong in Turkey/MENA; signed, awaiting Shiji integration
- **ABC Travel Taipei** — Taiwan; APAC / Southeast Asia route specialist
- **MG HOLIDA** — Bali (Indonesia); Southeast Asia direct + global aggregation; negotiating
- **OhmyHotel** — in review
- **Amerilink** — in review
- **Methabook** — in review

**Why we still connect this bucket:**
- Breadth of coverage for the long tail of hotels not addressable via GDS or direct
- Volume on leisure-style bookings (bleisure trips, optional traveler choices)
- Backup supply when corporate rates are exhausted or unavailable

**Why we still connect this bucket:**
- Breadth of coverage for the long tail of hotels not addressable via GDS or direct
- Volume on leisure-style bookings (bleisure trips, optional traveler choices)
- Backup supply when corporate rates are exhausted or unavailable

**Why this bucket alone is not enough (and is the wholesalers' fatal flaw):**
- **No corporate rates.** Hotels do not pass corporate-negotiated rates through wholesale. So if you only have bedbank supply, you cannot serve ~70% of a large corporate's actual booking pattern.
- **Reliability degrades through the chain.** When a wholesaler doesn't directly contract a hotel, they pull from another wholesaler, who pulls from another, who pulls from another. Bookings can pass through A→B→C→D before reaching the hotel. When something goes wrong (cancellation, hold, change, traveler emergency) accountability is opaque and resolution is slow or impossible. For leisure travel this is annoying. For corporate travel it is disqualifying.
- **Wrong DNA.** Bedbanks' business model is markup-middleware to OTAs first; TMC distribution is a side channel. Telltale signal: walk the GBTA expo floor — wholesale bedbanks are not exhibiting. FCG is.

**Sales framing:** We include bedbanks for breadth, but we don't sell on them. Bedbanks are necessary; they are not sufficient.

---

### 2.4 Bucket D — China & Asia Direct Supply

**What it is:** Direct relationships with Chinese hotel chains, Chinese B2B platforms, and Asia-specific specialty suppliers. This is the bucket that no global competitor can replicate.

**Direct Chinese Hotel Chain Deployments (G-link installed inside the chain):**
- **锦江国际 (Jin Jiang International)**
- **锦江 (Jin Jiang)**
- **亚朵 (Atour)**
- **如家 (Home Inns)**

**Chinese B2B Wholesalers (Live):**
- **Heytrip 喜玩**
- **Huitravel 汇智**
- **Meituan 美团 (Overseas Account)**
- **Dida Travel 道旅**

**Chinese B2B Wholesalers (Contracted, Pending):**
- **Tourmind 途灵** (Shenzhen-based, tier-1 domestic)

**Chinese Specialty Suppliers (Live):**
- **Mengtu 萌兔**

**Chinese Specialty / Third-Party Channels (Negotiating):**
- **几度 Travel** (contract received, pending review)
- **玩子云科技商务**
- **Harvest Elite**
- **SCTT**
- **游由国际** (HDP integration via Chinese third-party)
- **臻旅国际** (HDP integration via Chinese third-party)
- **樂遊五洲** (HDP integration via Chinese third-party)

**Asia-Region Specialty Suppliers:**
- **ABC Travel Taipei** (Taiwan — APAC / Southeast Asia)
- **MG HOLIDA** (Indonesia — Southeast Asia direct + aggregation)
- **TBO** (India — Asian regional strength alongside global breadth)

*Note: Many of the Asia-specialty suppliers also appear in Bucket C as bedbank-style aggregators. The dual listing is intentional — Bucket C is about supply-type (aggregator), Bucket D is about geographic moat. The same partner can serve both lenses.*

**Why this is the single biggest differentiator:**

**Market math:**
- China = **58% of the total Asia travel market** (per data referenced at GBTA)
- The other ~42% of Asia travel is the rest of the region combined
- Asia overall is one of the largest and fastest-growing travel markets in the world
- A TMC that serves global enterprise clients almost always has Asia exposure

**Structural facts about China supply:**
- China operates on a completely different ecosystem from global travel. Different platforms, different payment systems, different commercial norms, different regulatory environment.
- Chinese hotel chains and platforms are not meaningfully addressable from outside Asia without local presence and relationships.
- "Connecting to China" is not a technical task. It's a relationship and operations task that takes years.

**Why competitors can't fix this short-term:**
- **Spotnana** and **Nuitee** are based outside Asia. They can connect to some Asian inventory via bedbanks (Bucket C), but that loses corporate-rate access and reliability.
- B2B wholesalers don't help — same problem as above plus wrong rate type.
- A new entrant would need years of in-market work, plus Mandarin commercial team, plus local relationships, plus understanding of how Chinese hotel operations actually run.

**Why this is FCG's most durable advantage:**
- We are based here.
- The team has spent years building these relationships.
- Every new TMC customer that integrates with us for Asia coverage reinforces the moat by adding volume to the channel, which improves our commercial terms with the supply side.

---

## 3. What Else Is "Behind" the API

The four supply buckets above are the headline asset, but the supply network also includes the substantial back-end work required to make 4M+ hotels actually usable by a TMC's customer in a real booking flow.

### 3.1 Mapping (4M+ properties)

- FCG's hotel database covers **4 million+ properties** with active mapping across sources.
- Mapping is universally hard — described internally as "a worldwide problem that no one has perfectly solved." Different sources use different IDs, different names, different addresses, different geo-coordinates for the same hotel.
- The mapping work itself is a moat. Every new TMC customer benefits from years of accumulated mapping intelligence; they would never recreate it themselves.
- This is also why we're developing mapping as a potentially separate product offering — the work product has standalone value.

### 3.2 Multi-language and multi-currency

- Hotel content arrives in many languages from many sources. FCG normalizes it.
- Currency handling across sources is non-trivial — exchange rates, source-currency vs. display-currency vs. booking-currency, settlement currency for the TMC.
- These are not glamorous problems but they are integration blockers if not solved. A TMC trying to do this themselves would spend months per source.

### 3.3 Quality scoring and ranking

- An internal data platform tracks supplier quality (cancellation success rate, confermation reliability, price stability, etc.).
- This feeds future capabilities like **AI-driven automatic markup** — using machine learning to determine optimal markup per source per route per traveler segment, rather than the legacy "1% or 2% flat per supplier" approach.

### 3.4 Operations and mid-office handling

- Beyond bookings, FCG handles the operational events that follow a booking: cancellations, reschedules, traveler emergencies, modification requests, refund flows.
- This is the **天工 (Tian Gong) BMS** — the booking management mid-office.
- A booking is an order. An event (e.g., "I can't make this trip") is an entire ripple of work across the order, the traveler's profile, future itinerary, payment status, etc. Wholesalers don't handle this. We do.

### 3.5 Two-way supply integration (SR / supply platform)

- We integrate supply two ways:
  - **Active mode:** FCG onboards new suppliers proactively.
  - **Passive mode:** We expose our own ingestion interface so suppliers can self-onboard.
- This scales the network faster than one-by-one BD.

---

## 4. Why This Is a Real Moat (Not Just a Feature)

Five reinforcing reasons why the supply network cannot be cloned:

### 4.1 Time

- A single GDS integration: 180+ days minimum.
- A direct-hotel contract at scale: years to build the commercial relationship.
- A working channel-manager partnership: 6–12 months from BD to live.
- A network of dozens of sources: the cumulative time is measured in years, not quarters.

### 4.2 Relationships

- Corporate-rate access requires trust with hotels and corporates. You can't fast-track this with capital.
- China and Asia relationships in particular require local presence, local team, and local operating credibility.

### 4.3 Scale economics

- More sources → better coverage → more attractive to TMCs → more booking volume → better commercial terms from suppliers → more sources can afford to integrate with us → more coverage. Flywheel.
- A new entrant doesn't get good commercial terms from suppliers without volume. They don't get volume without good rates. The moat compounds.

### 4.4 Operational know-how

- Mapping, currency, multi-language, supplier quality scoring, mid-office event handling — every one of these is a year+ of accumulated experience to do well.
- Not buyable. Has to be built.

### 4.5 Geographic positioning

- Asia/China supply requires being based in Asia. A global competitor cannot pick this up by hiring a remote rep.
- The asymmetry is durable: we are physically positioned where the growth is.

---

## 5. How This Differentiates Us — Layer by Layer

### 5.1 vs. B2B Wholesalers / Bedbanks (Didatravel, HeyTrip, Hotelbeds, etc.)

The supply story doesn't just differentiate us — it **disqualifies them** for the corporate travel use case.

| Capability | B2B Wholesalers | FCG |
|---|---|---|
| Corporate negotiated (RFP) rates | No — structurally cannot | Yes — via GDS + direct hotel |
| Direct hotel relationships | Few — mostly resell from upstream | Many — primary channel |
| GDS connections | No (for corporate rate purpose) | Yes — Amadeus, Sabre |
| Booking accountability | Opaque re-routing chains | Direct-where-possible, full chain visibility |
| TMC-specific workflows | Side channel, not their DNA | The entire product |
| Visible at GBTA | No | Yes |

The buyer-side test: ask any large corporate's travel manager what share of their bookings are corporate-negotiated rates. If it's meaningful (typically 50–70% at large corporates), wholesalers cannot serve that share. End of story.

### 5.2 vs. Same-Category Players (Spotnana, Nuitee, etc.)

Here the supply story shifts from disqualification to gap-filling.

| Capability | Spotnana / Nuitee | FCG |
|---|---|---|
| Corporate rates in Western markets | Yes | Yes |
| Corporate rates in Asia/China | Limited | Strong — direct relationships |
| China hotel chain direct supply | Limited via bedbanks | Direct |
| Operational base in Asia | No (global-first) | Yes |
| Asian channel manager relationships | Limited | Established |

**Pitch reality:** Most large TMCs multiplex API providers — they don't pick one. The question is not "FCG vs Spotnana" but "do you have the Asia layer you need?" If yes via someone else, fine. If no, FCG is the answer.

---

## 6. How to Talk About the Supply Network

### 6.1 Tier 1 — The Headline

> "FCG aggregates four structurally different supply types — GDS, direct hotel, channel manager / NDC, and bedbank — into one corporate-grade pipe. The combination gives our TMC customers access to **corporate negotiated rates**, **reliable bookings**, and the **deepest Asia and China supply in the category**."

### 6.2 Tier 2 — The Differentiation

> "Wholesalers can sell you inventory. They cannot sell you corporate rates — that's a structural limitation of how hotels distribute. Global API competitors can connect to many of the same sources we do, but they cannot match our Asia depth. We are based here. We have direct relationships with Chinese hotel chains, regional channel managers, and the major Chinese platforms. China alone is 58% of Asian travel — that's not a side feature, it's a different category of value."

### 6.3 Tier 3 — The Operational Story

> "Connecting one new supply source takes a TMC roughly 180 days, ignoring the mapping, currency, multi-language, and ongoing operations work. We've done that work across dozens of sources, plus we've built the mid-office (Tian Gong) that handles what happens *after* the booking — cancellations, changes, traveler emergencies. The supply network is the headline; the operations behind it is what makes the supply usable."

### 6.4 Tier 4 — The Reliability Story

> "Open the front page of any wholesale bedbank. Their distribution channels include OTAs, TMCs, DMCs, and agencies — all in one channel. When a booking goes wrong, it's re-routed through other wholesalers and accountability disappears. Ask your operations team how often this happens today. For corporate travel, where a stranded traveler is an executive emergency, this is unacceptable. Our model is direct-where-possible. We can tell you exactly where your booking sits in the chain."

---

## 7. Canonical Supplier Inventory

Source: G-link Supplier Status Sheet (43 entries). Updated May 2026.

### 7.1 GDS — Live

| # | Supplier | Code | Notes |
|---|---|---|---|
| 9 | Sabre | — | Global GDS |
| 10 | SabreABC | — | Global GDS |

*Amadeus referenced as strategic direction in internal walkthrough; not on current G-link supplier list.*

### 7.2 International Tier-1 Wholesalers

**Live:**

| # | Supplier | Code | Notes |
|---|---|---|---|
| 1 | RateHawk Global | TS10000513 | Bedbank — direct + aggregation; ME, Europe, APAC pricing strength |
| 7 | Expedia EPS | TS10000501 | |
| 8 | MIKI | TS10000619 | UK (London); est. 1967; global B2B hotel + travel wholesaler; comparable to Hotelbeds, Webbeds, W2M, TBO, Restel |
| 11 | Hotelbeds | — | |
| 12 | Bedsonline | TS10000693 | |

**Contracted, pending activation / in review:**

| # | Supplier | Status | Notes |
|---|---|---|---|
| 14 | Agoda | Contract signed, pending | Deposit threshold high |
| 16 | Webbeds / DOTW | Coming soon | Web Travel Group (Webjet); Dubai HQ; 500K+ hotels, 30K+ direct, 50+ countries — #2 global B2B after Hotelbeds |
| 21 | Restel Hotels | Contract in review | Madrid (Hotusa Group); global direct + 100+ countries |
| 33 | Veturis 维途 | Contract signed, pending | Spanish; Southern Europe / Latin America strong |
| 35 | Nuitee | Contract signed, pending | (Note: also a competitor — see positioning doc) |

### 7.3 Pure Resource / B2B Direct Platforms

| # | Supplier | Code | Status | Notes |
|---|---|---|---|---|
| 13 | HyperGuest | TS10000691 | Live | Israel (Tel Aviv); hotel ↔ distributor direct-connect platform |
| 17 | Shiji 石基 | — | Contract signed, in development | Gateway to multiple hotel-chain integrations |
| 18 | Derbisoft 德比 | — | Coming soon | Channel manager |
| 23 | iOL X | — | Contract in review | |

### 7.4 Chinese Top-Tier B2B Wholesalers

**Live:**

| # | Supplier | Code | Notes |
|---|---|---|---|
| 2 | Heytrip 喜玩 | TS10000524 | China leading B2B wholesaler |
| 3 | Huitravel 汇智 | TS10000522 | China leading B2B wholesaler |
| 4 | Meituan 美团 (Overseas) | TS10000514 | Major Chinese hotel/lifestyle platform |
| 6 | Dida Travel 道旅 | TS10000525 | China leading B2B wholesaler |

**Contracted, pending:**

| # | Supplier | Notes |
|---|---|---|
| 20 | Tourmind 途灵 | Shenzhen-based; direct + aggregation; tier-1 domestic |

### 7.5 Mid-Size / Specialty B2B / Regional Route Suppliers

**Live:**

| # | Supplier | Code | Notes |
|---|---|---|---|
| 5 | Mengtu 萌兔 | TS10000508 | Niche route specialty |

**Contracted or in review:**

| # | Supplier | Status | Notes |
|---|---|---|---|
| 19 | ABC Travel Taipei | Contract signed, pending | Taiwan; APAC / Southeast Asia specialty |
| 21 | Pax2Night | Signed, awaiting Shiji | Turkey (Istanbul, Yuppi Group); Turkey/MENA strong, 600K+ inventory |
| 25 | YALAGO | Contract in review | Dubai; Emirates Airlines Group; ME / SE Asia strong |
| 26 | OhmyHotel | Contract in review | |
| 27 | Amerilink | Contract in review | |
| 28 | Methabook | Contract in review | |
| 29 | TBO | Coming soon | India (Gurugram); 1M+ rooms, 50K+ direct |
| 39 | MG HOLIDA | Negotiating | Bali (Indonesia); SE Asia direct + global aggregation |

### 7.6 Chinese Platforms Going Abroad

| # | Supplier | Status | Notes |
|---|---|---|---|
| 24 | 携程国际 (Trip.com International) | Coming soon | Indirect — via Chinese third-party partnership |

### 7.7 Chinese Specialty / Third-Party / HDP Channels

**Negotiating:**

| # | Supplier | Type | Notes |
|---|---|---|---|
| 30 | 几度 Travel | Mid-size B2B / resource | Contract received, pending |
| 31 | 玩子云科技商务 | Mid-size B2B / resource | |
| 32 | Harvest Elite | Mid-size B2B / resource | |
| 34 | SCTT | Mid-size B2B / resource | Contract signed, pending |
| 36 | 游由国际 | HDP integration (China third-party) | |
| 37 | 臻旅国际 | HDP integration (China third-party) | |
| 38 | 樂遊五洲 | HDP integration (China third-party) | |

### 7.8 Chinese Hotel Chains — G-link Deployed Directly

This is a distinct category. These are not vendor relationships — they are **G-link installations inside the chain's own distribution operations**.

| # | Chain | Status |
|---|---|---|
| 40 | 锦江国际 (Jin Jiang International) | G-link deployed |
| 41 | 锦江 (Jin Jiang) | G-link deployed |
| 42 | 亚朵 (Atour) | G-link deployed |
| 43 | 如家 (Home Inns) | G-link deployed |

**Strategic significance:** Direct deployment inside the top Chinese hotel groups is the deepest possible integration. It is also the most defensible — once a chain is running on G-link, it becomes infrastructure, not a swap-out vendor.

### 7.9 Air Supply (F-link)

| Supplier | Status | Notes |
|---|---|---|
| Travelsky / Zhifei | Live (white-label partnership) | China air ticket distribution; front-end consistency with FCG's CBT |

*Additional F-link air partners — to be documented as F-link matures.*

### 7.10 Supply Status Summary

| Status | Count |
|---|---|
| **Live** | 13 |
| **Contracted, pending / coming soon** | 14 |
| **Contract in review** | 5 |
| **Negotiating** | 7 |
| **Chinese hotel chains deployed** | 4 |
| **Total in pipeline** | **43** |

---

## 8. Key Stats — Quick Reference

| Stat | Source / Context |
|---|---|
| **4M+ hotels** in active mapping | FCG internal supply database |
| **43 suppliers** in the G-link pipeline (13 live, 30 in onboarding/negotiation) | G-link supplier status sheet, May 2026 |
| **4 top Chinese hotel chains** deployed on G-link directly (Jin Jiang International, Jin Jiang, Atour, Home Inns) | G-link supplier status sheet |
| **58%** of Asia travel volume = China | GBTA-published figure referenced internally |
| **180+ days** = single new GDS or major source integration | Industry standard, referenced internally |
| **~70%** of large-corporate bookings = corporate negotiated rates | E.g., Alibaba reference cited internally |
| **3 API surfaces** exposed through the Open Platform | G-link, F-link, TMC API |
| **3 integration methods** | API, SDK, Skills (AI-native) |

---

*Companion doc to: FCG-positioning-reference.md*
*Source: Internal walkthrough by Elaine Wan, May 2026. Supplier names below the line in Section 7 to be completed from Crystal's attached supply doc.*
