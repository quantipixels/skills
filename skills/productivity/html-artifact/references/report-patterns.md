# Report Patterns

Read this file only when supplied material must become a report, including an evidence report, living report, or candidate comparison.

Do not use the em dash character (`—`) in visible report copy. Use a colon, comma, parentheses, or a separate sentence instead.

## Shape the record

Render a **snapshot** by default and show its generation time or evidence cutoff. Render a **living report** only when the owning task says the artifact will receive material updates. Keep stable section, candidate, and evidence anchors; show the last-updated time and evidence cutoff; mark supplied evidence status; and record supplied conclusion or disposition changes in a short revision log. Never replace an earlier conclusion silently.

Infer and label one broad industry only to choose familiar report structure and vocabulary. Do not infer industry facts. Select one exact format from the closest purpose family below and keep it stable unless the user fundamentally changes the focus. When several formats fit, choose by the decision the primary reader must make. Keep secondary purposes in supporting sections or appendices instead of creating a hybrid format.

| Purpose family | Common formats | Built-in emphasis |
| --- | --- | --- |
| Product and business definition | PRD; business plan; business case | For a PRD: problem, users, outcomes, requirements, non-goals, and success evidence. For a business plan or case: opportunity, customer, model, market evidence, go-to-market, operations, supplied financials, and risks |
| Design and experience | Product-design report | User need, journey or state model, visual evidence, findings, implications, and next actions |
| Delivery and operations | Project-management report; incident report or postmortem | Status, milestones, dependencies, risks, owners, and next actions; for an incident, add impact, timeline, response, recovery, and follow-up |
| Evidence and assurance | Evidence report; research report; audit report; experiment report | Question or criteria, method and scope, evidence, findings, confidence, limitations, gaps, and supplied conclusion or disposition |
| Decision and technical assessment | Decision brief; technical assessment | Options or current state, conceptual model, evidence, trade-offs, risks, supplied decision or priorities, owner, and next action |
| Performance and analytics | KPI report; financial report; marketing or sales performance report; operational dashboard | Targets, actuals, trends, variance, drivers, anomalies, and next actions |
| Comparison and selection | Competitive analysis; options comparison; vendor evaluation; candidate assessment | Common criteria, normalized evidence, comparable scale, trade-offs, risks, and supplied disposition or recommendation |
| Narrative and outcomes | Presentation-style report; case study | For a briefing: one message per section and a closing action. For a case study: context, challenge, intervention, outcome, evidence, and lessons |

These are selection cues, not fixed templates or an exhaustive list. Honor another user-named report format and infer its conventional structure from the supplied material. Omit unsupported sections. Use `slides` instead when the requested outcome is a slide deck rather than a portable report.

Select and label one density profile. Default to **Working**. Use **Executive** for a concise decision layer with material exceptions and actions while retaining complete coverage through disclosures or deep links. Use **Working** for the decision layer plus enough context and evidence to act. Use **Archival** for a complete record that still starts with the same scan layer. Density changes presentation, not coverage. Keep it stable unless the audience or its decision changes.

Before composing a substantial report, derive one coverage ledger from the supplied material. Inventory every explicit user question and deliverable; supplied conclusion, decision, recommendation, and limitation; and in-scope project, candidate, or other subject unit. Preserve any supplied depth contract for each unit. Mark every ledger item as one of:

- **Full record:** rendered with its required evidence and explanation.
- **Summary + deep link:** summarized in an overview and linked to its full stable anchor.
- **Input gap:** material source content is missing; return it to the owning task instead of inventing it.
- **Excluded with reason:** the supplied scope or authority excludes it.

An overview, metric, card, or visual does not replace a required full record. Do not omit an in-scope unit merely because it has no dramatic finding; show its supplied no-finding state or input gap. Before delivery, reconcile the ledger against the final anchors. A structurally valid artifact is incomplete while a material item has no disposition or a claimed deep link has no useful destination.

## Build the visual argument

Select the report's central visual from the highest-priority relationship or result in the coverage ledger. Apply the shared limits on prose and tables.

Treat supplied designs, prototypes, screens, diagrams, and other visual evidence as primary report material. When several are best inspected one at a time, load [prototype patterns](prototype-patterns.md) and use its accessible carousel contract. Do not reduce them to filenames, links, or descriptive prose when they can be shown safely in the artifact.

For a substantial report, translate the supplied structure into this compact reading order when compatible: skip link, title and status, selected industry, format, and density, scan summary, local navigation, visual argument, supporting evidence, limitations, resource disclosure, and revision history when applicable. Omit empty sections. Link supplied conclusions and recommendations to their evidence identifiers. Keep the opening scan summary useful without expanding any disclosure.

Summarize a supplied log by outcome, time range, entry count, material warnings, and last known state when those fields exist. Keep critical entries visible beside the result they affect. Put non-critical entries in collapsed `<details>` groups split by a meaningful supplied boundary such as phase, date, source, or severity. Give each `<summary>` its boundary, entry count, warning or error count, and final state when supplied. Preserve exact order, timestamps, and text inside each group. Do not turn the full log or source record into one `<pre>`, one table cell, or one undifferentiated accordion.

When a full raw log would materially slow or dominate the artifact, use an accepted companion bundle: keep the summary, critical entries, group index, exact format, size, evidence cutoff, and stable relative link in the HTML, and store the exact raw log in an adjacent text or structured-data file. Do not silently omit or rewrite entries. If a bundle is not accepted, keep the log collapsed in the HTML and disclose the size or performance limitation.

Give linked evidence, log groups, and entries stable identifiers. Mark completeness-required disclosures with `data-print-expand` and embed the bundled [report control](../assets/report-control.html). It reveals a fragment target inside nested disclosures, expands marked disclosures for print, and restores their prior screen state after print. Keep critical content visible and do not mark a large raw-log disclosure for print when its indexed companion file is the coverage disposition.

Use the bundled foundation hooks `data-report-section`, `data-table-wrap`, `data-long-text`, and `data-log` for their named layout behavior. Add report-specific styling only when the material needs it.

For every material living-report update, reconcile the title and version, scan summary, navigation, affected detail, recommendations and dispositions, limitations, and revision log. Preserve superseded conclusions through an explicit revision; do not let a new section silently contradict an earlier headline or status.

## Present candidate decisions

Give each supplied candidate an explicit before-and-after visualization at a comparable scale and visual grammar. Label unchanged and changed elements and connect them to supplied evidence, risk, and recommendation. A code diff alone is not the before-and-after visual.

Render one supplied disposition:

- **Build now:** recommend implementation in the current scope.
- **Later:** accept it after a named prerequisite.
- **Deferred:** make no current commitment; reconsider after a named trigger.
- **Rejected:** do not pursue it under current premises.
- **Needs evidence:** withhold the decision until named evidence is available.

Do not assess or fill a missing disposition. Mark it as an input gap. For each supplied disposition, present the supplied reason, dependencies or blockers, re-entry condition, next action, owner, and change evidence when available. Preserve their meaning and surface inconsistencies instead of resolving them.

Return the report lifecycle, coverage-ledger result, unresolved input gaps, and shared delivery fields.
