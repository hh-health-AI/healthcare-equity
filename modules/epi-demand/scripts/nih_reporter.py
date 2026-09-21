#!/usr/bin/env python3
"""Query NIH RePORTER v2 for grant funding trends (life-science tools end market).

Stdlib only, no key.

Usage
-----
    python3 nih_reporter.py --fiscal-years 2022 2023 2024 2025 --activity-codes S10 --summarise
    python3 nih_reporter.py --fiscal-years 2024 2025 --text "single-cell" --summarise
    python3 nih_reporter.py --fiscal-years 2025 --institutes NCI NHGRI --limit 200

Activity codes that matter here:
  S10  shared instrumentation -- the cleanest open proxy for CAPITAL EQUIPMENT demand
  R01  investigator-initiated -- consumables and reagents
  P30 / U54  centre grants -- core facilities, the largest instrument buyers

RePORTER reports OBLIGATIONS (awards), not outlays. The demand effect spreads over the
grant period with a long, variable lag. Appropriations risk (continuing resolutions,
rescissions, indirect-cost policy) is NOT visible here and must be tracked separately.
"""
import argparse, collections, json, sys, urllib.request

from _ua import user_agent

URL = "https://api.reporter.nih.gov/v2/projects/search"


def post(payload):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(URL, data=data,
                                 headers={"Content-Type": "application/json",
                                          **user_agent("nih-reporter")})
    with urllib.request.urlopen(req, timeout=180) as r:
        return json.loads(r.read().decode("utf-8"))


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--fiscal-years", nargs="+", type=int, required=True)
    ap.add_argument("--activity-codes", nargs="*", default=[])
    ap.add_argument("--institutes", nargs="*", default=[], help="agency codes, e.g. NCI NIAID")
    ap.add_argument("--text", help="free-text search in title/abstract/terms")
    ap.add_argument("--limit", type=int, default=500, help="max records to pull (paged 500)")
    ap.add_argument("--summarise", action="store_true")
    a = ap.parse_args()

    criteria = {"fiscal_years": a.fiscal_years}
    if a.activity_codes:
        criteria["activity_codes"] = a.activity_codes
    if a.institutes:
        criteria["agencies"] = a.institutes
    if a.text:
        criteria["advanced_text_search"] = {"operator": "and", "search_field": "projecttitle,abstracttext,terms",
                                            "search_text": a.text}

    records, offset = [], 0
    while offset < a.limit:
        payload = {"criteria": criteria, "offset": offset,
                   "limit": min(500, a.limit - offset),
                   "include_fields": ["ProjectNum", "FiscalYear", "AwardAmount",
                                      "ActivityCode", "AgencyIcAdmin", "Organization",
                                      "ProjectTitle"]}
        res = post(payload)
        batch = res.get("results") or []
        records.extend(batch)
        if len(batch) < payload["limit"]:
            break
        offset += len(batch)

    if not records:
        sys.stderr.write("No records. Zero awards is a strong claim -- check the activity "
                         "code and fiscal years before reporting it.\n")
        sys.exit(2)

    if not a.summarise:
        json.dump(records, sys.stdout, indent=2); print(); return

    by_year_amt = collections.defaultdict(float)
    by_year_cnt = collections.Counter()
    by_ic = collections.defaultdict(float)
    by_org = collections.defaultdict(float)
    for r in records:
        fy = r.get("fiscal_year")
        amt = float(r.get("award_amount") or 0)
        by_year_amt[fy] += amt
        by_year_cnt[fy] += 1
        ic = ((r.get("agency_ic_admin") or {}) or {}).get("abbreviation") or "unknown"
        by_ic[ic] += amt
        org = ((r.get("organization") or {}) or {}).get("org_name") or "unknown"
        by_org[org] += amt

    years = sorted(by_year_amt)
    json.dump({
        "records": len(records),
        "by_fiscal_year": [{"fy": y, "award_usd": round(by_year_amt[y], 0),
                            "award_count": by_year_cnt[y],
                            "avg_award": round(by_year_amt[y] / by_year_cnt[y], 0)}
                           for y in years],
        "top_institutes": sorted(((k, round(v, 0)) for k, v in by_ic.items()),
                                 key=lambda x: -x[1])[:10],
        "top_organisations": sorted(((k, round(v, 0)) for k, v in by_org.items()),
                                    key=lambda x: -x[1])[:15],
        "reading": [
            "S10 instrument-grant counts falling year over year is one of the earliest "
            "open signals of an academic capital-equipment downturn.",
            "Rising dollars with flat award counts = larger grants to fewer labs, which "
            "favours high-end instrument vendors over broad-line consumables suppliers.",
            "Obligations, not outlays: spread the demand effect over the grant period.",
            "Apply the trend ONLY to the academic/government share of a tools company's "
            "revenue. Pharma and biotech end markets move on different cycles.",
            "Appropriations risk is invisible here. Track it separately.",
        ],
    }, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
