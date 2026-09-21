# Prompts — Device & Regulatory Diligence

From the Healthcare Equity Analyst Prompt Library v1.4. Standing instructions apply (`${CLAUDE_PLUGIN_ROOT}/CLAUDE.md`). Fill bracketed inputs.

## SUB-BIO-04 · Target Product Profile (TPP) Interrogation
Tags: `#biotech #fda-ema #senior-judgment`
**When to use.** When the commercial value depends on meeting a specific product profile.
**Inputs.** Corporate presentation, protocol, comparator data, payer readouts.
**Output.** TPP competitive assessment.

PROMPT:
> Interrogate TPP for [TICKER]'s [asset]. (1) Dosing/route vs SOC and competitors; (2) comparator endpoint design; (3) safety differentiation; (4) label breadth; (5) payor reimbursement readiness; (6) verdict — differentiated or me-too.

## SUB-BIO-05 · CMC and COGS Scalability Check
Tags: `#biotech #modeling #senior-judgment`
**When to use.** When manufacturing path from clinical to commercial scale is thesis-relevant.
**Inputs.** Filings, manufacturing disclosures, CDMO contracts.
**Output.** CMC assessment with COGS and margin.

PROMPT:
> Evaluate CMC readiness and COGS for [TICKER]'s [asset]. (1) Modality and scale-up complexity; (2) manufacturing setup; (3) specific bottleneck; (4) COGS at peak volume vs benchmarks; (5) gross margin implication; (6) CMC regulatory risk.

## SUB-BIO-06 · Freedom to Operate (FTO) IP Analysis
Tags: `#biotech #thesis #senior-judgment`
**When to use.** When IP exclusivity is thesis-critical.
**Inputs.** Patent databases, SEC disclosures, Para IV filings.
**Output.** IP risk assessment with thesis implications.

PROMPT:
> FTO analysis for [TICKER]'s [asset]. (1) Core IP estate by type and geography; (2) Orange/Purple Book listing; (3) third-party blocking IP; (4) IPR challenge durability; (5) lifecycle management; (6) net assessment: strong/adequate/fragile.

## SUB-BIO-07 · FDA Meeting History Risk Extraction
Tags: `#biotech #fda-ema #senior-judgment`
**When to use.** When evaluating regulatory risk beyond generic projections.
**Inputs.** SEC filings, presentations, FDA correspondence, Drugs@FDA.
**Output.** Regulatory risk assessment with evidence.

PROMPT:
> Regulatory history for [TICKER]'s [asset]. (1) Type A/B/C meeting outcomes; (2) friction signals; (3) pathway viability; (4) CRL history for class; (5) AdCom likelihood; (6) net risk: low/medium/high.

## SUB-MED-03 · 510(k) Predicate Validity Check
Tags: `#medtech #fda-ema #senior-judgment`
**When to use.** When the 510(k) predicate choice is thesis-relevant.
**Inputs.** FDA 510(k) database, classification, regulatory disclosures.
**Output.** Predicate risk assessment.

PROMPT:
> Evaluate predicate for [TICKER]'s [device]. (1) Predicate identity and clearance date; (2) validity — is it outdated or under different standards; (3) substantial equivalence argument; (4) rejection risk; (5) De Novo/PMA cost and timeline if forced; (6) thesis impact.

## SUB-MED-04 · De Novo vs PMA Regulatory Pathway Risk
Tags: `#medtech #fda-ema #senior-judgment`
**When to use.** For novel devices where pathway choice is material.
**Inputs.** FDA classification, regulatory strategy, recent decisions.
**Output.** Pathway risk with timeline and NPV sensitivity.

PROMPT:
> De Novo vs PMA for [TICKER]'s [device]. (1) Classification; (2) De Novo requirements and timeline; (3) PMA requirements if escalated; (4) competitive moat implications; (5) revenue delay NPV impact; (6) recent comparables.

## SUB-TLS-03 · LDT Regulatory Oversight Impact
Tags: `#tools-dx #fda-ema #senior-judgment`
**When to use.** When FDA's Laboratory Developed Test rule materially affects a diagnostics name.
**Inputs.** Company disclosures, FDA LDT final rule, competitive landscape.
**Output.** LDT regulatory impact with compliance cost and margin effect.

PROMPT:
> LDT oversight impact for [TICKER]. (1) Current LDT revenue as % of total and which tests are affected; (2) FDA's phased enforcement timeline and current status; (3) compliance cost — 510(k) or PMA filing for each at-risk test; (4) competitive impact — do large IVD manufacturers gain vs lab-specific LDTs; (5) margin impact at full compliance; (6) legal challenge status and probability of enforcement delay.

## SUB-TLS-05 · Companion Diagnostic Linkage and Precision Medicine Coupling
Tags: `#tools-dx #biotech #pharma #senior-judgment`
**When to use.** When evaluating a precision medicine therapy where a companion diagnostic governs use, or a diagnostics name whose revenue depends on therapy-test coupling.
**Inputs.** FDA approval letter and label for the therapy, CDx approval letter, clinical practice guidelines, peer commentary on testing patterns, company disclosures on testing volumes or partnerships.
**Output.** Therapy-diagnostic coupling analysis with volume flow, revenue translation, and model implications for both names.

PROMPT:
> Map the therapy-to-test linkage for [therapy TICKER] and [diagnostic TICKER]. (1) Regulatory coupling — is the companion diagnostic mandatory per the FDA label (CDx specified in the indications or dosing section), supportive but not required, or unapproved but commonly used? Cite the exact label language from Drugs@FDA. (2) CDx status — is the diagnostic FDA-approved as a CDx, CE-marked, or operating as a Laboratory Developed Test (LDT); which sponsor holds the approval and what testing platforms are covered. (3) Competing tests — list every test validated against the same biomarker, including LDTs from major reference labs (Quest, Labcorp, academic centres); rank by clinical adoption and by payor reimbursement; identify which test will actually capture volume in practice. (4) Volume flow — given the therapy's expected label, patient population, and testing cascade, what diagnostic test volume is realistically attributable to therapy uptake vs other indications testing the same biomarker? (5) Revenue translation — for the diagnostic company, the revenue contribution from this specific therapy launch; for the therapy company, the risk that test availability, turnaround time, or cost constrains prescription; for both, the scenario where LDT competition erodes the approved CDx's pricing. (6) Adoption acceleration or constraint — does the CDx accelerate therapy uptake (by defining an eligible population clearly) or constrain it (by adding diagnostic friction before prescribing)? (7) Model implications for both names. End with the confidence score.
