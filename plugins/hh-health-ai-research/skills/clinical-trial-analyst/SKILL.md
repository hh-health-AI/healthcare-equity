---
name: clinical-trial-analyst
description: Use to interpret a trial or readout and reconcile registry, protocol,
  publication and press release; examine endpoints, multiplicity, missing data, safety
  and applicability. Extract evidence before comparing and never infer misconduct
  solely from a textual discrepancy.
---

# Clinical Trial Analyst

## Workflow

1. Resolve the exact NCT ID and distinguish the primary trial, extension, subgroup, pooled analysis and follow-up report. Attribute sponsor/ticker mappings rather than assuming them from similar names.
2. Retrieve the registry, protocol, statistical analysis plan, primary publication, supplement and issuer release through available sources. Record which documents and historical versions are inaccessible. A current registry record does not prove what was prespecified when the study began.
3. Reconstruct the document and amendment timeline. Distinguish study dates, data cutoffs, registry updates and publication dates. When endpoint changes matter, compare relevant historical records or label the question unresolved.
4. Extract aligned fields: population and estimand, randomization/masking, intervention/comparator, sample size, primary/secondary endpoints, timepoints, analysis sets, multiplicity, missingness, intercurrent events, follow-up and safety denominators. Retain exact locators and brief passages. Compare like units and definitions.
5. Build a source-by-source discrepancy table. Separate actual inconsistencies from differences in wording, follow-up maturity, analysis population or reporting scope. A textual difference may merit investigation but does not establish endpoint switching or misconduct.
6. Assess relative and absolute effects where calculable, confidence intervals, prespecified versus exploratory analyses, clinical importance, multiplicity, missing data and harms. Avoid cross-trial efficacy rankings without addressing design and population differences. Do not reconstruct unavailable patient-level results.
7. Identify material omissions or overstatement in the press release. State what is supported, partly supported, unverified or contradicted, with the evidence boundary. Preserve null and adverse findings.
8. Deliver the clinical conclusion, comparison table, limitations, disconfirming evidence and questions that would change the interpretation. For an investment request, separately map the evidence to approval, label, population, timing or commercial assumptions; trial evidence alone does not establish commercial uptake.

## Output fields

Finding | source and version/date | exact endpoint/population/timepoint | discrepancy or agreement | likely explanation versus unresolved question | decision implication | confidence.

The source repository's optional comparison utility flags differences in extracted fields; it does not determine semantic truth. Do not claim that utility ran when following this workflow with host tools.

## Shared controls and output

Read [evidence controls](references/evidence-controls.md) before executing this workflow and use the [connector map](references/connector-routing.md) for source selection. Use the [evidence brief](references/evidence-brief.md) when producing investment-related evidence. The workflows use the host's available tools; upstream Python utilities and the local MCP server are not included or deployed by this plugin.
