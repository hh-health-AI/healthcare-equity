# Endpoint & Approval Precedents — indication-keyed seed map

Seed anchors for readout-handicap and the precedent-pack skill, compiled Aug 2026 from secondary reviews of FDA/EMA decisions — verify against primary records (Drugs@FDA review packages, labels, guidance) at use. Governing rule: **guidance is descriptive; decisions are precedential** — never handicap a filing off guidance alone without checking what regulators actually accepted.

## Cross-indication patterns

- **Response-based oncology approvals — the durability floor:** confirmed ORR (RECIST 1.1, blinded independent central review) with duration-of-response is the single-arm standard; the empirical DoR floor is **~6 months** — one clear sub-6-month approval in five years (adagrasib CRC, DoR 5.8 mo) vs a norm of ~8.3–14.1 months or not-reached. DCR-as-primary is a red flag; OS-as-phase-2-primary is over-scoped.
- **MRD (minimal residual disease):** accepted as a *primary* endpoint only in ALL; multiple-myeloma draft guidance (Jan 2026) proposes MRD-negativity (sensitivity ≥10⁻⁵) for accelerated approval; the teclistamab rejection on assay calibration shows **assay-vendor validation is trial risk**.
- **Subgroup rescue:** see crl-risk-rubric.md — failed overall trial + post-hoc subgroup ≈ CRL; prospective confirmatory trial is the historical remedy.
- **PROs:** Section-14 (efficacy) placement is achievable where the disease is symptom-defined (pruritus, migraine, pain — validated single-item scales like WI-NRS); elsewhere PROs land supportive-only. Pre-specification, multiplicity control, and anchor-based meaningfulness are the gates; a Section-14 PRO claim is a payer/HTA asset (route to cms-reimbursement / international).
- **RWE:** appears in reviews more than labels; reaches labeling with a credible external comparator and transparent limitations (registry-based orphan settings most amenable); overlapping case series get rejected.
- **Safety-label mechanics:** boxed warnings have no single evidence bar (RCT meta-analysis, FAERS cluster, or animal data have each sufficed) and show class contagion — a safety readout on one name is a class event (thesis implication).

## Indication templates (worked patterns)

- **IBD (UC/CD):** co-primary symptomatic + centrally-read endoscopic endpoints (UC: mMS-based remission; CD: CDAI plus SES-CD), corticosteroid-free remission expected, 52-week maintenance adds ~18–24 months; symptom-only packages draw deficiencies.
- **HNSCC phase 2:** confirmed ORR by BICR with DoR as single-arm primary → accelerated approval with confirmatory randomized expectation (KEYNOTE/CheckMate lineage).
- **Huntington's:** chorea endpoints settled (UHDRS TMC + global impression anchors; three approvals on the same design = low design risk); disease-modification has **no consensus endpoint** (TFC vs TMS vs cUHDRS) = elevated design risk premium.
- **oHCM (worked competitive-label pair):** mavacamten (boxed warning, REMS, CYP2C19/3A4 contraindications) vs aficamten (single major DDI contraindication, lighter program) — an example of label breadth/friction as the competitive variable, not efficacy.
- **Obesity/GLP-1 PRO layer:** SF-36v2 PF and IWQOL-Lite-CT function as de facto confirmatory standards; non-pre-specified PROs earn no claims.
- **Novel-modality template (psychedelics et al.):** the Lykos CRL rubric — functional unblinding measured, expectancy controlled, durability follow-up long enough, drug isolated from adjunct therapy — reusable for any subjectively-active agent.
- **Cell & gene therapy:** single-arm dominates (efficacy n≈12–156); CAR-T ORR precedents 72–98%; hemophilia uses within-subject ABR; accelerated approval is common and confirmatory misses happen (Elevidys/EMBARK) — price the confirmatory event separately; 15-year registry PMRs (≥1,500 patients, reports to ~2042) and post-approval class boxed warnings are the tail liabilities (route to healthcare-equity rNPV work).

## How precedent-pack consumes this

These are the *starting* analogs, not the pack. For any live event, assemble the named comparable set per the precedent-pack method (wide-then-narrow, negatives hunted, citations opened), then adjust `base-rates.md` priors with named precedents. When the Rhizome connector is installed, use it to pull the review packages and CRLs this map points at; otherwise Drugs@FDA/EMA + web.
