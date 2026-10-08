# Maintenance and source provenance

`research-suite/` is the canonical runnable Python research package. Root skills provide investment synthesis. Each specialist repository is authoritative for its own scripts and instructions; `modules/<name>/` is a bundled, frozen snapshot.

## Recorded specialist snapshots

On 2026-10-08 all twelve specialist repositories were cloned at their actual default-branch HEADs. The entire tracked upstream inventory was compared with the bundled directory, without copying or overwriting module content. [module-snapshots.json](../provenance/module-snapshots.json) records each commit, relative path, upstream Git blob, upstream SHA-256, bundled SHA-256 and exact difference posture.

| Module | Observed upstream main commit | Byte-identical bundled files | Documented adapted files |
|---|---|---:|---:|
| clinical-catalysts | `443669f98330890f626bc2f7c1b776654d7838df` | 25 | 1 |
| cms-reimbursement | `18c0d3c7a5ff0aec618b9aaf9c23b0550ec50231` | 16 | 1 |
| epi-demand | `1c769675a9756ea29b6bfe92d5b81975e1717762` | 14 | 1 |
| evidence-catalysts | `1a0603dcbad9910fdef5341a778694723e6cc167` | 13 | 1 |
| fda-safety-signals | `acfb4deae2dde508463b6d5b8e16f2744f89676a` | 14 | 1 |
| global-access | `84cde2884617f63e9aeb3e1d2e9664876ce89fa3` | 14 | 1 |
| ip-exclusivity | `5564642984a3a789752f3bea1dbf48a4ddd4dc36` | 14 | 1 |
| procedure-exposure | `fe3f194292ae9150deabd3d8112e699f7544d3a7` | 11 | 1 |
| provider-adoption | `74d02d046209427d65a0481582eeace19a0efd0c` | 11 | 2 |
| provider-economics | `b71aa3c16e4fe760ee05c83160c56bde5f3211a2` | 14 | 1 |
| rx-utilization | `9b29c59dfc0ebe100511af3d3e896a01584e3c43` | 18 | 1 |
| sec-forensics | `0f9c1a94af0ea25cd5e0e6ae12cb75f5885a986e` | 14 | 1 |

The previous Rx Utilization record, `b8ea54c9eae401f267291a2e9ba964c18279b06a`, referred to the earlier pagination change. The new observation records the later upstream HEAD and compares all files; it does not rewrite that history.

All twelve bundled READMEs omit standalone promotional/search-positioning introductions and keep concise module headings. The four installation READMEs updated on 2026-10-08 also use integrated-directory introductions linking to their standalone sources. CMS Reimbursement additionally changes the smoke-test requirement from forced model-variable movement to documenting a model implication, consistent with `CHANGE`, `NO_CHANGE`, `UNCERTAINTY_ONLY` and `NEEDS_DATA`. Provider Adoption's bundled changelog replaces a stale external-suite placeholder introduction with public maintenance guidance. The remaining operational text, scripts, instructions and tests are byte-identical at the recorded upstream commits. The four earlier observations are retained as `previous_observed_commit` in the manifest.

Repository metadata and redundant standalone license files are omitted from bundled directories; the flagship retains its MIT license. CMS Reimbursement's [distinct original copyright notice](../modules/cms-reimbursement/LICENSE) is preserved byte for byte. The standalone Rx Utilization CI file is also omitted; the flagship research-suite workflow runs the bundled module tests. These 35 omitted upstream paths and 13 adapted bundled files remain explicit report notes. This is a comparison of pinned snapshots, not a claim that complete repositories are synchronized or scientifically validated.

## Adapted plugin provenance

[plugin-source-map.json](../provenance/plugin-source-map.json) maps each of the thirteen adapted skills to the original package's reviewed source paths and freezes all 92 packaged skill, reference and agent files. It preserves the original source Git blobs from the 2026-10-04 [packaging provenance](../plugins/hh-health-ai-research/provenance.json), which was assembled from individual file reads rather than an atomic checkout. Current source fingerprints are separate from those original observations.

