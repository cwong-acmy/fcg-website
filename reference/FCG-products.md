# FCG Products — G-link, F-link, Open Platform

**Purpose:** Definitive product description for the three core APIs/products TMCs use from FCG. Used for product marketing, sales enablement, developer documentation framing, and internal alignment.

> "We have three products. Three integration methods. Same backend. The customer picks the door; what they get behind the door is what matters." — paraphrased from Elaine Wan

---

## 1. Product Stack Overview

FCG offers three product surfaces — all hosted on the **Open Platform** — that a TMC can consume independently or in combination:

| Product | What it is | What it serves | Maturity |
|---|---|---|---|
| **G-link API** | Hotel supply API | Hotel inventory across GDS, direct hotel, channel managers, bedbanks, and Asia-direct (4M+ hotels, 43 suppliers in pipeline) | **Core / mature** — heavy investment, primary product |
| **F-link API** | Air ticket supply API | Air inventory via Travelsky / Zhifei and other air sources | **Early stage** — light investment, two-person team currently |
| **TMC API** | White-label, plug-and-play TMC business modules | Expense management, duty of care, and other modular TMC capabilities that TMCs plug into their existing systems without building from scratch | **Live and expanding** — module set growing |
| **Open Platform** | The developer platform that hosts and exposes all three APIs above | Self-serve integration via API, SDK, or Skills (AI-native); developer registration, docs, error resolution, ticket support | **Live (V2)** — V3 in design, continuous improvement |

G-link and F-link sit on top of FCG's supply network (see [FCG-supply-network.md](FCG-supply-network.md)). The TMC API is a separate functional domain — operational TMC capabilities packaged as modular APIs. The Open Platform is the **single front door** through which developers discover, integrate, and operate against all three.

---

## 2. G-link

### 2.1 What G-link Is

G-link is FCG's **hotel supply API and back-end system**. It is the company's core product and the focus of the heaviest engineering investment.

What G-link technically delivers:
- A single API that abstracts FCG's full hotel supply network behind one interface
- Search, availability, booking, modification, cancellation, and post-booking event handling
- 4M+ mapped hotel properties
- Multi-source pricing with deduplication, ranking, and quality scoring
- Multi-currency, multi-language support
- Corporate-rate-aware (RFP rates routed through GDS / direct hotel channels)

### 2.2 Target Audience

**Primary:** TMCs that have their own platform or development team and need supply.

This is roughly **70% of FCG's pipeline today**. These TMCs do not need an FCG-built booking interface — they have their own. What they need is access to deep, reliable, corporate-grade hotel supply, delivered via a clean API.

**Secondary:** TMCs whose end-clients (corporates) have strong Asia or China travel exposure. These TMCs may integrate FCG specifically as an *Asia layer* on top of existing global supply.

**Disqualifier:** A TMC that doesn't have its own system and can't develop against an API — they need the OBT suite instead (or in addition).

### 2.3 What G-link Enables a TMC to Do

| Capability | What the TMC gets |
|---|---|
| **Single integration, multi-source supply** | Connect to one FCG API; instantly access GDS, direct hotel, channel managers, and Asia-direct supply. Avoid the 180+ days per source they'd otherwise spend. |
| **Corporate-rate access** | Serve corporate customers whose RFP-negotiated rates account for up to ~70% of their booking volume. Wholesalers cannot deliver this. |
| **China and Asia coverage** | Offer their end-clients deep Chinese hotel chain inventory and broader Asia inventory through direct relationships, not via opaque wholesale chains. |
| **Reliable booking-to-fulfillment** | Direct-where-possible booking paths; cancellations, holds, and changes traceable and accountable. |
| **Operational depth (mid-office)** | Beyond the order, the system handles traveler events — reschedules, cancellations, emergencies — through the BMS (Tian Gong) layer. |
| **Quality-scored sources** | Internal data platform ranks supplier reliability so the TMC's bookings flow through the most dependable available source. |

### 2.4 Key Features

