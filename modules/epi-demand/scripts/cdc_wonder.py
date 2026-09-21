#!/usr/bin/env python3
"""Query CDC WONDER via its XML POST API (no authentication required).

Stdlib only.

Usage
-----
    python3 cdc_wonder.py --database D76 --measure deaths \
        --group-by D76.V1-level1 --icd-starts C50 --years 2018 2019 2020

Databases: D76 = Underlying Cause of Death (1999+), D77 = Multiple Cause,
D66 = Natality. Confirm parameter codes against the WONDER documentation for the
database you use -- WONDER's parameter names are database-specific and change.

The API is NATIONAL ONLY. State, county, MSA, census-region and urbanisation
variables are blocked server-side by CDC even though the web interface offers them.
This script rejects them up front rather than letting CDC return an opaque permissions
error -- use CDC PLACES or the Delphi Epidata API for sub-national work.

Counts below 10 are returned suppressed. Never sum suppressed cells: the sum of a
suppressed set is not zero, and treating it as zero manufactures a clean trend.
"""
import argparse, json, sys, urllib.request, xml.etree.ElementTree as ET

from _ua import user_agent

URL = "https://wonder.cdc.gov/controller/datarequest/{db}"

# CDC enforces national-only access through the API. These variables exist in the web
# interface but are rejected server-side for API callers, and the resulting error is an
# opaque permissions message rather than anything that names the real cause. Reject them
# here so the failure is legible.
GEOGRAPHY_VARS = {
    "D76.V9": "State", "D76.V10": "County", "D76.V27": "Census Region",
    "D76.V19": "Urbanization (2013)", "D76.V11": "Urbanization (2006)",
    "D77.V9": "State", "D77.V10": "County", "D77.V27": "Census Region",
    "D66.V9": "State", "D66.V10": "County", "D66.V27": "Census Region",
}

SUBNATIONAL_ADVICE = (
    "CDC WONDER's API is national-only; sub-national grouping and filtering are "
    "blocked server-side, not by this script. For sub-national demand work use CDC "
    "PLACES (county and place health indicators) or the Delphi Epidata API. If you "
    "need this exact WONDER cut, run it in the web interface and transcribe the "
    "result with its own citation and access date."
)


def check_national_only(codes, kind):
    """Raise on any geography variable, whichever suffix form was passed."""
    bad = []
    for c in codes:
        base = str(c).split("-")[0]
        if base in GEOGRAPHY_VARS:
            bad.append(f"{c} ({GEOGRAPHY_VARS[base]})")
    if bad:
        raise SystemExit(
            f"error: sub-national {kind} rejected: {', '.join(bad)}\n\n"
            + SUBNATIONAL_ADVICE
        )


def build_request(params):
    root = ET.Element("request-parameters")
    def add(name, values):
        p = ET.SubElement(root, "parameter")
        ET.SubElement(p, "name").text = name
        for v in (values if isinstance(values, list) else [values]):
            ET.SubElement(p, "value").text = str(v)
    add("accept_datause_restrictions", "true")
    for k, v in params.items():
        add(k, v)
    return ET.tostring(root, encoding="utf-8")


def parse_response(xml_bytes):
    root = ET.fromstring(xml_bytes)
    rows = []
    for r in root.iter("r"):
        rows.append([c.findtext("l") or c.findtext("v") or "" for c in r.findall("c")])
    if not rows:
        msgs = [m.text for m in root.iter("message") if m.text]
        return {"rows": [], "messages": msgs or ["No rows and no message returned."]}
    return {"rows": rows}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--database", default="D76")
    ap.add_argument("--group-by", nargs="*", default=["D76.V1-level1"],
                    help="B_1..B_5 group-by codes for the chosen database")
    ap.add_argument("--measure", nargs="*", default=["D76.M1", "D76.M2", "D76.M3"],
                    help="M_1.. measures: deaths, population, crude rate")
    ap.add_argument("--icd-starts", nargs="*", default=[],
                    help="ICD-10 codes or prefixes for the underlying cause filter")
    ap.add_argument("--years", nargs="*", default=[])
    ap.add_argument("--filter-vars", nargs="*", default=[],
                    help="additional F_/V_ variable codes you intend to filter on; "
                         "checked against the national-only restriction before sending")
    ap.add_argument("--raw", action="store_true", help="print the raw XML response")
    a = ap.parse_args()

    check_national_only(a.group_by, "group-by")
    check_national_only(a.filter_vars, "filter")

    params = {}
    for i, g in enumerate(a.group_by, start=1):
        params[f"B_{i}"] = g
    for i, m in enumerate(a.measure, start=1):
        params[f"M_{i}"] = m
    if a.icd_starts:
        params["F_D76.V2"] = a.icd_starts
        params["V_D76.V2"] = a.icd_starts
    if a.years:
        params["F_D76.V1"] = a.years

    body = build_request(params)
    req = urllib.request.Request(URL.format(db=a.database), data=body,
                                 headers={"Content-Type": "application/xml",
                                          **user_agent("cdc-wonder")})
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            raw = r.read()
    except Exception as e:  # noqa: BLE001
        sys.stderr.write(f"WONDER request failed: {e}\nWONDER parameter names are "
                         "database-specific. Check the docs for the database and, if "
                         "the API refuses a sub-national query, use the web interface "
                         "and transcribe with its own citation.\n")
        sys.exit(3)

    if a.raw:
        sys.stdout.write(raw.decode("utf-8", errors="replace")); return
    out = parse_response(raw)
    out["source"] = f"CDC WONDER {a.database}"
    out["caveats"] = ["National-level only: CDC blocks sub-national grouping via the API.",
                      "Cells below 10 are suppressed. Do not sum suppressed cells.",
                      "Small cells are suppressed; unreliable rates are flagged by WONDER.",
                      "Sub-national queries are restricted through the API.",
                      "Mortality is not incidence -- do not use a death count as a "
                      "patient population without a survival adjustment."]
    json.dump(out, sys.stdout, indent=2); print()


if __name__ == "__main__":
    main()