Packaged workflows are intentional concise adaptations, not generated copies. When a source has changed since packaging, `PLUGIN_SOURCE_DIFFERS_FROM_PACKAGING` remains an explicit note even after recording a reviewed current source fingerprint. The two README source changes in this release were reviewed as installation/presentation documentation updates; individual workflow source instructions are unchanged. One packaged runtime reference corrects private-workflow wording to skills-only workflow, with its preceding fingerprint preserved. A source freeze alone does not certify that adapted instructions incorporate a source change; review the affected relationships before releasing updated workflow instructions.

Package README, NOTICE, validation documentation and static validation helpers are maintained directly and are excluded from generated-content fingerprints. All 102 package filenames remain inventoried so new runtime files or bindings cannot appear silently. The nine canonical biomedical skill entry points must retain frozen source bytes and adapted skill relationships. License content must match the source exactly. The checker validates the package name, version, repository, license and shared identity/interface fields across both plugin manifests, plus the marketplace package path and category.

## Run the checks

From the flagship root, with Python 3.10+ and no third-party Python dependencies:

```sh
python -m unittest discover -s tests -p 'test_source_sync.py' -v
python scripts/check_source_sync.py --report outputs/source-sync.json
```

Offline checks fail on changed or missing frozen bytes, new unrecorded module/package files, new or removed canonical suite skills, symlinks, unexpected runtime bindings, unsupported differences, inconsistent provenance and inconsistent plugin/marketplace identity. Documented exact adaptations and omissions are reported as notes. The checker never updates manifests or copies source files.

To verify recorded observations against local specialist Git checkouts stored in a parent directory:

```sh
python scripts/check_source_sync.py --upstream-dir /path/to/specialist-checkouts
```

To inspect current public upstream main HEADs and Git blob inventories:

```sh
python scripts/check_source_sync.py --live-upstream --report outputs/live-upstream-sync.json
```

New upstream commits and changed, added or removed upstream blobs fail this optional check and identify the exact relative paths. Network errors or truncated trees fail rather than implying synchronization. The [source provenance workflow](../.github/workflows/source-sync.yml) runs offline checks on relevant pushes and pull requests; its manual `live_upstream` input enables the external comparison. It does not install new content or schedule background updates.

## Review a change before updating a freeze

1. Test and merge a specialist implementation change upstream first. Read the full diff from the recorded commit to the proposed commit, including README and policy changes.
2. Copy only reviewed changed files into the corresponding bundled module. Preserve module-specific links and inspect additions and deletions.
3. Update the module manifest's commit, upstream blob inventory and SHA-256 values for the reviewed files. Preserve or revise every explicit adaptation/omission reason; do not turn an unresolved difference into `identical`.
4. For a plugin source change, identify affected adapted skills from the source map, inspect their instructions, update only required adaptations, and preserve original packaging observations. Record the reviewed source and package fingerprints; do not refresh all hashes to clear an unexplained failure.
5. Run provenance checks, affected module tests and package static validation. Inspect the manifest diff together with the implementation diff before committing.

Legacy `sync-from-suite.sh` scripts remain retired because they can overwrite public documentation. Broader research validation remains separate:

```sh
python -m unittest discover -s modules/rx-utilization/tests -v
cd research-suite
python -m unittest discover -s tests -v
python scripts/run_demo.py
python scripts/validate_package.py
python scripts/evaluate_reliability.py
```

Fingerprints cover bytes and paths, not executable permission modes; Python cache and virtual-environment directories are excluded. Default CI does not detect changes committed only to specialist repositories; run the explicit upstream comparison for that. Byte provenance and static manifest consistency do not establish citation entailment, clinical correctness, investment performance or end-to-end host compatibility. Those need their own source audit and evaluation evidence.
