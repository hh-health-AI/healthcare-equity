# Changelog — HH-health-AI

**HH-health-AI** is the standalone distribution of the `cms-reimbursement` plugin. Versions track the canonical copy in the `claude-healthcare-analyst-suite` monorepo (`github.com/<your-github-username>/claude-healthcare-analyst-suite`); this file carries the plugin-relevant slice of the suite changelog.

## [0.1.3] — 2026-08-26

- Workflow chart embedded in `CLAUDE.md` as a runtime **Workflow map**: routing guidance (enter at the node matching the question, offer the downstream node when a skill completes; pink edges = evidence-brief handoffs, dashed amber = scheduled agents), plus show-on-request behavior for "how does this plugin work".

## [0.1.2] — 2026-08-26

- README gains a **Workflow** section with a Mermaid flowchart (skills in blue, data sources in green, the rule-watcher agent in dashed amber, evidence outputs in pink, suite handoffs in violet, the coverage ≠ coding ≠ payment triad gate in grey). Render-verified with mermaid-cli.

## [0.1.1] — 2026-08-25

- coverage-check gains the **REMS/ETASU access-friction check** (restricted distribution as a TAM/conversion haircut alongside coverage status).
- Suite-wide evidence discipline: evidence-brief contract adds the `Coverage` line; pinpoint-citation rule ("an uncited regulatory or clinical claim is a draft, not evidence"); five-point precedent discipline checklist; evidence ledger under `~/.claude/data/cms-reimbursement/briefs/` and `.../snapshots/`; README smoke test (pass = the output moves a model variable with an openable citation).

## [0.1.0] — 2026-08-25

Initial release.

- CMS Coverage hosted connector (Medicare Coverage Database — NCDs, LCDs, coverage articles).
- 5 skills: coverage-check, reimbursement-impact, ma-bid-cycle, drug-pricing-ira, rule-cycle-calendar.
- rule-watcher agent (scheduled sweep of CMS release windows).
- References: payor glossary, payor-economics primer, payor metrics (evidence-translation rows).
