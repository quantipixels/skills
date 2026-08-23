# Report Patterns

Read this file only when supplied material must become a report, including an evidence report, living report, or candidate comparison.

Follow the artifact language's punctuation conventions. Do not impose an English punctuation rule on another language.

## Select the report contract

Before implementation, derive one internal direction brief in this order:

| Field | Decision rule |
| --- | --- |
| Format | Preserve a named form, governed schema, contract deliverable, required template, or explicit selection. Its identity and order override later fields |
| `Purpose` | Preserve the supplied reader outcome, such as decide, approve, act, correct, monitor, verify, learn, compare, or retain a record. Otherwise, infer one exact outcome |
| Family | Select the recognized evidence and accountability contract from the claims and proof required, not from the subject area |
| Primary reader and use | Identify who acts, their authority, and what they do after reading |
| Unique scenario | Identify what changes emphasis within the family, such as urgency, lifecycle stage, severity, disputed evidence, confidentiality, candidate count, or decision deadline |
| Entry resource and context | Record source authority, shape, completeness, provenance, confidence, freshness, limits, and gaps |
| Governing question and relationship | State what the report must answer and the dominant supplied evidence relationship |
| Information direction | Choose one opening, reading order, central representation, evidence hierarchy, and navigation rule |
| Density | Choose `Executive`, `Working`, or `Archival` |
| Rationale | State why the direction fits this report |

The table order sets precedence. Keep secondary readers and purposes in supporting layers. Do not create a hybrid for multiple purposes. Ask only when unresolved ambiguity would change the family or reader outcome. Otherwise, choose the best-supported contract.

Keep the brief internal and render only fields that help the reader. Return one direction, never rejected directions, design options, visual variants, or prototype behavior. Apply decorative treatment after information direction. Palette, typography, illustration, borders, and brand expression cannot determine the argument.

Use industry only as an internal vocabulary cue. Show it only when supplied or useful to the reader. Never infer industry facts. Use `slides` for a requested slide deck.

### Let `Purpose` set the reading order

The following cues are not an enum. Use the supplied reader outcome when it is more specific.

| Reader outcome | Open with | Give visual priority to |
| --- | --- | --- |
| Decide or approve | The decision, decision deadline, and material exceptions | Trade-offs, option consequences, confidence, reversibility, and the evidence behind the decision |
| Act or correct | Current state, required action, blockers, and ownership | Dependencies, sequence, responsibility, risk, and recovery |
| Monitor | Current trajectory and material change since the last cutoff | Target versus actual, trend, variance, thresholds, and anomalies without reducing judgment to a mechanical score |
| Verify or assure | Objective or criteria, scope, and conclusion or disposition | Criteria-to-evidence traceability, exceptions, confidence, limitations, and corrective action |
| Learn or understand | The governing question and the minimum context needed to follow it | Causes, relationships, mechanisms, findings, uncertainty, and implications |
| Compare or select | The choice, candidates, common criteria, and supplied disposition | Comparable evidence, meaningful differences, trade-offs, risks, and sensitivity to criteria |
| Retain a record | What occurred or changed, when, and with what current consequence | Sequence, state change, provenance, superseded conclusions, and follow-up |

### Let family set the required content

These are conventional content and evidence contracts, not fixed page templates. Preserve binding local or institutional rules. Omit unsupported optional material and mark unsupported required material as an input gap.

