"""Normalize registry records and compare explicitly extracted trial descriptions."""
from .common import require, table, report_header

FIELDS = ("primary_endpoints", "secondary_endpoints", "population", "sample_size", "analysis_population", "masking", "comparator", "follow_up", "primary_completion", "status")


def normalize(study):
    p = study.get("protocolSection", {})
    ident = p.get("identificationModule", {})
    require(bool(ident.get("nctId")), "Registry response lacks NCT identifier")
    design, status = p.get("designModule", {}), p.get("statusModule", {})
    return {
        "id": ident["nctId"], "title": ident.get("briefTitle"),
        "url": f"https://clinicaltrials.gov/study/{ident['nctId']}",
        "primary_endpoints": p.get("outcomesModule", {}).get("primaryOutcomes", []),
        "secondary_endpoints": p.get("outcomesModule", {}).get("secondaryOutcomes", []),
        "population": p.get("eligibilityModule", {}).get("eligibilityCriteria"),
        "sample_size": design.get("enrollmentInfo"),
        "analysis_population": None,
        "masking": design.get("designInfo", {}).get("maskingInfo"),
        "comparator": p.get("armsInterventionsModule", {}).get("armGroups", []),
        "follow_up": None, "primary_completion": status.get("primaryCompletionDateStruct"),
        "status": status.get("overallStatus"),
        "last_update_posted": status.get("lastUpdatePostDateStruct"),
        "has_results": study.get("hasResults", "resultsSection" in study),
    }


def compare(packet):
    require(packet.get("trial_id"), "trial_id is required")
    docs = packet.get("documents", [])
    require(len(docs) >= 2, "Supply at least two extracted documents")
    ids = set()
    for d in docs:
        for k in ("id", "kind", "url", "vintage", "fields"):
            require(bool(d.get(k)), f"Document {k} is required")
        require(d["id"] not in ids, "Document IDs must be unique")
        ids.add(d["id"])
        require(d.get("trial_id") == packet["trial_id"], "All documents must refer to the same trial")
        require(isinstance(d["fields"], dict), "Document fields must be an object")
    rows = []
    findings = []
    for field in FIELDS:
        values = [d["fields"].get(field) for d in docs]
        available = [v for v in values if v is not None]
        if not available:
            assessment = "Not reported in any supplied extraction"
        elif len(available) != len(docs):
            assessment = "Missing in at least one extraction"
            if any(v != available[0] for v in available):
                assessment += "; available extractions also differ"
        elif all(v == available[0] for v in available):
            assessment = "Matches as extracted"
        else:
            assessment = "Difference: inspect source wording and timing"
        rows.append([field, *values, assessment])
        findings.append({"field": field, "assessment": assessment, "values": dict(zip([d["id"] for d in docs], values))})
    return {"trial_id": packet["trial_id"], "findings": findings, "markdown": report_header("Clinical trial comparison", packet) + table(["Field", *[d["id"] for d in docs], "Assessment"], rows) + "\n\nDifferences are textual/structured discrepancies, not proof of outcome switching or misconduct. Establish the prespecified protocol and SAP versions, timing relative to unblinding, estimand, multiplicity plan, missing-data handling and source completeness. A nonsignificant result does not demonstrate equivalence. Cross-trial comparisons do not establish superiority.\n\n" + table(["Document", "Type", "Vintage", "Source"], [[d["id"], d["kind"], d["vintage"], d["url"]] for d in docs]) + "\n"}
