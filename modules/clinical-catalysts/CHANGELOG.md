# Changelog — HH-clinical-catalysts

**HH-clinical-catalysts** is the standalone distribution of the `clinical-catalysts` plugin. Versions track the canonical copy in the `claude-healthcare-analyst-suite` monorepo (`github.com/<your-github-username>/claude-healthcare-analyst-suite`); this file carries the plugin-relevant slice of the suite changelog.

## [0.2.2] — 2026-08-26

- Workflow chart embedded in `CLAUDE.md` as a runtime **Workflow map**: routing guidance (enter at the node matching the question, offer the downstream node when a skill completes; pink edges = evidence-brief handoffs, dashed amber = scheduled agents), plus show-on-request behavior for "how does this plugin work".

## [0.2.1] — 2026-08-26

- README gains a **Workflow** section with a Mermaid flowchart: four entry skills (catalyst-calendar, pipeline-landscape, literature-kol, device-diligence) feeding the two decision skills (readout-handicap, adcom-label), with precedent-pack and quality-signals sharpening the odds, the readout-watcher agent in dashed amber, and all briefs flowing to the ledger and to `healthcare-equity`. Render-verified with mermaid-cli.

## [0.2.0] — 2026-08-25

Regulatory-depth release, informed by a full review of primary FDA/EMA mechanics literature. Seed figures in new references are tagged "as of Aug 2026 — verify at use."

- New skills: **precedent-pack** (named historical analogs via the six-principle method; "guidance is descriptive, decisions are precedential") and **quality-signals** (two lanes: facility/enforcement ladder NAI→VAI→OAI→import alert→warning letter, and product safety via FAERS/MAUDE/recalls with signal-not-incidence caveats).
- New references: `crl-risk-rubric.md` (eight-category deficiency taxonomy, facility base rate, named red flags), `quality-escalation-ladder.md`, `endpoint-precedents.md` (DoR floor, MRD map, indication templates), `combination-products.md` (device-change evidence ladder, autoinjector deficiency base rates).
- `base-rates.md` expanded: empirical review-timeline medians by pathway, designation reality-check (BTD de-hype), accelerated-approval mechanics with ODAC lead indicator, meeting clocks, NMPA conditional-approval rates.
- `fda-pathways-fto.md` gains the AI/SaMD layer (PCCP-as-moat, CDS four-criteria codes, wellness enforcement line), Q-Sub mechanics, category-creation signals.
- adcom-label gains the pre-decision approval-odds checklist and the label-delta monitoring workflow; pipeline-landscape gains the negative-space sweep; catalyst-calendar adds EPAR Annex II obligations and PAS-clocked supplements; readout-watcher sweeps label supplements and enforcement hits.
- Suite-wide evidence discipline: evidence-brief contract adds the `Coverage` line; pinpoint-citation rule ("an uncited regulatory or clinical claim is a draft, not evidence"); five-point precedent discipline checklist; evidence ledger under `~/.claude/data/clinical-catalysts/briefs/` and `.../snapshots/`; README smoke test; optional Rhizome AI connector routed as the FDA/EMA primary-document depth layer with web fallback.

## [0.1.0] — 2026-08-25

Initial release.

- Clinical Trials + PubMed hosted connectors.
- 6 skills: catalyst-calendar, readout-handicap, adcom-label, pipeline-landscape, literature-kol, device-diligence.
- readout-watcher agent (scheduled CT.gov delta scan on the watchlist).
- References: base-rates, device-development checkpoints, FDA pathways/FTO, clinical evidence-translation.