| Family | Required content and evidence | Direction cue |
| --- | --- | --- |
| Governed disclosure | Required items in their prescribed identity and order, plus source and assurance records | Mirror the schema. Add navigation and a scan layer without reordering protected obligations |
| Audit or assurance | Objective or criteria, scope, method, findings, evidence, conclusion, limitations, responsible views, and supported corrective action | Make traceability and exceptions the organizing relationship |
| Evaluation, research, or experiment | Question, intended use, context, method, scope, findings, confidence, limitations, gaps, conclusion, and supported implications | Organize around questions and findings rather than the chronology of the work |
| Business case | Case for change, objectives, counterfactual, options, value, feasibility, affordability, risk, delivery, monitoring, and evaluation | Show the case-to-delivery argument and why the preferred course is credible |
| Incident report or postmortem | Impact, factual sequence, response, recovery, contributing causes, evidence, lessons, and owned corrective actions | Lead with impact and supported state or causal change. Temporal order does not establish cause |
| Status or delivery report | Evidence cutoff, trajectory, milestones, dependencies, risks, decisions, owners, and next actions | Emphasize exceptions, movement, blockers, and the decisions needed now |
| Performance or analytical report | Definitions, targets, actuals, trends, variance, drivers, anomalies, uncertainty, and actions | Lead with the supported quantitative relationship and its context, not a grid of headline numbers |
| Technical or decision assessment | Question or current state, conceptual model, constraints, evidence, alternatives, trade-offs, risks, decision or priorities, and proof | Make the governing technical relationship or before-and-after consequence central |
| Product or experience definition | User need, context, outcomes, requirements or experience states, non-goals, evidence, risks, and success evidence | Organize by the user journey, state model, or requirements. The subject is not its `Purpose` |
| Candidate or vendor assessment | Candidate identities, common criteria, normalized evidence, meaningful differences, trade-offs, risks, and supplied disposition | Keep candidates comparable and expose criteria sensitivity without manufacturing a recommendation |
| Case study or outcome record | Context, challenge, intervention, outcome, evidence, limitations, and lessons | Organize by change and supporting evidence. Sequence alone does not prove cause |

### Let the scenario and entry resource choose the representation

Read the entry resource before selecting a representation:

- A governed schema or template establishes the structure.
- A time-ordered log supports sequence or state change. Use a causal flow only when the source establishes causality.
- A dataset or metric series supports its dominant relationship, such as trend, variance, distribution, or correlation.
- Criteria and evidence support a traceability or exception view.
- A candidate set supports a matrix, paired views, or another common-scale comparison.
- A system, lifecycle, journey, or state model supports a structural or transition view.
- Screenshots, designs, diagrams, and other visual evidence stay primary when safe to embed.
- Findings, decisions, or narrative evidence support a supplied argument, hierarchy, or before-and-after relationship.

Use the scenario to decide what dominates within that shape. Urgency can move action ahead of background. A disputed cause can make provenance and competing evidence dominate an incident report. An early lifecycle can make uncertainty and prerequisites dominate a status report. Sparse context can require a constrained explanation or an input gap.

## Shape the record

Render a **snapshot** by default with its generation time or evidence cutoff. Render a **living report** only when the owning task expects material updates. Keep section, candidate, and evidence anchors stable. Show the last-updated time, evidence cutoff, and supplied evidence status. Record conclusion or disposition changes in a revision log. Never replace one silently.

Select one density profile and default to **Working**. **Executive** keeps a concise decision layer, material exceptions, and actions while preserving coverage through disclosures or deep links. **Working** adds enough context and evidence to act. **Archival** keeps the complete record behind the same scan layer. Density changes presentation, not coverage. Change it only when the audience or decision changes.

Before composing a substantial report, create a coverage ledger that includes:

- each explicit user question and deliverable
- each supplied conclusion, decision, recommendation, and limitation
- each in-scope project, candidate, or other subject unit, including its supplied depth contract

Give each item one disposition:

- **Full record:** rendered with its required evidence and explanation.
- **Summary + deep link:** summarized in an overview and linked to its full stable anchor.
- **Input gap:** material source content is missing. Return it to the owning task instead of inventing it.
- **Excluded with reason:** the supplied scope or authority excludes it.

An overview, metric, card, or visual does not replace a required full record. Show each in-scope unit, including a supplied no-finding state or input gap. Before delivery, reconcile the ledger with the final anchors. The report remains incomplete if a material item lacks a disposition or a deep link lacks a useful destination.

