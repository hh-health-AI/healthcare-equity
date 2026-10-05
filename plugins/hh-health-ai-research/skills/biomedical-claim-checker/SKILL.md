---
name: biomedical-claim-checker
description: Use to audit whether medical or scientific claims are supported by their
  citations, verify references, assess AI-generated biomedical text or identify overstatement
  in a press release. Evaluate source validity and entailment, not just identifier
  existence.
---

# Biomedical Claim Checker

## Workflow

1. Break the supplied text into atomic, checkable claims while preserving original wording, qualifiers and context. Keep separate claims separate even when they share a reference.
2. Resolve each PMID, DOI or other reference. Verify title, authors, year, document type and population, and inspect relevant correction or retraction notices when accessible. Read the cited passage, table or figure; metadata alone is insufficient.
3. Compare population, intervention/dose, comparator, endpoint, timepoint, effect measure, direction, magnitude and stated certainty with the claim. Distinguish association, causal evidence, model prediction and opinion. A technically true observation may still fail to support a broader generalization.
4. Search for material contradictory or qualifying primary evidence. Record the search boundary. Do not silently replace an incorrect citation with a different paper and label the original citation correct.
5. Assign one transparent assessment: supported, partially-supported, unsupported, contradicted or unverifiable. Supported means the inspected source supports the bounded claim, not that all evidence agrees. Unsupported means the inspected evidence does not substantiate it; contradicted requires actual contrary evidence. Inaccessible necessary text is unverifiable or partially verified, not a confident pass.
6. Provide a claim audit with original text, citation identity, short passage/locator, assessment, rationale, missing evidence and proposed corrected wording. Separate source validity from claim entailment. Preserve uncertainty and unresolved disagreement.
7. Summarize the consequential corrections without implying that structural validation or a successful lookup proves truth. An optional upstream CLI can format/validate an already appraised packet; it is not supplied by this plugin and does not replace reading.

## Decision rule

Use the narrowest defensible wording. Where a press release overstates a subgroup or exploratory result, retain the observable result but remove unwarranted certainty or generalization. Do not infer intent, fraud or misconduct merely because the wording is unsupported.

## Shared controls and output

Read [evidence controls](references/evidence-controls.md) before executing this workflow and use the [connector map](references/connector-routing.md) for source selection. Use the [evidence brief](references/evidence-brief.md) when producing investment-related evidence. The workflows use the host's available tools; upstream Python utilities and the local MCP server are not included or deployed by this plugin.
