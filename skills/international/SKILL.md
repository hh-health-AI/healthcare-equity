---
name: international
description: >
  This skill should be used when the user says "map the EU HTA pathway", "NICE/AMNOG
  read for [asset]", "Japan price revision exposure", "China biotech licensing",
  "BIOSECURE exposure", "UK/VPAG dynamics", or any ex-US regulatory, HTA, or
  reimbursement question for a global healthcare mandate.
metadata:
  version: "0.1.0"
---

# International Coverage

The ex-US dynamics a global mandate requires: European HTA, Japanese price revisions, Chinese licensing/BIOSECURE, and UK-specific considerations. Prompts in `${CLAUDE_PLUGIN_ROOT}/skills/international/references/prompts.md`.

## Route by geography

| Question | Prompt |
|---|---|
| European launch potential — JCA, NICE, G-BA/AMNOG, HAS | INTL-01 |
| Japan revenue trajectory — biennial revisions, market-expansion redetermination | INTL-02 |
| China — licensing economics, NMPA data acceptance, BIOSECURE, NRDL | INTL-03 |
| UK — MHRA/IRP, NICE/SMC, VPAG rebates, NHS dynamics, listing effects | INTL-04 |

## Execution rules

1. Primary sources by geography via web research: EMA EPARs and JCA materials, national HTA bodies (NICE, G-BA/IQWiG, HAS, AIFA), PMDA/NHI price lists and Chuikyo materials, NMPA/NRDL announcements, MHRA and NHS England publications. Time-stamp and version every HTA decision and price-list reference; these regimes move on fixed cycles.
2. The analytical spine of all four prompts is the same: **regulatory access ≠ reimbursed access ≠ realized price** — the ex-US mirror of the US coverage/coding/payment triad. Model country-level price × volume × time-to-reimbursement explicitly, and let HTA outcomes cluster (one restrictive major-market outcome propagates).
3. Key regime facts embedded in the prompts (verify current status when invoked): EU JCA scope phase-in (oncology/ATMPs from 2025 → orphans 2028 → all new medicines 2030); AMNOG additional-benefit categories driving German price; NICE thresholds (£20–30k/QALY base, higher end-of-life/HST) and international reference effects; Japan's biennial April revisions, market-expansion redetermination, and G1/G2 long-list decay; China NRDL's typical 50–70% discount for volume; BIOSECURE's procurement-restriction mechanism; UK VPAG's ~2% growth cap with rebates.
4. Route the outputs: launch-timing and label differences → clinical-catalysts catalysts; revenue bridges and Europe/Japan share-of-total deltas → model-valuation; UK/EU ESG-linked procurement (net-zero NHS, CSRD) → esg-stewardship.
5. End with the EVIDENCE BRIEF block (layer: regulatory or commercial as applicable) and the confidence score.

## Added regime specifics (v0.2 — as of Aug 2026, verify at use)

- **China conditional approvals (INTL-03):** ~36% of 2021 priority-review applications met conditional-approval criteria; 2026 revisions tighten post-approval obligations — a sponsor filing a **3-month confirmatory-trial extension is the revocation early-warning**. Single-arm ORR or randomized PFS accepted with the confirmatory OS trial agreed/underway.
- **CHMP qualification opinions (INTL-01):** SAWP qualification of novel methodologies/biomarkers has three outcome tiers — binding Qualification Opinion (for a stated context of use) > Qualification Advice > Letter of Support. A binding opinion de-risks an endpoint strategy for the whole class; "context of use is everything."
- **EU CTR transparency (competitive intelligence):** Article 81 defaults trial data public; commercial-confidentiality deferrals collapse at marketing authorization — CSR-level disclosure at approval is a scheduled competitive-intelligence unlock for multi-indication molecules. Phase-I deferrals are longest; PIP trials cannot defer.
- **EPAR Annex II obligations:** conditional-approval specific obligations (named confirmatory studies with hard deadlines, annual renewals) are dated catalysts — feed them to the clinical-catalysts catalyst-calendar.
