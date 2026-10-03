# Medical Evidence Skills

Use when a user asks a biomedical question, wants a PICO search, evidence table, critical appraisal, conflicting-evidence synthesis or plain-language explanation. Coordinate evidence retrieval and appraisal, retaining source passages and uncertainty. Do not trigger for personalized treatment decisions.

## Try it

- What does randomized evidence say about intervention X in population Y?
- Build a PICO search and evidence table for this question.
- Explain why these two studies disagree.

## Run the reproducible utility

```bash
hh-research evidence examples/evidence.json --out outputs/medical-evidence-skills.md
```

Run from `research-suite` after installation. The offline examples are explicitly synthetic; public API outputs carry retrieval metadata.

## Workflow

1. Define the question, population, intervention/exposure, comparator, outcomes, setting and date cutoff. If a missing element prevents a useful search, ask one focused question; otherwise state the scope and proceed.
2. Use the ten procedures in `references/methods.md`. Choose relevant procedures rather than running everything automatically.
3. Search primary records through the public-data toolkit or the host's available tools. Record exact queries, filters, database, retrieval time, record count and any cap. Seek null and conflicting findings.
4. Read the full text when available. Identify study design, prespecified endpoints, analysis population, effect size and uncertainty, harms and applicability. State when only an abstract is accessible.
5. Create one source record per actual document and one claim per material conclusion. Preserve locator and a short passage; distinguish a source's claim from independent confirmation.
6. Fill the evidence packet described in `references/output-contract.md`. Assign claim assessments only after reading cited material. Do not treat a numerical confidence score as a statistical probability.
7. Run `hh-research evidence packet.json --out evidence-brief.md --json-out evidence-brief.json`. Resolve validation errors by correcting the evidence, never by inventing citations.
8. End with the answer, supported observations, interpretation, limitations and next evidence needed. Add investment interpretation only if requested.

## Existing platform handoff

[evidence-catalysts](../../modules/evidence-catalysts/), [clinical-catalysts](../../modules/clinical-catalysts/)

[Skill instructions](../skills/medical-evidence-skills/SKILL.md) · [Agent workflow](../agents/medical-evidence-skills.md) · [Input contracts](input-contracts.md)
