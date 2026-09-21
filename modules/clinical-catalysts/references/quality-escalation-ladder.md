# Quality Escalation Ladder — enforcement mechanics as investment signal

The state machine behind the quality-signals skill. Seed patterns compiled Aug 2026 from secondary reviews of FDA enforcement records — verify against primary sources (FDA inspection classification database, warning-letter index, import-alert lists, MAUDE/FAERS, recall database) at use. Enforcement data ages fast: state the retrieval date; treat anything older than a week as stale for live positions.

## The facility ladder (monitor the transitions, not the levels)

**NAI** (no action) → **VAI** (voluntary action) → **OAI (official action indicated — the pivot to monitor)** → application **withhold** / **import alert** (66-40 drugs / device analogs: detention-without-exam; exit requires re-inspection) → **warning letter** (15-working-day response clock) → consent decree/seizure at the extreme.

- **PAI/PLI triggers** (risk-based, Compliance Program 7346.832): new facility or process, adverse compliance history, for-cause; ~60-day notice; records requests (704(a)(4)) and remote assessments can substitute. Track site novelty + surveillance history as PAI-probability proxies.
- **Approval linkage:** withhold criteria include data-integrity findings, failed PPQ, and "not ready for inspection"; an OAI at an application-listed site is a CRL channel independent of clinical merit (see crl-risk-rubric.md). OAI→VAI reclassification cycles have consumed years (INFUGEM pattern); missed inspections alone caused CRLs in the COVID era.
- **Worked escalation example (pattern to reuse):** Intas — aborted/deleted chromatograms found → OAI (12/2022) → import alert (6/2023) → warning letter (11/2023): the ladder ran in under a year, with supply consequences for the US generics market.

## What inspectors actually cite (governance beats technique)

Drug-side recurring 483 families: **211.22** (quality-unit authority), **211.192** (OOS/deviation investigations), 211.100 (procedures), 211.67 (cleaning); aseptic fill-finish adds environmental monitoring (211.42(c)(10)) and contamination-control failures — a failed media fill presages supply disruption. Device-side: **820.100 (CAPA)** and **820.198 (complaints)** dominate; design-control citations (protocols written after testing, non-production-unit validation) mark QS immaturity — which predicts inspection outcomes better than device sophistication. FDA's annual inspectional-observation summaries are the quantitative source.

**Data-integrity fingerprints** (severest class; often terminal for pending applications): disabled/absent audit trails, shared logins, deleted or aborted chromatograms (Sun Pharma's 5,301 as the canonical count), testing-into-compliance, clock-tampering. Data-integrity warning-letter velocity is a portfolio-level CMC-quality proxy.

## Product-safety lane (FAERS / MAUDE / recalls)

- **FAERS/MAUDE are signal, never incidence** — reporting biases, stimulated reporting around news, and no denominators. Use for cluster detection and trajectory, not rates; say so in every brief.
- **MAUDE mechanics:** no use-error code exists — narrative review required; sampled autoinjector reads run ~2:1 use-error:device-defect, and unreturned samples bias findings toward "user error." Complaint-handling/MDR citations in warning letters often follow.
- **Boxed-warning mechanics:** no single evidentiary bar — RCT meta-analysis, FAERS clusters, or animal carcinogenicity have each sufficed — and warnings exhibit **class contagion** (one product's warning reprices the class). Post-approval safety-trial readouts vs comparators are the scheduled channel.
- **Recall mechanics:** Class I (reasonable probability of serious harm) vs II/III; software/connectivity has displaced hardware as the failure locus in connected devices (insulin-pump Class I counts accelerating ~4→8→21 per multi-year period as of Aug 2026); **shared-supplier contagion** — one component maker's failure recalls multiple brands. Silent-failure modes (undetected non-delivery) escalate to Class I reliably.
- **REMS/ETASU changes** are demand-side friction events (certification, registries) — route TAM/funnel effects to cms-reimbursement and healthcare-equity.

## Scope note

This is **enforcement research** — not a QMS, not supplier-risk graphing, not inspection-readiness consulting. Minimum sources per brief: 483/WL status, recall record, multi-authority check where revenue is ex-US, and freshness stated.
