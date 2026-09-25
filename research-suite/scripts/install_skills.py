#!/usr/bin/env python3
"""Copy selected portable skills to an explicitly chosen host skills directory.

No default global location; existing directories are never overwritten.
"""
import argparse
import json
import shutil
from pathlib import Path


def main():
    root = Path(__file__).resolve().parents[1]
    catalog = json.loads((root / "catalog.json").read_text())
    available = {p["id"]: root / p["skill"] for p in catalog["projects"]}
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--target", type=Path, required=True, help="Your host's configured skills directory")
    p.add_argument("--skill", action="append", choices=sorted(available))
    p.add_argument("--all", action="store_true")
    a = p.parse_args()
    if bool(a.all) == bool(a.skill):
        p.error("Choose exactly one of --all or one/more --skill options")
    names = list(available) if a.all else list(dict.fromkeys(a.skill))
    for name in names:
        if (a.target / name).exists():
            p.error(f"Destination exists: {a.target / name}. Review and remove or choose a new directory.")
    a.target.mkdir(parents=True, exist_ok=True)
    for name in names:
        shutil.copytree(available[name], a.target / name)
        print(f"Copied {name} to {a.target / name}")


if __name__ == "__main__":
    main()
