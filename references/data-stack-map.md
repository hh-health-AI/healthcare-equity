# Data-Stack Map — breadth vs depth, and what answers what

For "should we buy tool X" questions and for routing hard questions to the right class of source. Core insight (industry-wide, as of Aug 2026): **breadth tools and depth tools are different products, and serious teams run both** — standing coverage/alerts on one side, primary-document depth on the other. This suite's watcher agents are the standing-coverage layer; its engines are free depth on four public data moats.

| Tool class | Exemplars | What it actually holds | The question it answers | What it does NOT do |
|---|---|---|---|---|
| Curated breadth / change alerts | Cortellis-class suites | Analyst-curated summaries + pipeline/deals modules, ~80+ markets, alerting | "What changed anywhere in my jurisdictions this week?" | Passage-level citations; clearance/review-level precedent — "device teams end up back in the primary documents anyway" |
| Requirements libraries | IQVIA RI-class | Current registration requirements, 110+ countries | "What are the rules to file in market X?" | Holds the rule, not the evidence — no reviews, no precedent, no "so what" |
| Primary-document depth | Rhizome-class (MCP connector; free tier limited; non-English HAs Enterprise-only) | ~51M primary health-authority documents (reviews, CRLs, 510(k)s, EPARs, 483s/WLs), passage-level citations | "What did regulators actually accept/refuse, across the last 30 comparable programs?" | Standing feeds/alerts; pipeline/deals data; CMS payment; market data |
| Pipeline/deals databases | Cortellis CI + Deals-class | Curated pipeline, partnering, deal terms | "Who is developing what, and what were the deal terms?" | Primary-source traceability |
| Market data & consensus | Bloomberg / FactSet terminals | Prices, consensus, ownership, screening | "What is priced in?" (the Valuation layer) | Regulatory or clinical evidence; this suite only *generates syntax* for them |
| Transcripts/filings | Quartr-class, EDGAR | Calls, filings, events | The Financial layer of the investable view | — |
| General AI (unconnected) | Chat assistants without connectors | Model memory + open web | Orientation and drafting | Health-authority corpora; citations that survive the click |
| **This suite's engines** | CMS Coverage · Clinical Trials · PubMed · NPI · ICD-10 (free, hosted) | The four public data moats + methodology | Coverage/payment, trials/catalysts, capacity, volume — composed into the investable view | Paid-tool breadth; commercial claims data |

## Buying rules of thumb

- Buy **breadth** (Cortellis/IQVIA-class) when multi-market standing coverage is the daily job — a portfolio of global names with jurisdictional change risk. Its alerting is the feature buyers credit; its curated layer is not precedent.
- Buy **depth** (Rhizome-class) when precedent questions decide positions — approval odds, endpoint acceptance, predicate strategy, enforcement history. Verifiable passage-level citation is the differentiator; the free tier makes the trial costless.
- **Never substitute either for the terminal** (Valuation layer) or for this suite's engines (they cover what none of the above hold: CMS payment mechanics, NPI capacity, ICD-10/volume linkage).
- The failure mode to avoid is paying for breadth to answer depth questions or vice versa — state which class a question belongs to before proposing a purchase.
