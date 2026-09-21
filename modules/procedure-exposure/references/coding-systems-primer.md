# Coding Systems Primer — keeping the code systems straight

Investment-analysis orientation; the healthcare coding profession's full rules are out of scope.

## The systems and what they key

| System | Codes | What they describe | Where used | Rates live in |
|---|---|---|---|---|
| **ICD-10-CM** | A00–Z99 alphanumeric dx codes | Diagnoses — why care happened; medical necessity | All settings, all claims | (Gates payment; doesn't price it) |
| **ICD-10-PCS** | 7-char procedure codes | Inpatient hospital procedures | Inpatient claims → group to DRGs | IPPS (DRG payments) |
| **MS-DRG** | ~770 groups | Inpatient episode payment bundles | Medicare inpatient | IPPS final rule (annual, FY, Oct 1) |
| **CPT (HCPCS Level I)** | 5-digit; Cat I permanent, Cat II quality, Cat III temporary/emerging | Physician and outpatient procedures/services | Professional & outpatient claims | PFS (professional), OPPS/ASC (facility) — CY, Jan 1 |
| **HCPCS Level II** | Letter+4 digits (J-codes drugs, C-codes device pass-through, G/A/L etc.) | Drugs, devices, supplies, temp services | Outpatient/DME/drug billing | ASP files, OPPS, fee schedules |

Update cadence: ICD-10 annually effective **Oct 1**; CPT annually effective **Jan 1** (Cat III and editorial actions released during the year); HCPCS quarterly-to-annually; payment rules per the CMS calendar (cms-reimbursement plugin).

## The ladder new technology climbs

Unlisted/miscellaneous code (unpredictable payment, invisible in data) → Category III CPT or temporary HCPCS (trackable, payment contractor-discretionary) → **Category I CPT** (requires widespread use + literature — promotion is itself adoption evidence) / dedicated ICD-10 codes → stable fee-schedule or DRG placement (± NTAP/TPT bridges in the interim). Each rung: public, dated, catalyst-grade.

## Analyst rules

1. **Name the system** every claim rests on; "the code" is ambiguous across five systems.
2. **Coding ≠ coverage ≠ payment** — a code's existence doesn't mean payors cover it (cms-reimbursement) or that the rate is viable.
3. **Dx codes gate, procedure codes price** — eligible-population arguments run on ICD-10-CM; revenue-per-case arguments run on CPT/HCPCS/DRG.
4. **Site of service changes the code and the price** — the same clinical act bills differently inpatient/HOPD/ASC/office; site-shift is repricing without volume change.
5. **Volume data follows codes** — you can only track what has a code; unlisted-code products are dark to claims data (a diligence fact in itself).
6. **Code churn breaks time series** — check for redefinitions/splits before reading a volume discontinuity as demand.
