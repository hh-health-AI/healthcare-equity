#!/usr/bin/env python3
"""Validate catalog, portable skill metadata, local links and example artifacts."""
import ast
import json
import re
from pathlib import Path
import yaml


def main():
    root = Path(__file__).resolve().parents[1]
    catalog = json.loads((root / "catalog.json").read_text())
    assert len(catalog["projects"]) == 9, "Expected nine projects"
    ids = [p["id"] for p in catalog["projects"]]
    assert len(set(ids)) == 9
    for project in catalog["projects"]:
        skill = root / project["skill"]
        text = (skill / "SKILL.md").read_text()
        fields = yaml.safe_load(text.split("---", 2)[1])
        assert set(fields) == {"name", "description"}, skill
        assert fields["name"] == project["id"] and len(fields["name"]) < 64
        assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", fields["name"])
        assert len(text.splitlines()) < 500
        assert len(fields["description"]) > 50
        meta = yaml.safe_load((skill / "agents/openai.yaml").read_text())["interface"]
        assert 25 <= len(meta["short_description"]) <= 64
        assert "$" + project["id"] in meta["default_prompt"]
        assert (root / project["agent"]).is_file()
        assert (root / project["guide"]).is_file()
    for path in list((root / "hh_research").glob("*.py")) + list((root / "scripts").glob("*.py")):
        ast.parse(path.read_text(), filename=str(path))
    for path in root.rglob("*.md"):
        if any(x in path.parts for x in (".venv", "build", "outputs")):
            continue
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", path.read_text()):
            if re.match(r"(?:[a-z]+:|#)", target):
                continue
            local = target.split("#", 1)[0]
            if local:
                assert (path.parent / local).exists(), f"Broken link in {path}: {target}"
    for name in ("evidence", "trial", "claims", "catalysts", "literature", "public-data", "rnpv", "conference", "journal-club"):
        p = root / "examples/outputs" / f"{name}.md"
        assert p.exists() and "SYNTHETIC" in p.read_text(), f"Missing/labeled example {p}"
    print("PASS: nine catalog projects; nine portable skills and metadata; Python syntax; local documentation links; nine labeled sample reports")


if __name__ == "__main__":
    main()