- **Multi-channel supply aggregation** — four structurally different supply buckets behind one interface
- **4 million+ mapped hotels**
- **Corporate-rate routing** — automatic preference for negotiated rates when available
- **Multi-language hotel content normalization**
- **Multi-currency handling** including source/display/booking/settlement currency separation
- **Booking management mid-office (Tian Gong / BMS)** — handles events post-booking
- **Mapping intelligence** — years of accumulated property-mapping work, exposed as a reliable layer
- **API versioning** — V2 currently live, V3 in design for international standards alignment
- **Integration via API, SDK, or Skills (AI-native)** through the Open Platform

### 2.5 Why G-link Is Special

**The "what's behind it" advantage.** G-link's competitive value is not the API — it is the **supply network it connects to**. No competitor can match the combination of corporate-rate access + Asia depth + four-bucket source diversity.

**Corporate-travel-native, not B2B-wholesale-repackaged.** G-link was built for the TMC use case from day one. Approval flows, traveler policy, corporate-rate routing, event handling — all native concerns, not afterthoughts.

**Built by a team operating in the market it serves.** The product reflects deep familiarity with Asia's travel ecosystem because the engineering and BD teams are based here.

**Time-replacement value.** A TMC connecting one new GDS or major supply source takes 180+ days. G-link replaces dozens of such projects with one integration. That alone is the business case.

### 2.6 What G-link Does Not Do

- It is **not a booking interface** by itself — it's the supply layer. If a TMC needs a UI, they need the OBT suite or to build their own.
- It is **not a corporate-facing product**. G-link is for the TMC. The TMC's end-customer (the corporate) interacts with the TMC's interface, not G-link directly.
- It is **not optimized for OTA distribution**. Building G-link to serve OTAs would compromise its corporate-travel focus — that's a deliberate choice.

---

## 3. F-link

### 3.1 What F-link Is

F-link is FCG's **air ticket supply API and system** — the air equivalent of G-link.

F-link is currently **early stage** with light investment relative to G-link. The team is small (two people). The product exists, has live integrations, but is not the company's primary commercial focus today.

### 3.2 Target Audience

**Primary:** TMCs that need both hotel and air supply and want a single vendor for both.

**Secondary:** TMCs with specific Asia or China air ticket needs, particularly where Travelsky/Zhifei integration matters (China-domestic and China-international air requires specific connectivity that global air APIs handle poorly).

### 3.3 What F-link Enables a TMC to Do

| Capability | What the TMC gets |
|---|---|
| **Air ticket supply** | Search, price, book, and ticket air inventory through FCG's air supply network |
| **China air via Travelsky/Zhifei** | Integration with China's primary air ticket distribution system, with consistent inventory between F-link's front-end and Zhifei's own white-label experience |
| **Co-integration with G-link** | One vendor for hotel + air supply — simpler procurement, single contract, single integration partnership |
| **Unified booking management** | Air bookings flow into the same BMS (Tian Gong) layer that handles hotel mid-office events |

### 3.4 Key Features

- **Travelsky / Zhifei integration** — white-labeled, with front-end consistency between FCG's CBT (Corporate Booking Tool) and Zhifei's own interface
- **China-route specialty** — designed to handle China's air ticket distribution quirks that global air APIs handle poorly
- **F-link MCP version** of the API currently exposed (next versioning to be announced)
- **Integration via API, SDK, or Skills** through the Open Platform
- **TC team operational integration** — internal TC operators are directed to use the unified CBT front-end (powered by F-link) rather than Zhifei's own white-label, to consolidate volume and data through F-link

### 3.5 Status — Where F-link Is Today

**Maturity:** Roughly equivalent to a 5/10 score internally. Functional but not yet a mature, polished product.

**Investment level:** Light. The strategic decision is to keep F-link focused while G-link investment continues.

**Strategic posture (per Elaine):** *"Don't lead with F-link. Marketing-light for now. We lack experience in air relative to hotel. We'll grow into it."*

**What this means for sales:** F-link is a capability we can offer when a customer asks, especially when it bundles cleanly with G-link. It is not the headline.

### 3.6 Why F-link Is (Eventually) Special

**China air is hard for global players.** Travelsky is the gatekeeper for Chinese air ticket distribution and is not trivially addressable from outside China. F-link is positioned to offer something global TMC-focused air APIs struggle with.

