# Passage-level semantic evaluation — development set v1

This public set contains 24 claims grounded in four primary-source records:
ClinicalTrials.gov ACTT-1, the trial's final publication abstract, FDA's original
22 October 2020 approval announcement, and AbCellera's 2025 Form 10-K. Sources were
retrieved on 8 October 2026. It tests population, endpoint, confidence-interval,
historical-label, unit, financial-statement and missing-evidence interpretation.

The candidate [corpus](corpus.json) excludes labels. The separately stored
[answer key](answer-key.json) includes author rationales. [Sources](sources.json)
record exact locators, retrieval timestamps and SHA-256 hashes of original HTTP
response bytes. Original full responses are not redistributed; item passages are
short **author paraphrases**, not verbatim quotations. Those paraphrases reduce the
task's difficulty relative to interpretation of full original documents.

This is a small author-designed **public development set**, not a held-out test,
an independently clinically adjudicated benchmark or an investment-performance
study. Labels were prepared by a coding assistant. A separate assistant review is
recorded in [review.json](review.json); assistant agreement does not confer domain
expert validation. Multiple items reuse sources, so observations are correlated.

## Generate predictions separately

Give [prompt.md](prompt.md) and `corpus.json` to the system being assessed. Withhold
the answer key until its response is archived. Add run metadata to the response
using the shape in [baseline-predictions.json](baseline-predictions.json).

For an AI run, use `evaluation_kind: external_ai_predictions` and identify the
actual `model_id`, provider, system version, prompt version and SHA-256, canonical
corpus SHA-256, execution timestamp, prompt archive and response archive. Do not
claim an exact model version when your host does not expose it. Declare whether
the answer key was accessed; this scorer rejects a run declaring access.

The corpus hash is SHA-256 of JSON serialized with sorted keys, separators `,` and
`:`, UTF-8 and `ensure_ascii=False` (the scorer's `digest` function). Prompt hashes
refer to the exact archived prompt bytes. Archive the raw response before any
schema repair and record repairs in the caller's execution log.

```bash
python scripts/evaluate_semantic.py \
  --predictions evaluation/semantic/my-model-predictions.json \
  --out outputs/my-model-semantic-results.json
```

The scorer computes accuracy, per-class precision/recall/F1, a confusion matrix,
false-support rate, coverage, abstention and an itemized error analysis. Accuracy
includes all 24 items; processing failures must appear as `abstain`. Selective
accuracy excludes abstentions and is always reported alongside coverage. A zero
denominator produces `null`, not an invented perfect score. `insufficient` is an
answerable evidence classification; `abstain` is a system's decision not to
classify. The scorer rejects missing/duplicate IDs, unknown labels, answer-key
echo declarations and submitted score fields. It cannot verify self-declared
model identity or answer-key isolation; its reports state that limitation.

`session_ai_review` is available for an archived separate-session assistant review
of the labels. It requires the same model, prompt and response metadata as an AI
run. Report the exact model revision as unavailable when the host does not expose
it. This is a label-agreement check, not independent human clinical validation or
a deployed-system performance benchmark. The answer key must remain withheld until
predictions and archives are frozen.

## Current results

**Deployed-system semantic performance: NOT_MEASURED.** The recorded
[separate assistant review](review.json) agreed with the author's 24 labels, with
no abstentions. The [task prompt](session-review-prompt.md),
[review response](session-review-response.json) and
[computed agreement scorecard](session-review-results.json) are available for
inspection. The response was archived before the reviewer viewed the answer key.
The reviewer shared the development-session context; the exact model revision is
unavailable, and no external model API was invoked. This label review measures
agreement on compressed author paraphrases, not entailment of unabridged source
documents, clinical accuracy or the performance of a deployed agent.

The [all-abstain baseline](baseline-predictions.json) uses no
model and reads no answer labels. Its [scorecard](baseline-results.json) exercises
the scorer with 0% accuracy, 100% abstention and undefined selective accuracy.
These are pipeline smoke results, not AI performance. Do not turn the answer key
into predictions or display a perfect reference-label score as measured ability.

```bash
python scripts/evaluate_semantic.py \
  --predictions evaluation/semantic/baseline-predictions.json \
  --out outputs/semantic-baseline.json
python -m unittest discover -s tests -p test_semantic_evaluation.py -v
```

AI/review runs require readable local prompt and JSON response archives. The CLI
checks the declared SHA-256 against the archived task-prompt bytes and checks that
the archived predictions equal the scored submission. This verifies file
integrity, not full-session reconstruction, model execution or answer-key isolation.

Expand and clinically review the source set, freeze a private held-out partition,
run separately versioned systems, and inspect failures before drawing broader
accuracy conclusions. Historical passages intentionally do not describe current
clinical practice or product labels.
