#!/usr/bin/env python3
"""Check frozen module and adapted-plugin provenance without rewriting a baseline.

Offline mode validates recorded local bytes and manifest identity. Optional
upstream modes compare Git blob inventories; they do not download or import
changed source files. Only Python's standard library is required.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import urllib.error
import urllib.request


IGNORED_PARTS = {".git", "__pycache__", ".venv", ".pytest_cache", ".mypy_cache"}
HEX40 = re.compile(r"[0-9a-f]{40}\Z")
HEX64 = re.compile(r"[0-9a-f]{64}\Z")


def hashes(data: bytes) -> tuple[str, str]:
    return (hashlib.sha256(data).hexdigest(),
            hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest())


def inventory(directory: Path) -> dict[str, Path]:
    if not directory.is_dir():
        return {}
    return {
        file.relative_to(directory).as_posix(): file
        for file in directory.rglob("*")
        if (file.is_file() or file.is_symlink())
        and not set(file.relative_to(directory).parts) & IGNORED_PARTS
        and file.suffix not in {".pyc", ".pyo"}
    }


def safe_path(root: Path, relative: str) -> Path:
    path = PurePosixPath(relative)
    if path.is_absolute() or ".." in path.parts or not path.parts:
        raise ValueError(f"invalid relative path: {relative}")
    target = root.joinpath(*path.parts)
    if not target.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"path escapes repository: {relative}")
    return target


def check_repository(root: Path, *, upstream_dir: Path | None = None,
                     live_upstream: bool = False) -> dict:
    root = root.resolve()
    failures, notes = [], []

    def issue(code: str, path: str, message: str, *, note: bool = False) -> None:
        (notes if note else failures).append({"code": code, "path": path, "message": message})

    def read_json(path: str) -> dict:
        return json.loads(safe_path(root, path).read_text(encoding="utf-8"))

    def check_file(path: str, expected: str, code: str) -> None:
        file = safe_path(root, path)
        if file.is_symlink():
            issue(code, path, "Symlinks are not covered by the frozen byte manifest.")
        elif not file.is_file():
            issue(code, path, "Recorded file is missing.")
        elif not HEX64.fullmatch(expected) or hashes(file.read_bytes())[0] != expected:
            issue(code, path, "Bytes differ from the reviewed SHA-256; review the diff before updating provenance.")

    try:
        module_map = read_json("provenance/module-snapshots.json")
        plugin_map = read_json("provenance/plugin-source-map.json")
        if module_map.get("schema_version") != 1 or plugin_map.get("schema_version") != 1:
            raise ValueError("unsupported provenance schema")
        modules = module_map["modules"]
        names = [module["name"] for module in modules]
        if len(set(names)) != len(names) or len(names) != module_map["module_count_expected"]:
            raise ValueError("module count or duplicate name mismatch")
        actual_modules = {path.name for path in (root / "modules").iterdir() if path.is_dir()}
        if set(names) != actual_modules:
            issue("MODULE_INVENTORY_CHANGED", "modules", f"Recorded {sorted(names)}; found {sorted(actual_modules)}.")
        for path in (root / "modules").iterdir():
            if not path.is_dir() or path.is_symlink():
                issue("UNRECORDED_MODULE_ROOT_FILE", f"modules/{path.name}",
                      "Only recorded module directories are covered; loose files and symlinks need explicit provenance.")
        for module in modules:
            name, files = module["name"], module["files"]
            if not HEX40.fullmatch(module["upstream_commit"]):
                raise ValueError(f"invalid upstream commit for {name}")
            seen = set()
            for file in files:
                path = file["path"]
                safe_path(root / "modules" / name, path)
                if path in seen:
                    raise ValueError(f"duplicate module entry: {name}/{path}")
                seen.add(path)
                local_hash, upstream_hash = file["bundled_sha256"], file["upstream_sha256"]
                posture = file["comparison"]
                if upstream_hash is not None and (not HEX64.fullmatch(upstream_hash)
                        or not HEX40.fullmatch(file["upstream_git_blob_sha"])):
                    raise ValueError(f"invalid upstream fingerprint: {name}/{path}")
                if posture == "identical":
                    if local_hash is None or local_hash != upstream_hash:
                        raise ValueError(f"false identical declaration: {name}/{path}")
                elif posture in {"documented-adaptation", "upstream-file-omitted"}:
                    if not file.get("difference_reason"):
                        raise ValueError(f"undocumented difference: {name}/{path}")
                    if posture == "documented-adaptation" and (local_hash is None or local_hash == upstream_hash):
                        raise ValueError(f"invalid adaptation: {name}/{path}")
                    if posture == "upstream-file-omitted" and (local_hash is not None or upstream_hash is None):
                        raise ValueError(f"invalid omission: {name}/{path}")
                    issue("RECORDED_MODULE_DIFFERENCE", f"modules/{name}/{path}",
                          file["difference_reason"], note=True)
                else:
                    issue("UNREVIEWED_MODULE_DIFFERENCE", f"modules/{name}/{path}", f"Unsupported comparison posture: {posture}.")
                if local_hash is not None:
                    check_file(f"modules/{name}/{path}", local_hash, "BUNDLED_MODULE_CHANGED")
                    bundled_path = safe_path(root, f"modules/{name}/{path}")
                    if posture == "identical" and bundled_path.is_file() and not bundled_path.is_symlink():
                        if hashes(bundled_path.read_bytes())[1] != file["upstream_git_blob_sha"]:
                            issue("MODULE_BLOB_DIFFERENCE", f"modules/{name}/{path}",
                                  "Local Git blob differs from the claimed identical upstream blob.")
            expected = {file["path"] for file in files if file["bundled_sha256"] is not None}
            actual = inventory(root / "modules" / name)
            for path in sorted(set(actual) - expected):
                issue("UNRECORDED_MODULE_FILE", f"modules/{name}/{path}", "New bundled file has no reviewed upstream relationship.")
            if upstream_dir is not None or live_upstream:
                compare_upstream(module, upstream_dir, live_upstream, issue)

        package = plugin_map["package_path"]
        package_directory = safe_path(root, package)
        package_inventory = inventory(package_directory)
        for path, file in package_inventory.items():
            if file.is_symlink():
                issue("PLUGIN_SYMLINK_UNSUPPORTED", f"{package}/{path}",
                      "The workflow package supports regular files only; symlinks are outside the reviewed scope.")
        package_files = set(package_inventory)
        expected_package_files = set(plugin_map["package_file_inventory"])
        for path in sorted(package_files - expected_package_files):
            issue("UNRECORDED_PACKAGE_FILE", f"{package}/{path}", "New package file is outside the reviewed workflow edition.")
        for path in sorted(expected_package_files - package_files):
            issue("RECORDED_PACKAGE_FILE_MISSING", f"{package}/{path}", "Recorded package file is missing.")
        inventory_source_paths = set()
        for scope in plugin_map["source_skill_inventory"]:
            directory = safe_path(root, scope["root"])
            actual = {file.relative_to(root).as_posix() for file in directory.glob("*/SKILL.md")}
            expected = set(scope["paths"])
            inventory_source_paths.update(expected)
            if actual != expected:
                issue("CANONICAL_SKILL_INVENTORY_CHANGED", scope["root"],
                      f"Added {sorted(actual - expected)}; removed {sorted(expected - actual)}. Review plugin routing/source relationships.")
        source_paths = set()
        for source in plugin_map["sources"]:
            path = source["path"]
            if path in source_paths:
                raise ValueError(f"duplicate plugin source: {path}")
            source_paths.add(path)
            check_file(path, source["frozen_sha256"], "PLUGIN_SOURCE_CHANGED")
            if not HEX40.fullmatch(source["packaged_source_git_blob_sha"]) or not HEX40.fullmatch(source["frozen_git_blob_sha"]):
                raise ValueError(f"invalid packaging source blob: {path}")
            source_file = safe_path(root, path)
            if source_file.is_file() and not source_file.is_symlink():
                sha256, git_blob = hashes(source_file.read_bytes())
                if sha256 == source["frozen_sha256"] and git_blob != source["frozen_git_blob_sha"]:
                    issue("PLUGIN_SOURCE_BLOB_INCONSISTENT", path,
                          "Recorded Git blob does not identify the frozen source bytes.")
            # Preserve original packaging observations even when recording a
            # current source freeze. A new baseline must not imply adaptation.
            if source["frozen_git_blob_sha"] != source["packaged_source_git_blob_sha"]:
                issue("PLUGIN_SOURCE_DIFFERS_FROM_PACKAGING", path,
                      source["difference_reason"], note=True)
        adaptation_source_paths = {path for adaptation in plugin_map["adaptations"]
                                   for path in adaptation["source_paths"]}
        for path in sorted(inventory_source_paths - (source_paths & adaptation_source_paths)):
            issue("CANONICAL_SKILL_SOURCE_UNMAPPED", path,
                  "Canonical skill inventory entries must have frozen source bytes and an adapted skill relationship.")
        recorded_package_files = set()
        for adaptation in plugin_map["adaptations"]:
            if not adaptation["source_paths"] or not set(adaptation["source_paths"]) <= source_paths:
                raise ValueError(f"unmapped adaptation: {adaptation['skill']}")
            if not adaptation.get("adaptation_reason"):
                raise ValueError(f"missing adaptation reason: {adaptation['skill']}")
            for file in adaptation["packaged_files"]:
                path = file["path"]
                if path in recorded_package_files or not path.startswith("skills/" + adaptation["skill"] + "/"):
                    raise ValueError(f"invalid packaged path: {path}")
                recorded_package_files.add(path)
                check_file(f"{package}/{path}", file["sha256"], "PLUGIN_ADAPTATION_CHANGED")
        actual_package_files = {"skills/" + path for path in inventory(root / package / "skills")}
        for path in sorted(actual_package_files - recorded_package_files):
            issue("UNRECORDED_PLUGIN_FILE", f"{package}/{path}", "New adapted skill file has no reviewed source relationship.")
        for file in plugin_map["exact_copies"]:
            check_file(f"{package}/{file['packaged_path']}", file["sha256"], "PLUGIN_EXACT_COPY_CHANGED")
            source_file = safe_path(root, file["source_path"])
            copy_file = safe_path(root, f"{package}/{file['packaged_path']}")
            if source_file.is_file() and copy_file.is_file() and source_file.read_bytes() != copy_file.read_bytes():
                issue("PLUGIN_EXACT_COPY_DIFFERS", file["packaged_path"], f"Must match {file['source_path']} byte for byte.")
        historical = read_json(plugin_map["historical_provenance_path"])
        original_sources = {source["path"]: source["git_blob_sha"] for source in historical["sources"]}
        recorded_sources = {source["path"]: source["packaged_source_git_blob_sha"] for source in plugin_map["sources"]}
        if original_sources != recorded_sources:
            issue("PLUGIN_HISTORICAL_PROVENANCE_MISMATCH", plugin_map["historical_provenance_path"],
                  "Original packaging source observations differ from the new drift map.")
        original_skills = {skill["name"]: skill["source_paths"] for skill in historical["skills"]}
        recorded_skills = {adaptation["skill"]: adaptation["source_paths"] for adaptation in plugin_map["adaptations"]}
        if original_skills != recorded_skills:
            issue("PLUGIN_SOURCE_MAPPING_MISMATCH", package, "Adapted skill source relationships differ from packaging provenance.")
        check_plugin_identity(root, plugin_map, issue)
    except (KeyError, ValueError, TypeError, OSError, json.JSONDecodeError) as error:
        issue("INVALID_PROVENANCE", "provenance", str(error))
    return {"status": "FAIL" if failures else ("PASS_WITH_DOCUMENTED_DIFFERENCES" if notes else "PASS"),
            "scope": "Recorded local byte fingerprints and plugin identity; upstream checked only when explicitly requested.",
            "upstream_checked": upstream_dir is not None or live_upstream,
            "failure_count": len(failures), "note_count": len(notes), "failures": failures, "notes": notes}


def compare_upstream(module: dict, upstream_dir: Path | None, live: bool, issue) -> None:
    name = module["name"]
    try:
        if live:
            repository = module["upstream_repository"]
            if not re.fullmatch(r"hh-health-AI/[a-z0-9-]+", repository):
                raise ValueError("unapproved upstream repository")

            def get(endpoint):
                request = urllib.request.Request(f"https://api.github.com/repos/{repository}/{endpoint}",
                    headers={"Accept": "application/vnd.github+json", "User-Agent": "hh-health-ai-source-sync"})
                with urllib.request.urlopen(request, timeout=30) as response:
                    return json.load(response)

            head = get("commits/" + module["upstream_branch"])["sha"]
            tree = get("git/trees/" + head + "?recursive=1")
            if tree.get("truncated"):
                raise ValueError("upstream tree was truncated")
            blobs = {entry["path"]: entry["sha"] for entry in tree["tree"] if entry["type"] == "blob"}
        else:
            directory = upstream_dir / name
            head = subprocess.check_output(["git", "-C", str(directory), "rev-parse", "HEAD"], text=True).strip()
            raw = subprocess.check_output(["git", "-C", str(directory), "ls-tree", "-r", "-z", "HEAD"])
            blobs = {}
            for record in raw.split(b"\0"):
                if record:
                    metadata, path = record.split(b"\t", 1)
                    _mode, kind, sha = metadata.decode().split()
                    if kind == "blob":
                        blobs[path.decode()] = sha
        if head != module["upstream_commit"]:
            issue("UPSTREAM_HEAD_CHANGED", module["upstream_repository"],
                  f"Recorded {module['upstream_commit']}; observed {head}. Bundled bytes were not changed.")
        recorded = {file["path"]: file["upstream_git_blob_sha"] for file in module["files"]
                    if file["upstream_git_blob_sha"] is not None}
        for path in sorted(set(recorded) | set(blobs)):
            if recorded.get(path) != blobs.get(path):
                issue("UPSTREAM_FILE_CHANGED", f"{name}/{path}",
                      f"Recorded blob {recorded.get(path)}; observed blob {blobs.get(path)}.")
    except (OSError, ValueError, KeyError, subprocess.SubprocessError, urllib.error.URLError) as error:
        issue("UPSTREAM_CHECK_FAILED", name, str(error))


def check_plugin_identity(root: Path, manifest: dict, issue) -> None:
    package = manifest["package_path"]
    portable = json.loads(safe_path(root, package + "/plugin.json").read_text(encoding="utf-8"))
    codex = json.loads(safe_path(root, package + "/.codex-plugin/plugin.json").read_text(encoding="utf-8"))
    runtime_fields = {"mcpServers", "apps", "hooks", "commands", "agents", "mcp", "appBindings"}
    for label, plugin in (("portable", portable), ("codex", codex)):
        for field in sorted(runtime_fields & plugin.keys()):
            issue("UNEXPECTED_PLUGIN_RUNTIME_BINDING", label + ":" + field,
                  "This reviewed edition contains instruction skills only; runtime bindings require a separate reviewed package scope.")
    for field in manifest["identity_fields"]:
        if portable.get(field) != codex.get(field):
            issue("PLUGIN_IDENTITY_MISMATCH", field, "Portable and Codex manifests disagree.")
    for field, expected in manifest["expected_identity"].items():
        if portable.get(field) != expected:
            issue("PLUGIN_IDENTITY_CHANGED", field, f"Expected {expected!r}; found {portable.get(field)!r}.")
    portable_ui = portable["extensions"]["com.openai"]["interface"]
    codex_ui = dict(codex["interface"])
    for field, allowed in manifest["codex_interface_only"].items():
        if codex_ui.pop(field, None) != allowed:
            issue("PLUGIN_INTERFACE_MISMATCH", field, "Codex-only interface field changed.")
    if portable_ui != codex_ui:
        issue("PLUGIN_INTERFACE_MISMATCH", package, "Portable and Codex interface metadata disagree.")
    if codex.get("skills") != "./skills":
        issue("PLUGIN_SKILLS_PATH_MISMATCH", package, "Codex manifest must resolve the packaged skills directory.")
    marketplace = json.loads(safe_path(root, manifest["marketplace_path"]).read_text(encoding="utf-8"))
    entries = [entry for entry in marketplace["plugins"] if entry["name"] == portable["name"]]
    if len(entries) != 1:
        issue("MARKETPLACE_IDENTITY_MISMATCH", manifest["marketplace_path"], "Package must appear exactly once.")
    else:
        entry = entries[0]
        if entry.get("source") != {"source": "local", "path": "./" + package}:
            issue("MARKETPLACE_SOURCE_MISMATCH", manifest["marketplace_path"], "Local package path disagrees with the provenance map.")
        if entry.get("category") != portable_ui.get("category"):
            issue("MARKETPLACE_CATEGORY_MISMATCH", manifest["marketplace_path"], "Marketplace and package categories disagree.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--upstream-dir", type=Path, help="Parent directory of local specialist Git checkouts")
    group.add_argument("--live-upstream", action="store_true", help="Read public GitHub main HEADs and Git trees; network failures fail")
    parser.add_argument("--report", type=Path, help="Optional JSON report output; provenance is never updated")
    args = parser.parse_args()
    result = check_repository(args.root, upstream_dir=args.upstream_dir, live_upstream=args.live_upstream)
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return int(result["failure_count"] > 0)


if __name__ == "__main__":
    raise SystemExit(main())
