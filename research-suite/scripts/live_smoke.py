#!/usr/bin/env python3
"""Small opt-in live API checks; no clinical inference or population claims."""
import argparse
import json
from hh_research import data
from hh_research.common import utcnow, write, require


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--out", required=True)
    a = p.parse_args()
    checks = []
    for name, fn in [
        ("exact_trial", lambda: data.trial("NCT04280705")),
        ("capped_trial_search", lambda: data.trials("diabetes", 2)),
        ("pubmed_exact_pmid", lambda: data.pubmed("32445440[uid]", 1)),
        ("capped_pubmed_search", lambda: data.pubmed("remdesivir", 2)),
        ("openfda_label", lambda: data.fda("drug/label", 'openfda.generic_name:"semaglutide"', 2)),
        ("cms_catalog", lambda: data.cms_discover("Medicare Part D Prescribers - by Provider and Drug")),
    ]:
        try:
            result = fn()
            require(result["returned"] > 0, "Expected a representative positive result")
            if name.startswith("capped_"):
                require(result["complete"] is False and result["total_reported"] > result["returned"], "Cap should be disclosed")
            checks.append({"name": name, "status": "pass", "returned": result["returned"], "total_reported": result["total_reported"], "complete": result["complete"], "provenance": result["provenance"]})
            if name == "cms_catalog":
                candidate = result["records"][0]
                sample = data.cms_sample(candidate["dataset_id"], max_records=2)
                require(sample["complete"] is False and sample["returned"] == 2, "CMS sample must remain incomplete")
                checks.append({"name": "cms_sample", "status": "pass", "returned": sample["returned"], "complete": sample["complete"], "dataset": candidate, "provenance": sample["provenance"]})
        except Exception as e:
            checks.append({"name": name, "status": "fail", "error": f"{type(e).__name__}: {e}"})
    report = {"run_at": utcnow(), "scope": "Representative endpoint/coverage checks only; not exhaustive validation or clinical accuracy evaluation", "checks": checks}
    write(a.out, report)
    print(json.dumps({"pass": sum(c["status"] == "pass" for c in checks), "fail": sum(c["status"] == "fail" for c in checks), "report": a.out}))
    if any(c["status"] == "fail" for c in checks):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
