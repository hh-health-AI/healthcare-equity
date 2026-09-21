# Changelog — HH-procedure-exposure

**HH-procedure-exposure** is the standalone distribution of the `procedure-exposure` plugin. Versions track the canonical copy in the `claude-healthcare-analyst-suite` monorepo (`github.com/<your-github-username>/claude-healthcare-analyst-suite`); this file carries the plugin-relevant slice of the suite changelog.

## [0.1.3] — 2026-08-26

- Workflow chart embedded in `CLAUDE.md` as a runtime **Workflow map**: routing guidance (enter at the node matching the question, offer the downstream node when a skill completes; pink edges = evidence-brief handoffs, dashed amber = scheduled agents), plus show-on-request behavior for "how does this plugin work".

## [0.1.2] — 2026-08-26

- README gains a **Workflow** section with a Mermaid flowchart: exposure-map fanning out to the procedure-volume, epi-funnel, and code-shift lanes, the code-update-watcher agent in dashed amber, the funnel-discipline gate before the evidence brief, and briefs flowing to `healthcare-equity`. Render-verified with mermaid-cli.

## [0.1.1] — 2026-08-25

- Suite-wide evidence discipline: evidence-brief contract adds the `Coverage` line; pinpoint-citation rule ("an uncited regulatory or clinical claim is a draft, not evidence"); five-point precedent discipline checklist; evidence ledger under `~/.claude/data/procedure-exposure/briefs/` and `.../snapshots/`; README smoke test (pass = the output moves a model variable with an openable citation).

## [0.1.0] — 2026-08-25

Initial release.

- ICD10 Codes hosted connector (diagnosis-code landscape and lookups).
- 4 skills: exposure-map, procedure-volume-tracker, epi-funnel-input, code-shift-monitor.
- code-update-watcher agent (annual/quarterly code-update sweep against tracked exposure maps).
- References: coding-systems primer (ICD-10-CM vs CPT/HCPCS vs ICD-10-PCS/DRG, where rates live), funnel discipline (observed usage maps to ONE stage: ordered → completed → paid → persistent → cash).
