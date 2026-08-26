# Prompts — Portfolio Construction & Risk

From the Healthcare Equity Analyst Prompt Library v1.4. Standing instructions apply (`${CLAUDE_PLUGIN_ROOT}/CLAUDE.md`). Fill bracketed inputs.

## PORT-01 · Healthcare Sleeve Positioning Review
Tags: `#portfolio #cross-sector #pm-level`
**When to use.** Quarterly positioning review.
**Inputs.** Sleeve composition; benchmark; macro view.
**Output.** Sleeve review, 1,000–1,500 words, with action list.

PROMPT:
> Review healthcare sleeve. (1) Sub-sector mix vs benchmark; (2) factor exposure; (3) concentration; (4) coherence test; (5) liquidity; (6) 2 trims, 2 adds, 1 missing exposure.

## PORT-02 · Catalyst Concentration and Path Dependence Map
Tags: `#portfolio #risk #biotech #cross-sector #pm-level`
**When to use.** When multiple binary catalysts cluster.
**Inputs.** Sleeve; catalyst calendar.
**Output.** Catalyst map with hedges.

PROMPT:
> Map all catalysts in next 90 days. (1) Calendar concentration; (2) factor concentration; (3) worst/best P&L scenarios; (4) hedge suggestions; (5) pre-trim vs hold/add per event.

## PORT-03 · Pair Trade Construction
Tags: `#portfolio #thesis #cross-sector #senior-judgment`
**When to use.** When expressing a relative-value insight.
**Inputs.** Two tickers; rationale; spread.
**Output.** Pair trade memo, 600–1,000 words.

PROMPT:
> Long [A] / Short [B]. (1) Relative-value mechanism; (2) beta/factor neutralisation; (3) catalyst alignment; (4) borrow cost and squeeze risk; (5) entry/target/stop; (6) carry.

## PORT-04 · Borrow, Float, and Short Interest Analysis
Tags: `#portfolio #risk #cross-sector #bloomberg #senior-judgment`
**When to use.** Before initiating or sizing a short.
**Inputs.** SI data, borrow rates, float details, catalyst calendar.
**Output.** Short setup report with sizing recommendation.

PROMPT:
> Short setup for [TICKER]. (1) SI as % float and days-to-cover; (2) borrow availability/cost; (3) float dynamics; (4) squeeze risk catalysts; (5) retail/momentum signals; (6) structural vs tactical; (7) sizing recommendation.

## SCR-06 · 13F Institutional Ownership Delta Scanner
Tags: `#screen #cross-sector #sec-filings #senior-judgment`
**When to use.** Quarterly after 13F filings.
**Inputs.** 13F data; my portfolio.
**Output.** Ownership delta table with conviction, contrarian, and crowding flags.

PROMPT:
> Extract 13F data for top 20 healthcare funds. (1) Net buying/selling by name; (2) conviction signals (3+ funds initiating); (3) contrarian signals; (4) crowding risk (>40% of float); (5) my portfolio ownership delta.

## SCR-07 · Cross-Sector Correlation Identifier
Tags: `#screen #portfolio #cross-sector #bloomberg #senior-judgment`
**When to use.** When portfolio has hidden macro linkages.
**Inputs.** Holdings; macro index data.
**Output.** Correlation matrix with scenario analysis.

PROMPT:
> 5-year rolling correlation between healthcare holdings and: (1) tools vs SOXX; (2) payors vs 10Y yield; (3) hospitals vs employment; (4) biotech vs XBI/R2000; (5) digital health vs WCLD. Per pair: correlation, R², scenario for spike or breakdown. Flag unintended macro bets.

## TECH-05 · SEC EDGAR Autonomous Agent Configuration
Tags: `#data-extraction #cross-sector #sec-filings #senior-judgment`
**When to use.** When setting up automated monitoring of SEC filings for thesis-relevant events.
**Inputs.** Coverage universe CIK numbers; filing types; keyword list.
**Output.** Agent configuration with API endpoints and JSON schema.

PROMPT:
> Configure an autonomous agent to monitor SEC EDGAR filings across my coverage universe. (1) Form 4 insider trading — flag any open-market purchase >$100K by C-suite or board members, cross-referenced against upcoming catalyst calendar. (2) 8-K current reports — parse for keywords: 'Complete Response Letter', 'CRL', 'accelerated approval', 'voluntary recall', 'consent decree', 'executive departure', and any material definitive agreement. (3) 13F institutional holdings — quarterly delta for the top 20 healthcare-focused funds. (4) Output as structured JSON mapped to predefined schemas: {ticker, form_type, filing_date, key_event, relevance_score}. (5) Provide the EDGAR XBRL API endpoint structure and the query parameters for each filing type.
