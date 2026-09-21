---
name: exposure-map
description: >
  This skill should be used when the user asks "what codes does [TICKER] bill against",
  "map [company]'s procedure/diagnosis exposure", "which indications drive [franchise]
  revenue", "code-level exposure for [device/drug/test]", or needs the revenue-by-code
  scaffold behind a healthcare name.
metadata:
  version: "0.1.0"
---

# Exposure Map

Map a company or franchise to the diagnosis and procedure code landscape it monetizes — the code-level scaffold under the revenue model.

## Workflow

1. Decompose the company into revenue units from filings/IR: products → clinical uses → sites of service. For each unit, identify the code stack: ICD-10-CM diagnoses that establish medical necessity (via the ICD10 Codes connector — enumerate the code families, not just headline codes), the CPT/HCPCS procedure or product codes billed (via web research: AMA/CMS references, company reimbursement guides — device makers publish coding guides; cite them), and the inpatient DRG mapping where relevant. Use `${CLAUDE_PLUGIN_ROOT}/references/coding-systems-primer.md` to keep the systems straight.
2. Build the exposure table: revenue unit · dx code families · procedure/product codes · site(s) of service · payer mix skew · revenue share (company-disclosed or estimated, labeled). Flag units where coding is immature (unlisted/miscellaneous codes, C-codes, cash-pay) — immature coding is both a risk and, when new codes arrive, a catalyst (hand to code-shift-monitor).
3. Read the concentration: which one or two code families carry the thesis; what share of revenue rides on codes whose coverage (cms-reimbursement) or payment is in motion.
4. Then quantify what flows through the codes — hand the code list to procedure-volume-tracker for volumes and to epi-funnel-input for the disease-burden ceiling. Exposure mapping states *where* revenue comes from; it does not itself prove *how much*.
5. End with the EVIDENCE BRIEF block (layer: commercial-volume/exposure). Feed the scaffold to healthcare-equity model-valuation (revenue build by code) and thesis work (concentration risk).
