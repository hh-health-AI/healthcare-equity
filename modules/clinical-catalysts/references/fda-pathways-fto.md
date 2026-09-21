# FDA Pathways & IP/FTO Checklists

Diligence scaffolds distilled from the regulatory/IP literature in the project KB (*FDA and Intellectual Property Strategies for Medical Devices*) — `project_search` it for depth. Investment-diligence screens, not legal advice.

## Device pathways (risk-tiered)

| Pathway | For | Evidence bar | Typical timeline signal | Diligence checks |
|---|---|---|---|---|
| **510(k)** | Class II with a predicate | Substantial equivalence; often bench-only | Fastest; moderate cost | Predicate identity, age, and standards vintage; SE argument strength; "predicate creep" risk (SUB-MED-03) |
| **De Novo** | Novel low/moderate risk, no predicate | Reasonable assurance via special controls; usually clinical data | Slower than 510(k) | Classification logic; whether FDA could escalate expectations; creates the predicate competitors will later ride |
| **PMA** | Class III / life-sustaining | Full clinical evidence of safety & effectiveness (pivotal IDE) | Longest, costliest; panel possible | Trial design vs claims sought; manufacturing inspection readiness; supplement strategy for iterations |
| **HDE / Breakthrough Device** | Rare-condition / breakthrough designations | Modified bars; priority interaction | Signals engagement, not approval | What the designation actually commits FDA to (little) vs what management implies |

Drug/biologic equivalents to keep straight: NDA/BLA, 505(b)(2) (leaning on prior findings), accelerated approval (surrogate endpoints + confirmatory obligation), Fast Track/Breakthrough/Priority Review (process, not standard, changes); ANDA/biosimilar on the copy side.

## Pathway-choice red flags

Management guiding a 510(k) for a claim that sounds like a new intended use; predicates cleared under decades-old standards; a De Novo timeline assumed in the model at 510(k) length; PMA-track economics (trial cost, review time) not in cash-runway math; UKCA/CE/MDR transition exposure for EU revenue.

## FTO / IP screen (SUB-BIO-06 companion)

1. **Estate map** — composition/design patents vs method-of-use vs formulation/manufacturing; geographies; expiry ladder incl. extensions (PTE/SPC).
2. **Regulatory exclusivities** — separate from patents: NCE, orphan, pediatric, biologic 12-year, device-side data protections where applicable; Orange Book / Purple Book listings.
3. **Blocking-IP scan** — third-party patents the product could read on; license needs; litigation history in the class; Para IV notices and IPR petitions as leading indicators.
4. **Durability** — how the estate survives challenge: independent claim breadth, prosecution history, IPR survival rates in the art unit; "patent thicket vs single-patent cliff" shape.
5. **Lifecycle management** — next-gen filings, formulation switches, device+drug combos — credible extension vs evergreening the market will discount.
6. **Verdict** — strong / adequate / fragile, with the single most breakable link named.

## FDA interaction forensics (SUB-BIO-07 companion)

Type A (stalled program), B (milestone: pre-IND, EOP2, pre-NDA/BLA), C (other) meetings — frequency and disclosed outcomes signal friction. Watch for: endpoint disagreements surfacing in filings' risk language, refuse-to-file history, clinical holds, repeat CRLs in the class, inspection 483s at named facilities. The absence of disclosed FDA alignment on endpoints before Phase 3 is itself a risk finding. Q-Sub mechanics: written FDA feedback in ~70 days, non-binding and stale after ~1 year — disciplined Q-Sub usage is a management-quality tell for diligence calls.

## Empirical review-timeline base rates

See the table in `base-rates.md` (510(k) ~128d median, De Novo ~299d, PMA ~252d+, standard BLA ~408d; mean–median gap = tail risk) — use it to date pathway catalysts and widen windows on long-tailed pathways. SE-vs-NSE mechanics: five-step SE sequence; four NSE grounds (new intended use, different questions of safety/effectiveness, inadequate performance data, insufficient information); NSE is final → Class III default — and NSE letters are unpublished, so public base rates *understate* failure risk.

## AI/SaMD & digital-health regulatory layer

- **PCCP (predetermined change control plans):** FDA pre-authorizes an AI update envelope (final guidance 2025); allowed = retraining, compatibility expansion; prohibited = new indications/claims/architecture. ~21 authorizations as of Aug 2026 — **PCCP possession is a measurable iteration-velocity moat** for AI-device names (update without resubmission); its absence means every model improvement is a regulatory event.
- **CDS four-criteria test** (final guidance, 520(o)(1)(E)): failing any criterion — especially image/signal processing or non-transparent basis — makes software a regulated device. First movers took De Novos and minted product codes (SAK sepsis, SBQ ECG-AF, QNL) — later entrants inherit 510(k) predicates: map who holds the predicate advantage.
- **Wellness-exemption enforcement line:** "suggestive-of" notification features clear (Apple AFib/hypertension, Samsung sleep apnea, Dexcom Stelo, Fitbit lineage); numeric *estimation* draws enforcement (WHOOP BP warning-letter pattern). Score consumer-health feature launches against this line before crediting them as regulated-device milestones.
- **Category-creation signals:** a new product code (often minted by a De Novo) is a leading indicator of a new addressable category, and one De Novo seeds a whole 510(k) field (Bose → OTC hearing aids; contactless-vitals entrants converging on a single predicate). Federal Register reclassification orders reprice whole classes in one dated event (up-classing strands predicates; down-classing expands markets).
- **Predicate-quality screen (SUB-MED-03 companion):** predicate age, standards vintage, recall history, split-predicate prohibition, disqualification events — a scoreable NSE/delay factor. Competitive-entry cadence template: track a modality's pathway × product-code landscape over time (the pulsed-field-ablation pattern: six PMAs in ~25 months = a share-shift battleground announced in advance).

All figures as of Aug 2026 — verify at use.
