---
name: site-adoption-tracker
description: >
  This skill should be used when the user asks to "track sites offering [procedure/
  program]", "is the installed/site base growing", "adoption curve for [device/therapy]",
  "center expansion for [TICKER]", or wants period-over-period evidence of site or
  program adoption.
metadata:
  version: "0.1.0"
---

# Site Adoption Tracker

Produce period-over-period evidence of site/program adoption: where the delivery footprint is expanding, at what pace, and against which S-curve stage.

## Workflow

1. Define the tracked unit precisely — organizational NPIs matching a program signature (taxonomy + organization-name terms), certified centers (from company or society lists via web research), or provider cohorts at target institutions — and the cadence (quarterly default).
2. Take the current snapshot via the NPI Registry connector with the recorded query definition. If a prior snapshot exists (canonically in `~/.claude/data/provider-adoption/snapshots/`, else in conversation, project files, or pasted), diff as a **matched cohort**: adds, drops, and net — never raw count subtraction across different query definitions (`${CLAUDE_PLUGIN_ROOT}/CLAUDE.md`).
3. Triangulate each apparent add/drop where material: company account disclosures, center press releases, job postings, conference posters from the site. Single-source deltas are flagged as unconfirmed.
4. Place the trajectory on the adoption curve using `${CLAUDE_PLUGIN_ROOT}/references/adoption-scurve-vignettes.md`: which stage (KOL/evangelist centers → early-majority community spread → guideline/payment-driven mainstream), what historically gates the next stage (evidence, guideline inclusion, reimbursement, usability, training burden — see references/usability-adoption-checklist.md), and whether this product's gates are open (check with cms-reimbursement for the payment gate).
5. Translate: site-base growth moves the **units/adoption** variables (active sites, utilization ramp assumptions) — it is not revenue; per the metrics reference, placements/sites without utilization is the classic overvaluation error. Pair with procedure-exposure volume evidence before concluding demand.
6. End with the EVIDENCE BRIEF block (layer: commercial-adoption; competitive when tracking share-of-sites vs a rival). Save the snapshot (query + results + date) so the footprint-refresh agent can diff next period.
