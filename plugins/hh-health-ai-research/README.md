# HH Health AI Research

**Version 0.1.0 · Private workflow edition · Source review 2026-10-04**

A single plugin adapted from **hh-health-AI/healthcare-equity**, the canonical integration repository for the HH Health AI healthcare research modules. It links biomedical and healthcare evidence to explicit commercial assumptions, valuation scenarios and falsifiable investment views.

## What is included

**13 instruction skills:** a front-door router; healthcare-equity research; the investable-view capstone; a twelve-module evidence workflow; and all nine biomedical workflow adaptations.

| Capability | Included workflow |
|---|---|
| Healthcare investment research | Initiation, earnings, valuation framing, thesis challenge, screens, portfolio research, meetings, sell discipline, international exposure, communications and stewardship. |
| Evidence engines | Clinical catalysts, publications/KOL evidence, safety, drug utilization, epidemiology, CMS reimbursement, provider adoption, provider economics, procedure exposure, IP/exclusivity, global access and SEC forensics. |
| Biomedical research suite | Medical evidence, trial analysis, claim checking, catalyst radar, literature review, public-data retrieval, biotech rNPV, conference evidence and journal club. |

The individual nine biomedical source skills and investable-view skill were read and adapted. The twelve evidence-module briefs and broader investment workflow map are concise adaptations of the canonical README, not full imports of every original subskill or reference library. The archive retains source blob identifiers and the original MIT notice.

## Start a conversation

Select the saved plugin, then ask a concrete research question. Examples:

> Build an investable view for ABCL using current primary evidence. Separate facts, assumptions and valuation scenarios, and identify a catalyst and falsifier.

> Compare this Phase III release with its ClinicalTrials.gov record and publication. Show discrepancies, supported claims and unresolved questions.

> Assess the reimbursement, utilization and provider-adoption evidence for this product. Show exactly which revenue assumptions change, remain unchanged or need more data.

> Prepare an eight-slide journal-club outline from this paper, including methods, effect sizes, harms, applicability and discussion questions.

## Evidence contract

Investment-related evidence updates use **CHANGE, NO_CHANGE, UNCERTAINTY_ONLY or NEEDS_DATA**, with the affected assumption, prior/proposed values or unavailable, rationale, source locator and next observable. The capstone distinguishes facts, inference, model impact, market-implied expectations, scenarios and falsifiers. Missing data remain missing.

## Data access and runtime

This is a **skills-only plugin**. It uses documents supplied by the user and the host's already available browsing, calculation and connected-data tools. Conditional routing covers ClinicalTrials.gov, PubMed, openFDA, DailyMed, RxNorm, CMS Coverage, CMS Open Data, NPI Registry, Medicare Care Compare and primary corporate sources. These tool names are routing guidance, not new app connections or guaranteed availability.

The upstream Python CLI and local stdio MCP server are **not included, installed, hosted or connected** by this package. Paid market/consensus data are not supplied. No background watch, filesystem ledger, scheduled notification, trade or message starts on installation. Local runtime setup instructions are included only as a reference for a separate user-requested setup task.

No GitHub repository was modified. This is a snapshot, not an automatically synchronized GitHub import. No secrets or private account connection IDs are included.

## Validation and limits

See [validation report](VALIDATION.md) for the exact static checks and [smoke-test specification](tests/smoke-cases.json) for expected behavior. Static validation does not certify live connector access, clinical validity, investment performance or end-to-end execution in every host. The upstream Python tests were not run because that implementation is not bundled. The journal-club default is Markdown; an actual PPTX/PDF requires the host's corresponding artifact tools.

Research outputs require appropriate professional judgment. Public data, papers and company disclosures retain their own licensing and access restrictions.

## Files

- plugin.json: portable Agent Plugins 1.0 manifest and listing metadata.
- skills/: thirteen workflows, shared controls, source notes and module references.
- provenance.json: reviewed source paths, observed Git blob identifiers and adaptation scope.
- LICENSE and NOTICE.md: original permission notice and adaptation disclosure.
- tests/: reproducible static checks and synthetic acceptance specifications.

Source repository: https://github.com/hh-health-AI/healthcare-equity
