# Biotech rNPV scenarios

**SYNTHETIC DEMONSTRATION — not clinical or investment evidence.**

Generated: 2026-09-25T16:51:01.891776+00:00

Input SHA-256: `9dec391b88ede4b6616a0f7089ae118a95033633c1c3620d7461637478133d5c`

Currency: USD · Cash-flow units: millions (shares also in millions) · As of: 2026-09-25

| Scenario | Discount rate | Asset rNPV | Equity value | Value/share |
| --- | --- | --- | --- | --- |
| bear | 14.0% | -0.5931 | 15.4069 | 1.5407 |
| base | 12.0% | 56.0137 | 72.0137 | 7.2014 |
| bull | 10.0% | 168.3178 | 184.3178 | 18.4318 |

## bear equity bridge

| Component | Value |
| --- | --- |
| cash | 25.0 |
| debt | 5.0 |
| unallocated_overhead_pv | 4.0 |

## bear cash-flow audit

| t (years) | Kind | Cash flow | Probability | Expected | PV | Assumption |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | development | -10 | 1 | -10.0 | -10.0 | Synthetic committed development spend |
| 1 | development | -20 | 0.7 | -14.0 | -12.2807 | Synthetic 70% probability of incurring the next stage cost |
| 3 | commercial | 30 | 0.2 | 6.0 | 4.0498 | Synthetic after-tax unlevered cash flow; unconditional commercial probability 0.2 |
| 4 | commercial | 70 | 0.2 | 14.0 | 8.2891 | Synthetic after-tax unlevered cash flow; unconditional commercial probability 0.2 |
| 5 | commercial | 90 | 0.2 | 18.0 | 9.3486 | Synthetic after-tax unlevered cash flow; unconditional commercial probability 0.2 |

## base equity bridge

| Component | Value |
| --- | --- |
| cash | 25.0 |
| debt | 5.0 |
| unallocated_overhead_pv | 4.0 |

## base cash-flow audit

| t (years) | Kind | Cash flow | Probability | Expected | PV | Assumption |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | development | -10 | 1 | -10.0 | -10.0 | Synthetic committed development spend |
| 1 | development | -20 | 0.7 | -14.0 | -12.5 | Synthetic 70% probability of incurring the next stage cost |
| 3 | commercial | 50 | 0.4 | 20.0 | 14.2356 | Synthetic after-tax unlevered cash flow; unconditional commercial probability 0.4 |
| 4 | commercial | 110 | 0.4 | 44.0 | 27.9628 | Synthetic after-tax unlevered cash flow; unconditional commercial probability 0.4 |
| 5 | commercial | 160 | 0.4 | 64.0 | 36.3153 | Synthetic after-tax unlevered cash flow; unconditional commercial probability 0.4 |

## bull equity bridge

| Component | Value |
| --- | --- |
| cash | 25.0 |
| debt | 5.0 |
| unallocated_overhead_pv | 4.0 |

## bull cash-flow audit

| t (years) | Kind | Cash flow | Probability | Expected | PV | Assumption |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | development | -10 | 1 | -10.0 | -10.0 | Synthetic committed development spend |
| 1 | development | -20 | 0.7 | -14.0 | -12.7273 | Synthetic 70% probability of incurring the next stage cost |
| 3 | commercial | 80 | 0.6 | 48.0 | 36.0631 | Synthetic after-tax unlevered cash flow; unconditional commercial probability 0.6 |
| 4 | commercial | 160 | 0.6 | 96.0 | 65.5693 | Synthetic after-tax unlevered cash flow; unconditional commercial probability 0.6 |
| 5 | commercial | 240 | 0.6 | 144.0 | 89.4127 | Synthetic after-tax unlevered cash flow; unconditional commercial probability 0.6 |

End-of-year cash flows at t years from as_of; probability is unconditional payment/receipt probability for each row. No additional global PoS multiplier. No terminal value unless explicitly entered as a cash flow.

Use matching units for cash, debt and shares (e.g. USD millions and millions of shares). Supply unlevered after-tax cash flows for an enterprise-value interpretation. Subtract corporate overhead only if not already included. These user-defined probabilities are assumptions, not calibrated trial-success predictions. Correlated assets and financing dilution need separate scenarios.
