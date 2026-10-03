#!/usr/bin/env python3
"""Generate all offline sample reports without network calls or model credentials."""
import argparse
from pathlib import Path
from hh_research.cli import main as run
from hh_research.common import load, table, write


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--out", type=Path, default=Path("outputs/demo"))
    a = p.parse_args()
    root = Path(__file__).resolve().parents[1]
    for command, filename in (("evidence", "evidence.json"), ("trial", "trial.json"), ("claims", "evidence.json"), ("literature", "literature.json"), ("rnpv", "valuation.json"), ("conference", "conference.json"), ("journal-club", "evidence.json")):
        code = run([command, str(root / "examples" / filename), "--out", str(a.out / (command + ".md")), "--json-out", str(a.out / (command + ".json"))])
        if code:
            raise SystemExit(code)
    code = run(["catalysts", "--before", str(root / "examples/snapshot-before.json"), "--after", str(root / "examples/snapshot-after.json"), "--out", str(a.out / "catalysts.md"), "--json-out", str(a.out / "catalysts.json")])
    if code:
        raise SystemExit(code)
    d = load(root / "examples/data-sample.json")
    write(a.out / "public-data.md", "# Public data coverage example\n\n**SYNTHETIC DEMONSTRATION.**\n\n" + table(["Property", "Value"], [(k, d[k]) for k in ("source", "returned", "total_reported", "complete", "limitations")]) + "\n")
    print(f"Nine offline sample reports written to {a.out}")


if __name__ == "__main__":
    main()
