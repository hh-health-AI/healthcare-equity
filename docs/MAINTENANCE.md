# Maintenance and publication

`healthcare-equity/research-suite` is the canonical Python research package. Its root skills are the synthesis workflow. Each specialist repository is authoritative for its own scripts and instructions; `healthcare-equity/modules/<name>` is a bundled snapshot, not an independently maintained implementation.

For a specialist change: test and merge upstream first; copy the reviewed changed files into the same module path; record the upstream commit below; run the module tests in the flagship; inspect the diff before committing. Preserve module-specific README links. Never overwrite the flagship from an unpublished external suite. Legacy `sync-from-suite.sh` scripts now fail without changing files.

| Module | Reviewed upstream commit | Bundled scope |
|---|---|---|
| rx-utilization | f51735d4904b1b17e92649b499768e37927cdac1 | Strict pagination scripts, tests and README from PR #1 |

Other bundled modules retain their existing snapshots; their synchronization has not been certified. Documentation corrections in this release are applied to both the four specialist repositories and their bundled copies.

Run from the flagship root:

```sh
python -m unittest discover -s modules/rx-utilization/tests -v
cd research-suite
python -m unittest discover -s tests -v
python scripts/run_demo.py
python scripts/validate_package.py
python scripts/evaluate_reliability.py
```
