# FCG Positioning Reference

**Purpose:** Definitive reference doc on FCG's ICP, USP, moat, and competitive differentiation. Source: Elaine Wan's internal walkthrough (May 2026). For use in internal training and external materials.

---

## 1. TL;DR — One-page Summary

**Who we sell to:** TMCs (Travel Management Companies), with a strategic focus on **Asia-based TMCs serving corporate travelers**. Single audience. No DMC, no OTA, no direct corporate.

**What we sell:** Connectivity to a corporate-travel-grade supply network, wrapped in a complete front-/mid-/back-office system. Three product lines: **G-link** (hotels — core), **F-link** (air — early stage), and a **TMC OBT suite** (CBT + ABT + AI Booking Tool).

**Why customers pick us — two layers:**

| Comparison axis | Our answer |
|---|---|
| **vs. B2B wholesalers / bedbanks** (Didatravel, HeyTrip, Hotelbeds, Expedia TAAP, etc.) | We're the only category built for **corporate travel** specifically. Wholesalers physically cannot deliver RFP/corporate-negotiated rates (hotels don't pass corporate rates through wholesale channels). For large corporates, ~70% of bookings are RFP rates. Wholesalers also fail on reliability — they re-route bookings through opaque chains and can't honor cancellations/holds/changes the way corporate travel demands. |
| **vs. same-category TMC API platforms** (Spotnana, Nuitee) | We own the **China + Asia supply chain** at a depth no global competitor can match. China = 58% of Asia travel volume and is a structurally unique ecosystem. We are based here and have spent years negotiating direct relationships. |

**The strategic insight:** Customers don't actually want our API. They want **what's behind the API** — the supply network, the corporate-rate access, the reliability. The API is just an integration method; the moat is the network it connects to.

---

## 2. ICP — Who We Sell To

### 2.1 Primary ICP: TMCs

FCG's single audience is **TMCs**. This is non-negotiable and defines every product decision.

Customers come in two sub-segments based on technical maturity:

| Segment | Profile | Product Fit |
|---|---|---|
| **TMCs with their own systems** (~70% of pipeline today) | Has in-house dev, existing booking platform, just needs supply | **G-link API** (or SDK / AI-native skills integration) |
| **TMCs without systems** | No internal platform, can't go through GDS easily, needs out-of-the-box tooling | **OBT suite** (CBT, ABT, AI Booking Tool) — and the OBT integration pulls them onto our supply by default |

### 2.2 Geographic focus: Asia-based TMCs

