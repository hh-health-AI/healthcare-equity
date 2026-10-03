"""Conservative identifier deduplication and auditable screening counts."""
import re
from .common import require, table, report_header


def doi(value):
    return re.sub(r"^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)", "", str(value or "").strip(), flags=re.I).lower()


def deduplicate(records):
    require(isinstance(records, list), "records must be a list")
    groups, owners = [], {}
    seen = set()
    for r in records:
        require(isinstance(r, dict) and r.get("id") and r.get("title"), "Each record requires id and title")
        require(r["id"] not in seen, "Input record IDs must be unique; use import-specific IDs")
        seen.add(r["id"])
        keys = []
        if r.get("doi"):
            keys.append("doi:" + doi(r["doi"]))
        if r.get("pmid"):
            keys.append("pmid:" + str(r["pmid"]).strip())
        hits = {owners[k] for k in keys if k in owners}
        if hits:
            target = min(hits)
            for old in sorted(hits - {target}):
                groups[target].extend(groups[old]); groups[old] = []
                for key, group in list(owners.items()):
                    if group == old:
                        owners[key] = target
            groups[target].append(r)
        else:
            target = len(groups); groups.append([r])
        for k in keys:
            owners[k] = target
    kept, duplicates, conflicts, screening_conflicts = [], [], [], []
    for g in groups:
        if not g:
            continue
        ds = {doi(r["doi"]) for r in g if r.get("doi")}
        ps = {str(r["pmid"]).strip() for r in g if r.get("pmid")}
        if len(ds) > 1 or len(ps) > 1:
            kept.extend(g)
            conflicts.append({"ids": [r["id"] for r in g], "reason": "Conflicting identifiers; retain all pending review"})
        else:
            representative = dict(g[0])
            decisions = {r.get("decision") for r in g if r.get("decision") in {"include", "exclude"}}
            if len(decisions) > 1:
                representative["decision"] = "uncertain"
                representative["reason"] = "Duplicate records have conflicting include/exclude decisions; adjudication required"
                screening_conflicts.append({"ids": [r["id"] for r in g], "retained": g[0]["id"]})
            kept.append(representative)
            duplicates.extend({"removed": r["id"], "retained": g[0]["id"], "basis": "shared DOI/PMID", "record": r} for r in g[1:])
    titles = {}
    for r in kept:
        key = re.sub(r"\W+", "", r["title"].casefold())
        titles.setdefault(key, []).append(r["id"])
    candidates = [ids for ids in titles.values() if len(ids) > 1]
    return {"records": kept, "duplicates": duplicates, "identifier_conflicts": conflicts, "screening_conflicts": screening_conflicts, "title_matches_for_review": candidates}


def review(packet):
    result = deduplicate(packet.get("records", []))
    require(bool(packet.get("search_log")), "search_log is required, including databases, exact queries, dates and caps")
    counts = {"include": 0, "exclude": 0, "uncertain": 0, "unscreened": 0}
    for r in result["records"]:
        decision = r.get("decision", "unscreened")
        require(decision in counts, "Unknown screening decision")
        require(decision != "exclude" or bool(r.get("reason")), "Every exclusion needs a reason")
        counts[decision] += 1
    result["counts"] = {"imported": len(packet["records"]), "duplicates_removed": len(result["duplicates"]), "unique_records": len(result["records"]), **counts}
    result["markdown"] = report_header("Literature review worklist", packet) + table(["Metric", "Count"], result["counts"].items()) + "\n\n" + table(["Record", "Title", "Decision", "Reason"], [[r["id"], r["title"], r.get("decision", "unscreened"), r.get("reason", "Not supplied")] for r in result["records"]]) + "\n\nThese are record-level worklist counts, not a validated PRISMA flow diagram. Title matches and conflicting identifiers are retained for review. Multiple reports from one trial must be linked at study level before synthesis. A PubMed-only search is not a complete systematic review.\n\n## Search log\n\n" + table(["Field", "Value"], packet["search_log"].items()) + "\n"
    return result
