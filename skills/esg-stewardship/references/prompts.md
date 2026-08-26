# Prompts — ESG Integration & Stewardship

From the Healthcare Equity Analyst Prompt Library v1.4. Standing instructions apply (`${CLAUDE_PLUGIN_ROOT}/CLAUDE.md`). Fill bracketed inputs.

## ESG-01 · Healthcare Materiality Map
Tags: `#esg #cross-sector #senior-judgment`
**When to use.** When initiating coverage and need materiality beyond MSCI/Sustainalytics.
**Inputs.** Sustainability report, 10-K, proxy, ESG ratings.
**Output.** Materiality map with forward flags.

PROMPT:
> Materiality map for [TICKER] per SASB/IFRS S1-S2 and CSRD double-materiality. E: scope 1-2-3, decarbonisation, water/waste. S: drug pricing/access, product safety, trial diversity, workforce. G: capital allocation, comp alignment, board, audit. Per item: financial materiality, disclosure quality, performance. 2–3 forward-looking materiality flags.

## ESG-02 · Stewardship Engagement Plan
Tags: `#esg #mgmt-meeting #cross-sector #senior-judgment #pm-level`
**When to use.** When designing an engagement arc on an ESG-material issue.
**Inputs.** Issue; company position; position size.
**Output.** Engagement plan with escalation and reporting.

PROMPT:
> Engage [TICKER] on [issue]. (1) Financial materiality case; (2) specific ask; (3) counterparty sequencing; (4) 12–24 month milestones; (5) escalation; (6) coalition; (7) reporting (SFDR Art 9, UK Stewardship Code).

## ESG-04 · Access to Medicine Index and EM Pricing Strategy Review
Tags: `#esg #pharma #senior-judgment`
**When to use.** Annual review for pharma where access is commercially material.
**Inputs.** AtMI scorecard, sustainability report, EM strategy.
**Output.** Access strategy review with peer benchmark.

PROMPT:
> Access review for [TICKER]. (1) AtMI scorecard; (2) assets where access shapes TAM; (3) peer comparison; (4) LMIC commercial upside; (5) engagement opportunity.

## ESG-05 · Healthcare Climate Risk and Decarbonisation Pathway Assessment
Tags: `#esg #cross-sector #pharma #medtech #tools-dx #senior-judgment`
**When to use.** When integrating climate physical and transition risk into healthcare investment work, particularly for CSRD-reporting companies and the TCFD/IFRS S2 disclosure regime.
**Inputs.** Company sustainability report, CSRD statement or TCFD disclosure, CDP submission if available, facility location data, supplier disclosure, peer benchmarks.
**Output.** Climate risk map with physical and transition risk inventory, pathway credibility assessment, financial materiality scoring, and engagement opportunity.

PROMPT:
> Map [TICKER]'s exposure to climate physical risk and transition risk as material to the investment case, consistent with TCFD, IFRS S2, and EU CSRD double-materiality reporting. (1) Physical risk inventory — manufacturing and R&D sites by location, with exposure to acute hazards (flooding, wildfire, tropical storm) and chronic hazards (heat stress, water scarcity, sea-level rise). Pharma and biologics manufacturing is particularly exposed because of dependence on water-intensive processes, cold-chain logistics, and single-source facilities. Quantify using the company's disclosure under CSRD ESRS E1 or equivalent if available, supplemented by public facility location data. (2) Supply chain physical risk — API manufacturing concentration (India, China for small-molecule; US, EU, Puerto Rico for biologics), single-source supplier exposure, and the realistic disruption scenario. The 2017 Hurricane Maria IV bag shortage is the canonical precedent. (3) Transition risk — decarbonisation pathway credibility. Pharma scope 1 and 2 emissions are manageable (facility electrification, renewable power purchasing); scope 3 dominates and is driven by supplier emissions (APIs, excipients, packaging, distribution). Credible pathways require supplier engagement programmes, not just own-operation targets. Medtech transition risk concentrates in single-use disposables and device take-back. (4) Product-level carbon footprint — is the company disclosing product carbon footprint (PCF) for major products? NHS and several European procurement bodies are beginning to factor PCF into formulary decisions. This is an emerging commercial exposure, not just a disclosure exercise. (5) Regulatory exposure — EU CSRD Article 8 implementation timeline for the company's size class, UK-specific TCFD and SDR requirements, and the SEC climate disclosure rule status. (6) Financial materiality score — rank physical, transition, and regulatory risk from 0 to 3 on financial materiality over a 3-year and 10-year horizon. The 10-year score often differs materially from the 3-year score, and both matter for long-duration holders. (7) Engagement opportunity — if climate disclosure or pathway credibility is materially weaker than peers, is this an engagement priority? Reference to CA100+ targets or the IIGCC Net Zero Investment Framework where applicable. End with confidence score.

## SUB-DIG-03 · Health Equity and Digital Divide Assessment
Tags: `#digital-health #esg #senior-judgment`
**When to use.** When evaluating whether a digital health platform's architecture limits its realistic TAM.
**Inputs.** Platform architecture docs, clinical study demographics, CMS programme eligibility.
**Output.** Health equity TAM assessment with competitive implication.

PROMPT:
> Assess [TICKER]'s health equity profile. (1) Platform accessibility — minimum bandwidth, hardware requirements, language support, literacy assumptions; (2) Medicaid population reach — can the platform serve low-income, rural, or elderly populations where government-sponsored healthcare is the primary payor? (3) Clinical validation diversity — were clinical studies conducted across representative demographics? (4) Regulatory tailwinds — does the platform qualify for CMS innovation centre programmes, FQHC funding, or state Medicaid waivers? (5) TAM implication — if the platform cannot serve Medicaid/dual-eligible populations, what percentage of the claimed TAM is effectively inaccessible? (6) Competitive positioning — are competitors specifically targeting underserved populations, creating a flanking risk?
