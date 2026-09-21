# Prompts — Catalyst Calendar

From the Healthcare Equity Analyst Prompt Library v1.4. Standing instructions apply (`${CLAUDE_PLUGIN_ROOT}/CLAUDE.md`). Fill bracketed inputs.

## SCR-02 · Catalyst Calendar Screen
Tags: `#screen #biotech #fda-ema #ctgov #senior-judgment`
**When to use.** Quarterly catalyst review for event-driven ideas.
**Reasoning.** build signal stack → validate components → rank opportunities → diligence next
**Inputs.** Universe; ClinicalTrials.gov, FDA AdCom calendar.
**Output.** Calendar with prioritised idea list.

PROMPT:
> Catalyst calendar for next 6 months. Per catalyst: (1) ticker, asset, event type; (2) date window; (3) base rate; (4) prior data and success threshold; (5) implied vs fundamental move; (6) preliminary take; (7) top 5 for deeper work.

## TECH-02 · Bloomberg Catalyst and Event Calendar Query
Tags: `#data-extraction #biotech #bloomberg #bql #senior-judgment`
**When to use.** When building or refreshing a catalyst calendar from Bloomberg data.
**Reasoning.** schema design → pipeline build → validate → deploy
**Inputs.** Coverage universe tickers; date window.
**Output.** BQL query or terminal navigation with structured output.

PROMPT:
> Generate a BQL query to extract the upcoming catalyst calendar for my healthcare coverage universe, specifically filtering for: (1) FDA Advisory Committee (AdCom) meetings in the next 90 days; (2) PDUFA dates in the next 180 days; (3) Phase 3 trial readout windows from Bloomberg BI DRUG <GO> or equivalent; (4) CMS rate notice and final rule dates. Output as a structured table with ticker, event type, expected date, and Bloomberg event ID. If a BQL approach is limited, provide the alternative Bloomberg terminal navigation (BI, EVTS, DRUG <GO>) with the specific screen settings.

## TECH-06 · ClinicalTrials.gov Agent Query Construction
Tags: `#data-extraction #biotech #ctgov #senior-judgment`
**When to use.** When extracting structured clinical trial data programmatically.
**Reasoning.** FQL construct → test → deploy ownership or estimate workflow
**Inputs.** Condition, intervention, sponsor, or NCT numbers.
**Output.** API query URL and JSON output schema.

PROMPT:
> Build a resilient query for ClinicalTrials.gov that bypasses fragile DOM selectors. (1) Construct the API query URL (using the v2 API: https://clinicaltrials.gov/api/v2/studies) to extract: NCTId, BriefTitle, Condition, InterventionName, Phase, OverallStatus, StartDate, PrimaryCompletionDate, StudySponsor. (2) Filter for multiple statuses simultaneously (e.g. 'RECRUITING' and 'ACTIVE_NOT_RECRUITING'). (3) Filter by condition, intervention type, or sponsor. (4) Construct a comparative query for [TICKER]'s lead asset vs all competing trials in the same indication/mechanism. (5) Output as structured JSON for downstream analysis. (6) If using an AI agent framework (e.g. AgentQL), provide the natural-language extraction query. My query: [describe the trial data needed].