## Build the visual argument

Build the opening, hierarchy, and central representation from the direction brief. Choose the central visual from the highest-priority ledger relationship or result. Identify its message and relationship before choosing a chart, timeline, matrix, diagram, card system, or other form. Apply the shared prose and table limits.

Do not default to a dashboard, hero metrics, or a uniform card grid. Use a dashboard scan layer only when the reader must monitor simultaneous measures and exceptions. Use cards for independently scanned peer units, not generic section containers. Decorative variation is not a report direction.

Keep supplied designs, screens, diagrams, and other visual evidence primary when they can be shown safely. Do not reduce them to filenames, links, or prose. Report composition does not authorize design options or a prototype. Load [prototype patterns](prototype-patterns.md) only for a supplied prototype, demo, interface specimen, or design-variant set.

Keep the opening useful without expanding a disclosure. Follow the selected direction, not a universal section order. When compatible, include a skip link, title and status, local navigation, central visual, supporting evidence, limitations, resource disclosure, and revision history. Omit empty sections. Link conclusions and recommendations to their evidence identifiers.

Before delivery, run these direction checks:

- **Purpose counterfactual:** Changing `Purpose` would change the opening, order, or action layer.
- **Family counterfactual:** Changing family would change the evidence obligations and support structure.
- **Scenario:** The central representation reveals the unique scenario without the title.
- **Entry resource:** The composition respects the resource's authority, shape, and limits.
- **Relationship:** Each material visual encodes a supplied claim or relationship.
- **Interchangeability:** Removing the title and subject nouns would not leave a composition suitable for an unrelated report.
- **Gap:** Missing required content appears as an input gap, not an invented section.
- **Decoration:** Removing ornament leaves the information direction intact.

When supplied, summarize a log's outcome, time range, entry count, warnings, and last known state. Keep critical entries visible beside the affected result. Group non-critical entries in collapsed `<details>` elements by a supplied boundary such as phase, date, source, or severity. Put the boundary, entry count, warning or error count, and final state in each `<summary>` when available. Preserve exact order, timestamps, and text. Do not use one `<pre>`, table cell, or undifferentiated accordion for the full record.

If a raw log would slow or dominate the artifact, use an accepted companion bundle. Keep its summary, critical entries, group index, format, size, evidence cutoff, and stable relative link in the HTML. Store the exact log in an adjacent text or structured-data file. Never omit or rewrite entries silently. Without bundle approval, keep the log collapsed in the HTML and disclose the limitation.

Give linked evidence, log groups, and entries stable identifiers. Mark required print disclosures with `data-print-expand` and embed the [report control](../assets/report-control.html). It reveals nested fragment targets and restores disclosure state after print. Keep critical content visible. Do not print-expand a large raw log when its indexed companion file supplies complete coverage.

Use `data-report-section`, `data-table-wrap`, `data-long-text`, and `data-log` for their named foundation behavior. Add report styling only when the material needs it.

After a material living-report update, reconcile the title, version, summary, navigation, affected detail, recommendations, dispositions, limitations, and revision log. Preserve superseded conclusions explicitly. Never let new detail silently contradict an earlier headline or status.

## Present candidate decisions

Give each supplied candidate a before-and-after visual at a comparable scale and visual grammar. Label changed and unchanged elements. Connect them to supplied evidence, risk, and recommendation. A code diff alone is insufficient.

Render one supplied disposition:

- **Build now:** recommend implementation in the current scope.
- **Later:** accept it after a named prerequisite.
- **Deferred:** make no current commitment. Reconsider after a named trigger.
- **Rejected:** do not pursue it under current premises.
- **Needs evidence:** withhold the decision until named evidence is available.

Do not fill a missing disposition. Mark it as an input gap. For each supplied disposition, present the reason, dependencies or blockers, re-entry condition, next action, owner, and change evidence when available. Preserve its meaning and surface inconsistencies instead of resolving them.
