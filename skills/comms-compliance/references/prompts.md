# Prompts — Client Communication & Compliance

From the Healthcare Equity Analyst Prompt Library v1.4. Standing instructions apply (`${CLAUDE_PLUGIN_ROOT}/CLAUDE.md`). Fill bracketed inputs.

## COMM-01 · IC Memo Draft
Tags: `#client-comms #cross-sector #senior-judgment #pm-level`
**When to use.** Before presenting to investment committee.
**Inputs.** Thesis memo, model, valuation.
**Output.** IC-ready memo, ≤1,000 words.

PROMPT:
> IC memo for [TICKER]. (1) Recommendation in three bullets; (2) 100-word thesis; (3) variant perception; (4) three catalysts; (5) three risks; (6) sizing logic; (7) single chart; (8) two open questions. Under 1,000 words.

## COMM-02 · Quarterly Letter Section Draft
Tags: `#client-comms #cross-sector #senior-judgment`
**When to use.** Drafting the healthcare section for the quarterly LP letter.
**Inputs.** Performance, attribution, thesis evolutions.
**Output.** Polished 600-word section.

PROMPT:
> Healthcare section. (1) Macro context; (2) top 3 contributors/detractors with operational attribution; (3) one position update; (4) what we got wrong; (5) next-quarter theme. 600 words, confident and honest.

## COMM-04 · Translate Technical Biology for Generalist PMs
Tags: `#client-comms #biotech #cross-sector #senior-judgment`
**When to use.** When generalist PMs need to engage with biotech science.
**Inputs.** Asset details, mechanism, endpoints.
**Output.** 500-word generalist explainer.

PROMPT:
> Translate [asset/mechanism/readout] for a generalist PM. (1) Disease in two sentences; (2) SOC and failure; (3) mechanism with accurate analogy; (4) clinical endpoint in concrete terms; (5) FDA/clinician success criteria; (6) two reasons statistical positive could be clinically irrelevant. ~500 words.

## COMM-05 · MNPI Scrubbing Audit for Client Communications
Tags: `#compliance #client-comms #cross-sector #senior-judgment`
**When to use.** Before sending any outbound communication where you've had recent expert calls or management meetings.
**Inputs.** Draft; list of recent expert/management interactions.
**Output.** Marked-up document with MNPI flags and actions.

PROMPT:
> Audit draft [type] for MNPI risk. (1) Flag statements derived from non-public sources; (2) identify unreported financial data references; (3) flag implied references; (4) recommend: remove / rephrase with attribution / retain with compliance review; (5) confirm conflict disclosures current. Err on caution.

## COMM-06 · Disclosure and Conflict of Interest Check
Tags: `#compliance #client-comms #cross-sector #junior-task`
**When to use.** Before publishing any communication naming specific equities.
**Inputs.** Draft; holdings; personal account declarations.
**Output.** Disclosure checklist with pass/fail.

PROMPT:
> Disclosure audit. (1) Position (long/short/none) per equity; (2) personal holdings flagged; (3) recent meeting/call notes; (4) past PTs dated; (5) standard disclaimer. Checklist output.

## COMM-07 · Public Speaking and Conference Pre-Flight
Tags: `#compliance #client-comms #cross-sector #senior-judgment`
**When to use.** Before any public-facing presentation or media appearance.
**Inputs.** Talking points; restricted list; trade blotter.
**Output.** Pre-flight checklist with rephrasings.

PROMPT:
> Pre-flight for [event] on [topic]. (1) Position disclosure confirmed; (2) forward statements grounded in public data; (3) investment advice boundary check; (4) restricted window check; (5) rephrasings for borderline statements; (6) disclaimer included.
