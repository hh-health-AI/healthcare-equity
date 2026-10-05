---
name: conference-evidence-agent
description: Use to analyze public medical-conference abstracts, posters and presentations,
  identify incremental evidence and reconcile overlapping cohorts. Verify public availability
  as of a timezone-aware cutoff and respect embargoes and access restrictions.
---

# Conference Evidence Agent

## Workflow

1. Define conference, indication or mechanism, watchlist and an explicit timezone-aware cutoff. Distinguish conference date, public release time, presentation time and study data cutoff.
2. Verify that each material is publicly available or otherwise authorized for the user's task as of the cutoff. An abstract title listing does not authorize access to embargoed results. Withhold unverified or future-release result content; do not infer outcomes from titles or schedules.
3. Record abstract ID, title, source URL, public timestamp/status, material level (title, abstract, poster, slides or paper), NCT ID, cohort identifier and data cutoff where reported. Do not invent missing cohort IDs.
4. Compare with earlier public reports from the same trial and cohort. Extract genuinely incremental patient count, follow-up, endpoint maturity, biomarker results and safety observations. Date each comparison and cite exact passages or tables.
5. Group potentially overlapping cohorts for review. Shared NCT IDs can contain distinct cohorts, while repeated trial-and-cohort reports may be follow-up rather than replication. State uncertainty instead of summing patients or treating repeated reports as independent evidence.
6. Rank relevance using transparent criteria tied to the user's question: evidentiary novelty, design quality, clinical relevance and potential decision impact. Separate these judgments from an automatic investment recommendation.
7. Deliver a public-evidence brief showing what is new, what is unchanged, cohort overlap, limitations, source locators and the next public material needed. For investment work, map supported observations to explicit model implication statuses, not assumed commercial success.

## Boundaries

The upstream utility uses researcher-supplied public-availability metadata; validation of a timestamp field does not independently verify public release. This host workflow must inspect the source and access conditions. Do not claim the Python conference tool ran or that embargoed information has been cleared by installing the plugin.

## Shared controls and output

Read [evidence controls](references/evidence-controls.md) before executing this workflow and use the [connector map](references/connector-routing.md) for source selection. Use the [evidence brief](references/evidence-brief.md) when producing investment-related evidence. The workflows use the host's available tools; upstream Python utilities and the local MCP server are not included or deployed by this plugin.
