import copy
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout, redirect_stderr
from pathlib import Path
from unittest.mock import patch
from hh_research import evidence, trials, literature, catalysts, valuation, conference, data, cli
from hh_research.common import ResearchError, load, write

ROOT = Path(__file__).resolve().parents[1]


def fixture(name):
    return load(ROOT / "examples" / name)


def registry(rid="NCT00000001"):
    return {"protocolSection": {"identificationModule": {"nctId": rid, "briefTitle": "Test"}, "statusModule": {"overallStatus": "RECRUITING"}}}


class FakeClient:
    def __init__(self, payloads):
        self.payloads = iter(payloads)
        self.calls = []

    def get(self, url, params=None, xml=False):
        self.calls.append((url, params, xml))
        return next(self.payloads), {"url": url, "retrieved_at": "2026-09-25T12:00:00Z", "response_sha256": "fixture"}


class EvidenceTests(unittest.TestCase):
    def test_valid_packet(self):
        self.assertEqual(len(evidence.validate(fixture("evidence.json"))), 2)

    def test_unresolved_citation(self):
        p = fixture("evidence.json"); p["claims"][0]["source_ids"] = ["missing"]
        with self.assertRaises(ResearchError): evidence.validate(p)

    def test_claim_requires_passage(self):
        p = fixture("evidence.json"); del p["sources"][0]["excerpt"]
        with self.assertRaises(ResearchError): evidence.validate(p)

    def test_retracted_only_support_rejected(self):
        p = fixture("evidence.json"); p["sources"][0]["status"] = "retracted"
        with self.assertRaises(ResearchError): evidence.validate(p)

    def test_uncited_unverifiable_is_allowed(self):
        p = fixture("evidence.json")
        p["claims"] = [{"id": "C", "text": "Unknown", "verdict": "unverifiable", "source_ids": [], "rationale": "Full text not accessible"}]
        evidence.validate(p)

    def test_synthetic_and_judgment_labels(self):
        text = evidence.render(fixture("evidence.json"))
        self.assertIn("SYNTHETIC", text); self.assertIn("supplied", text)

    def test_journal_club_eight_slides(self):
        self.assertEqual(evidence.render(fixture("evidence.json"), "journal-club").count("### Slide "), 8)


class TrialTests(unittest.TestCase):
    def test_endpoint_difference_and_missingness(self):
        r = trials.compare(fixture("trial.json"))
        f = {x["field"]: x["assessment"] for x in r["findings"]}
        self.assertTrue(f["primary_endpoints"].startswith("Difference"))
        self.assertTrue(f["analysis_population"].startswith("Missing"))
        self.assertIn("also differ", f["analysis_population"])
        self.assertIn("Not reported", f["population"])

    def test_mismatched_trial_rejected(self):
        p = fixture("trial.json"); p["documents"][1]["trial_id"] = "OTHER"
        with self.assertRaises(ResearchError): trials.compare(p)

    def test_registry_missing_fields_remain_missing(self):
        r = trials.normalize(registry())
        self.assertIsNone(r["sample_size"]); self.assertIsNone(r["primary_completion"])


class LiteratureTests(unittest.TestCase):
    def test_conflicting_screening_requires_adjudication(self):
        r = literature.deduplicate([{"id": "a", "title": "A", "doi": "x", "decision": "include"}, {"id": "b", "title": "B", "doi": "x", "decision": "exclude", "reason": "different reviewer"}])
        self.assertEqual(r["records"][0]["decision"], "uncertain")
        self.assertEqual(len(r["screening_conflicts"]), 1)

    def test_doi_normalization_and_title_candidates(self):
        r = literature.review(fixture("literature.json"))
        self.assertEqual(r["counts"]["duplicates_removed"], 1)
        self.assertEqual(r["counts"]["unique_records"], 4)
        self.assertEqual(len(r["title_matches_for_review"]), 1)

    def test_conflicting_identifiers_retained(self):
        r = literature.deduplicate([{"id": "a", "title": "A", "doi": "x", "pmid": "1"}, {"id": "b", "title": "B", "doi": "x", "pmid": "2"}])
        self.assertEqual(len(r["records"]), 2); self.assertEqual(len(r["identifier_conflicts"]), 1)

    def test_transitive_identifier_links(self):
        r = literature.deduplicate([{"id": "a", "title": "A", "doi": "x"}, {"id": "b", "title": "B", "pmid": "1"}, {"id": "c", "title": "C", "doi": "x", "pmid": "1"}])
        self.assertEqual(len(r["records"]), 1); self.assertEqual(len(r["duplicates"]), 2)

    def test_exclusion_requires_reason(self):
        p = fixture("literature.json"); del p["records"][2]["reason"]
        with self.assertRaises(ResearchError): literature.review(p)


