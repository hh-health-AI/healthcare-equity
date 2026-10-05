---
name: evidence-modules
description: Use for healthcare reimbursement, clinical catalysts, utilization, epidemiology,
  provider adoption or economics, procedure exposure, safety, IP/exclusivity, international
  access, publications or SEC forensics. Produce source-bounded evidence briefs and
  model implications, not a generic overview.
---

# Healthcare Evidence Modules

## Select and bound the engine

Start with the exact decision, entity, geography, period and required units. Read the relevant module reference below; choose more than one only when the question requires their combined evidence. These are portable module briefs adapted from the canonical integration map. They do not reproduce every original subskill or scoring rubric.

- [Clinical and regulatory catalysts](references/clinical-catalysts.md): What changes approval probability, label, timing or clinical differentiation?
- [Publications, guidelines and KOL evidence](references/evidence-catalysts.md): How are publications, guidelines, abstracts and expert signals evolving?
- [FDA safety signals](references/fda-safety-signals.md): Do regulatory actions or safety reports change the risk profile?
- [Drug utilization](references/rx-utilization.md): What do published utilization and launch proxies imply about demand?
- [Epidemiology and demand](references/epi-demand.md): Which population and disease-burden observations define the demand funnel?
- [CMS reimbursement and access](references/cms-reimbursement.md): How do coverage, coding, payment and policy affect economics?
- [Provider adoption](references/provider-adoption.md): Is observed provider or site capacity translating into adoption?
- [Provider and payer economics](references/provider-economics.md): What do hospital, managed-care or nonprofit economics imply for customers and payers?
- [Procedure and code exposure](references/procedure-exposure.md): How do procedure codes and volumes map to addressable company exposure?
- [IP and exclusivity](references/ip-exclusivity.md): When could exclusivity loss, competition or patent proceedings change the revenue curve?
- [International market access](references/global-access.md): How do ex-US regulation, HTA, pricing and reimbursement affect launch and value?
- [SEC and financial forensics](references/sec-forensics.md): What do filings, accounting disclosures and ownership records imply?

## Common procedure

Retrieve the appropriate primary record or dataset through available tools. Confirm entity aliases, record granularity, definitions, reporting/effective dates, filters, result caps and denominator. Preserve the exact source or query so another researcher can retrace the finding. Cross-check material interpretation with a second relevant source where possible, without falsely treating correlated sources as independent evidence.

Extract facts before interpreting them. Produce an evidence brief with coverage and limitations, model implication status, prior/proposed assumption or unavailable, rationale, forbidden inference, next observable and confidence. When multiple engines affect the same assumption, reconcile their findings in one change log rather than adding their effects independently. A limited sample supports a limited statement, not a population conclusion.

For exact upstream methods beyond these briefs, use authorized GitHub reads to inspect the current module's README and skill directory before selecting a file. Do not invent names, claim an unread prompt was followed, or execute imported code. A retrieval failure is a declared gap, never evidence of absence.

## Shared controls and output

Read [evidence controls](references/evidence-controls.md) before executing this workflow and use the [connector map](references/connector-routing.md) for source selection. Use the [evidence brief](references/evidence-brief.md) when producing investment-related evidence. The workflows use the host's available tools; upstream Python utilities and the local MCP server are not included or deployed by this plugin.
