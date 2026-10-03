# rNPV

Root: `as_of` (valuation date), `currency`, `units`, nonempty `scenarios`, optional `synthetic`. Each scenario needs unique `name`, `discount_rate` between 0 and 1, and nonempty `cashflows`. Optional nonnegative `cash`, `debt`, `unallocated_overhead_pv`, and positive `diluted_shares`. Equity value is calculated only when all three bridge components are explicitly supplied; missing components do not default to zero. Per-share value also requires diluted shares.

Each row requires nonnegative numeric `year` (years from valuation date, fractional allowed), signed `cashflow`, `probability` between 0 and 1, `kind` (`development`, `commercial`, `other`), and an `assumption` note with source or explicit modeling rationale.

Formula: PV = cashflow × unconditional probability / (1 + discount rate)^year. Sum rows for asset rNPV; add cash and subtract debt and overhead for equity. Use compatible units for cash and shares. Do not preweight cash flows and then weight them again. No terminal value, automatic probability estimation, scenario weighting or cross-asset correlation is assumed. Run alternate input scenarios for sensitivity analysis.

Output: scenario values plus every row's expected cash flow and discounted contribution. Enterprise value interpretation requires unlevered after-tax cash flows.

Example: `examples/valuation.json`.


See the repository suite examples for complete synthetic input files.
