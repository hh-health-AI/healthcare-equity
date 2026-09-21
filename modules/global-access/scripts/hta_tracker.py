#!/usr/bin/env python3
"""Watch-target registry for international HTA, pricing and approval sources.

These bodies publish through HTML, not APIs, so the workflow is snapshot-and-diff.
This script keeps the registry of what to watch and shells out to page_snapshot_diff.py.

Usage
-----
    python3 hta_tracker.py --list-sources
    python3 hta_tracker.py --calendar
    python3 hta_tracker.py --add-target --label nice-ta-xyz --url https://...
    python3 hta_tracker.py --check-all

Add the specific appraisal, assessment or announcement pages for the assets the desk
actually covers -- the generic landing pages change constantly and generate noise.
"""
import argparse, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REG = os.path.expanduser("~/.desk-snapshots/hta-targets.json")

SOURCES = {
    "EMA CHMP monthly highlights": "Timely source for opinions; the EPAR follows later.",
    "NICE technology appraisals": "Search nice.org.uk DIRECTLY -- HTA aggregators miss a "
                                  "large share of NICE output.",
    "G-BA benefit assessments / IQWiG": "The benefit CATEGORY is the financial event, not "
                                        "the approval. Drives the AMNOG negotiation.",
    "HAS transparency committee": "SMR sets the reimbursement rate, ASMR the price premium.",
    "Scottish SMC": "Faster than NICE; sometimes a leading indicator.",
    "Japan MHLW / Chuikyo": "NHI listing, premium categories, scheduled revisions and "
                            "overshoot repricing. Primary sources are in Japanese.",
    "PMDA": "Japanese approvals.",
    "China NMPA / CDE": "Approvals, breakthrough designations, IND acceptances. Chinese.",
    "China NHSA / NRDL results": "Annual negotiation, announced late in the year, "
                                 "effective the following January.",
    "chinadrugtrials.org.cn": "Chinese trial registry.",
}

CALENDAR = [
    ("CHMP meeting highlights", "monthly", "EU opinions"),
    ("NICE appraisal committee dates", "rolling; check the published programme", "UK access"),
    ("G-BA decisions", "published on a regular schedule", "German price negotiation input"),
    ("HAS transparency committee opinions", "rolling", "French rate and premium"),
    ("Japan NHI price revision", "on the MHLW revision cycle; direction is down", "Japan price"),
    ("Chuikyo deliberations", "regular meetings, materials published", "Japan system changes"),
    ("China NRDL negotiation", "annual, concluding late in the year, effective January", "China price/volume"),
    ("China VBP tenders", "periodic by category", "Mature portfolio and medtech risk"),
]


def load():
    return json.load(open(REG)) if os.path.exists(REG) else {}


def save(d):
    os.makedirs(os.path.dirname(REG), exist_ok=True)
    json.dump(d, open(REG, "w"), indent=2)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--list-sources", action="store_true")
    ap.add_argument("--calendar", action="store_true")
    ap.add_argument("--add-target", action="store_true")
    ap.add_argument("--label")
    ap.add_argument("--url")
    ap.add_argument("--check-all", action="store_true")
    a = ap.parse_args()

    if a.list_sources:
        json.dump(SOURCES, sys.stdout, indent=2); print(); return
    if a.calendar:
        json.dump([{"event": e, "cadence": c, "moves": m} for e, c, m in CALENDAR],
                  sys.stdout, indent=2); print(); return

    reg = load()
    if a.add_target:
        if not (a.label and a.url):
            ap.error("--label and --url required with --add-target")
        reg[a.label] = a.url
        save(reg)
        json.dump({"added": a.label, "url": a.url, "targets": len(reg)},
                  sys.stdout, indent=2); print(); return

    if a.check_all:
        if not reg:
            sys.stderr.write("No targets registered. Add the specific appraisal or "
                             "announcement pages for covered assets with --add-target.\n")
            sys.exit(2)
        out = []
        for label, url in reg.items():
            r = subprocess.run([sys.executable, os.path.join(HERE, "page_snapshot_diff.py"),
                                "--url", url, "--label", label],
                               capture_output=True, text=True)
            try:
                out.append(json.loads(r.stdout))
            except json.JSONDecodeError:
                out.append({"label": label, "error": r.stderr.strip()[:400]})
        json.dump({"checked": len(out), "results": out,
                   "next_step": "A detected change is not an interpreted change. Read each "
                                "diff, confirm against the body's own publication record, "
                                "then write the brief."},
                  sys.stdout, indent=2); print(); return

    ap.error("pick --list-sources / --calendar / --add-target / --check-all")


if __name__ == "__main__":
    main()
