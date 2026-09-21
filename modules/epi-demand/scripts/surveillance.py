#!/usr/bin/env python3
"""Pull respiratory surveillance: Delphi Epidata (FluView) and CDC Socrata (wastewater).

Stdlib only, no key required for the endpoints used here.

Usage
-----
    python3 surveillance.py --fluview --regions nat --epiweeks 202540-202620
    python3 surveillance.py --wastewater --dataset 2ew6-ywp6 --limit 500

Weekly, provisional and revised. Laboratory and site participation change between
seasons: a step in the series that coincides with a participation change is not
epidemiology.
"""
import argparse, json, sys, urllib.parse, urllib.request

from _ua import user_agent

DELPHI = "https://api.delphi.cmu.edu/epidata/fluview/"
SOCRATA = "https://data.cdc.gov/resource/{ds}.json"
UA = user_agent("surveillance")


def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read().decode("utf-8"))


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--fluview", action="store_true")
    ap.add_argument("--regions", nargs="*", default=["nat"],
                    help="nat, hhs1..hhs10, cen1..cen9, or state abbreviations")
    ap.add_argument("--epiweeks", default="202001-202620",
                    help="epiweek range, e.g. 202540-202620")
    ap.add_argument("--wastewater", action="store_true")
    ap.add_argument("--dataset", default="2ew6-ywp6", help="data.cdc.gov resource id")
    ap.add_argument("--where", help="SoQL $where clause")
    ap.add_argument("--limit", type=int, default=1000)
    a = ap.parse_args()

    if a.fluview:
        q = urllib.parse.urlencode({"regions": ",".join(a.regions), "epiweeks": a.epiweeks})
        res = get(DELPHI + "?" + q)
        if res.get("result") != 1:
            sys.stderr.write(f"Delphi returned result={res.get('result')}: "
                             f"{res.get('message')}\n")
            sys.exit(2)
        json.dump({
            "source": "Delphi Epidata / CDC FluView",
            "epidata": res.get("epidata", []),
            "reading": [
                "Compare against the SAME WEEK in prior seasons, never week-on-week.",
                "Read percent positivity together with test volume: positivity up with "
                "tests down is mostly a testing artefact.",
                "wILI is outpatient visits for influenza-like illness, not confirmed flu.",
                "Provisional and revised -- state this in the vintage field.",
            ],
        }, sys.stdout, indent=2); print(); return

    if a.wastewater:
        params = {"$limit": str(a.limit)}
        if a.where:
            params["$where"] = a.where
        url = SOCRATA.format(ds=a.dataset) + "?" + urllib.parse.urlencode(params)
        rows = get(url)
        json.dump({
            "source": f"CDC data.cdc.gov resource {a.dataset}",
            "rows": rows,
            "reading": [
                "NWSS updates Fridays and the data are preliminary.",
                "Site participation changes between seasons -- check coverage before "
                "reading a level change as a wave.",
                "Wastewater leads clinical presentation, so it is a better early "
                "indicator for diagnostics than for hospital-facing products.",
            ],
        }, sys.stdout, indent=2); print(); return

    ap.error("--fluview or --wastewater required")


if __name__ == "__main__":
    main()
