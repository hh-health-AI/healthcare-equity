#!/usr/bin/env python3
"""OpenAlex bibliometrics: publication trend, citation velocity and author ranking.

Stdlib only, no key. OpenAlex asks for a mailto in the query string for the polite
pool -- set OPENALEX_MAILTO.

Usage
-----
    python3 openalex_kol.py --concept "GLP-1 receptor agonist" --from-year 2016 --trend
    python3 openalex_kol.py --concept "spatial transcriptomics" --authors --top 25
"""
import argparse, collections, json, os, sys, urllib.parse, urllib.request

from _ua import user_agent

BASE = "https://api.openalex.org/works"


def get(url):
    req = urllib.request.Request(url, headers={**user_agent("openalex-kol")})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read().decode("utf-8"))


def build(concept, from_year, to_year, cursor, per_page=200, work_type=None):
    filters = [f"from_publication_date:{from_year}-01-01",
               f"to_publication_date:{to_year}-12-31"]
    if work_type:
        filters.append(f"type:{work_type}")
    params = {"search": concept, "filter": ",".join(filters),
              "per-page": str(per_page), "cursor": cursor}
    mail = os.environ.get("OPENALEX_MAILTO")
    if mail:
        params["mailto"] = mail
    return BASE + "?" + urllib.parse.urlencode(params)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--concept", required=True, help="target, mechanism, modality or platform")
    ap.add_argument("--from-year", type=int, default=2015)
    ap.add_argument("--to-year", type=int, default=2026)
    ap.add_argument("--max-works", type=int, default=2000)
    ap.add_argument("--trend", action="store_true")
    ap.add_argument("--authors", action="store_true")
    ap.add_argument("--top", type=int, default=20)
    a = ap.parse_args()

    works, cursor = [], "*"
    while len(works) < a.max_works and cursor:
        page = get(build(a.concept, a.from_year, a.to_year, cursor))
        works.extend(page.get("results") or [])
        cursor = (page.get("meta") or {}).get("next_cursor")
        if not page.get("results"):
            break

    if not works:
        sys.stderr.write("No works returned. Broaden the concept or check spelling.\n")
        sys.exit(2)

    by_year = collections.Counter()
    cites_by_year = collections.Counter()
    types = collections.Counter()
    authors = collections.Counter()
    last_authors = collections.Counter()
    insts = collections.Counter()

    for w in works:
        y = w.get("publication_year")
        by_year[y] += 1
        cites_by_year[y] += int(w.get("cited_by_count") or 0)
        types[w.get("type") or "unknown"] += 1
        auth = w.get("authorships") or []
        for i, au in enumerate(auth):
            name = ((au.get("author") or {}) or {}).get("display_name")
            if not name:
                continue
            weight = int(w.get("cited_by_count") or 0)
            if i == 0 or i == len(auth) - 1:
                authors[name] += weight
                if i == len(auth) - 1:
                    last_authors[name] += weight
            for inst in au.get("institutions") or []:
                if inst.get("display_name"):
                    insts[inst["display_name"]] += weight

    years = sorted(y for y in by_year if y)
    trend = [{"year": y, "works": by_year[y], "citations": cites_by_year[y],
              "citations_per_work": round(cites_by_year[y] / by_year[y], 2) if by_year[y] else 0}
             for y in years]

    accel = None
    if len(trend) >= 3:
        d1 = trend[-1]["works"] - trend[-2]["works"]
        d0 = trend[-2]["works"] - trend[-3]["works"]
        accel = d1 - d0

    out = {"concept": a.concept, "works_examined": len(works)}
    if a.trend or not a.authors:
        out.update({
            "trend": trend,
            "publication_acceleration_latest": accel,
            "work_types": types.most_common(),
            "reading": [
                "Acceleration matters more than volume: second derivative of works, plus "
                "citations per work in the first 24 months.",
                "Reviews rising faster than primary research = a field consolidating, "
                "often a late-stage signal.",
                "Citation counts lag publication by ~2 years -- structural, not timely.",
                "The most recent year is incomplete; do not read its decline as a trend.",
            ],
        })
    if a.authors:
        out.update({
            "top_first_or_last_authors_by_citations": authors.most_common(a.top),
            "top_senior_authors": last_authors.most_common(a.top),
            "top_institutions": insts.most_common(a.top),
            "author_reading": [
                "Rank on recent first/last authorship, not lifetime citations -- lifetime "
                "ranking just finds emeritus figures.",
                "Join this list to trial investigators (a catalyst engine) "
                "and to sites (a provider-adoption engine). Heavy overlap with one "
                "sponsor's network tells you whose science it is.",
                "Bibliometrics measure attention, not truth or commercial value.",
            ],
        })
    json.dump(out, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