class CatalystTests(unittest.TestCase):
    def test_estimated_month_precision_retained(self):
        r = catalysts.diff(fixture("snapshot-before.json"), fixture("snapshot-after.json"))
        self.assertEqual(len(r["changes"]), 2)
        self.assertIn("2027-06", r["markdown"]); self.assertNotIn("2027-06-01", r["markdown"])

    def test_incomplete_snapshot_rejected(self):
        p = fixture("snapshot-after.json"); p["complete"] = False
        with self.assertRaises(ResearchError): catalysts.diff(fixture("snapshot-before.json"), p)

    def test_changed_scope_rejected(self):
        p = fixture("snapshot-after.json"); p["scope"] = {"source": "different"}
        with self.assertRaises(ResearchError): catalysts.diff(fixture("snapshot-before.json"), p)

    def test_timezone_order_uses_instant(self):
        before = fixture("snapshot-before.json"); after = fixture("snapshot-after.json")
        before["as_of"] = "2026-09-25T12:00:00+00:00"
        after["as_of"] = "2026-09-25T09:00:00-04:00"
        catalysts.diff(before, after)

    def test_watch_failure_preserves_state(self):
        with tempfile.TemporaryDirectory() as td:
            state, report = Path(td) / "state.json", Path(td) / "report.md"
            write(state, fixture("snapshot-before.json")); original = state.read_bytes()
            with patch("hh_research.data.watch_snapshot", side_effect=ResearchError("Missing trial")), redirect_stderr(io.StringIO()):
                code = cli.main(["watch", "--ids", "NCT00000001", "--state", str(state), "--out", str(report)])
            self.assertEqual(code, 2); self.assertEqual(state.read_bytes(), original); self.assertFalse(report.exists())


class ValuationTests(unittest.TestCase):
    def test_missing_bridge_is_not_zero(self):
        p = self.packet(); del p["scenarios"][0]["debt"]
        s = valuation.calculate(p)["scenarios"][0]
        self.assertAlmostEqual(s["asset_rnpv"], 40)
        self.assertIsNone(s["equity_value"]); self.assertIsNone(s["value_per_share"])
        self.assertIn("debt", s["missing_bridge_fields"])

    def packet(self):
        return {"as_of": "2026-09-25", "currency": "USD", "units": "millions", "scenarios": [{"name": "test", "discount_rate": .1, "cash": 10, "debt": 2, "unallocated_overhead_pv": 1, "diluted_shares": 2, "cashflows": [{"year": 0, "kind": "development", "cashflow": -10, "probability": 1, "assumption": "committed"}, {"year": 1, "kind": "commercial", "cashflow": 110, "probability": .5, "assumption": "explicit"}]}]}

    def test_hand_calculated_pv_and_equity(self):
        s = valuation.calculate(self.packet())["scenarios"][0]
        self.assertAlmostEqual(s["asset_rnpv"], 40)
        self.assertAlmostEqual(s["equity_value"], 47)
        self.assertAlmostEqual(s["value_per_share"], 23.5)

    def test_probability_bounds(self):
        p = self.packet(); p["scenarios"][0]["cashflows"][0]["probability"] = 1.1
        with self.assertRaises(ResearchError): valuation.calculate(p)

    def test_nonfinite_rejected(self):
        p = self.packet(); p["scenarios"][0]["cashflows"][0]["cashflow"] = float("nan")
        with self.assertRaises(ResearchError): valuation.calculate(p)

    def test_zero_shares_rejected(self):
        p = self.packet(); p["scenarios"][0]["diluted_shares"] = 0
        with self.assertRaises(ResearchError): valuation.calculate(p)

    def test_bear_base_bull_order(self):
        values = [s["asset_rnpv"] for s in valuation.calculate(fixture("valuation.json"))["scenarios"]]
        self.assertEqual(values, sorted(values))


