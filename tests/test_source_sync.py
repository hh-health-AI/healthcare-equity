"""Provenance regression tests: detect drift without refreshing the baseline."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import urllib.error


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/check_source_sync.py"
SPEC = importlib.util.spec_from_file_location("source_sync", SCRIPT)
SYNC = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SYNC)


class SourceSyncTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.package = "plugins/example"
        self.write("modules/example/scripts/query.py", "print('reviewed')\n")
        self.write("README.md", "Reviewed source workflow.\n")
        self.write("LICENSE", "MIT\n")
        self.write("plugins/example/LICENSE", "MIT\n")
        self.write("plugins/example/README.md", "Initial installation guide.\n")
        self.write("plugins/example/skills/example/SKILL.md", "Reviewed portable adaptation.\n")
        module_sha, module_blob = SYNC.hashes((self.root / "modules/example/scripts/query.py").read_bytes())
        source_sha, source_blob = SYNC.hashes((self.root / "README.md").read_bytes())
        package_sha, _ = SYNC.hashes((self.root / "plugins/example/skills/example/SKILL.md").read_bytes())
        license_sha, _ = SYNC.hashes((self.root / "LICENSE").read_bytes())
        self.module_map = {"schema_version": 1, "module_count_expected": 1, "modules": [{
            "name": "example", "upstream_commit": "a" * 40,
            "upstream_repository": "hh-health-AI/example", "upstream_branch": "main",
            "files": [{"path": "scripts/query.py", "bundled_sha256": module_sha,
                       "upstream_sha256": module_sha, "upstream_git_blob_sha": module_blob,
                       "comparison": "identical"}]}]}
        self.plugin_map = {"schema_version": 1, "package_path": self.package,
            "marketplace_path": ".agents/plugins/marketplace.json",
            "historical_provenance_path": "plugins/example/provenance.json",
            "sources": [{"path": "README.md", "frozen_sha256": source_sha,
                         "frozen_git_blob_sha": source_blob, "packaged_source_git_blob_sha": source_blob}],
            "adaptations": [{"skill": "example", "source_paths": ["README.md"],
                             "adaptation_reason": "Portable concise workflow edition.",
                             "packaged_files": [{"path": "skills/example/SKILL.md", "sha256": package_sha}]}],
            "exact_copies": [{"source_path": "LICENSE", "packaged_path": "LICENSE", "sha256": license_sha}],
            "identity_fields": ["name", "version", "license"],
            "expected_identity": {"name": "example", "version": "0.1.0", "license": "MIT"},
            "codex_interface_only": {"capabilities": []}}
        interface = {"displayName": "Example", "category": "Productivity"}
        portable = {"name": "example", "version": "0.1.0", "license": "MIT",
                    "extensions": {"com.openai": {"interface": interface}}}
        codex = {"name": "example", "version": "0.1.0", "license": "MIT",
                 "skills": "./skills", "interface": {**interface, "capabilities": []}}
        self.write_json("plugins/example/plugin.json", portable)
        self.write_json("plugins/example/.codex-plugin/plugin.json", codex)
        self.write_json("plugins/example/provenance.json", {
            "sources": [{"path": "README.md", "git_blob_sha": source_blob}],
            "skills": [{"name": "example", "source_paths": ["README.md"]}]})
        self.write_json(".agents/plugins/marketplace.json", {"plugins": [{"name": "example",
            "source": {"source": "local", "path": "./plugins/example"}, "category": "Productivity"}]})
        self.plugin_map["package_file_inventory"] = sorted(SYNC.inventory(self.root / self.package))
        self.plugin_map["source_skill_inventory"] = [{"root": "research-suite/skills", "paths": []}]
        self.freeze()

    def write(self, relative, text):
        file = self.root / relative
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(text, encoding="utf-8")

    def write_json(self, relative, value):
        self.write(relative, json.dumps(value))

    def freeze(self):
        self.write_json("provenance/module-snapshots.json", self.module_map)
        self.write_json("provenance/plugin-source-map.json", self.plugin_map)

    def codes(self, **options):
        return {failure["code"] for failure in SYNC.check_repository(self.root, **options)["failures"]}

    def test_clean_snapshot_passes_without_network(self):
        with patch.object(SYNC.urllib.request, "urlopen", side_effect=AssertionError("offline means offline")):
            result = SYNC.check_repository(self.root)
        self.assertEqual(result["status"], "PASS")
        self.assertFalse(result["upstream_checked"])

    def test_changed_module_bytes_fail(self):
        self.write("modules/example/scripts/query.py", "print('unreviewed')\n")
        self.assertIn("BUNDLED_MODULE_CHANGED", self.codes())

    def test_missing_module_file_fails(self):
        (self.root / "modules/example/scripts/query.py").unlink()
        self.assertIn("BUNDLED_MODULE_CHANGED", self.codes())

    def test_new_bundled_file_needs_provenance(self):
        self.write("modules/example/scripts/new.py", "print('new')\n")
        self.assertIn("UNRECORDED_MODULE_FILE", self.codes())

    def test_new_module_needs_provenance(self):
        self.write("modules/new/README.md", "new module\n")
        self.assertIn("MODULE_INVENTORY_CHANGED", self.codes())

    def test_loose_module_root_file_needs_provenance(self):
        self.write("modules/new.py", "unreviewed root script\n")
        self.assertIn("UNRECORDED_MODULE_ROOT_FILE", self.codes())

    def test_python_cache_does_not_create_false_drift(self):
        self.write("modules/example/scripts/__pycache__/query.pyc", "cache")
        self.assertEqual(self.codes(), set())

    def test_changed_plugin_source_fails_without_refresh(self):
        self.write("README.md", "New source instructions.\n")
        self.assertIn("PLUGIN_SOURCE_CHANGED", self.codes())
        recorded = json.loads((self.root / "provenance/plugin-source-map.json").read_text())
        self.assertEqual(recorded, self.plugin_map)

    def test_changed_adapted_plugin_bytes_fail(self):
        self.write("plugins/example/skills/example/SKILL.md", "New adaptation.\n")
        self.assertIn("PLUGIN_ADAPTATION_CHANGED", self.codes())

    def test_new_plugin_reference_needs_provenance(self):
        self.write("plugins/example/skills/example/references/new.md", "New reference.\n")
        self.assertIn("UNRECORDED_PLUGIN_FILE", self.codes())

    def test_new_canonical_suite_skill_needs_routing_review(self):
        self.write("research-suite/skills/new/SKILL.md", "new canonical skill\n")
        self.assertIn("CANONICAL_SKILL_INVENTORY_CHANGED", self.codes())

    def test_inventory_refresh_without_source_mapping_fails(self):
        self.write("research-suite/skills/new/SKILL.md", "new canonical skill\n")
        self.plugin_map["source_skill_inventory"][0]["paths"] = ["research-suite/skills/new/SKILL.md"]
        self.freeze()
        self.assertIn("CANONICAL_SKILL_SOURCE_UNMAPPED", self.codes())

    def test_new_package_root_runtime_file_is_rejected(self):
        self.write("plugins/example/server.py", "print('new runtime')\n")
        self.assertIn("UNRECORDED_PACKAGE_FILE", self.codes())

    def test_new_runtime_binding_is_rejected_even_with_existing_target(self):
        file = self.root / "plugins/example/.codex-plugin/plugin.json"
        manifest = json.loads(file.read_text())
        manifest["mcpServers"] = "./provenance.json"
        file.write_text(json.dumps(manifest))
        self.assertIn("UNEXPECTED_PLUGIN_RUNTIME_BINDING", self.codes())

    def test_manifest_symlink_outside_repository_is_rejected(self):
        with tempfile.TemporaryDirectory() as outside:
            file = self.root / "plugins/example/.codex-plugin/plugin.json"
            target = Path(outside) / "plugin.json"
            target.write_bytes(file.read_bytes())
            file.unlink()
            file.symlink_to(target)
            codes = self.codes()
        self.assertIn("PLUGIN_SYMLINK_UNSUPPORTED", codes)
        self.assertIn("INVALID_PROVENANCE", codes)

    def test_manifest_version_mismatch_fails(self):
        file = self.root / "plugins/example/.codex-plugin/plugin.json"
        manifest = json.loads(file.read_text())
        manifest["version"] = "0.2.0"
        file.write_text(json.dumps(manifest))
        self.assertIn("PLUGIN_IDENTITY_MISMATCH", self.codes())

    def test_marketplace_path_mismatch_fails(self):
        file = self.root / ".agents/plugins/marketplace.json"
        manifest = json.loads(file.read_text())
        manifest["plugins"][0]["source"]["path"] = "./plugins/wrong"
        file.write_text(json.dumps(manifest))
        self.assertIn("MARKETPLACE_SOURCE_MISMATCH", self.codes())

    def test_documented_adaptation_remains_visible_and_frozen(self):
        file = self.module_map["modules"][0]["files"][0]
        file.update({"comparison": "documented-adaptation", "upstream_sha256": "b" * 64,
                     "difference_reason": "Intentional reviewed local header adaptation."})
        self.freeze()
        result = SYNC.check_repository(self.root)
        self.assertEqual(result["failure_count"], 0)
        self.assertEqual(result["notes"][0]["code"], "RECORDED_MODULE_DIFFERENCE")
        self.write("modules/example/scripts/query.py", "another change\n")
        self.assertIn("BUNDLED_MODULE_CHANGED", self.codes())

    def test_source_rebaseline_preserves_original_packaging_difference(self):
        original_blob = self.plugin_map["sources"][0]["packaged_source_git_blob_sha"]
        self.write("README.md", "New documented source.\n")
        sha256, blob = SYNC.hashes((self.root / "README.md").read_bytes())
        source = self.plugin_map["sources"][0]
        source.update({"frozen_sha256": sha256, "frozen_git_blob_sha": blob,
                       "difference_reason": "Source updated after packaging; adaptation review pending."})
        self.freeze()
        result = SYNC.check_repository(self.root)
        self.assertEqual(result["failure_count"], 0)
        self.assertIn("PLUGIN_SOURCE_DIFFERS_FROM_PACKAGING", {note["code"] for note in result["notes"]})
        self.assertEqual(source["packaged_source_git_blob_sha"], original_blob)

    def test_false_identical_declaration_is_rejected(self):
        self.module_map["modules"][0]["files"][0]["upstream_sha256"] = "b" * 64
        self.freeze()
        self.assertIn("INVALID_PROVENANCE", self.codes())

    def test_original_packaging_blob_must_agree_with_history(self):
        self.plugin_map["sources"][0].update({"packaged_source_git_blob_sha": "c" * 40,
            "difference_reason": "Changed history should fail."})
        self.freeze()
        self.assertIn("PLUGIN_HISTORICAL_PROVENANCE_MISMATCH", self.codes())

    def test_advanced_upstream_head_and_file_fail(self):
        raw = b"100644 blob " + b"c" * 40 + b"\tscripts/query.py\0"
        with patch.object(SYNC.subprocess, "check_output", side_effect=["b" * 40 + "\n", raw]):
            codes = self.codes(upstream_dir=self.root / "upstream")
        self.assertIn("UPSTREAM_HEAD_CHANGED", codes)
        self.assertIn("UPSTREAM_FILE_CHANGED", codes)

    def test_live_upstream_network_failure_is_not_a_pass(self):
        with patch.object(SYNC.urllib.request, "urlopen", side_effect=urllib.error.URLError("unavailable")):
            self.assertIn("UPSTREAM_CHECK_FAILED", self.codes(live_upstream=True))

    def test_path_traversal_is_rejected(self):
        self.plugin_map["sources"][0]["path"] = "../outside.md"
        self.freeze()
        self.assertIn("INVALID_PROVENANCE", self.codes())

    def test_packaging_readme_is_directly_maintained(self):
        self.write("plugins/example/README.md", "Installation correction.\n")
        self.assertEqual(self.codes(), set())


if __name__ == "__main__":
    unittest.main()
