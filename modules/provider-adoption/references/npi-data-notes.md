# NPI Data Notes — what the registry is and how to query it well

## What an NPI is

The National Provider Identifier is the HIPAA-mandated ID every US healthcare provider needs to bill electronically. Two types: **Type 1** (individual clinicians — physicians, NPs, PAs, therapists) and **Type 2** (organizations — hospitals, group practices, labs, pharmacies, DME suppliers). One clinician = one NPI for life; organizations can hold several (subparts).

## What a record contains

Name, NPI type, **taxonomy code(s)** (specialty, with one flagged primary), practice address(es), mailing address, enumeration date, deactivation/reactivation flags, and sometimes organizational affiliation and endpoint data. No volumes, no claims, no quality data, no payer mix.

## Taxonomy mapping discipline

Taxonomies are the Healthcare Provider Taxonomy Code Set (e.g., cardiology and its sub-specialties like interventional cardiology or clinical cardiac electrophysiology; medical oncology vs hematology-oncology; vascular surgery vs vascular & interventional radiology). Rules of thumb:

- Start from the clinical reality (who actually delivers this product) and enumerate ALL plausible taxonomies, including NP/PA taxonomies where mid-levels prescribe, then justify inclusions/exclusions in the recorded query definition.
- Primary vs secondary taxonomy matters: querying primary-only undercounts dual-boarded specialists; state which was used.
- Facility-gated products (capital equipment, certification programs, REMS-restricted drugs) need Type 2 organizational counts alongside Type 1 clinician counts.

## Known biases and hygiene

- **Registration lag & stale records:** clinicians register at training exit and rarely update addresses promptly; deactivation reporting lags retirement/death. Counts skew high; locations skew stale.
- **Never diff mismatched queries:** period-over-period comparisons require the identical query definition; prefer matched-cohort tracking of named NPIs (adds/drops/net) over raw count subtraction.
- **Address ≠ practice site:** billing addresses can be administrative; for site-level claims corroborate with the organization's own listings.
- **Snapshot dating:** every count carries a retrieval date; the registry is updated continuously.

## Complementary public datasets (via web research, when volume or payment context is needed)

CMS Physician & Other Practitioners utilization files (code-level volumes by NPI — the bridge to procedure-exposure), Open Payments (industry payments to clinicians — KOL conflict checks), Medicare Provider Enrollment, and hospital cost reports. Cite vintage; most are annual with a lag.
