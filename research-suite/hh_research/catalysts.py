"""Snapshot comparison with scope and completeness gates."""
from datetime import datetime
from .common import require, table, report_header


def validate(snapshot):
    require(snapshot.get("complete") is True, "Incomplete snapshot: do not compare or advance state")
    require(bool(snapshot.get("scope")) and bool(snapshot.get("as_of")), "Snapshot scope and as_of are required")
    timestamp = datetime.fromisoformat(snapshot["as_of"].replace("Z", "+00:00"))
    require(timestamp.tzinfo is not None, "Snapshot as_of must include timezone")
    require(isinstance(snapshot.get("records"), list) and snapshot["records"], "Snapshot has no records; cannot infer absence")
    index = {}
    for record in snapshot["records"]:
        require(record.get("id") and record["id"] not in index, "Snapshot IDs must be unique")
        index[record["id"]] = record
    return index


def diff(before, after):
    old, new = validate(before), validate(after)
    require(before["scope"] == after["scope"], "Snapshot scopes differ; establish a new baseline explicitly")
    require(datetime.fromisoformat(before["as_of"].replace("Z", "+00:00")) < datetime.fromisoformat(after["as_of"].replace("Z", "+00:00")), "after.as_of must be later than before.as_of")
    require(set(old) == set(new), "Watchlist membership changed; rebaseline rather than imply disappearance")
    ignored = {"retrieved_at", "last_update_posted", "raw_sha256"}
    changes = []
    for rid in sorted(new):
        for field in sorted((set(old[rid]) | set(new[rid])) - ignored - {"id"}):
            a, b = old[rid].get(field), new[rid].get(field)
            if a != b:
                changes.append({"id": rid, "field": field, "before": a, "after": b, "source": new[rid].get("url")})
    out = {"changes": changes, "before_as_of": before["as_of"], "after_as_of": after["as_of"], "scope": after["scope"]}
    out["markdown"] = report_header("Biotech catalyst changes", after) + table(["Trial", "Field", "Before", "After", "Source"], [[x[k] for k in ("id", "field", "before", "after", "source")] for x in changes]) + "\n\n" + ("No changes in compared fields. " if not changes else "") + "Registry updates can lag. Primary completion is not the date results will be released. Estimated month/quarter dates must retain their precision; FDA decision dates require separate authoritative or clearly attributed sponsor sources.\n"
    return out
