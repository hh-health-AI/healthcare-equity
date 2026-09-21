# Prompts — AdCom Prep & Post-Approval Label Delta

From the Healthcare Equity Analyst Prompt Library v1.4. Standing instructions apply (`${CLAUDE_PLUGIN_ROOT}/CLAUDE.md`). Fill bracketed inputs.

## SUB-BIO-02 · FDA AdCom Prep
Tags: `#biotech #fda-ema #senior-judgment`
**When to use.** Ahead of an AdCom.
**Reasoning.** AdCom precedent → panel framing → vote distribution → position
**Inputs.** FDA materials, panelists, class precedent.
**Output.** AdCom prep with positioning.

PROMPT:
> AdCom prep for [asset] on [date]. (1) Expected discussion topics; (2) panel composition and voting history; (3) three likely FDA questions and vote split; (4) stock-impact mapping; (5) positioning.

## SUB-BIO-08 · Post-Approval Label Delta Analyser
Tags: `#biotech #pharma #fda-ema #senior-judgment`
**When to use.** Within 48 hours of FDA or EMA approval, when the exact label language materially affects peak sales and payor reception.
**Reasoning.** expected label vs actual → commercial unlock → peak-sales delta → precedent
**Inputs.** Drugs@FDA approval letter and label, FDA review documents if posted, company press release, pre-approval sell-side peak sales forecasts for bridge construction.
**Output.** Structured label delta analysis with model bridge and precedent implications.

PROMPT:
> Analyse the approved label and approval package for [TICKER]'s [asset]. Use Drugs@FDA for the official label text, the FDA approval letter, and the review documents (cross-disciplinary review, medical officer review, statistical review, CMC review) where posted. Do not use FDALabel for exact language; use it only as a navigation aid. Output: (1) Expected vs actual label — a side-by-side of the label language the company and street expected vs what the FDA actually granted. Cover indication scope, line of therapy, patient population subsetting (biomarker, age, comorbidity), dosing, monitoring requirements, black-box warnings, contraindications, and post-marketing commitments (PMCs) or post-marketing requirements (PMRs). (2) Commercial unlock — what does the label enable that a narrower label would not? Quantify in patient populations addressable and in payor coverage likelihood. (3) Commercial restriction — what does the label still restrict? REMS programs, specialty pharmacy channels, prior-auth burden, step-therapy eligibility. (4) Peak-sales model delta — recalculate peak sales under the actual label and bridge vs the prior model. Show the sensitivity to each label element. (5) Post-marketing overhang — any confirmatory trial requirement, safety study, or subpopulation study that could materially affect the label over the next 24–36 months. (6) Precedent implications — does this label set a precedent useful for another asset in the pipeline or the competitive set? End with the confidence score from the standing instructions.