**Single-vendor simplicity.** For TMCs already integrating G-link, adding F-link is far cheaper than negotiating and integrating a separate air supplier.

**Future-state opportunity:** As F-link matures and as China outbound + Asia air volume grows, F-link becomes a meaningful expansion product on top of G-link's TMC base.

---

## 4. TMC API

### 4.1 What the TMC API Is

The TMC API is FCG's **library of plug-and-play, white-label TMC business modules**, exposed as APIs. Each module corresponds to a discrete operational capability a TMC needs to run its business — expense management, duty of care, and other modular functions — packaged so TMCs can integrate them into their existing systems without building from scratch.

The TMC API is **not** a supply product. It does not include hotels or flights. It is a separate functional domain.

**Mental model:** G-link and F-link give you *what to sell* (inventory). The TMC API gives you *how to run a TMC business* (operations and policy modules) — pre-built, white-labeled, ready to integrate.

### 4.2 Modules in the TMC API

| Module | What it does |
|---|---|
| **Expense Management** | Expense capture, categorization, policy enforcement, expense routing, expense reporting — drop-in alternative to building or licensing standalone expense software |
| **Duty of Care** | Traveler tracking, location-based risk monitoring, emergency response workflows, traveler communication during incidents |
| **Reporting** | Travel spend reporting, booking analytics, supplier performance, policy compliance, savings tracking — pre-built reporting layer that TMCs can embed in their client deliverables without building a BI stack |
| **Approval Workflows** | Multi-level approval chains, policy-driven routing, out-of-policy escalation, manager and finance sign-off flows, audit trail — drop-in approval engine that respects each corporate client's policy structure |

Each module is a discrete plug-and-play API that a TMC can integrate independently. A TMC can take only the duty-of-care module, only the expense module, only reporting, only approval workflows — or any combination.

*The TMC module library is expanding. New modules to be documented as they ship.*

### 4.3 Target Audience

**Primary:** TMCs that need specific operational TMC capabilities but don't want to build them in-house or license them from multiple vendors.

Specifically:
- **Mid-size TMCs** that have core booking handled but lack mature operational modules
- **TMCs expanding service offerings** — e.g., a TMC that wants to add duty of care to their proposition for enterprise clients without building it
- **TMCs running on legacy systems** that need to bolt modern modular capabilities onto an older stack
- **White-label partners and resellers** that want to ship a "complete TMC" without building every component

### 4.4 What the TMC API Enables a TMC to Do

| Capability | What the TMC gets |
|---|---|
| **Skip the build** | Plug in expense management, duty of care, and other modules via API instead of building or buying separately |
| **White-label delivery** | Modules are designed to be embedded into the TMC's own branded experience — the end-corporate sees the TMC's brand, not FCG's |
| **Pick what you need** | Modular — take only the modules that fit your stack, ignore the rest |
| **Stay on your own platform** | The TMC API plugs into the TMC's existing booking system, CRM, and front-end. No platform replacement required. |
| **Single vendor for operations** | If a TMC is already using G-link / F-link for supply, adding TMC API modules consolidates onto one commercial relationship |

### 4.5 Key Features

- **Modular by design** — each module is independently consumable
- **White-label by default** — built to be invisible to the end-corporate
- **Plug-and-play** — designed to integrate into a TMC's existing systems, not replace them
- **Same integration methods as G-link / F-link** — API, SDK, or Skills (AI-native) via the Open Platform
- **Unified billing** — for TMCs already on G-link or F-link, TMC API consumption rolls into a single commercial relationship

### 4.6 Why the TMC API Is Special

**It addresses a real gap in the market.** Most TMCs run on a mix of cobbled-together vendors (one for expense, one for duty of care, one for reporting, etc.) or build everything in-house at significant cost. The TMC API offers a single source for modular, white-label TMC capabilities.

**It compounds the FCG relationship.** A TMC that starts with G-link for supply has a low-friction path to adding TMC API modules. The integration is already familiar, the developer tooling is the same, and the commercial relationship is one.

**It's the operational counterpart to G-link's inventory moat.** G-link is the moat on supply. TMC API is the moat on TMC operations. Together they make FCG a near-complete TMC infrastructure provider.

