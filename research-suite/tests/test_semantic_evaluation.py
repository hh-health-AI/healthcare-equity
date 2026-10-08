"""Synthetic scorer tests; these are not measured model predictions."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "evaluate_semantic.py"
spec = importlib.util.spec_from_file_location("evaluate_semantic", SCRIPT)
evaluation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(evaluation)


def fixtures():
    # Synthetic three-class cases exercise scoring arithmetic independently.
    corpus = {"benchmark_id": "SYNTHETIC-test", "items": [
        {"id": "S", "domain": "test", "source_id": "synthetic", "locator": "a", "claim": "A", "passage": "A"},
        {"id": "C", "domain": "test", "source_id": "synthetic", "locator": "b", "claim": "A", "passage": "Not A"},
        {"id": "I", "domain": "test", "source_id": "synthetic", "locator": "c", "claim": "A", "passage": "B"},
    ]}
    key = {"benchmark_id": corpus["benchmark_id"], "answers": [
        {"id": iid, "label": label, "rationale": "Synthetic expected label."}
        for iid, label in zip(("S", "C", "I"), evaluation.LABELS)
    ]}
    packet = {"run": {
        "run_id": "synthetic-scoring-test", "benchmark_id": corpus["benchmark_id"],
        "evaluation_kind": "deterministic_baseline", "system_name": "Synthetic fixture", "system_version": "1",
        "provider": "NONE", "model_id": "NONE", "prompt_version": "fixture-v1", "prompt_sha256": "0" * 64,
        "corpus_sha256": evaluation.digest(corpus), "generated_at": "2026-10-08T00:00:00Z",
        "generation_method": "Synthetic test fixture; not an AI result", "answer_key_accessed": False,
    }, "predictions": [
        {"id": "S", "label": "supported", "rationale": "Synthetic match."},
        {"id": "C", "label": "supported", "rationale": "Deliberate false support."},
        {"id": "I", "label": "abstain", "rationale": "Deliberate processing abstention."},
    ]}
    return corpus, key, packet


class SemanticEvaluationTests(unittest.TestCase):
    def test_class_metrics_and_abstention_use_all_items(self):
        report = evaluation.score(*fixtures())
        m = report["metrics"]
        self.assertEqual(m["total"], 3)
        self.assertEqual(m["accuracy"], 0.333333)
        self.assertEqual(m["coverage"], 0.666667)
        self.assertEqual(m["selective_accuracy"], 0.5)
        self.assertEqual(m["abstention_rate"], 0.333333)
        self.assertEqual(m["per_class"]["supported"]["precision"], 0.5)
        self.assertEqual(m["per_class"]["supported"]["recall"], 1.0)
        self.assertEqual(m["false_support_rate"], 0.5)
        self.assertEqual(report["confusion"]["contradicted"]["supported"], 1)
        self.assertEqual(report["confusion"]["insufficient"]["abstain"], 1)
        self.assertEqual({e["id"] for e in report["errors"]}, {"C", "I"})

    def test_all_abstain_does_not_invent_perfect_selective_score(self):
        corpus, key, packet = fixtures()
        for p in packet["predictions"]:
            p["label"] = "abstain"
        m = evaluation.score(corpus, key, packet)["metrics"]
        self.assertEqual(m["accuracy"], 0)
        self.assertEqual(m["coverage"], 0)
        self.assertIsNone(m["selective_accuracy"])
        self.assertIsNone(m["per_class"]["supported"]["precision"])

    def test_missing_duplicate_unknown_and_invalid_predictions_are_rejected(self):
        for mutate in (
            lambda p: p["predictions"].pop(),
            lambda p: p["predictions"].append(copy.deepcopy(p["predictions"][0])),
            lambda p: p["predictions"][0].update(id="OTHER"),
            lambda p: p["predictions"][0].update(label="probably supported"),
        ):
            with self.subTest(mutate=mutate):
                corpus, key, packet = fixtures()
                mutate(packet)
                with self.assertRaises(ValueError):
                    evaluation.score(corpus, key, packet)

    def test_submitted_scores_and_reference_label_echo_declarations_rejected(self):
        for mutate in (
            lambda p: p.update(accuracy=1.0),
            lambda p: p["run"].update(accuracy=1.0),
            lambda p: p["predictions"][0].update(score=1.0),
            lambda p: p["run"].update(answer_key_accessed=True),
        ):
            corpus, key, packet = fixtures()
            mutate(packet)
            with self.assertRaises(ValueError):
                evaluation.score(corpus, key, packet)

    def test_versions_hashes_and_timestamp_are_required(self):
        for mutate in (
            lambda p: p["run"].pop("system_version"),
            lambda p: p["run"].pop("prompt_version"),
            lambda p: p["run"].update(corpus_sha256="0" * 64),
            lambda p: p["run"].update(prompt_sha256="invented"),
            lambda p: p["run"].update(generated_at="2026-10-08T00:00:00"),
        ):
            corpus, key, packet = fixtures()
            mutate(packet)
            with self.assertRaises(ValueError):
                evaluation.score(corpus, key, packet)

    def test_ai_run_requires_recorded_prompt_response_and_model(self):
        corpus, key, packet = fixtures()
        packet["run"].update(evaluation_kind="external_ai_predictions", model_id="test-model")
        with self.assertRaisesRegex(ValueError, "archive"):
            evaluation.score(corpus, key, packet)
        packet["run"].update(prompt_archive="synthetic-prompt.txt", response_archive="synthetic-response.json")
        report = evaluation.score(corpus, key, packet)
        self.assertIn("submitter declarations", report["run_provenance"])
        packet["run"]["evaluation_kind"] = "session_ai_review"
        self.assertIn("Separate-session assistant", evaluation.score(corpus, key, packet)["measurement_interpretation"])

    def test_archived_prompt_hash_and_prediction_consistency(self):
        corpus, key, packet = fixtures()
        packet["run"].update(evaluation_kind="session_ai_review", model_id="synthetic-model", prompt_archive="prompt.md", response_archive="response.json")
        prompt = b"SYNTHETIC prompt, not a model execution."
        packet["run"]["prompt_sha256"] = evaluation.hashlib.sha256(prompt).hexdigest()
        with tempfile.TemporaryDirectory() as path:
            root = Path(path)
            (root / "prompt.md").write_bytes(prompt)
            (root / "response.json").write_text(json.dumps(packet))
            self.assertEqual(evaluation.verify_archives(packet, root)["status"], "local_archive_integrity_checked")
            (root / "prompt.md").write_text("tampered")
            with self.assertRaisesRegex(ValueError, "prompt bytes"):
                evaluation.verify_archives(packet, root)
            (root / "prompt.md").write_bytes(prompt)
            altered = copy.deepcopy(packet)
            altered["predictions"][0]["label"] = "abstain"
            (root / "response.json").write_text(json.dumps(altered))
            with self.assertRaisesRegex(ValueError, "response differs"):
                evaluation.verify_archives(packet, root)

    def test_candidate_answer_leakage_and_key_mismatch_rejected(self):
        corpus, key, packet = fixtures()
        corpus["items"][0]["label"] = "supported"
        with self.assertRaisesRegex(ValueError, "exclude answers"):
            evaluation.score(corpus, key, packet)
        corpus, key, packet = fixtures()
        key["answers"].pop()
        with self.assertRaisesRegex(ValueError, "coverage"):
            evaluation.score(corpus, key, packet)


if __name__ == "__main__":
    unittest.main()
