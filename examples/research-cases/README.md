# Dated healthcare research cases

These three cases connect real primary-source evidence to explicit model assumptions and reproducible calculations. Each folder contains a source ledger, dated observations, assumptions, a standard-library Python model and its recorded results. The financial scenarios illustrate mechanisms; they are not current stock recommendations or fully underwritten price targets.

| Case | Evidence snapshot | Model question | Key boundary |
|---|---|---|---|
| [Biotech: HELIOS-B / vutrisiran](biotech-trial-rnpv/README.md) | HELIOS-B publication abstract; US approval dated 20 March 2025 | How does a realized approval gate change illustrative commercial rNPV? | Trial hazard ratios do not determine market share; commercial scenarios remain assumptions. |
| [Medtech: Intuitive Surgical](medtech-procedures-revenue/README.md) | FY2025 baseline and Q2 release on 16 July 2026 | How do procedures, recurring revenue and systems/service assumptions affect revenue? | End-of-period installed bases cannot establish utilization; platform revenue allocation is assumed. |
| [Managed care: UnitedHealth](managed-care-mlr-earnings/README.md) | Q2 release on 16 July 2026 | How does a medical-cost-ratio change flow through quarterly earnings and EPS? | Development includes current-year service dates; reported EPS needs its disclosed numerator adjustment. |

## Reproduce the calculations

From the repository root, with Python 3.10 or later:

```sh
python3 examples/research-cases/biotech-trial-rnpv/model.py --check
python3 examples/research-cases/medtech-procedures-revenue/model.py --check
python3 examples/research-cases/managed-care-mlr-earnings/model.py --check
```

These commands check the committed results without changing them. They require no API key, network access or model provider. Each case README explains its inputs, formula, scenario sensitivities and source limits. The consolidated [repository validator](../../scripts/validate_repository.py) also runs all three cases.

## Read the evidence before changing an assumption

The source ledgers identify documents, retrieval dates, exact locators and what was actually read. Distinguish observations from modeling assumptions and retain their dates. A later registry update, current share price or new company disclosure does not silently become part of an earlier snapshot.

The [24-case source audit](../../skills/model-valuation/references/case-source-audit.md) covers additional scoped evidence statements across the healthcare sector. The [semantic evaluation](../../research-suite/evaluation/semantic/README.md) tests claim interpretation on a small public development set. Its recorded assistant agreement is separate from independent clinical validation, source extraction accuracy and investment performance.
