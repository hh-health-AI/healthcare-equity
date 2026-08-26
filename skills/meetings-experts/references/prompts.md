# Prompts — Management Meetings & Expert Networks

From the Healthcare Equity Analyst Prompt Library v1.4. Standing instructions apply (`${CLAUDE_PLUGIN_ROOT}/CLAUDE.md`). Fill bracketed inputs.

## MGMT-01 · 1-on-1 Question Stack
Tags: `#mgmt-meeting #cross-sector #transcripts #sec-filings #senior-judgment`
**When to use.** Before a 30–45 minute 1-on-1 with management.
**Inputs.** Last four transcripts, conference appearances, thesis memo.
**Output.** Three-tier question stack with follow-up scripts.

PROMPT:
> Build a tiered question stack for a 30-minute meeting with [TICKER]'s [role]. Tier 1 (must-ask, 5) — thesis-moving, hard to deflect. Tier 2 (good-to-ask, 5) — competitive/capital allocation tests. Tier 3 (colour, 5) — culture, talent, leading indicators. For Tier 1: exact wording, boilerplate answer, follow-up, informative answer. Avoid questions with public answers.

## MGMT-02 · What Has Already Been Asked? Filter
Tags: `#mgmt-meeting #cross-sector #transcripts #junior-task`
**When to use.** To avoid burning meeting time on already-answered questions.
**Inputs.** Draft questions; transcripts.
**Output.** Question-by-question audit table.

PROMPT:
> For each of my draft questions, search last four earnings calls and three conference appearances: (1) has it been asked; (2) management answer; (3) specific or hand-wave; (4) re-frame or drop.

## MGMT-03 · Site Visit Brief
Tags: `#mgmt-meeting #cross-sector #sec-filings #senior-judgment`
**When to use.** Before a manufacturing site visit, R&D centre tour, or hospital site visit.
**Inputs.** Site location, capex announcements, quality history.
**Output.** One-page brief with post-visit template.

PROMPT:
> Build a brief for visiting [TICKER]'s [site]. (1) What official agenda looks like and what they won't show; (2) five operational tells; (3) three questions for site lead; (4) safety/quality/culture signals; (5) post-visit synthesis template.

## MGMT-04 · KOL Day / Capital Markets Day Pre-Read
Tags: `#mgmt-meeting #biotech #pharma #medtech #ir-materials #senior-judgment`
**When to use.** Before a KOL day, R&D day, or capital markets day.
**Inputs.** Agenda, prior materials, KOL bios.
**Output.** Pre-read brief, 1,000–1,500 words.

PROMPT:
> Pre-read for [TICKER]'s [event] on [date]. (1) Agenda mapped to thesis; (2) prior precedent credibility scorecard; (3) expected new disclosures with ranges; (4) featured KOLs — bios, conflicts, questions; (5) peer cross-reads; (6) one-page note plan.

## EN-01 · Expert Call Prep Brief
Tags: `#expert-network #cross-sector #senior-judgment`
**When to use.** Before any expert network call.
**Inputs.** Expert profile; thesis question.
**Output.** Prep brief with MNPI-safe question stack.

PROMPT:
> Prep brief for [60]-minute call with [expert background]. Working on [TICKER / thesis]. (1) 5 questions only this expert can credibly answer; (2) wrong vs right answer for each; (3) calibration question; (4) question order for candour; (5) follow-up if hand-wave; (6) adjacent question worth one slot. MNPI guardrail: flag questions that could elicit material non-public information and rephrase to stay within public or general industry knowledge.

## EN-02 · Post-Call Debrief and Triangulation
Tags: `#expert-network #cross-sector #senior-judgment`
**When to use.** Within 24 hours of an expert call.
**Inputs.** Raw notes; thesis.
**Output.** Debrief memo, 600–1,000 words, with MNPI audit.

PROMPT:
> Debrief from call on [TICKER / topic]. (1) 3–5 insights with confidence scores; (2) 1–2 surprises vs my prior; (3) gap analysis; (4) credibility scorecard; (5) thesis update; (6) next call to triangulate; (7) one anonymised quote for client comms. MNPI audit: flag any insight that appears to stem from non-public information for compliance review.

## EN-03 · Expert Network Scoping Plan
Tags: `#expert-network #cross-sector #senior-judgment #pm-level`
**When to use.** When designing the expert network arc strategically.
**Inputs.** Thesis sketch; budget; network coverage.
**Output.** 8-week plan with sequencing and stop triggers.

PROMPT:
> Expert plan for [TICKER] over 8 weeks. (1) Map questions to expert profiles; (2) sequence for broad→specialist→thesis-specific; (3) budget and prioritisation; (4) conviction-shifting question per call; (5) stop trigger; (6) two calls for cross-triangulation.

## EN-04 · Expert-Management Divergence Triangulation
Tags: `#expert-network #thesis #cross-sector #senior-judgment #pm-level`
**When to use.** When an expert network call surfaces information that contradicts or materially differs from management's public statements, and the analyst must decide which source to weight and how to act.
**Inputs.** Expert call notes; relevant management statements (transcripts, slides, filings); any adjacent channel or alternative data.
**Output.** Divergence triangulation with credibility scores, verification path, pre-committed decision rule, and follow-up call design.

PROMPT:
> An expert call on [TICKER / topic] has surfaced information that diverges from management's public statements. Triangulate the divergence. (1) Specify the divergence precisely — what did the expert say, what has management said publicly (cite the specific call, slide, or filing), and in what dimension do they differ (fact, forecast, interpretation, sequencing)? Not all divergences are equivalent. (2) Expert credibility audit — how recent is the expert's direct experience? How specific is their claim (a concrete mechanism-level detail vs a general impression)? Is the claim within their verifiable scope of work or adjacent to it? Is the claim consistent with other independent data points I have gathered? Score the expert's claim on a 0–3 scale for recency, specificity, scope, and consistency. (3) Management incentive audit — what would management's incentive be to understate or overstate this specific dimension? Is the divergence in a direction consistent with known management tells (e.g. consistent under-promising on margin, consistent optimism on pipeline timing)? Prior guide-in vs deliver history matters here. (4) MNPI guardrail — if the expert's information would constitute material non-public information if sourced from management, I cannot act on it regardless of credibility. Flag this explicitly. If the divergence reflects the expert's opinion or synthesis of public information rather than non-public insider knowledge, it is tradeable. (5) Verification path — identify the independent data point that would confirm or refute the expert's claim without requiring another expert call. Channel data, competitor disclosure, regulatory filing, alternative data, or medical literature. Define the specific data and the threshold that would resolve the divergence. (6) Decision rule — in advance of verification, define what action the resolved divergence would trigger. If the expert is right, what do I do? If management is right, what do I do? Pre-committing to action prevents rationalisation after the fact. (7) Second expert call — design a follow-up call with a different expert whose scope of work could independently speak to the divergence, and specify the one question that would most efficiently resolve it. End with the action plan, the verification path, and the confidence score.

## SUB-DIG-01 · Enterprise Health-Tech Sales Cycle Diligence
Tags: `#digital-health #expert-network #senior-judgment`
**When to use.** When bookings and renewal economics matter more than reported revenue.
**Inputs.** Filings, IR commentary, peer commentary.
**Output.** Enterprise motion diligence with expert plan.

PROMPT:
> Enterprise sales diligence for [TICKER]. (1) Customer segmentation; (2) sales cycle stages and conversion; (3) renewal dynamics; (4) net revenue retention; (5) competitive bake-offs; (6) deterioration tells; (7) expert call list.