Strategy is to win Asia first. Reasons:
- Proximity for high-touch OBT deployments (OBT changes a TMC's entire operating workflow — requires daily comms, not a one-time install).
- Our supply moat is strongest in China + Asia.
- China alone represents 58% of Asia's travel spend, and is a structurally distinct market.

### 2.3 What FCG does NOT sell to

- **Not OTAs** — would erase our differentiation (we'd just be another wholesale source).
- **Not DMCs** — DMCs just want cheap inventory; we don't compete on price-as-inventory.
- **Not direct corporates** — that's Accomy's lane (service delivery, not system licensing).

### 2.4 FCG vs Accomy (critical org distinction)

| | FCG | Accomy |
|---|---|---|
| Sells | A **system** (tools + API + supply) | A **service / solution** |
| Customer | TMCs | End corporates |
| RFP example | Licenses the RFP tool to a TMC (e.g., UOB uses our tool with their own sourcing team) | Delivers the full RFP project for a corporate (e.g., JD asks Accomy → Nanli team sources, signs, reports back) |
| Accomy's place in FCG's worldview | Just another user of FCG's system | n/a |

**Rule of thumb:** If the buyer wants *the tool*, it's FCG. If they want *the outcome delivered*, it's Accomy.

---

## 3. The Product Stack

### 3.1 Three product lines

```
┌─────────────────────────────────────────────────────────────┐
│  G-LINK (hotel)        F-LINK (air)        TMC OBT SUITE    │
│  — core, 10/10 mature  — early, ~5/10      — CBT + ABT +    │
│  — heavy investment    — light investment     AI Booking    │
│                                            — 4–5/10 mature  │
└─────────────────────────────────────────────────────────────┘
              ▲                    ▲                    ▲
              │                    │                    │
         API / SDK / Skills (3 integration methods, same backend)
```

### 3.2 G-link — what it actually connects to

G-link's job is to abstract a **chaotic, multi-source supply landscape** into one corporate-grade API. The supply network has four buckets:

| Bucket | Sources | Why it matters |
|---|---|---|
| **GDS direct** | Amadeus, Sabre | The only channel that can carry corporate negotiated rates (RFP rates). Third-party aggregators *physically cannot* connect here for corporate rates. |
| **NDC / Direct-to-hotel** | Direct hotel contracts, channel managers (Derbisoft, etc.), email confirmations for some flows | Most reliable channel. Hotels won't pass corporate rates through wholesale. |
| **Bedbank aggregators** | HotelBeds (HBX), Expedia, Meituan, Qunar/Monster, Trip.com, Travelfusion, Xixin | Volume/leisure coverage. We connect them but they are not the moat. |
| **China-specific supply** | Direct relationships with Chinese hotel chains, regional channels | Our biggest single differentiator vs Western competitors. |

**Why this matters:** A TMC integrating with us avoids 180+ days of integration work per source, plus the mapping, currency, multi-language, and data-normalization problems that come with each new channel. This is not just a tech problem — it's an experience problem.

### 3.3 TMC OBT Suite — purpose and components

The OBT suite is **not the product we lead with**. It exists because some TMCs have no system, and the only way to get them onto our supply is to give them a system.

| Component | Status | Purpose |
|---|---|---|
| **CBT** (Corporate Booking Tool) | ~10/10 — fully mature | Front-end booking interface for corporate travelers |
| **ABT** (Agent Booking Tool) | ~5/10 — mid-maturity | Interface for TMC agents booking on behalf of corporates |
| **AI Booking Tool** | Demo stage | Future product — natural-language booking. Currently being built/tested via Alan (Accomy) as the trial user. |
| **Mid-office (BMS)** | Available | Handles event-level ops (cancellations, reschedules, traveler issues — not just orders) |
| **RFP tool (天机 / Tianji)** | Available | Lets TMCs run their own RFPs. (Accomy uses the same tool internally to deliver RFPs as a service via the Nanli team.) |
| **White-label front-end** | In development | Goal: upload logo + a sentence → AI auto-generates a differentiated branded page. Today: template-based. |

### 3.4 Three integration methods (same backend, three doors)

| Method | Best for | Status |
|---|---|---|
| **Skills (AI-native)** | New developers, AI agent integrations, fastest path | Recommended default going forward |
| **API** | Traditional integrations, full control | V2 live; V3 in design |
| **SDK** | Standard developer experience | Supported |

**Note on the three API surfaces hosted on the Open Platform:**
- **G-link API** — hotel supply.
- **F-link API** — air supply.
- **TMC API** — plug-and-play white-label TMC modules (expense management, duty of care, etc.) that TMCs can integrate independently of supply. Not a "view" of supply — a separate functional domain.

See [FCG-products.md](FCG-products.md) for full product detail.

### 3.5 Open Platform (developer portal)

The strategic goal: a developer can register, read docs, and self-serve integrate **without ever talking to a human at FCG**. AI-assisted error resolution + skills-based natural-language integration. The API itself becomes a product, not a deliverable.

---

## 4. The Moat — Why We Can Sell This

### 4.1 The supply chain moat (primary)

Years of TMC-specific supply chain negotiation. We connect:
- **Multiple GDS** (Amadeus, Sabre) — the only path to corporate-rate inventory
- **Direct hotel** contracts and channel-manager connections (carries corporate RFP rates)
- **Bedbank aggregators** for breadth
- **Deep China + Asia direct supply** — competitors based outside Asia structurally cannot match this

This is non-replicable in the short term. It is the product.

### 4.2 The corporate-travel domain moat

We are the only category player **built specifically for corporate travel scenarios**. Not B2B wholesale repackaged for TMCs. This shows up in:
- Corporate-rate handling (RFP, negotiated rates)
- Approval workflows, traveler policy
- Mid-office event handling (not just order handling)
- Reliability standards corporate travel demands

### 4.3 The integration ease moat (emerging)

Open developer platform + AI-native skills integration + SDK + traditional API. Designed so a new dev with light IT background can integrate without a human handoff. Most competitors still gatekeep behind business teams + ticketed support.

### 4.4 The geographic/regulatory moat

Being based in Asia / China gives us structural advantages no Spotnana-style global competitor can replicate:
- Direct relationships with Chinese hotel chains
- Local payment, currency, language handling
- Understanding of a market that operates on completely different rules than global

---

## 5. USP — The Dual-Layer Differentiation

Sales must be able to answer two distinct questions. They are different objections from different competitor classes.

### Layer 1 — "How are you different from Didatravel / HeyTrip / Hotelbeds?"
(The B2B wholesale / bedbank objection)

**Answer:** Their business model is **markup middleware**. They source upstream → mark up → distribute to anyone who'll buy (OTAs, TMCs, DMCs, agencies). This model fails corporate travel on three counts:

1. **No corporate rates.** Hotels do not pass corporate-negotiated (RFP) rates through wholesale channels. A wholesaler physically cannot deliver the rate type that represents ~70% of a large corporate's bookings.
2. **No reliability.** Wholesalers re-route bookings through opaque supplier chains (A → B → C → D). When a cancellation, hold, or change is needed, nobody owns the resolution. For corporate travel, this is disqualifying.
3. **Wrong customer focus.** Their "TMC distribution" channel is a side line. Walk any corporate-travel trade show (GBTA) — they're not exhibiting. We are. That's not an accident.

**Telltale sales line:** *"They can sell you inventory. We can sell you a corporate-travel-ready solution. Open the front page of any wholesaler — they distribute to OTAs and TMCs in the same channel. We don't have an OTA channel. Our entire stack only makes sense for corporate travel."*

### Layer 2 — "How are you different from Spotnana / Nuitee?"
(The same-category competitor objection)

**Answer:** Same shape of product, fundamentally different supply position.

1. **China + Asia supply depth.** Asia = unique market with rules global players don't understand. China alone = 58% of Asia travel spend. We are based here; they are not. Any TMC whose corporate clients touch Asia or China has a hard reason to add us even if already integrated elsewhere.
2. **Corporate-rate access in Asia.** Same point as Layer 1, but specifically in a region global competitors don't have the relationships to deliver.
3. **System completeness for emerging TMCs.** OBT + CBT + ABT + AI Booking Tool + BMS + RFP tool — full vertical for TMCs that don't have their own stack. Spotnana competes here too; Nuitee less so. Our edge is regional fit + Asian-corporate workflows.

**Telltale sales line:** *"If you already connect via [Spotnana/Nuitee], great — add us for Asia. Most large TMCs won't pick a single API; they multiplex. The question isn't whether to replace, it's why you'd skip the Asia layer."*

### Combined positioning statement

> FCG is a **corporate-travel-grade connectivity platform for TMCs**, with the deepest **China + Asia supply chain** in the category and a **full TMC operating system** (CBT, ABT, AI Booking Tool, BMS, RFP) for TMCs that need more than just an API. We are not a wholesaler. We are not a global generalist. We are the layer TMCs use when corporate travel reliability and Asian inventory both matter.

---

## 6. Competitive Map — Category of One

```
                    ┌─────────────────────────────────────────┐
                    │   CORPORATE TRAVEL FOCUS                │
                    │                                         │
                    │              FCG                        │
                    │    (Asia/China-native,                  │
                    │     full TMC stack +                    │
                    │     corporate-rate supply)              │
                    │                                         │
   GLOBAL  ◄────────┤   Spotnana   Nuitee                     │────►  ASIA-NATIVE
                    │   (global,   (global API,               │
                    │    TMC-       supply marketplace)       │
                    │    focused)                             │
                    │                                         │
                    └─────────────────────────────────────────┘
                                       │
                    ┌──────────────────┴──────────────────────┐
                    │                                         │
                    │    Didatravel   HeyTrip   Hotelbeds     │
                    │    Expedia TAAP   Travelfusion          │
                    │                                         │
                    │   B2B WHOLESALE / BEDBANK               │
                    │   (markup-middleware, no corporate-     │
                    │    rate capability, OTA-first DNA)      │
                    │                                         │
                    └─────────────────────────────────────────┘
```

**Category creation:** FCG is positioning itself as the only player that is *both* corporate-travel-specialist *and* Asia-native with deep regional supply. Spotnana/Nuitee occupy the corporate-travel-specialist quadrant but are global-first. Didatravel/HeyTrip/Hotelbeds occupy adjacent markets but are structurally unable to serve corporate travel.

| Player | Corporate-travel native? | Asia/China supply depth? | Full TMC stack? | RFP/corporate rates? |
|---|---|---|---|---|
| **FCG** | Yes | Deep | Yes | Yes |
| **Spotnana** | Yes | Limited | Yes | Yes (Western) |
| **Nuitee** | Partial (API-first) | Limited | No (API-only) | Limited |
| **Didatravel** | No (B2B wholesale) | Some China | No | No |
| **HeyTrip** | No (B2B wholesale) | Some Asia | No | No |
| **Hotelbeds / HBX** | No (B2B wholesale) | Limited Asia | No | No |

---

## 7. Sales Talk Track — Cheat Sheet

### Discovery questions that surface our fit

1. *"What share of your client bookings are corporate-negotiated (RFP) rates?"* — If meaningful (corporate clients above mid-market typically 50–70%), wholesalers are disqualified for that share.
2. *"Where do your clients travel?"* — Asia/China presence = strong FCG fit.
3. *"Do you have your own booking platform, or do you need tooling?"* — Decides API-only vs full OBT suite.
4. *"What's your dev capacity for new integrations?"* — If thin, lead with Skills/AI integration as the unlock.

### Objection handling

| Objection | Response |
|---|---|
| *"We already use Didatravel / Hotelbeds."* | They give you leisure-grade inventory. They cannot give you corporate-negotiated rates. ~70% of your large-corporate volume is unreachable through them. We add the RFP layer they can't. |
| *"We already use Spotnana / Nuitee."* | Most large TMCs multiplex. The question is your Asia exposure. If China is in your client mix, we close a gap your current API can't. |
| *"Your API is one more integration to maintain."* | We support Skills + SDK + API. A new dev can integrate via natural language without talking to a human at FCG. Closer to one-click than one-integration. |
| *"Pricing — why are you not the cheapest?"* | We aren't sold on price-per-room — we're sold on corporate-rate access, reliability, and Asia depth. Cheapest wholesaler bookings get re-routed and dropped. Ask your ops team how often that happens today. |
| *"We just want the API, not the system."* | That's fine — most of our TMC customers (~70%) only take API. The full OBT suite is for TMCs without their own platform. |

### What to lead with (depending on buyer)

| Buyer profile | Lead with |
|---|---|
| TMC with own platform, dev team, global footprint | G-link API + Asia/China supply story |
| TMC with no platform, growing | OBT suite + "we get you to launch in weeks not years" |
| TMC with corporate clients in Asia | RFP capability + direct-hotel + GDS corporate-rate story |
| TMC piloting AI agent products | Skills integration + open platform + AI Booking Tool reference |

---

## 8. Pricing Model (directional, to be finalized)

Per Elaine: pricing will be standardized and published. Current directional structure:

- **Setup fee** (e.g., ~$8,000 reference point)
- **Monthly subscription** (e.g., ~$3,000–4,000/month reference point)
- Tiered by product (G-link only vs full OBT suite, white-label, etc.)
- RFP delivery via Accomy/Nanli team is priced separately (service, not tool)

**Internal rule:** When licensing the RFP tool to a TMC, FCG charges for the tool. When a corporate buys RFP-as-a-service, Accomy charges for the service and pays the Nanli sourcing team.

---

## 9. Strategy & Roadmap Markers

### Near-term focus (per Elaine)
1. **Split G-link, F-link, and TMC product lines** clearly in all marketing — they answer different needs.
2. **Lead with "what's behind the API"** — supply network, Asia depth, corporate-rate access. The API is the door, not the value.
3. **Standardize pricing and publish it.**
4. **Ship open developer platform** so integration is self-serve.
5. **Launch Skills / AI-native integration** as the default recommended path.
6. **Standardize white-label generation** — long-term goal: upload logo + sentence → AI generates a differentiated branded page.

### Where we are honest about gaps
- **F-link** is early stage. Two-person team. Light investment for now.
- **ABT and AI Booking Tool** are mid-maturity (5/10) — usable but iterating.
- **Mapping** is a hard problem industry-wide. We don't claim perfect; we claim "better than most."
- **OBT deployment is high-touch** — changes a TMC's whole operating workflow, requires Asia-proximity delivery, which is why we focus there first.

### Long-term moat building
- Deepen China + Asia direct supply (irreplaceable advantage).
- Become the default API for AI booking agents (Skills + open platform positions us here).
- Win Asian TMCs to a point where global TMCs add us specifically for Asia coverage — same pattern as how Western platforms get added for Western coverage.

---

## 10. Glossary

| Term | Meaning |
|---|---|
| **TMC** | Travel Management Company — sells/manages travel for corporate clients |
| **OBT** | Online Booking Tool — broad term for booking interface stack |
| **CBT** | Corporate Booking Tool — front-end for corporate travelers |
| **ABT** | Agent Booking Tool — front-end for TMC agents |
| **BMS** | Booking Management System — mid-office order/event handling |
| **RFP rate** | Hotel rate negotiated via a corporate Request-for-Proposal — not available through wholesale channels |
| **GDS** | Global Distribution System (Amadeus, Sabre) — legacy backbone, carries corporate rates |
| **NDC** | New Distribution Capability — modern direct-hotel content protocol |
| **Bedbank** | B2B hotel wholesaler aggregating supply for resale |
| **Skills (integration)** | AI-native integration method — developer issues natural-language requests, AI generates integration code from our docs |
| **G-link / F-link** | FCG hotel / flight product lines |
| **Nanli team** | Accomy's RFP sourcing team — described internally as the most professional RFP sourcing team in Asia |
| **Tianji (天机)** | FCG's RFP tool product |

---

*Source: Internal walkthrough by Elaine Wan, May 2026. This doc is the canonical positioning reference — update here before updating marketing materials.*
