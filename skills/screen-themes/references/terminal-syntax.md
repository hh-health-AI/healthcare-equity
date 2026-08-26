# Terminal Syntax Generation (Bloomberg BQL) — shared reference

Used by screen-themes, model-valuation, portfolio, and earnings when the user needs terminal-executable syntax. Rule: **generate syntax for the user to run; never fabricate terminal output.** FactSet equivalents: TECH-03/04 in prompts.md.

## TECH-01 · Bloomberg BQL Syntax Generator for Healthcare
Tags: `#data-extraction #cross-sector #bloomberg #bql #junior-task`
**When to use.** When you need executable Bloomberg BQL syntax for healthcare-specific data queries.
**Inputs.** Natural-language data query; target securities; output format (Excel or Python).
**Output.** Executable BQL string ready to paste into Excel or Python.

PROMPT:
> Translate my natural-language query into executable BQL syntax for Excel or Python. (1) Construct the =BQL() formula using get(<field>) for(<security>) with(<parameters>). (2) Define parameters (dates, periods, fill rules). (3) For fiscal-period data, format calculated periods correctly (e.g. FA_PERIOD_REFERENCE, FA_PERIOD_TYPE=LTM). (4) For healthcare-specific fields, use the correct BQL field names for R&D expense, pipeline data, patent expiry via PTNT <GO>, catalyst calendar. (5) Output validation — verify parentheses and nesting. (6) If Python, provide the bql.Execute() syntax with proper DataFrame handling. My query: [describe the data needed].

## Companion prompts elsewhere in the suite

- TECH-02 (Bloomberg catalyst/event calendar query) — clinical-catalysts › catalyst-calendar
- TECH-05 (SEC EDGAR autonomous monitoring config) — portfolio › references
- TECH-06 (ClinicalTrials.gov API query construction) — clinical-catalysts › catalyst-calendar
