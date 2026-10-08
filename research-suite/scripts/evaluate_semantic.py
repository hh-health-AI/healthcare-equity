#!/usr/bin/env python3
"""Score separately generated passage-level predictions; never generate verdicts."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys

LABELS = ("supported", "contradicted", "insufficient")
PREDICTIONS = LABELS + ("abstain",)
ROOT = Path(__file__).resolve().parents[1] / "evaluation" / "semantic"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def validate_benchmark(corpus, key):
    require(corpus.get("benchmark_id") == key.get("benchmark_id"), "Corpus and answer key differ")
    items = corpus.get("items")
    require(isinstance(items, list) and bool(items), "Corpus has no items")
    index = {}
    for item in items:
        require(isinstance(item, dict) and item.get("id") and item["id"] not in index, "Corpus IDs must be unique")
        require(all(item.get(k) for k in ("claim", "passage", "domain", "source_id", "locator")), "Item lacks claim, passage or provenance")
        require(not any(k in item for k in ("label", "verdict", "answer", "expected")), "Candidate corpus must exclude answers")
        index[item["id"]] = item
    answers = key.get("answers")
    require(isinstance(answers, list), "Answer key must contain answers")
    answer_index = {}
    for row in answers:
        require(isinstance(row, dict) and row.get("id") not in answer_index, "Answer IDs must be unique")
        require(row.get("label") in LABELS and bool(row.get("rationale")), "Answer label or rationale is invalid")
        answer_index[row["id"]] = row
    require(set(index) == set(answer_index), "Answer key coverage differs from corpus")
    return index, answer_index


def validate_predictions(corpus, packet):
    require(isinstance(packet, dict) and set(packet) == {"run", "predictions"}, "Predictions accept only run metadata and predictions; supplied scores are forbidden")
    run = packet["run"]
    require(isinstance(run, dict), "Run metadata must be an object")
    fields = ("run_id", "benchmark_id", "evaluation_kind", "system_name", "system_version", "provider", "prompt_version", "prompt_sha256", "corpus_sha256", "generated_at", "generation_method")
    require(all(isinstance(run.get(k), str) and run[k].strip() for k in fields), "Run metadata must identify system/provider/version, prompt and generation method")
    require(set(run) <= set(fields) | {"answer_key_accessed", "model_id", "response_archive", "prompt_archive"}, "Unknown run fields; submitter metrics are forbidden")
    require(run["evaluation_kind"] in ("external_ai_predictions", "session_ai_review", "deterministic_baseline"), "Unknown evaluation kind")
    require(run["benchmark_id"] == corpus["benchmark_id"], "Prediction benchmark differs")
    require(run["corpus_sha256"] == digest(corpus), "Prediction corpus hash differs")
    require(re.fullmatch(r"[0-9a-f]{64}", run["prompt_sha256"]) is not None, "Prompt must have a SHA-256 digest")
    require(run.get("answer_key_accessed") is False, "Run must declare answer_key_accessed=false; reference-label echoes are not evaluations")
    stamp = datetime.fromisoformat(run["generated_at"].replace("Z", "+00:00"))
    require(stamp.tzinfo is not None, "Prediction timestamp must contain timezone")
    if run["evaluation_kind"] in ("external_ai_predictions", "session_ai_review"):
        require(run.get("model_id") and run.get("response_archive") and run.get("prompt_archive"), "AI runs require model ID, prompt archive and response archive")
    else:
        require(run.get("model_id") in (None, "NONE"), "Deterministic baseline cannot claim an AI model")
    rows = packet["predictions"]
    require(isinstance(rows, list), "Predictions must be a list")
    index = {}
    for row in rows:
        require(isinstance(row, dict) and set(row) == {"id", "label", "rationale"}, "Each prediction must contain only id, label and rationale")
        require(row["id"] not in index, "Duplicate prediction ID")
        require(row["label"] in PREDICTIONS and isinstance(row["rationale"], str) and bool(row["rationale"].strip()), "Invalid prediction label/rationale")
        index[row["id"]] = row
    require(set(index) == {item["id"] for item in corpus["items"]}, "Predictions must cover every corpus ID exactly once; use abstain for failed responses")
    return index


def ratio(numerator, denominator):
    return round(numerator / denominator, 6) if denominator else None


def verify_archives(packet, directory):
    """Check local task-prompt/response archives, not the caller's entire session."""
    if packet["run"]["evaluation_kind"] == "deterministic_baseline":
        return {"status": "not_applicable_non_ai_baseline"}
    run = packet["run"]
    prompt = (directory / run["prompt_archive"]).read_bytes()
    response = (directory / run["response_archive"]).read_bytes()
    prompt_sha = hashlib.sha256(prompt).hexdigest()
    require(prompt_sha == run["prompt_sha256"], "Archived prompt bytes do not match the declared hash")
    archived = json.loads(response)
    archived_predictions = archived.get("predictions") if isinstance(archived, dict) else None
    require(archived_predictions == packet["predictions"], "Archived response differs from submitted predictions")
    return {"status": "local_archive_integrity_checked", "prompt_sha256": prompt_sha, "response_sha256": hashlib.sha256(response).hexdigest(), "scope": "Task prompt and submitted response only; no model execution, answer-key isolation or full-session reconstruction assurance"}