### 4.7 What the TMC API Does Not Do

- **It is not supply.** No hotels, no flights. Use G-link or F-link for that.
- **It is not a TMC platform replacement.** It's modules that bolt onto the TMC's existing platform.
- **It is not corporate-facing.** Like G-link and F-link, the TMC API is consumed by the TMC, not by the end-corporate traveler.

---

## 5. Open Platform

### 5.1 What the Open Platform Is

The Open Platform is FCG's **unified developer portal and access layer** — the front door through which TMCs and their developers integrate with G-link, F-link, and the TMC API.

Think of it as **the shelf**: a single, public-facing platform that exposes everything FCG offers — products, docs, integration methods, support tools — to any developer who registers.

The Open Platform itself is a product. It is not just a docs site.

### 5.2 What the Open Platform Exposes

Three independent API surfaces, hosted side-by-side on the Open Platform:

| API Surface | Functional domain | Best for |
|---|---|---|
| **G-link API** | Hotel supply — search, availability, book, modify, cancel, mid-office events | TMCs that need hotel inventory |
| **F-link API** | Air supply — search, price, book, ticket | TMCs that need air inventory |
| **TMC API** | Plug-and-play white-label TMC modules — expense management, duty of care, and other modular operational capabilities | TMCs that want to drop in pre-built TMC business functions instead of building them from scratch |

**Critical framing:** These are **three different functional domains**, not three tiers of the same product. A TMC chooses by need:

- Need hotel inventory? → **G-link API**
- Need air inventory? → **F-link API**
- Need an expense management module without building it? → **TMC API** (expense module)
- Need duty of care without building it? → **TMC API** (duty of care module)
- Need travel-spend reporting without building a BI stack? → **TMC API** (reporting module)
- Need multi-level approval workflows that respect each client's policy? → **TMC API** (approval workflows module)
- Need all of the above? → All three APIs, mix-and-matched.

The TMC API is not a "different view of supply." It does not include hotels or flights. It is a separate **white-label modules library** for the operational and policy layers of a TMC's business — packaged so TMCs can plug them into their existing systems via API calls.

### 5.3 Three Integration Methods

The Open Platform offers three ways for a developer to integrate with any of the three API surfaces:

| Method | What it is | When to choose |
|---|---|---|
| **Skills (AI-native)** | Developer pastes a Skills command into their local AI tool (e.g., Codex). They then talk to the AI in natural language ("I want to integrate destination search → hotel listing → filter by X"). AI fetches FCG's API docs and generates working integration code. | New developers, fastest path, modern AI-first dev workflows. **Recommended default.** |
| **API** | Traditional REST API integration against versioned docs (V2 live, V3 in design to international standards) | Developers who want full control, custom logic, or are working in environments without AI tooling |
| **SDK** | Pre-built SDK packages | Developers who prefer a managed integration surface with less boilerplate |

Same back-end. Same content. Three doors.

### 5.4 Target Audience

**Primary:** Any developer or engineering team at a TMC, partner, or aligned company who is integrating FCG.

**Specifically built to serve:**
- **External TMC dev teams** — register, self-serve, integrate without needing to talk to FCG humans
- **Partner companies building white-label products** on FCG's stack
- **AI agent / AI booking tool developers** — Skills integration is purpose-built for AI-driven coding workflows
- **Less technical integrators** — Skills lowers the bar dramatically; even developers without deep hotel/messaging integration experience can self-serve

### 5.5 What the Open Platform Enables

