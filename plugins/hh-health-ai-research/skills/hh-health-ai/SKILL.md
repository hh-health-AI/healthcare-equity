---
name: hh-health-ai
description: Use for an explicit HH Health AI request, a cross-domain healthcare research
  question, or help choosing among the bundled evidence, trial, valuation and investment
  workflows. Route narrowly; do not activate all modules for a simple question.
---

# HH Health AI Research

## Start with the decision

Identify the company, product, trial, indication or research claim and the decision the answer should support. Reuse details already supplied. Specify geography, date cutoff, relevant reporting period and output only where material. If the request is underspecified but workable, state a sensible scope and proceed; reserve questions for genuinely blocking information.

## Select the smallest useful workflow

Read the selected sibling skill through the host's skill loader when available, or the corresponding relative SKILL.md. If the loader cannot read a sibling, explain the access gap rather than claiming that workflow ran.

| User goal | Bundled skill |
|---|---|
| An evidence-backed company thesis or full underwriting view | [Investable View](../investable-view/SKILL.md) |
| Initiation, earnings, model framing, thesis challenge, portfolio or investment communication | [Healthcare Equity](../healthcare-equity/SKILL.md) |
| Reimbursement, utilization, provider economics, safety, IP or other evidence engine | [Evidence Modules](../evidence-modules/SKILL.md) |
| A biomedical question or evidence synthesis | [Medical Evidence Skills](../medical-evidence-skills/SKILL.md) |
| Registry–paper–press-release comparison | [Clinical Trial Analyst](../clinical-trial-analyst/SKILL.md) |
| Checking whether citations support claims | [Biomedical Claim Checker](../biomedical-claim-checker/SKILL.md) |
| Trial watchlist changes or a catalyst calendar | [Biotech Catalyst Radar](../biotech-catalyst-radar/SKILL.md) |
| Literature search, deduplication or screening worklist | [Literature Review Assistant](../literature-review-assistant/SKILL.md) |
| Public data retrieval and completeness checks | [Healthcare Public Data](../healthcare-public-data/SKILL.md) |
| Probability-weighted biotech cash flows and equity bridge | [Biotech rNPV Modeler](../biotech-rnpv-modeler/SKILL.md) |
| Public conference materials and incremental evidence | [Conference Evidence Agent](../conference-evidence-agent/SKILL.md) |
| Paper appraisal and an eight-slide discussion outline | [Journal Club Agent](../journal-club-agent/SKILL.md) |

For combined work, retrieve once, assign source identifiers, run only material evidence modules, and feed their implication records into the requested synthesis. Do not mistake multiple summaries of one source for independent corroboration. Declare material steps skipped or blocked.

## Final handoff

Lead with the decision-relevant answer. Distinguish observations, inference, changed or unchanged assumptions, disconfirming evidence and remaining diligence. Use an evidence appendix when detail would otherwise obscure the result. Do not append every possible follow-up. This release is a snapshot of adapted workflows, not a live mirror of the repositories.

## Shared controls and output

Read [evidence controls](references/evidence-controls.md) before executing this workflow and use the [connector map](references/connector-routing.md) for source selection. Use the [evidence brief](references/evidence-brief.md) when producing investment-related evidence. The workflows use the host's available tools; upstream Python utilities and the local MCP server are not included or deployed by this plugin.
