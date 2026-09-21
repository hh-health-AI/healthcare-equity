---
name: quality-signals
description: >
  This skill should be used when the user asks about "warning letters or 483s for
  [company]", "facility/inspection risk", "manufacturing risk on [TICKER]", "import
  alert exposure", "FAERS/MAUDE signals", "recall risk", "is there a safety signal on
  [product]", or wants manufacturing-quality and post-market-safety evidence behind a
  thesis or a pending approval.
metadata:
  version: "0.1.0"
---

# Quality Signals

Manufacturing-quality and post-market-safety evidence engine: translate enforcement and safety records into approval-risk, launch-delay, supply-disruption, and label-risk briefs. Mechanics reference: `${CLAUDE_PLUGIN_ROOT}/references/quality-escalation-ladder.md`. Scope: **enforcement research** — not a QMS, supplier-risk graph, or inspection-readiness program.

## Lane 1 — Facility / enforcement

1. Build the facility map from filings and application disclosures: named manufacturing sites (own + CDMO), what each makes, and which pending applications list them. Concentration = single points of failure.
2. Pull each site's enforcement state via web research (FDA inspection classification database, warning-letter index, import-alert lists, EU EudraGMDP non-compliance reports) — or via the Rhizome connector when installed (prefer it for document depth; carry its citation URLs). Record: latest classification (NAI/VAI/**OAI**), open 483 themes, warning-letter status and response state, import alerts, PAI history.
3. Read the ladder, not the level: transitions are the signal (VAI→OAI; OAI→import alert; the Intas one-year pattern). Classify citation themes — governance (quality unit, OOS investigations, CAPA, complaints) vs technical — and flag **data-integrity fingerprints** as the severest class.
4. Translate per the CMC evidence row and `crl-risk-rubric.md`: enforcement moves **launch probability, timing, capacity, capital** — and for pending applications, an OAI/unresolved-WL at a listed site is a named CRL channel. For revenue products: supply-disruption and shortage-share scenarios (who gains if this site stops shipping — cross-read to competitors).

## Lane 2 — Product safety (FAERS / MAUDE / recalls)

1. For the product set, sweep FAERS (drugs) or MAUDE (devices) for adverse-event clusters and trajectory, plus the recall database and any REMS changes. **Signal, never incidence** — reporting biases and no denominators; say so in every brief.
2. Devices: narrative-review MAUDE (no use-error code exists); separate use-error vs device-defect patterns (~2:1 in sampled autoinjector reads — see combination-products.md); watch complaint-handling/MDR citations as the enforcement echo. Recalls: class, root cause (software/connectivity now the dominant locus in connected devices), and **shared-supplier contagion** across brands.
3. Drugs: case-count the specific patterns that move regulators — Hy's Law counts (see crl-risk-rubric.md), event clusters that historically produced boxed warnings — and treat any class member's safety event as a **class repricing event** (route to healthcare-equity thesis).

## Output & wiring

End each lane's finding with the EVIDENCE BRIEF block (layer: regulatory or commercial as applicable) — enforcement data freshness stated (stale >1 week for live positions) — and save to the evidence ledger. Wire standing coverage: add OAI/import-alert/warning-letter/recall keywords for held names to the readout-watcher and rule-watcher sweeps, and encode thresholds into healthcare-equity SELL-02 watchlists ("warning letter at [site] → re-underwrite" as a pre-committed action). Escalate to the adcom-label pre-decision checklist when a scored facility serves a pending application.
