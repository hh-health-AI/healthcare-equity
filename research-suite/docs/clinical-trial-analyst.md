# Clinical Trial Analyst

Use to interpret a clinical trial, assess a readout, reconcile a registry with a publication or press release, examine endpoints, multiplicity, missing data, safety or applicability. Extract evidence before comparing; never infer misconduct from a textual difference alone.

## Try it

- Compare this trial press release with its registry and publication.
- Audit the statistical interpretation of this Phase III result.
- What would change the conclusion of this study?

## Run the reproducible utility

```bash
hh-research trial examples/trial.json --out outputs/clinical-trial-analyst.md
```

Run from `research-suite` after installation. The offline examples are explicitly synthetic; public API outputs carry retrieval metadata.

## Workflow

1. Resolve the exact NCT ID and distinguish trial from extension, subgroup and pooled analyses.
2. Fetch the registry with `hh-research data trial --id NCT04280705 --out registry.json`, substituting the requested ID. Read protocol, SAP, paper, supplements and release through available tools. Record access gaps.
3. Reconstruct the document timeline. Current registry data are not proof of original prespecification; retrieve historical documents where the question depends on amendments.
4. Extract fields into `documents[]` using identical definitions and units. Include outcome/timepoint, estimand, analysis population, sample size, masking, comparator and follow-up. Preserve detailed passages separately in an evidence packet.
5. Run `hh-research trial comparison.json --out trial-comparison.md --json-out trial-comparison.json`. This flags differences in supplied fields, not semantic truth.
6. Analyze effect sizes, confidence intervals, absolute effects if calculable, multiplicity, intercurrent events, missingness and harms. Report what is prespecified versus exploratory.
7. Check whether the release omitted important results or changed the population/timepoint. Do not mistake a wording change for an endpoint change.
8. Deliver a supported conclusion, discrepancy table, design limitations, disconfirming evidence and questions for follow-up. For investment requests, separately explain assumptions affected.

## Existing platform handoff

[clinical-catalysts](../../modules/clinical-catalysts/)

[Skill instructions](../skills/clinical-trial-analyst/SKILL.md) · [Agent workflow](../agents/clinical-trial-analyst.md) · [Input contracts](input-contracts.md)
