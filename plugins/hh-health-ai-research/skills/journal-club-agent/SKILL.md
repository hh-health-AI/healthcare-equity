---
name: journal-club-agent
description: Use to prepare a journal club, critical-appraisal discussion guide or
  eight-slide medical research briefing. Read the actual study and methods, preserve
  evidence boundaries, and distinguish a Markdown outline from an exported presentation
  file.
---

# Journal Club Agent

## Workflow

1. Identify paper, clinical question, audience and discussion time from the request. Unless another format is specified, use a concise eight-slide Markdown briefing. Do not treat this default as an instruction to ignore a requested presentation format.
2. Read the paper, methods and supplement; obtain registry, protocol or statistical analysis plan where material. Use Clinical Trial Analyst for an interventional trial. Record access gaps and precise source locators. Do not fill unreported methods with expected textbook practices.
3. Build a bounded evidence packet with actual observations, short supporting passages, appraisals, uncertainty and unresolved questions. Separate the authors' conclusion from what the design supports.
4. Draft eight slides: clinical question; study design; intervention/comparator; endpoints and analysis; effects and uncertainty; harms and missingness; validity and applicability; conclusions and open questions. Put the appropriate citation alongside each factual result.
5. Add useful speaker notes, three discussion questions and a short explanation of the most consequential statistical concept for this study. Clearly label any synthetic teaching example and keep it separate from the study data.
6. Check denominators, timepoints, relative versus absolute effects, confidence intervals, prespecified versus exploratory findings and applicability. Do not simplify away a limitation that could reverse the conclusion.
7. Deliver the actual format produced. Markdown is not PowerPoint. For a requested PPTX, PDF or other artifact, use an available artifact tool, preserve citations, inspect the resulting file and provide a real download link. If export is unavailable, state that only the outline was produced.
8. Close with what the study supports, what it cannot establish and the evidence that would change the interpretation. No personalized clinical treatment recommendation follows automatically from the teaching brief.

## Upstream distinction

The repository's optional journal-club command exports Markdown and JSON, not a PPTX file. This plugin supplies the appraisal workflow; it does not install that command or certify that the output has undergone independent clinical review.

## Shared controls and output

Read [evidence controls](references/evidence-controls.md) before executing this workflow and use the [connector map](references/connector-routing.md) for source selection. Use the [evidence brief](references/evidence-brief.md) when producing investment-related evidence. The workflows use the host's available tools; upstream Python utilities and the local MCP server are not included or deployed by this plugin.