class ConferenceTests(unittest.TestCase):
    def test_future_material_withheld(self):
        r = conference.triage(fixture("conference.json"))
        self.assertEqual(len(r["public_records"]), 2); self.assertEqual(len(r["blocked"]), 1)
        self.assertNotIn("Future embargoed fictional material", r["markdown"])

    def test_same_trial_distinct_cohorts_not_combined(self):
        p = fixture("conference.json"); p["abstracts"][1]["cohort_id"] = "B"
        self.assertFalse(conference.triage(p)["cohort_groups"])

    def test_naive_embargo_timestamp_rejected(self):
        p = fixture("conference.json"); p["abstracts"][0]["public_at"] = "2026-09-20T12:00:00"
        with self.assertRaises(ResearchError): conference.triage(p)


class DataTests(unittest.TestCase):
    def test_trials_pagination_complete(self):
        c = FakeClient([{"studies": [registry()], "totalCount": 2, "nextPageToken": "next"}, {"studies": [registry("NCT00000002")], "totalCount": 2}])
        r = data.trials("test", 2, c)
        self.assertTrue(r["complete"]); self.assertEqual(len(c.calls), 2)

    def test_trial_cap_is_partial(self):
        c = FakeClient([{"studies": [registry()], "totalCount": 5, "nextPageToken": "next"}])
        self.assertFalse(data.trials("test", 1, c)["complete"])

    def test_trial_duplicate_page_rejected(self):
        c = FakeClient([{"studies": [registry()], "totalCount": 2, "nextPageToken": "next"}, {"studies": [registry()], "totalCount": 2}])
        with self.assertRaises(ResearchError): data.trials("test", 2, c)

    def test_changing_total_rejected(self):
        c = FakeClient([{"studies": [registry()], "totalCount": 2, "nextPageToken": "next"}, {"studies": [registry("NCT00000002")], "totalCount": 3}])
        with self.assertRaises(ResearchError): data.trials("test", 2, c)

    def test_exact_trial_identity_checked(self):
        with self.assertRaises(ResearchError): data.trial("NCT00000002", FakeClient([registry()]))

    def test_openfda_cap_disclosed(self):
        r = data.fda("drug/event", "test", 1, FakeClient([{"results": [{"id": "x"}], "meta": {"results": {"total": 20}}}]))
        self.assertFalse(r["complete"])

    def test_cms_short_sample_never_complete(self):
        r = data.cms_sample("00000000-0000-0000-0000-000000000000", max_records=10, client=FakeClient([[{"Product": "A"}]]))
        self.assertFalse(r["complete"]); self.assertIsNone(r["total_reported"])

    def test_cms_ignored_filter_rejected(self):
        with self.assertRaises(ResearchError): data.cms_sample("00000000-0000-0000-0000-000000000000", {"Product": "A"}, client=FakeClient([[{"Product": "B"}]]))

    def test_arbitrary_network_target_rejected(self):
        for url in ("http://clinicaltrials.gov/", "https://localhost/", "https://data.cms.gov.evil.test/", "https://user:secret@data.cms.gov/"):
            with self.assertRaises(ResearchError): data.check_url(url)

    def test_secrets_redacted(self):
        self.assertNotIn("secret", data.safe_url("https://api.fda.gov/drug/event.json?api_key=secret&search=test"))

    def test_pubmed_missing_fetch_records_rejected(self):
        c = FakeClient([{"esearchresult": {"count": "1", "idlist": ["123"]}}, "<PubmedArticleSet/>"])
        with self.assertRaises(ResearchError): data.pubmed("test", 1, c)


class CliTests(unittest.TestCase):
    def test_all_offline_commands(self):
        with tempfile.TemporaryDirectory() as td:
            for cmd, filename in [("evidence", "evidence.json"), ("claims", "evidence.json"), ("journal-club", "evidence.json"), ("trial", "trial.json"), ("literature", "literature.json"), ("rnpv", "valuation.json"), ("conference", "conference.json")]:
                out = Path(td) / f"{cmd}.md"
                self.assertEqual(cli.main([cmd, str(ROOT / "examples" / filename), "--out", str(out)]), 0)
                self.assertTrue(out.exists())


if __name__ == "__main__":
    unittest.main()
