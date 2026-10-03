#!/usr/bin/env python3
"""Offline regression scorecard, including a deliberate semantic false-pass probe."""
import copy
import io
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tests'))
from hh_research import evidence, trials
import test_research


def evaluate():
    groups = {}
    for name in ('EvidenceTests', 'TrialTests', 'DataTests', 'ValuationTests'):
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(getattr(test_research, name))
        result = unittest.TextTestRunner(stream=io.StringIO()).run(suite)
        groups[name] = {'total': result.testsRun, 'passed': result.testsRun-len(result.failures)-len(result.errors)-len(result.skipped), 'failed': len(result.failures)+len(result.errors), 'skipped': len(result.skipped)}
    # New explicit field extraction check with expected values independent of normalization code.
    record = {'protocolSection': {
        'identificationModule': {'nctId': 'NCT00000099', 'briefTitle': 'SYNTHETIC audit'},
        'designModule': {'enrollmentInfo': {'count': 80, 'type': 'ACTUAL'}, 'designInfo': {'maskingInfo': {'masking': 'DOUBLE'}}},
        'outcomesModule': {'primaryOutcomes': [{'measure': 'Synthetic score', 'timeFrame': 'Week 12'}]},
        'statusModule': {'overallStatus': 'COMPLETED', 'primaryCompletionDateStruct': {'date': '2026-01', 'type': 'ACTUAL'}}}}
    expected = {'sample_size': {'count': 80, 'type': 'ACTUAL'}, 'masking': {'masking': 'DOUBLE'}, 'primary_endpoints': [{'measure': 'Synthetic score', 'timeFrame': 'Week 12'}], 'primary_completion': {'date': '2026-01', 'type': 'ACTUAL'}, 'analysis_population': None, 'follow_up': None}
    actual = trials.normalize(record)
    checks = {k: actual[k] == v for k,v in expected.items()}
    packet = json.loads((ROOT / 'examples/evidence.json').read_text())
    probe = copy.deepcopy(packet)
    probe['claims'] = [{'id': 'FALSE', 'text': 'The treatment reduced mortality by 90% and proved a survival benefit.', 'verdict': 'supported', 'source_ids': ['S1'], 'rationale': 'Deliberately wrong researcher judgment for a boundary test.'}]
    # Expected to pass schema validation despite an unsupported substantive assertion.
    evidence.validate(probe)
    return {'benchmark_version': 1, 'dataset': 'Small author-designed synthetic regression set; not held out or independently adjudicated', 'groups': groups, 'trial_field_exact_match': {'passed': sum(checks.values()), 'total': len(checks), 'fields': checks}, 'claim_entailment_probe': {'false_claims': 1, 'accepted_by_structural_validator': 1, 'interpretation': 'Known limitation: citation presence and valid schema do not establish claim support. Semantic accuracy is NOT MEASURED.'}, 'live_endpoint_accuracy': 'NOT_MEASURED', 'clinical_accuracy': 'NOT_MEASURED'}


if __name__ == '__main__':
    report = evaluate()
    print(json.dumps(report, indent=2))
    failed = any(g['failed'] for g in report['groups'].values()) or not all(report['trial_field_exact_match']['fields'].values())
    raise SystemExit(1 if failed else 0)
