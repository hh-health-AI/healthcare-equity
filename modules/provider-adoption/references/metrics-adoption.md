# Adoption Metrics & Evidence Translation (from the project frameworks)

Slices of `Healthcare_and_Life_Sciences_Commercial_Metrics.xlsx` and `Healthcare_Evidence_to_Valuation_Framework.xlsx` relevant to adoption evidence. Master copies: healthcare-equity plugin.

## Adoption/volume metric ladder (Commercial Metrics workbook)

| Sector | Flow metric ("new demand") | Stock metric ("installed demand") | Utilization/economics link |
|---|---|---|---|
| Pharma/biotech | NRx (new scripts); NBRx (first-time-on-brand — isolates true organic growth) | TRx (total scripts) | Refill rate (TRx−NRx) = adherence/persistence |
| Tools & diagnostics | Placements / net placements | Active installed base | Pull-through ($/instrument/yr); attachment rate (service/reagent contracts) |
| MedTech | Account reorder/utilization rate | Procedure volume; system placements | ASP (pricing power/erosion) |
| Managed care | Net organic additions | Covered lives | PMPM; MLR |

Footprint data from this plugin sits **upstream** of all of these: registered/adopting providers and sites are the capacity base that NRx/placements/procedures then flow through. State the position explicitly in every brief.

## Evidence translation — the usage row (Evidence-to-Valuation workbook)

| Evidence | Model variables | Modeling instruction | NOT automatic | Observable follow-up |
|---|---|---|---|---|
| Prescriptions, orders or usage | Observed stage of the commercial funnel | Bridge ordered → completed → paid → persistent → cash | Revenue, gross profit or durable retention | Paid conversion; collections; cohort retention |

## Case-library patterns to reuse (Evidence-to-Valuation workbook)

- **Intuitive (C06):** separate placements from active systems, procedures/system, recurring revenue/procedure — placements alone do not establish utilization; falsifier is installed base growing while utilization or recurring GP/system weakens.
- **argenx (C05):** a format conversion (self-administration) is not a new patient; broader label is not automatically a paid start — track total patient growth, cycles, persistence.
- **Dexcom (C07):** clinical benefit ≠ immediate coverage; longer wear can *reduce* units per user — model users, persistence, and units/user separately.
- **IDEXX (C24):** a weak placement quarter does not mean recurring economics weakened — utilization and pull-through per installed unit are the discriminators.

## Scenario discipline (medtech row)

Primary discriminator: **utilization per active installed system** — bear: flat/down utilization despite placements; bull: utilization and recurring revenue/system materially exceed plan. Set thresholds before the operating update.