| Capability | What developers and TMCs get |
|---|---|
| **Self-serve registration and integration** | A new developer can register, read docs, and integrate without going through FCG sales or support. Goal: zero-human-touch integration path. |
| **Natural-language integration via Skills** | Skills integration lets developers describe what they want in plain language; AI generates the code. Massive lowering of the integration bar. |
| **AI-assisted error resolution** | Built-in AI system inside the Open Platform reads the developer's error context (e.g., a 404, missing parameter, bad token timestamp) and suggests fixes — without needing a human at FCG. |
| **Online ticket system (when AI can't resolve)** | For issues requiring a human, registered developers can file tickets in-platform. Tickets are scoped to the developer's account for privacy. |
| **Multi-product, multi-method choice** | Developer picks which API surface (G-link / F-link / TMC) and which integration method (API / SDK / Skills) fits their use case. |
| **Hotel static-data service** | Hotel basic info, geo-codes, content — useful for mapping, baselining, and offline data work. (Migrating onto the Open Platform.) |
| **Knowledge base that updates as products evolve** | When TMC ships a new feature, the corresponding API surface (and matching SDK / Skills) is updated in the Open Platform. Developers always have the current spec. |

### 5.6 Why the Open Platform Is Special

**It treats integration as a product, not a deliverable.** Most B2B platforms treat integration as a service done by their internal team to the customer's team. FCG treats it as a self-serve product the developer consumes. This radically scales how many integrations FCG can support.

**AI-native by design.** Skills integration is purpose-built for the era of AI-driven coding. As AI agents become the default way developers ship code, FCG's Open Platform is structurally positioned to be one of the easiest travel APIs to integrate against.

**Removes the "I need to talk to your sales team to get an API key" pattern.** Developers register, integrate, ship. Sales gets involved when it should be — at commercial discussion, not at integration unblock.

**Reduces the dependency on FCG engineering time.** Internal engineering can focus on the supply network and the product, not on hand-holding every new integration. Reduces support load, increases customer ship velocity.

**Reference competitor benchmark:** **Nuitee's developer console / Light API** offers a similar self-serve developer platform model. FCG's Open Platform is being designed with awareness of Nuitee's approach, while differentiating on supply depth (the underlying value).

### 5.7 Status and Roadmap

**Live capabilities:**
- Developer registration and login
- G-link API documentation (V1 / V2)
- F-link API documentation (current MCP version)
- Skills integration for G-link
- AI-assisted error resolution
- Ticket system for human escalation

**In progress (timeline as discussed):**
- **TMC API documentation** — full surface to ship next Wednesday (Skills-integration ready)
- **G-link / D-Hub API refactor** — to align with international standards (V3)
- **UI re-skin** — to match the new FCG website design system
- **Hotel static-data service migration** onto the Open Platform
- **Knowledge base auto-update pipeline** — as products iterate, doc/SDK/Skills update automatically

**Strategic posture:** The Open Platform is being treated as a real product with continuous investment. Skills is the recommended default integration path going forward.

---

## 6. How the Products Work Together

A useful mental model:

```
                ┌───────────────────────────────────────────────────────┐
                │                    OPEN PLATFORM                      │
                │         (developer portal hosting all APIs)           │
                │                                                       │
                │       API  ──────  SDK  ──────  Skills (AI)           │
                │                                                       │
                └──────┬─────────────────┬─────────────────┬────────────┘
                       │                 │                 │
                ┌──────▼─────┐    ┌──────▼─────┐    ┌──────▼─────┐
                │  G-LINK    │    │  F-LINK    │    │  TMC API   │
                │   API      │    │   API      │    │            │
                │            │    │            │    │ White-label│
                │  Hotel     │    │  Air       │    │ plug-and-  │
                │  supply    │    │  supply    │    │ play TMC   │
                │            │    │            │    │ modules    │
                │            │    │            │    │            │
                │            │    │            │    │ • Expense  │
                │            │    │            │    │ • Duty of  │
                │            │    │            │    │   care     │
                │            │    │            │    │ • Reporting│
                │            │    │            │    │ • Approval │
                │            │    │            │    │   workflows│
                └──────┬─────┘    └──────┬─────┘    └────────────┘
                       │                 │
                       └────────┬────────┘
                                │
                     ┌──────────▼──────────┐
                     │   SUPPLY NETWORK    │
                     │   (the real moat)   │
                     │                     │
                     │   GDS + Direct +    │
                     │   Bedbank + Asia    │
                     └─────────────────────┘
```

**Key insight:** G-link and F-link are **supply** products — they connect to the supply network moat. The TMC API is a **separate functional domain** — operational TMC modules that have nothing to do with supply. A TMC mixes and matches based on what they need.

### Picking the right product(s) per buyer scenario:

| Buyer scenario | Recommend |
|---|---|
| TMC needs hotel supply only | **G-link API** |
| TMC needs air supply only | **F-link API** |
| TMC needs hotel + air supply | **G-link + F-link APIs** |
| TMC has supply sorted, needs expense management without building it | **TMC API** (expense module) |
| TMC wants duty of care but doesn't want to build or license a standalone product | **TMC API** (duty of care module) |
| TMC needs travel-spend reporting and analytics for client deliverables without building a BI stack | **TMC API** (reporting module) |
| TMC needs multi-level approval flows that respect each corporate client's policy structure | **TMC API** (approval workflows module) |
| TMC is modernizing — wants supply + plug-and-play operational modules in one stack | **G-link + F-link + TMC API** |
| Asia-focused TMC adding Asia/China hotel coverage to existing supply | **G-link API**, Skills integration for fast time-to-live |
| Developer building any of the above with AI-assisted coding | Same product choice, **Skills integration method** |
| TMC has no platform at all and needs a full booking interface | Full **OBT suite** (CBT + ABT + AI Booking Tool), which itself consumes G-link / F-link / TMC API under the hood |

---

## 7. Pitch Lines — Quick Reference

### G-link
> *"G-link is our hotel supply API. What we're really selling is the supply network behind it — four buckets of supply (GDS, direct hotel, bedbank, Asia-direct), corporate-rate access through GDS and direct channels, the deepest Asia and China coverage in the category, four major Chinese hotel chains deployed directly on G-link, and 4M+ mapped properties. One integration replaces 180-day-each integrations to dozens of sources."*

### F-link
> *"F-link is our air supply API. It's earlier stage than G-link — we're investing carefully — but for customers already on G-link who need air, especially in China-routing scenarios where Travelsky integration matters, F-link is the simplest path to single-vendor coverage."*

### TMC API
> *"The TMC API is our plug-and-play library of white-label TMC modules — expense management, duty of care, reporting, approval workflows, and more. Pre-built, ready to integrate, white-labeled by default. TMCs that don't want to build operational modules from scratch or stitch together multiple vendors can just plug ours in. If you're already on G-link or F-link, adding TMC modules consolidates everything onto one stack and one commercial relationship."*

### Open Platform
> *"The Open Platform is the developer platform that hosts all three of our APIs — G-link, F-link, and TMC API. Skills lets a developer describe what they want in natural language and AI writes the code. API and SDK are still supported. AI-assisted error resolution means most issues don't need a human. We treat integration as a product, not a service — your team ships faster, and ours stays focused on supply and modules."*

---

## 8. Common Misunderstandings to Correct

| Misunderstanding | Correction |
|---|---|
| "G-link is the API" | The API is the door. G-link is the supply network behind the door. |
| "Open Platform = docs site" | Open Platform = the developer platform that hosts G-link, F-link, and TMC API. It includes docs + integration tooling + AI assistance + ticket system + self-serve onboarding. It's a product, not a docs site. |
| "TMC API is a different way to access supply" | **No.** TMC API has nothing to do with supply. It's a separate functional domain — plug-and-play white-label modules for TMC business operations (expense, duty of care, etc.). G-link / F-link are for supply; TMC API is for operations. |
| "If a TMC needs everything, give them TMC API" | TMC API alone has no inventory. A TMC that needs hotels and ops takes **G-link + TMC API**. The products are independent and combinable. |
| "F-link is a major product" | F-link is early-stage and under-invested. Sell it when it bundles. Don't lead with it. |
| "Skills is just a marketing version of the API" | No — Skills is a fundamentally different integration method. The developer talks to an AI; AI generates code from our docs. It's not the same API with a wrapper. |
| "Three APIs = three different products to sell separately" | They are three independent products, but most customers consume them in combination. Pricing reflects what they actually consume. |

---

## 9. Companion Docs

- [FCG-positioning-reference.md](FCG-positioning-reference.md) — overall ICP, USP, competitive positioning
- [FCG-supply-network.md](FCG-supply-network.md) — deep-dive on the supply moat behind the APIs

*Source: Internal walkthrough by Elaine Wan, May 2026, including Tian Ye's Open Platform walkthrough.*
