"""Filter public conference records and group cohorts without pooling outcomes."""
from datetime import datetime
from .common import require, report_header, table


def triage(packet):
    require(packet.get("as_of"), "as_of with timezone is required")
    now = datetime.fromisoformat(packet["as_of"].replace("Z", "+00:00"))
    require(now.tzinfo is not None, "as_of must include timezone")
    records, blocked, ids = [], [], set()
    for r in packet.get("abstracts", []):
        require(r.get("id") and r["id"] not in ids, "Abstract IDs must be unique")
        ids.add(r["id"])
        require(r.get("title") and r.get("source_url"), "Abstract title and source_url required")
        public = r.get("public_at")
        stamp = datetime.fromisoformat(public.replace("Z", "+00:00")) if public else None
        require(stamp is None or stamp.tzinfo is not None, "public_at must include timezone")
        if r.get("public") is not True or stamp is None or stamp > now:
            blocked.append({"id": r["id"], "reason": "Public availability not established as of the cutoff"})
            continue
        require(r.get("material_level") in {"title", "abstract", "poster", "presentation", "publication"}, "material_level required")
        records.append(r)
    cohorts = {}
    for r in records:
        # Shared trial ID alone does not identify the same cohort.
        key = (r.get("trial_id"), r.get("cohort_id"))
        if all(key):
            cohorts.setdefault(" / ".join(key), []).append(r["id"])
    out = {"public_records": records, "blocked": blocked, "cohort_groups": {k: v for k, v in cohorts.items() if len(v) > 1}}
    out["markdown"] = report_header("Conference evidence triage", packet) + table(["ID", "Title", "Material", "Trial/cohort", "What is new (supplied)", "Source"], [[r["id"], r["title"], r["material_level"], f"{r.get('trial_id', 'Unknown')} / {r.get('cohort_id', 'Unknown')}", r.get("new_evidence", "Not assessed"), r["source_url"]] for r in records]) + f"\n\nWithheld records: {len(blocked)}. Their content is excluded from this report.\n\n" + table(["Potential overlapping cohort", "Records"], out["cohort_groups"].items()) + "\n\nConfirm enrollment dates, cohort identifiers and data cutoffs before linking reports. Title-only material cannot support efficacy or safety conclusions. Abstract-to-poster changes need full source verification. Do not pool overlapping patients.\n"
    return out
