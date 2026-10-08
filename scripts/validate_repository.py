#!/usr/bin/env python3
"""Offline reproducibility/provenance checks for the research gallery and evaluation.

This checks recorded arithmetic, source linkage and local artifact consistency.
It does not retrieve sources or certify clinical, financial or semantic truth.
The source-sync checker supplies specialist-module/plugin byte provenance.
"""
import argparse
from datetime import datetime, timezone
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SUITE = ROOT / "research-suite"
SEMANTIC = SUITE / "evaluation" / "semantic"
CASES = ("biotech-trial-rnpv", "medtech-procedures-revenue", "managed-care-mlr-earnings")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


def https_url(url):
    parsed = urlparse(url)
    require(parsed.scheme == "https" and bool(parsed.netloc), f"Expected an explicit HTTPS source URL: {url}")


def source_references(value):
    if isinstance(value, dict):
        for key, item in value.items():
            if key == "source_id":
                yield item
            elif key == "source_ids":
                yield from item
            else:
                yield from source_references(item)
    elif isinstance(value, list):
        for item in value:
            yield from source_references(item)


def validate_case_ledgers():
    require((ROOT / "examples/research-cases/README.md").is_file(), "Research gallery README is missing")
    for name in CASES:
        path = ROOT / "examples/research-cases" / name
        for filename in ("README.md", "model.py", "inputs.json", "results.json", "sources.json"):
            require((path / filename).is_file(), f"Missing case artifact: {name}/{filename}")
        inputs, results, ledger = (load(path / filename) for filename in ("inputs.json", "results.json", "sources.json"))
        require(inputs.get("case_id") == results.get("case_id"), f"Case ID mismatch: {name}")
        sources = ledger.get("sources")
        require(isinstance(sources, list) and bool(sources), f"Empty source ledger: {name}")
        source_ids = {row["id"] for row in sources}
        require(len(source_ids) == len(sources), f"Duplicate source IDs: {name}")
        for source in sources:
            https_url(source["url"])
            require(source.get("title"), f"Source title missing: {name}")
            require(source.get("locators") or any(row.get("source_id") == source["id"] and row.get("locator") for row in ledger.get("statements", [])), f"Source locator missing: {name}/{source['id']}")
        require(set(source_references(inputs)) <= source_ids, f"Unresolved input source ID: {name}")
        statements = ledger.get("statements", [])
        statement_index = {row["id"]: row for row in statements}
        require(len(statement_index) == len(statements), f"Duplicate statement IDs: {name}")
        for row in statements:
            require(row.get("source_id") in source_ids and row.get("locator") and row.get("unit"), f"Statement provenance missing: {name}/{row.get('id')}")
        for field, observation in inputs.get("observations", {}).items():
            if not isinstance(observation, dict) or "statement_id" not in observation:
                continue
            require(observation["statement_id"] in statement_index, f"Unresolved statement: {name}/{field}")
            expected = statement_index[observation["statement_id"]]["value"]
            require(observation["value"] in expected if isinstance(expected, list) else observation["value"] == expected, f"Observation differs from its source ledger: {name}/{field}")


def validate_24_case_audit():
    ledger = load(ROOT / "skills/model-valuation/references/case-sources.json")
    require(isinstance(ledger, list) and len(ledger) == 24, "Case source audit must contain 24 scoped cases")
    require({row.get("case_id") for row in ledger} == {f"C{i:02}" for i in range(1, 25)}, "Audit case IDs must cover C01–C24 exactly once")
    require(len({row.get("source_id") for row in ledger}) == 24, "Audit source IDs must be unique")
    for row in ledger:
        require(row.get("status") in {"VERIFIED_SCOPE_ONLY", "NEEDS_DATA", "PENDING_SOURCE_AUDIT"}, f"Unscoped audit status: {row.get('case_id')}")
        require(row.get("review_method") and row.get("unverified_scope") and row.get("audit_date"), f"Review boundary missing: {row.get('case_id')}")
        datetime.fromisoformat(row["audit_date"])
        require(isinstance(row.get("urls"), list) and row["urls"], f"Audit source URLs missing: {row.get('case_id')}")
        for url in row["urls"]:
            https_url(url)
        if row["status"] == "VERIFIED_SCOPE_ONLY":
            require(row.get("verified_statement") and row.get("locator"), f"Verified claim/locator missing: {row.get('case_id')}")


