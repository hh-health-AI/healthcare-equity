# Biomedical Claim Checker

Use when checking whether a medical or scientific claim is supported by its cited paper, verifying references, auditing an AI-generated biomedical answer or examining overstatement in a press release. Assess entailment, source validity and missing evidence, not just whether a DOI exists.

## Try it

- Audit the citations and claims in this AI-generated medical answer.
- Does this paper actually support the press release headline?
- Check these five claims and propose defensible wording.

## Run the reproducible utility

```bash
hh-research claims examples/evidence.json --out outputs/biomedical-claim-checker.md
```

Run from `research-suite` after installation. The offline examples are explicitly synthetic; public API outputs carry retrieval metadata.

## Workflow

1. Split the supplied text into atomic checkable claims. Retain original wording and document context.
2. Resolve each PMID/DOI/reference and read the relevant passage, table or figure. Confirm title, authors, year and the claimed cohort. Check correction/retraction notices when possible.
3. Test population, intervention/dose, comparator, endpoint, timepoint, effect measure and certainty against the passage. Distinguish association, causal evidence, model prediction and opinion.
4. Search for contradicting or qualifying primary evidence when the claim is material. Report the search boundary.
5. Assign supported, partially-supported, unsupported, contradicted or unverifiable with a rationale. Inaccessible full text leads to limited verification, not a confident supported verdict.
6. Save an evidence packet and run `hh-research claims packet.json --out claim-audit.md --json-out claim-audit.json`.
7. Explain which wording can be retained, what needs qualification and what remains unverified. A valid reference is not proof that it supports the claim.

## Existing platform handoff

[evidence-catalysts](../../modules/evidence-catalysts/)

[Skill instructions](../skills/biomedical-claim-checker/SKILL.md) · [Agent workflow](../agents/biomedical-claim-checker.md) · [Input contracts](input-contracts.md)
