# Reliability evaluation

Run from `research-suite` after installing the package:

```sh
python scripts/evaluate_reliability.py
```

The [recorded result](results.json) was produced on 2026-10-03 with Python 3.11. The script exits nonzero on regression failures. CI runs it on Python 3.10 and 3.12. It uses actual package functions, synthetic offline inputs and explicit expectations. No live API, model call or clinical data is involved.

| Dimension | What is measured | What is not measured |
|---|---|---|
| Claim/source linkage | Missing citations, missing passages, retracted-only support, labeled unverifiable claims | Whether a supplied passage actually entails the claim |
| Trial fields | Six exact-match fields in one synthetic registry record plus mismatch/missingness regressions | Clinical interpretation or extraction from PDF prose |
| Data completeness | Caps, duplicate pages, changing totals, missing records and CMS sample disclosure | Live endpoint uptime, real population representativeness or source suppression |
| Valuation | Hand-calculated asset PV 40, equity 47 and per-share value 23.5; missing bridge and invalid inputs | Whether clinical probabilities or commercial forecasts are correct |
| Passage entailment development set | [24 real-source cases](semantic/README.md), separately archived assistant label review, precision/recall, confusion/errors and abstention scorer | Held-out generalization, original-document interpretation, deployed agent accuracy or independent human clinical validation |

## Deliberate failure boundary

The evaluation labels an unsupported 90% mortality claim as `supported`, attaches a valid citation to a synthetic passage about a different, imprecise event outcome, and passes it through the evidence validator. **The validator accepts it.** This is expected for a structural validator, but demonstrates why successful code checks cannot be advertised as claim-verification accuracy. The benchmark records one false semantic pass out of one adversarial probe; it does not extrapolate that rate to real research.

## Dataset and scoring limitations

These checks were designed by the same project author/assistant workflow that maintains the code. They are small, synthetic and not a blinded or held-out evaluation. Exact-match checks use structured fields, not expert medical judgment. Existing regression cases are reused and counted once within each named group. Six field checks belong to one additional record, not six independent trials. Clinical accuracy and live endpoint accuracy remain NOT_MEASURED.

## Separate passage-level evaluation

The [semantic development set](semantic/README.md) adds 24 claims from four retrieved
primary-source records, exact locators and response checksums. Its public candidate
corpus excludes the author answer key. Passages are short, clearly labeled author
paraphrases, making the task easier than full-document extraction and interpretation.

A separate assistant assessed the candidate corpus before viewing the answer key.
The [archived review](semantic/review.json) records agreement on 24 labels, not a
claim of universal AI accuracy. The reviewer shared development-session context;
the exact model revision is unavailable. No independently qualified human clinical
review, external API benchmark, held-out dataset or deployed-agent performance
measurement was performed. Source-original document entailment remains NOT_MEASURED.

The scorer consumes external predictions and computes per-class precision/recall,
accuracy, abstention, coverage, confusion and errors. It rejects submitted score
claims, partial ID coverage and declared answer-key access. CLI archive checks
verify task-prompt/response file integrity; model identity and key isolation remain
self-declared. A distinct all-abstain non-AI baseline exercises the scoring pipeline.
See [instructions and limits](semantic/README.md) before running a system or reporting
results. The original 27 structural regression cases remain separate and unchanged.