def validate_semantic():
    scorer = module("repository_semantic_scorer", SUITE / "scripts/evaluate_semantic.py")
    corpus, key, sources = (load(SEMANTIC / name) for name in ("corpus.json", "answer-key.json", "sources.json"))
    items, answers = scorer.validate_benchmark(corpus, key)
    require(len(items) == 24, "Semantic development set must contain 24 frozen claims")
    source_rows = sources["sources"]
    source_index = {row["id"]: row for row in source_rows}
    require(len(source_index) == len(source_rows) == 4, "Semantic source records must contain four unique primary documents")
    for source in source_rows:
        https_url(source["url"])
        require(re.fullmatch(r"[0-9a-f]{64}", source["response_sha256"]), "Original response checksum is invalid")
        require(datetime.fromisoformat(source["retrieved_at"]).tzinfo is not None, "Source retrieval timestamp lacks timezone")
        require(source.get("checksum_scope") and source.get("passage_transform") and source.get("locators"), "Source transform or checksum scope is missing")
    for item in items.values():
        require(item["source_id"] in source_index, f"Unresolved semantic source: {item['id']}")
        require(item["locator"] in source_index[item["source_id"]]["locators"], f"Semantic locator not recorded in source ledger: {item['id']}")
        require(item.get("passage_kind") == "author_paraphrase", f"Unlabeled passage transform: {item['id']}")
    for stem in ("baseline", "session-review"):
        prediction_name = "baseline-predictions.json" if stem == "baseline" else "session-review-response.json"
        packet = load(SEMANTIC / prediction_name)
        recorded = load(SEMANTIC / f"{stem}-results.json")
        actual = scorer.score(corpus, key, packet)
        actual["archive_verification"] = scorer.verify_archives(packet, SEMANTIC)
        actual.pop("scored_at", None)
        recorded.pop("scored_at", None)
        require(actual == recorded, f"Recorded semantic scorecard differs from recomputation: {stem}")
    review = load(SEMANTIC / "review.json")
    require(set(review["reviewed_ids"]) == set(items), "Review scope differs from semantic corpus")
    require(review["corpus_sha256"] == scorer.digest(corpus), "Review corpus checksum differs")
    require(review["original_document_entailment"] == review["deployed_system_accuracy"] == "NOT_MEASURED", "Session agreement must not certify original-source/deployed-system accuracy")


def validate_structural_record():
    sys.path.insert(0, str(SUITE))
    reliability = module("repository_reliability", SUITE / "scripts/evaluate_reliability.py")
    actual = reliability.evaluate()
    require(actual == load(SUITE / "evaluation/results.json"), "Recorded structural result differs from evaluate_reliability.py emission")
    require(sum(group["total"] for group in actual["groups"].values()) == 27, "Original structural case count changed")
    require(all(group["failed"] == group["skipped"] == 0 for group in actual["groups"].values()), "Structural regression failure or skip")


def validate_scoped_links():
    paths = set((ROOT / "examples/research-cases").rglob("*.md")) | set((SUITE / "evaluation").rglob("*.md"))
    paths |= {ROOT / "skills/model-valuation/references/case-source-audit.md", ROOT / "skills/model-valuation/references/case-library.md"}
    # Check new cross-links in root README; unrelated legacy module docs retain
    # their own validators instead of acquiring new gallery requirements.
    if (ROOT / "README.md").exists():
        paths.add(ROOT / "README.md")
    for path in paths:
        require(path.is_file(), f"Missing scoped documentation: {path.relative_to(ROOT)}")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            if re.match(r"(?:[a-zA-Z][a-zA-Z0-9+.-]*:|#)", target):
                continue
            if path == ROOT / "README.md" and not any(scope in target for scope in ("research-cases", "evaluation", "case-source-audit", "validate_repository")):
                continue
            local = target.split("#", 1)[0]
            if local:
                require((path.parent / local).exists(), f"Broken local link in {path.relative_to(ROOT)}: {target}")


def model_check(name):
    path = ROOT / "examples/research-cases" / name
    result = subprocess.run([sys.executable, str(path / "model.py"), "--check"], cwd=ROOT, capture_output=True, text=True, timeout=60)
    require(result.returncode == 0, f"{name} model --check failed: {result.stdout}{result.stderr}")


def validate_plugin():
    script = ROOT / "plugins/hh-health-ai-research/tests/validate_static.py"
    result = subprocess.run([sys.executable, str(script)], cwd=ROOT, capture_output=True, text=True, timeout=60)
    require(result.returncode == 0, f"Plugin static validation failed: {result.stdout}{result.stderr}")


def validate_frozen_provenance():
    checker = module("repository_source_sync", ROOT / "scripts/check_source_sync.py")
    report = checker.check_repository(ROOT)
    require(report["failure_count"] == 0, f"Frozen source provenance failed: {json.dumps(report['failures'])}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, help="Optional JSON check report; no artifact is rewritten unless requested")
    args = parser.parse_args()
    checks = [
        ("gallery JSON/source linkage", validate_case_ledgers),
        *[(f"{name} model --check", lambda name=name: model_check(name)) for name in CASES],
        ("24-case source audit schema/scope", validate_24_case_audit),
        ("24-claim semantic scores/source/archive integrity", validate_semantic),
        ("original 27-case structural result reproduction", validate_structural_record),
        ("scoped local documentation links", validate_scoped_links),
        ("instruction plugin static validation", validate_plugin),
        ("frozen module/plugin source provenance", validate_frozen_provenance),
    ]
    rows = []
    for name, check in checks:
        try:
            check()
            rows.append({"name": name, "status": "pass"})
            print(f"PASS: {name}")
        except (ValueError, KeyError, TypeError, OSError, subprocess.TimeoutExpired) as exc:
            rows.append({"name": name, "status": "fail", "error": str(exc)})
            print(f"FAIL: {name}: {exc}", file=sys.stderr)
    report = {"checked_at": datetime.now(timezone.utc).isoformat(), "scope": "Offline arithmetic reproduction, record/provenance linkage and local archive/file integrity only; not source truth, clinical validation, host compatibility or live endpoint availability", "checks": rows}
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return int(any(row["status"] == "fail" for row in rows))


if __name__ == "__main__":
    sys.exit(main())
