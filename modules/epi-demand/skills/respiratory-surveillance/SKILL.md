---
name: respiratory-surveillance
description: >
  This skill should be used when the user asks about "flu season", "RSV", "COVID
  wave", "respiratory surveillance", "FluView", "wastewater data", "test volumes",
  "vaccine season", or wants a near-term demand read for vaccines, respiratory
  diagnostics or antivirals.
metadata:
  version: "0.1.0"
  layer: "Commercial"
---

# Respiratory surveillance nowcast

Convert weekly public surveillance into a near-term demand read for respiratory
vaccines, diagnostics and therapeutics — and be explicit about what is provisional.

## Workflow

1. **Pull the series** (`scripts/surveillance.py`): outpatient influenza-like illness
   (wILI), clinical and public-health laboratory percent positivity by pathogen,
   hospitalisation rates, and wastewater concentration levels from NWSS.
2. **Establish the baseline.** Compare against the same week in the previous three to
   five seasons, not against last week. Respiratory demand is violently seasonal and a
   week-on-week number tells you almost nothing.
3. **Separate activity from testing.** Percent positivity rises when activity rises *or*
   when testing narrows to symptomatic patients. Test volume and positivity must be read
   together, and a positivity spike with falling test volume is mostly a testing artefact.
4. **Watch coverage changes.** Laboratory participation in NREVSS and site participation
   in NWSS change between seasons. A step in the series that coincides with a
   participation change is not epidemiology.
5. **Map to the revenue line.** Different products respond to different parts of the
   curve, at different lags:
   - **Vaccines**: demand is set in the September–November administration window and by
     retail pharmacy capacity, not by peak season severity. A severe December helps next
     season's uptake more than this season's revenue.
   - **Diagnostics**: respond within one to two weeks of activity; the most direct link.
   - **Antivirals**: track symptomatic presentations and prescribing, lagging activity
     slightly.
   - **Hospital-facing products**: track the hospitalisation series, which lags cases.
6. **Size it.** State the revenue line, the historical relationship between the series
   and reported quarterly revenue for that product in prior seasons, and the residual.
   A nowcast with no historical fit is a chart, not evidence.
7. Emit the brief with **provisional** stated in the vintage field.

## Not-automatic

Surveillance activity does not license a revenue conclusion without the historical
relationship between the series and that specific product's reported revenue. Severity
and revenue are related but the relationship differs by product type and by season.

Contract: `../../references/evidence-brief.md`.
