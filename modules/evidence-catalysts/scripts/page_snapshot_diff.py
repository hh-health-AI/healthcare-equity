#!/usr/bin/env python3
"""Snapshot a public page and diff it against the previous snapshot.

For sources that publish through HTML rather than an API: USPSTF recommendation pages,
ACIP meeting pages, NCCN version notices, NICE appraisal pages, NMPA announcements.

Stdlib only.

Usage
-----
    python3 page_snapshot_diff.py --url https://example.gov/recommendation --label uspstf-lung
    python3 page_snapshot_diff.py --list
    python3 page_snapshot_diff.py --url ... --label ... --store ~/.desk-snapshots

Respect robots.txt and terms of use, and keep polling gentle -- daily is plenty for a
body that meets quarterly. This tool detects that a page CHANGED; a human still has to
read what changed and why.
"""
import argparse, datetime, difflib, hashlib, html.parser, json, os, re, sys, urllib.request

from _ua import user_agent


class Text(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "noscript"):
            self.skip += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript") and self.skip:
            self.skip -= 1

    def handle_data(self, data):
        if not self.skip:
            t = data.strip()
            if t:
                self.parts.append(t)


def extract(raw):
    p = Text()
    p.feed(raw)
    text = "\n".join(p.parts)
    return re.sub(r"\n{3,}", "\n\n", text)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--url")
    ap.add_argument("--label", help="short name for this watch target")
    ap.add_argument("--store", default=os.path.expanduser("~/.desk-snapshots"))
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--context", type=int, default=2)
    a = ap.parse_args()

    os.makedirs(a.store, exist_ok=True)
    index_path = os.path.join(a.store, "index.json")
    index = json.load(open(index_path)) if os.path.exists(index_path) else {}

    if a.list:
        json.dump(index, sys.stdout, indent=2); print(); return
    if not (a.url and a.label):
        ap.error("--url and --label required")

    req = urllib.request.Request(a.url, headers={**user_agent("page-snapshot-diff")})
    with urllib.request.urlopen(req, timeout=90) as r:
        raw = r.read().decode("utf-8", errors="replace")
    text = extract(raw)
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]

    path = os.path.join(a.store, f"{a.label}.txt")
    prev = open(path, encoding="utf-8").read() if os.path.exists(path) else None
    now = datetime.datetime.now().isoformat(timespec="seconds")

    if prev is None:
        open(path, "w", encoding="utf-8").write(text)
        index[a.label] = {"url": a.url, "first_seen": now, "last_checked": now, "hash": digest}
        json.dump(index, open(index_path, "w"), indent=2)
        json.dump({"label": a.label, "status": "baseline_stored", "chars": len(text),
                   "hash": digest}, sys.stdout, indent=2); print(); return

    if prev == text:
        index.setdefault(a.label, {}).update({"url": a.url, "last_checked": now, "hash": digest})
        json.dump(index, open(index_path, "w"), indent=2)
        json.dump({"label": a.label, "status": "unchanged", "last_checked": now},
                  sys.stdout, indent=2); print(); return

    diff = list(difflib.unified_diff(prev.splitlines(), text.splitlines(),
                                     fromfile="previous", tofile="current",
                                     n=a.context, lineterm=""))
    open(path, "w", encoding="utf-8").write(text)
    index.setdefault(a.label, {}).update({"url": a.url, "last_checked": now,
                                          "last_changed": now, "hash": digest})
    json.dump(index, open(index_path, "w"), indent=2)
    json.dump({
        "label": a.label, "url": a.url, "status": "CHANGED", "detected": now,
        "diff": diff[:400],
        "next_step": "A change was detected, not interpreted. Read the diff, confirm "
                     "against the body's own publication record, and only then write a "
                     "brief. Boilerplate and navigation changes are common false positives.",
    }, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
