#!/usr/bin/env bash
# Sync this standalone repo from the canonical plugin copy in the suite monorepo.
#
# Usage:  scripts/sync-from-suite.sh /path/to/claude-healthcare-analyst-suite
#
# What it does:
#   1. Replaces the plugin content at this repo's root (skills/, agents/, references/,
#      CLAUDE.md, README.md, .mcp.json, .claude-plugin/plugin.json) with the suite's
#      plugins/procedure-exposure copy.
#   2. Re-inserts the standalone Installation section into README.md (the suite copy
#      doesn't carry it), using the <!-- standalone-install --> markers.
#   3. Copies the plugin version from plugin.json into .claude-plugin/marketplace.json
#      (marketplace version and the single plugin entry's version).
# It does NOT touch: LICENSE, CHANGELOG.md, .gitignore, scripts/, .git/.
# After running: update CHANGELOG.md by hand, then commit + tag (see README of the suite's docs/RELEASING.md).

set -euo pipefail

SUITE="${1:?usage: scripts/sync-from-suite.sh /path/to/claude-healthcare-analyst-suite}"
SRC="$SUITE/plugins/procedure-exposure"
REPO="$(cd "$(dirname "$0")/.." && pwd)"

[ -f "$SRC/.claude-plugin/plugin.json" ] || { echo "error: $SRC is not the plugin dir" >&2; exit 1; }

# 1. replace plugin content
for item in skills agents references CLAUDE.md README.md .mcp.json; do
  rm -rf "$REPO/${item:?}"
  cp -R "$SRC/$item" "$REPO/$item"
done
cp "$SRC/.claude-plugin/plugin.json" "$REPO/.claude-plugin/plugin.json"

# 2. re-insert the standalone Installation section before "## Setup"
python3 - "$REPO/README.md" <<'PY'
import sys, pathlib
p = pathlib.Path(sys.argv[1]); t = p.read_text()
SECTION = """<!-- standalone-install:start -->
## Installation

This standalone distribution is published as **HH-procedure-exposure**; the plugin inside keeps its suite id `procedure-exposure`. Two ways to install — **pick one**, not both (both distribute the same plugin under the same name):

**Standalone (this repo):**

```shell
/plugin marketplace add <your-github-username>/HH-procedure-exposure
/plugin install procedure-exposure@HH-procedure-exposure
```

**As part of the five-plugin suite (recommended if you want the full evidence→investable-view chain):**

```shell
/plugin marketplace add <your-github-username>/claude-healthcare-analyst-suite
/plugin install procedure-exposure@healthcare-analyst-suite
```

Updates: `/plugin marketplace update HH-procedure-exposure` (standalone) or `/plugin marketplace update healthcare-analyst-suite` (suite). If you switch sources later, uninstall the plugin first, then remove the old marketplace.
<!-- standalone-install:end -->

"""
if "standalone-install:start" not in t:
    assert t.count("\n## Setup\n") == 1, "README: expected exactly one '## Setup' header"
    t = t.replace("\n## Setup\n", "\n" + SECTION + "## Setup\n")
    p.write_text(t)
    print("README: installation section inserted")
else:
    print("README: installation section already present")
PY

# 3. sync versions marketplace.json <- plugin.json
python3 - "$REPO" <<'PY'
import sys, json, pathlib
repo = pathlib.Path(sys.argv[1])
ver = json.loads((repo/".claude-plugin/plugin.json").read_text())["version"]
mp = repo/".claude-plugin/marketplace.json"
m = json.loads(mp.read_text())
m["version"] = ver
m["plugins"][0]["version"] = ver
mp.write_text(json.dumps(m, indent=2, ensure_ascii=False) + "\n")
print(f"marketplace.json -> {ver}")
PY

echo "sync complete — review 'git status', update CHANGELOG.md, then commit and tag v$(python3 -c "import json;print(json.load(open('$REPO/.claude-plugin/plugin.json'))['version'])")"
