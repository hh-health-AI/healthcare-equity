"""Validation, provenance and artifact utilities. No LLM calls or telemetry."""
import hashlib
import json
import math
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path


class ResearchError(ValueError):
    """An input or upstream response is insufficient for a reliable output."""


def utcnow():
    return datetime.now(timezone.utc).isoformat()


def require(condition, message):
    if not condition:
        raise ResearchError(message)


def number(value, field, low=None, high=None):
    require(isinstance(value, (int, float)) and not isinstance(value, bool), f"{field} must be numeric")
    require(math.isfinite(value), f"{field} must be finite")
    require(low is None or value >= low, f"{field} must be >= {low}")
    require(high is None or value <= high, f"{field} must be <= {high}")
    return float(value)


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f, parse_constant=lambda s: (_ for _ in ()).throw(ResearchError(f"Nonfinite JSON: {s}")))


def digest(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, ensure_ascii=False, allow_nan=False).encode()).hexdigest()


def write(path, value):
    """Atomic replacement avoids a half-written monitoring state on interruption."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    body = value if isinstance(value, str) else json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + "\n"
    name = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=p.parent, delete=False) as f:
            name = f.name
            f.write(body)
            f.flush()
            os.fsync(f.fileno())
        os.replace(name, p)
    finally:
        if name and os.path.exists(name):
            os.unlink(name)


def cell(value):
    if value is None:
        return "Not reported"
    if isinstance(value, (dict, list)):
        value = json.dumps(value, ensure_ascii=False, sort_keys=True)
    return str(value).replace("|", "\\|").replace("\n", " ").replace("<", "&lt;").replace(">", "&gt;")


def table(headers, rows):
    return "\n".join(["| " + " | ".join(map(cell, headers)) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"] + ["| " + " | ".join(map(cell, row)) + " |" for row in rows])


def report_header(title, obj):
    marker = "\n**SYNTHETIC DEMONSTRATION — not clinical or investment evidence.**\n" if obj.get("synthetic") else ""
    return f"# {title}\n{marker}\nGenerated: {utcnow()}\n\nInput SHA-256: `{digest(obj)}`\n\n"
