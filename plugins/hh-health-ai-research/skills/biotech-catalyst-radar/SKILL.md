---
name: biotech-catalyst-radar
description: Use for a defined biotech trial watchlist, registry-version comparisons,
  catalyst calendars or changed enrollment, status and completion estimates. Distinguish
  registry dates, sponsor readout guidance and regulatory decision dates; do not imply
  unscheduled background monitoring.
---

# Biotech Catalyst Radar

## Workflow

1. Resolve the watchlist to exact NCT IDs. Record sponsor/company/ticker mappings with sources and note aliases. Specify the comparison dates and watchlist version.
2. Obtain current registry records through actual tools and compare against supplied or user-authorized saved snapshots for the same IDs. A first observation establishes a baseline, not a change history. Do not compare against memory or invent a prior record.
3. Check retrieval success and completeness before updating state. On a failed or incomplete fetch, keep the prior successful record, identify the affected IDs and report a monitoring gap. Failed retrieval is not trial disappearance or NO_CHANGE.
4. Inspect changes in status, enrollment, endpoints, sites and completion estimates. Verify relevant context in primary records and sponsor disclosures. State plausible interpretations and what the changes cannot establish. Date slippage alone does not prove trial failure.
5. Maintain separate catalyst types: registry primary/study completion estimate; sponsor-guided data readout; conference presentation; filing; regulator-announced decision date. Record source date, date precision, timezone where relevant, confirmation status and last verification. Registry utilities do not establish PDUFA dates.
6. When the watchlist composition changes, create a separately identified baseline or explicitly reconcile additions/removals. Do not overwrite incompatible state. For each material change, record the old value, new value, source/version and model implication or remaining uncertainty.
7. Deliver the change report, calendar, coverage/gaps, implications, next observables and confidence. If there is no usable prior snapshot, deliver a clearly labeled baseline and current source-backed milestones.

## Scheduling boundary

This skill performs the present analysis. Only create a recurring watch when the user explicitly requests it and an actual scheduling tool is available. Preserve exact watchlist, source, timezone, cadence and notification conditions in an authorized scheduled task. Never promise future delivery from instructions alone. Installation of this plugin does not start a job, persist a watch state or send a notification.

## Shared controls and output

Read [evidence controls](references/evidence-controls.md) before executing this workflow and use the [connector map](references/connector-routing.md) for source selection. Use the [evidence brief](references/evidence-brief.md) when producing investment-related evidence. The workflows use the host's available tools; upstream Python utilities and the local MCP server are not included or deployed by this plugin.
