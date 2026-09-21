# Changelog — HH-provider-adoption

**HH-provider-adoption** is the standalone distribution of the `provider-adoption` plugin. Versions track the canonical copy in the `claude-healthcare-analyst-suite` monorepo (`github.com/<your-github-username>/claude-healthcare-analyst-suite`); this file carries the plugin-relevant slice of the suite changelog.

## [0.1.3] — 2026-08-26

- Workflow chart embedded in `CLAUDE.md` as a runtime **Workflow map**: routing guidance (enter at the node matching the question, offer the downstream node when a skill completes; pink edges = evidence-brief handoffs, dashed amber = scheduled agents), plus show-on-request behavior for "how does this plugin work".

## [0.1.2] — 2026-08-26

- README gains a **Workflow** section with a Mermaid flowchart: the capacity pipeline — provider-footprint → site-adoption-tracker (matched-cohort snapshots) → kol-site-map → channel-check-prep — with the footprint-refresh agent in dashed amber, the snapshots store, the presence ≠ volume caveat gate, and briefs flowing to `healthcare-equity`. Render-verified with mermaid-cli.

## [0.1.1] — 2026-08-25

- Canonical snapshot-store paths (`~/.claude/data/provider-adoption/snapshots/`) wired into site-adoption-tracker and the footprint-refresh agent — deltas diff against the stored snapshot, never against memory.
- Suite-wide evidence discipline: evidence-brief contract adds the `Coverage` line; pinpoint-citation rule ("an uncited regulatory or clinical claim is a draft, not evidence"); five-point precedent discipline checklist; evidence ledger under `~/.claude/data/provider-adoption/briefs/`; README smoke test (pass = the output moves a model variable with an openable citation).

## [0.1.0] — 2026-08-25

Initial release.

- NPI Registry hosted connector (US National Provider Identifier registry — providers, taxonomies, locations, organizations).
- 4 skills: provider-footprint, site-adoption-tracker, kol-site-map, channel-check-prep.
- footprint-refresh agent (quarterly matched-cohort refresh of tracked footprints).
- References: NPI data notes (registration-file-not-claims-file caveats), adoption S-curve vignettes, usability-adoption checklist, adoption metrics (funnel-stage evidence translation).
