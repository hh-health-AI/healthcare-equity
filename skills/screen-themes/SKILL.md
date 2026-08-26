---
name: screen-themes
description: >
  This skill should be used when the user says "design a screen", "find hidden
  compounders", "screen for activist targets", "validate this theme", "TAM bottoms-up",
  "build a thematic basket", "map GLP-1 dynamics", "bioprocessing cycle", or wants
  Bloomberg/FactSet screen syntax and thematic idea generation.
metadata:
  version: "0.1.0"
---

# Screening & Thematic Research

Systematic idea generation — quant screens, thematic validation, and basket construction. Prompts in `${CLAUDE_PLUGIN_ROOT}/skills/screen-themes/references/prompts.md`; terminal syntax patterns in `references/terminal-syntax.md`.

## Route by need

| Need | Prompt |
|---|---|
| Design an analytically grounded screen | SCR-01 (Bloomberg EQS / FactSet) |
| Quality names off the crowded path | SCR-03 hidden compounders |
| Theme → listed beneficiaries | SCR-04 thematic beneficiary screen |
| Activist setups | SCR-05 activist target screen |
| Validate a theme before 3 weeks of work | THM-01 theme validation |
| Test the TAM claim | THM-02 bottoms-up TAM build |
| Investable expression | THM-03 basket construction |
| GLP-1 exposure map (any name) | SUB-PHA-02 class dynamics |
| Bioprocessing/tools cycle position | SUB-TLS-01 cycle tracker |
| FactSet screen/transcript syntax | TECH-03 / TECH-04 |

## Execution rules

1. **Terminal syntax is generated, never executed:** BQL/EQS/FQL output (TECH-01/03, references/terminal-syntax.md) is for the user to paste into their terminal; results come back from them. Never fabricate screen results, consensus, or ownership data. Event-calendar screens (SCR-02) live in clinical-catalysts.
2. Screens follow SCR-01's shape: universe → 4–7 filters with thresholds *and reasoning* → field codes → expected hit count and triage → the one filter to loosen for long-tail ideas → post-screen workflow. Screening starts at Bloomberg/FactSet then verifies against filings (workflow-mapped entry points, `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md`).
3. Thematic chain: THM-01 validation (real? durable? differentiated? investable? horizon-matched?) → THM-02 TAM (population → use case → addressable → price → penetration; healthcare funnel tops come from procedure-exposure epi-funnel-input) → SCR-04 supply-chain beneficiary map with pass-through quality ranking → THM-03 basket (purity × quality, weights, pair shorts, factor map, rebalance trigger, kill switch) → portfolio skill for sleeve fit.
4. Sub-sector trackers (SUB-PHA-02, SUB-TLS-01) are standing theme monitors — refresh them on the cadence the user sets and route dated events to the suite catalyst calendar.
5. Screen hits and validated themes hand off to initiate (INIT-01 scoping) for name-level work; sector-wide primers and comps spreads can go to the market-researcher plugin.
