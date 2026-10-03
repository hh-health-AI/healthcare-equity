"""Validate supplied appraisals and render traceable evidence, claim and journal-club reports.

This module does not infer truth or grade evidence automatically. A host agent or
reviewer supplies judgments; these functions enforce traceability and disclosure.
"""
from datetime import datetime
from urllib.parse import urlparse
from .common import require, table, report_header

VERDICTS = {"supported", "partially-supported", "unsupported", "contradicted", "unverifiable"}


def validate(packet):
    require(isinstance(packet, dict), "Evidence packet must be an object")
    require(bool(packet.get("question")), "question is required")
    sources = packet.get("sources", [])
    require(isinstance(sources, list), "sources must be a list")
    index = {}
    for s in sources:
        require(isinstance(s, dict), "Each source must be an object")
        for key in ("id", "title", "url", "retrieved_at", "vintage", "kind"):
            require(isinstance(s.get(key), str) and bool(s[key].strip()), f"Source {key} is required")
        require(s["id"] not in index, f"Duplicate source ID: {s['id']}")
        parsed = urlparse(s["url"])
        require(parsed.scheme in ("https", "http", "file") and bool(parsed.netloc or parsed.path), "Source URL must be HTTP(S) or a local file URI")
        try:
            stamp = datetime.fromisoformat(s["retrieved_at"].replace("Z", "+00:00"))
            require(stamp.tzinfo is not None, "retrieved_at must include timezone")
        except ValueError:
            raise ValueError("retrieved_at must be an ISO timestamp with timezone") from None
        index[s["id"]] = s
    claims = packet.get("claims", [])
    require(isinstance(claims, list) and bool(claims), "At least one claim is required")
    seen = set()
    for c in claims:
        require(isinstance(c, dict), "Each claim must be an object")
        require(bool(c.get("id")) and c["id"] not in seen, "Claim IDs must be present and unique")
        seen.add(c["id"])
        require(bool(c.get("text")), "Claim text is required")
        require(c.get("verdict") in VERDICTS, "Unknown claim verdict")
        require(bool(c.get("rationale")), "A reviewer rationale is required for every claim")
        refs = c.get("source_ids", [])
        require(isinstance(refs, list), "source_ids must be a list")
        require(all(ref in index for ref in refs), f"Unresolved citation in {c['id']}")
        if c["verdict"] in {"supported", "partially-supported", "contradicted"}:
            require(bool(refs), f"{c['verdict']} requires sources")
            for ref in refs:
                require(bool(index[ref].get("locator")), f"Source {ref} needs a page, section or record locator")
                require(bool(index[ref].get("excerpt")), f"Source {ref} needs a supporting/conflicting passage")
        if c["verdict"] == "supported":
            require(any(index[r].get("status", "unknown") != "retracted" for r in refs), "A supported claim cannot rely solely on retracted sources")
    return index


def render(packet, mode="evidence"):
    sources = validate(packet)
    titles = {"evidence": "Medical evidence brief", "claims": "Biomedical claim audit", "journal-club": "Journal club briefing"}
    out = report_header(titles[mode], packet)
    out += f"## Question\n\n{packet['question']}\n\n"
    out += "Judgments below were supplied by the researcher or host agent. Structural validation does not establish clinical validity.\n\n"
    out += table(["Claim", "Assessment", "Rationale", "Sources"], [[c["text"], c["verdict"], c["rationale"], ", ".join(c.get("source_ids", [])) or "None"] for c in packet["claims"]]) + "\n\n"
    out += "## Evidence and source passages\n\n"
    for key, s in sources.items():
        out += f"### {key}: {s['title']}\n\nSource: {s['url']}\n\nType: {s['kind']} · Vintage: {s['vintage']} · Retrieved: {s['retrieved_at']}\n\nLocator: {s.get('locator', 'Not supplied')}\n\nPassage: {s.get('excerpt', 'Not supplied')}\n\nStatus: {s.get('status', 'Retraction/correction status not checked')}\n\n"
    for field, label in (("methods", "Search and appraisal methods"), ("limitations", "Limitations"), ("open_questions", "Open questions"), ("model_impact", "Optional investment interpretation")):
        vals = packet.get(field, [])
        out += f"## {label}\n\n" + ("\n".join(f"- {x}" for x in vals) if vals else "Not supplied; do not infer completeness.") + "\n\n"
    if mode == "journal-club":
        out += "## Slide-ready discussion outline\n\n"
        sections = ["Clinical question and relevance", "Design, setting and eligibility", "Intervention and comparator", "Endpoints and analysis plan", "Effect sizes and uncertainty", "Harms and missing data", "Internal validity and applicability", "Conclusions and unresolved questions"]
        slides = packet.get("slides", {})
        for i, title in enumerate(sections, 1):
            out += f"### Slide {i}: {title}\n\n{slides.get(str(i), 'Not supplied. Extract from the primary materials before presentation.')}\n\n"
        out += "Discussion prompts: What changes the conclusion? How does the enrolled population differ from practice? Which missing result matters most?\n\n"
    out += "Clinical treatment decisions require qualified review. An evidence brief is not a treatment recommendation.\n"
    return out
