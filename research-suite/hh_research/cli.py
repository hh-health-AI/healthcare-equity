"""CLI entry point. Clinical judgments are supplied by a researcher/host agent."""
import argparse
import json
import sys
from pathlib import Path
from . import evidence, trials, literature, catalysts, valuation, conference, data
from .common import ResearchError, load, write, require


def parser():
    ap = argparse.ArgumentParser(prog="hh-research", description=__doc__)
    sub = ap.add_subparsers(dest="command", required=True)
    for command in ("evidence", "trial", "claims", "literature", "rnpv", "conference", "journal-club"):
        p = sub.add_parser(command)
        p.add_argument("input", help="JSON packet; see examples and docs/input-contracts.md")
        p.add_argument("--out", help="Markdown output file, otherwise stdout")
        p.add_argument("--json-out", help="Structured output file")
    p = sub.add_parser("catalysts")
    p.add_argument("--before", required=True); p.add_argument("--after", required=True)
    p.add_argument("--out"); p.add_argument("--json-out")
    p = sub.add_parser("watch", help="Fetch a fixed NCT watchlist, compare and atomically save state")
    p.add_argument("--ids", nargs="+", required=True)
    p.add_argument("--state", required=True); p.add_argument("--out", required=True)
    p = sub.add_parser("data")
    ds = p.add_subparsers(dest="source", required=True)
    for source in ("trial", "trials", "pubmed", "fda", "cms-discover", "cms-sample"):
        p = ds.add_parser(source)
        p.add_argument("--out")
        if source == "trial":
            p.add_argument("--id", required=True)
        elif source in ("trials", "pubmed"):
            p.add_argument("--query", required=True); p.add_argument("--max-records", type=int, default=100)
        elif source == "fda":
            p.add_argument("--endpoint", choices=sorted(data.FDA_ENDPOINTS), required=True)
            p.add_argument("--search", required=True); p.add_argument("--max-records", type=int, default=100)
        elif source == "cms-discover":
            p.add_argument("--keyword", required=True)
        else:
            p.add_argument("--dataset-id", required=True); p.add_argument("--filters", default="{}", help="JSON object of exact field/value filters")
            p.add_argument("--max-records", type=int, default=100)
    return ap


def execute(a):
    if a.command == "data":
        if a.source == "trial":
            result = data.trial(a.id)
        elif a.source in ("trials", "pubmed"):
            result = getattr(data, a.source)(a.query, a.max_records)
        elif a.source == "fda":
            result = data.fda(a.endpoint, a.search, a.max_records)
        elif a.source == "cms-discover":
            result = data.cms_discover(a.keyword)
        else:
            result = data.cms_sample(a.dataset_id, json.loads(a.filters), a.max_records)
        if a.out:
            write(a.out, result)
        else:
            print(json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False))
        return 0
    if a.command == "watch":
        require(Path(a.state).resolve() != Path(a.out).resolve(), "State and report must use different paths")
        before = load(a.state) if Path(a.state).exists() else None
        after = data.watch_snapshot(a.ids)
        if before is None:
            report = "# Catalyst baseline established\n\nNo prior snapshot exists. No change inference has been made.\n"
        else:
            report = catalysts.diff(before, after)["markdown"]
        # Write the report before advancing state; failures preserve the baseline.
        write(a.out, report)
        write(a.state, after)
        print(f"Saved complete snapshot of {len(after['records'])} trials and report.")
        return 0
    if a.command == "catalysts":
        result = catalysts.diff(load(a.before), load(a.after))
    else:
        packet = load(a.input)
        if a.command in ("evidence", "claims", "journal-club"):
            result = {"markdown": evidence.render(packet, a.command), "validated_packet": packet}
        elif a.command == "trial":
            result = trials.compare(packet)
        elif a.command == "literature":
            result = literature.review(packet)
        elif a.command == "rnpv":
            result = valuation.calculate(packet)
            result["markdown"] = valuation.render(packet)
        else:
            result = conference.triage(packet)
    if a.out:
        write(a.out, result["markdown"])
    else:
        print(result["markdown"])
    if a.json_out:
        write(a.json_out, result)
    return 0


def main(argv=None):
    a = parser().parse_args(argv)
    try:
        return execute(a)
    except (ResearchError, ValueError, KeyError, TypeError, OSError) as exc:
        print(f"Research input/data error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