def score(corpus, key, packet):
    items, answers = validate_benchmark(corpus, key)
    predicted = validate_predictions(corpus, packet)
    confusion = {truth: {label: 0 for label in PREDICTIONS} for truth in LABELS}
    errors, domains = [], {}
    for iid, item in items.items():
        truth, prediction = answers[iid]["label"], predicted[iid]["label"]
        confusion[truth][prediction] += 1
        domain = domains.setdefault(item["domain"], Counter(total=0, correct=0, abstained=0))
        domain["total"] += 1
        domain["correct"] += truth == prediction
        domain["abstained"] += prediction == "abstain"
        if truth != prediction:
            errors.append({"id": iid, "domain": item["domain"], "expected": truth, "predicted": prediction, "claim": item["claim"], "prediction_rationale": predicted[iid]["rationale"], "answer_rationale": answers[iid]["rationale"], "source_id": item["source_id"], "locator": item["locator"]})
    total = len(items)
    correct = sum(confusion[x][x] for x in LABELS)
    abstained = sum(confusion[x]["abstain"] for x in LABELS)
    per_class = {}
    for label in LABELS:
        tp = confusion[label][label]
        predicted_n = sum(confusion[truth][label] for truth in LABELS)
        actual_n = sum(confusion[label].values())
        p, r = ratio(tp, predicted_n), ratio(tp, actual_n)
        per_class[label] = {"precision": p, "recall": r, "f1": ratio(2 * tp, predicted_n + actual_n), "true_count": actual_n, "predicted_count": predicted_n}
    interpretations = {
        "deterministic_baseline": "Non-AI scorer smoke test; not semantic model performance",
        "session_ai_review": "Separate-session assistant label review on a public author-designed set; no independent human clinical adjudication, exact model-revision assurance or deployed-system accuracy claim",
        "external_ai_predictions": "Externally submitted system predictions on a public development set; model and isolation provenance are self-declared",
    }
    return {"schema_version": 1, "scored_at": datetime.now(timezone.utc).isoformat(), "benchmark_id": corpus["benchmark_id"], "corpus_sha256": digest(corpus), "answer_key_sha256": digest(key), "prediction_sha256": digest(packet), "run": packet["run"], "measurement_interpretation": interpretations[packet["run"]["evaluation_kind"]], "scope": "Passage-level entailment on a small public development set; no end-to-end retrieval, clinical validation, investment performance or held-out generalization claim", "run_provenance": "Generation metadata and answer-key isolation are submitter declarations, not independently verified by this scorer", "metrics": {"total": total, "correct": correct, "accuracy": ratio(correct, total), "abstained": abstained, "abstention_rate": ratio(abstained, total), "coverage": ratio(total - abstained, total), "selective_accuracy": ratio(correct, total - abstained), "false_support_count": sum(confusion[x]["supported"] for x in LABELS if x != "supported"), "false_support_rate": ratio(sum(confusion[x]["supported"] for x in LABELS if x != "supported"), sum(sum(confusion[x].values()) for x in LABELS if x != "supported")), "per_class": per_class}, "confusion": confusion, "by_domain": {name: {**dict(counts), "accuracy": ratio(counts["correct"], counts["total"])} for name, counts in sorted(domains.items())}, "errors": errors}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", type=Path, default=ROOT / "corpus.json")
    parser.add_argument("--answer-key", type=Path, default=ROOT / "answer-key.json")
    parser.add_argument("--predictions", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    try:
        packet = load(args.predictions)
        report = score(load(args.corpus), load(args.answer_key), packet)
        report["archive_verification"] = verify_archives(packet, args.predictions.resolve().parent)
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(json.dumps({"evaluation_kind": report["run"]["evaluation_kind"], "total": report["metrics"]["total"], "accuracy": report["metrics"]["accuracy"], "abstention_rate": report["metrics"]["abstention_rate"], "report": str(args.out)}))
    except (ValueError, KeyError, TypeError, OSError) as exc:
        print(f"Evaluation rejected: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
