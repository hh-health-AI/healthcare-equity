# Passage entailment prompt v1

For each item in the supplied corpus, assess the claim against only that item's
passage. Do not use world knowledge or assume missing information. The passages
are explicitly marked author paraphrases of retrieved primary-source records.

Return an object with a `predictions` array, one row per corpus ID, containing
`id`, `label`, and a short `rationale`. Use:

- `supported`: the passage provides the material facts required by the claim.
- `contradicted`: the passage provides materially incompatible facts.
- `insufficient`: the passage neither establishes nor refutes the claim.
- `abstain`: you cannot complete the assessment (a processing failure or genuine
  inability to assess), distinct from an ordinary insufficient-evidence verdict.

Keep populations, dates, units, comparator, endpoint and statistical uncertainty
intact. A registry completion date is not a disclosure date. A historical FDA
announcement is not a current label. A confidence interval crossing the null does
not establish conventional two-sided 5% statistical significance. A cash balance
alone does not establish runway. Return no aggregate scores.

The caller must provide the corpus without the answer key and archive this exact
prompt, the submitted input, the complete model response, model/provider version
and execution timestamp before invoking the deterministic scorer.

## Submitted blind corpus

```json
{
  "schema_version": 1,
  "benchmark_id": "hh-healthcare-passage-entailment-v1",
  "frozen_at": "2026-10-08T10:17:07.651625+00:00",
  "scope": "Public development set of author-paraphrased primary-source passages; passage entailment only",
  "label_policy": {
    "supported": "Passage establishes material claim facts",
    "contradicted": "Passage provides materially incompatible facts",
    "insufficient": "Passage neither establishes nor refutes the claim",
    "abstain": "Prediction only: system declines or fails to classify"
  },
  "items": [
    {
      "id": "REG-01",
      "domain": "registry",
      "source_id": "CTG-ACTT1",
      "locator": "protocolSection.designModule.enrollmentInfo",
      "passage_kind": "author_paraphrase",
      "passage": "ACTT-1 lists ACTUAL enrollment of 1,062 participants. Its narrative describes an initial projection of 572.",
      "claim": "The registry reports 1,062 as the actual enrollment."
    },
    {
      "id": "REG-02",
      "domain": "registry",
      "source_id": "CTG-ACTT1",
      "locator": "protocolSection.designModule.enrollmentInfo; descriptionModule.detailedDescription",
      "passage_kind": "author_paraphrase",
      "passage": "ACTT-1 lists ACTUAL enrollment of 1,062 participants. Its narrative describes an initial projection of 572.",
      "claim": "ACTT-1 enrolled exactly 572 participants according to its actual-enrollment field."
    },
    {
      "id": "REG-03",
      "domain": "registry",
      "source_id": "CTG-ACTT1",
      "locator": "protocolSection.designModule.designInfo",
      "passage_kind": "author_paraphrase",
      "passage": "The registry describes randomized allocation, parallel assignment and double masking, with participants and investigators masked.",
      "claim": "ACTT-1 used randomized allocation and masked both participants and investigators."
    },
    {
      "id": "REG-04",
      "domain": "registry",
      "source_id": "CTG-ACTT1",
      "locator": "protocolSection.designModule.designInfo",
      "passage_kind": "author_paraphrase",
      "passage": "The registry describes randomized allocation, parallel assignment and double masking, with participants and investigators masked.",
      "claim": "The registry describes ACTT-1 as an open-label trial."
    },
    {
      "id": "REG-05",
      "domain": "registry",
      "source_id": "CTG-ACTT1",
      "locator": "protocolSection.statusModule.primaryCompletionDateStruct",
      "passage_kind": "author_paraphrase",
      "passage": "The primary-completion field is an ACTUAL date of 2020-05-21. The extracted field does not identify a sponsor-announced readout date.",
      "claim": "The sponsor publicly released the final ACTT-1 results on 21 May 2020."
    },
    {
      "id": "REG-06",
      "domain": "registry",
      "source_id": "CTG-ACTT1",
      "locator": "protocolSection.designModule.designInfo",
      "passage_kind": "author_paraphrase",
      "passage": "The registry describes randomized allocation, parallel assignment and double masking, with participants and investigators masked.",
      "claim": "Remdesivir reduced 29-day mortality by a statistically significant amount."
    },
    {
      "id": "PUB-01",
      "domain": "publication",
      "source_id": "PMID-32445440",
      "locator": "MedlineCitation/Article/Abstract/AbstractText[@Label=\"RESULTS\"]",
      "passage_kind": "author_paraphrase",
      "passage": "The final ACTT-1 abstract gives recovery medians of 10 days with remdesivir and 15 with placebo; the recovery comparison has P<0.001.",
      "claim": "Median recovery was five days shorter with remdesivir than with placebo."
    },
    {
      "id": "PUB-02",
      "domain": "publication",
      "source_id": "PMID-32445440",
      "locator": "MedlineCitation/Article/Abstract/AbstractText[@Label=\"RESULTS\"]",
      "passage_kind": "author_paraphrase",
      "passage": "The final ACTT-1 abstract gives recovery medians of 10 days with remdesivir and 15 with placebo; the recovery comparison has P<0.001.",
      "claim": "Placebo patients recovered in a median 10 days and remdesivir patients in 15."
    },
    {
      "id": "PUB-03",
      "domain": "publication",
      "source_id": "PMID-32445440",
      "locator": "MedlineCitation/Article/Abstract/AbstractText[@Label=\"RESULTS\"]",
      "passage_kind": "author_paraphrase",
      "passage": "By day 29, estimated mortality was 11.4% with remdesivir versus 15.2% with placebo; mortality HR=0.73, 95% CI 0.52–1.03.",
      "claim": "The mortality hazard-ratio point estimate favored remdesivir, but its 95% interval included 1."
    },
    {
      "id": "PUB-04",
      "domain": "publication",
      "source_id": "PMID-32445440",
      "locator": "MedlineCitation/Article/Abstract/AbstractText[@Label=\"RESULTS\"]",
      "passage_kind": "author_paraphrase",
      "passage": "By day 29, estimated mortality was 11.4% with remdesivir versus 15.2% with placebo; mortality HR=0.73, 95% CI 0.52–1.03.",
      "claim": "The reported mortality interval excluded 1, establishing conventional two-sided 5% statistical significance."
    },
    {
      "id": "PUB-05",
      "domain": "publication",
      "source_id": "PMID-32445440",
      "locator": "MedlineCitation/Article/Abstract/AbstractText[@Label=\"METHODS\"]",
      "passage_kind": "author_paraphrase",
      "passage": "The final report studied intravenous treatment in hospitalized adults with COVID-19 and lower-respiratory infection, comparing remdesivir with placebo.",
      "claim": "These data establish efficacy for children receiving remdesivir at home."
    },
    {
      "id": "PUB-06",
      "domain": "publication",
      "source_id": "PMID-32445440",
      "locator": "MedlineCitation/Article/Abstract/AbstractText[@Label=\"RESULTS\"]",
      "passage_kind": "author_paraphrase",
      "passage": "The final ACTT-1 abstract gives recovery medians of 10 days with remdesivir and 15 with placebo; the recovery comparison has P<0.001.",
      "claim": "The trial established a statistically significant reduction in long-COVID symptoms at one year."
    },
    {
      "id": "FDA-01",
      "domain": "regulatory",
      "source_id": "FDA-20201022",
      "locator": "Opening paragraph, FDA news release dated 2020-10-22",
      "passage_kind": "author_paraphrase",
      "passage": "On 22 October 2020, FDA approved Veklury for hospitalized COVID-19 patients aged at least 12 years and weighing at least 40 kg.",
      "claim": "The original announced approval covered a hospitalized 12-year-old weighing 40 kg."
    },
    {
      "id": "FDA-02",
      "domain": "regulatory",
      "source_id": "FDA-20201022",
      "locator": "Opening paragraph and pediatric EUA paragraph",
      "passage_kind": "author_paraphrase",
      "passage": "The October 2020 approval required age ≥12 and weight ≥40 kg. A revised EUA separately covered hospitalized younger or lighter children weighing ≥3.5 kg.",
      "claim": "FDA granted full approval in October 2020 for every hospitalized child weighing at least 3.5 kg."
    },
    {
      "id": "FDA-03",
      "domain": "regulatory",
      "source_id": "FDA-20201022",
      "locator": "Opening paragraph, administration-setting sentence",
      "passage_kind": "author_paraphrase",
      "passage": "FDA stated that Veklury administration should occur in hospital or another healthcare setting able to provide acute care comparable to inpatient care.",
      "claim": "The announcement permitted administration in an acute-care-equivalent healthcare setting outside a hospital."
    },
    {
      "id": "FDA-04",
      "domain": "regulatory",
      "source_id": "FDA-20201022",
      "locator": "Opening paragraph, administration-setting sentence",
      "passage_kind": "author_paraphrase",
      "passage": "FDA stated that Veklury administration should occur in hospital or another healthcare setting able to provide acute care comparable to inpatient care.",
      "claim": "The October 2020 announcement allowed administration in any setting, with no acute-care capability requirement."
    },
    {
      "id": "FDA-05",
      "domain": "regulatory",
      "source_id": "FDA-20201022",
      "locator": "Opening paragraph, historical release date 2020-10-22",
      "passage_kind": "author_paraphrase",
      "passage": "On 22 October 2020, FDA approved Veklury for hospitalized COVID-19 patients aged at least 12 years and weighing at least 40 kg.",
      "claim": "The current October 2026 US label still has exactly these age and hospitalization restrictions."
    },
    {
      "id": "FDA-06",
      "domain": "regulatory",
      "source_id": "FDA-20201022",
      "locator": "Opening paragraph, historical release date 2020-10-22",
      "passage_kind": "author_paraphrase",
      "passage": "On 22 October 2020, FDA approved Veklury for hospitalized COVID-19 patients aged at least 12 years and weighing at least 40 kg.",
      "claim": "EMA granted an identical approval on 22 October 2020."
    },
    {
      "id": "FIN-01",
      "domain": "financial",
      "source_id": "ABCL-2025-10K",
      "locator": "Item 8, Consolidated Statements of Loss and Comprehensive Loss, F-6; 2025 column; amounts in USD thousands",
      "passage_kind": "author_paraphrase",
      "passage": "AbCellera reported 2025 total revenue of 75,128 and net loss of 146,412, with both amounts in thousands of US dollars.",
      "claim": "AbCellera reported 2025 total revenue of $75.128 million."
    },
    {
      "id": "FIN-02",
      "domain": "financial",
      "source_id": "ABCL-2025-10K",
      "locator": "Item 8, Consolidated Statements of Loss and Comprehensive Loss, F-6; 2025 column; amounts in USD thousands",
      "passage_kind": "author_paraphrase",
      "passage": "AbCellera reported 2025 total revenue of 75,128 and net loss of 146,412, with both amounts in thousands of US dollars.",
      "claim": "AbCellera earned $146.412 million of GAAP net profit in 2025."
    },
    {
      "id": "FIN-03",
      "domain": "financial",
      "source_id": "ABCL-2025-10K",
      "locator": "Item 7, Financial Position table, December 31 2025 column; amounts in USD thousands",
      "passage_kind": "author_paraphrase",
      "passage": "At 31 December 2025, cash and equivalents were 128,513; marketable securities were 405,313; their combined total was 533,826, all in USD thousands.",
      "claim": "Cash, equivalents and marketable securities totaled $533.826 million at year-end 2025."
    },
    {
      "id": "FIN-04",
      "domain": "financial",
      "source_id": "ABCL-2025-10K",
      "locator": "Item 7, Financial Position table, December 31 2025 column; amounts in USD thousands",
      "passage_kind": "author_paraphrase",
      "passage": "At 31 December 2025, cash and equivalents were 128,513; marketable securities were 405,313; their combined total was 533,826, all in USD thousands.",
      "claim": "Cash and cash equivalents alone were $533.826 million at year-end 2025."
    },
    {
      "id": "FIN-05",
      "domain": "financial",
      "source_id": "ABCL-2025-10K",
      "locator": "Item 7, Financial Position table, December 31 2025 column; amounts in USD thousands",
      "passage_kind": "author_paraphrase",
      "passage": "At 31 December 2025, cash and equivalents were 128,513; marketable securities were 405,313; their combined total was 533,826, all in USD thousands.",
      "claim": "This balance proves the company can fund all activities through 2030 without further financing."
    },
    {
      "id": "FIN-06",
      "domain": "financial",
      "source_id": "ABCL-2025-10K",
      "locator": "Item 8, Consolidated Statements of Loss and Comprehensive Loss, F-6; 2025 column; amounts in USD thousands",
      "passage_kind": "author_paraphrase",
      "passage": "AbCellera reported 2025 total revenue of 75,128 and net loss of 146,412, with both amounts in thousands of US dollars.",
      "claim": "AbCellera will report at least $100 million of revenue in 2026."
    }
  ]
}
```
