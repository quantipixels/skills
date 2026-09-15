# Report Patterns

Read this file only when supplied material must become a report, including an evidence report, living report, or candidate comparison. Read [source composition](source-composition.md) first for substantial, reused, living, or owner-record inputs. It owns source normalization, coverage, placement, fidelity, source mapping, and agent-context rules.

Follow the artifact language's punctuation conventions. Do not impose an English punctuation rule on another language.

## Select the report contract

Choose the reader's job before composing. Preserve an explicitly required format or schema; otherwise keep this brief internal and compact:

| Field | Decision rule |
| --- | --- |
| Reader and purpose | Who needs to understand, decide or act, and what do they need from this view? |
| Governing question | What source-supported conclusion or relationship should the opening explain? |
| Evidence and limits | What is current, authoritative, uncertain, human-critical or required by the report's contract? |
| Composition | What reading order, central representation, visual premise and density serve this question? |
| Detail | What stays exact and visible, what supports the argument, and what can remain linked? |

Keep secondary purposes in supporting layers. Ask only when ambiguity would materially change the reader outcome or source meaning.

Return one finished report by default. An explicitly requested comparison may present supplied visual variants or exploration results; use `adanwo` when creating a decision prototype is the actual task. Design representation and visual expression together while keeping the argument source-owned.

Use industry only as an internal vocabulary cue. Show it only when supplied or useful to the reader. Never infer industry facts. Use the installed presentation capability for a requested slide deck.

### Let `Purpose` set the reading order

The following cues are not an enum. Use the supplied reader outcome when it is more specific.

| Reader outcome | Open with | Give visual priority to |
| --- | --- | --- |
| Decide or approve | The decision, deadline, and material exceptions | Trade-offs, consequences, confidence, reversibility, and evidence |
| Act or correct | Current state, required action, blockers, and ownership | Dependencies, sequence, responsibility, risk, and recovery |
| Monitor | Current trajectory and material change since the cutoff | Target versus actual, trend, variance, thresholds, and anomalies |
| Verify or assure | Objective or criteria, scope, and conclusion or disposition | Criteria-to-evidence traceability, exceptions, confidence, limits, and correction |
| Learn or understand | Governing question and minimum necessary context | Causes, relationships, mechanisms, findings, uncertainty, and implications |
| Compare or select | Choice, candidates, common criteria, and supplied disposition | Comparable evidence, meaningful differences, trade-offs, risks, and criteria sensitivity |
| Retain a record | What occurred or changed, when, and current consequence | Sequence, state change, provenance, superseded conclusions, and follow-up |

### Preserve the report's obligations

A governed disclosure retains its prescribed items and order. Assurance needs criteria-to-evidence traceability and exceptions; an experiment needs method and limits; an incident needs impact and supported causal findings; a business case needs alternatives, cost, feasibility and risk. Use the actual contract, not a mandatory family taxonomy. Mark missing required evidence as a gap, and omit unsupported optional sections.

### Let the entry resource choose the representation

- A governed schema or template establishes structure.
- A time-ordered log supports sequence or state change. Use causal flow only when the source establishes causality.
- A dataset or metric series supports trend, variance, distribution, or correlation.
- Criteria and evidence support traceability or exception views.
- Candidate sets support matrices, paired views, or common-scale comparison.
- A system, lifecycle, journey, or state model supports structural or transition views.
- Screenshots, designs, diagrams, and other visual evidence stay primary when safe to embed.
- Findings, decisions, or narrative evidence support a supplied argument, hierarchy, or before-and-after relationship.

Use the actual situation to decide what dominates. Urgency can move action ahead of background. Disputed cause can make provenance and competing evidence dominate. Early lifecycle can make uncertainty and prerequisites dominate. Sparse context can require a constrained explanation or input gap.

## Shape the record

Render a `snapshot` by default with generation time or evidence cutoff. Render a `living` report only when the owning task expects material updates. Pin the owner record and revision. Keep section, candidate, evidence, and source anchors stable. Show last-updated time, cutoff, and supplied evidence status. Record conclusion or disposition changes without retaining every wording revision in the working view.

Select one density profile and default to `Working`. `Executive` keeps a concise decision layer, material exceptions, and actions while preserving coverage through links or disclosures. `Working` adds enough context and evidence to act. `Archival` retains complete reader-required records behind the same scan layer; it does not automatically embed native archives. Density changes presentation, not source coverage.

Before composing, reconcile every explicit question, deliverable, supplied conclusion, decision, recommendation, limitation, and in-scope subject unit through source composition. Every material unit needs coverage, placement, fidelity, and source. An overview, metric, card, visual, or aggregate does not replace complete coverage; complete coverage can remain source-only when the retrieval path is reliable.

## Build the visual argument

Build the opening, hierarchy, and governing representation from the direction brief. Choose the representation from the highest-priority foreground relationship or result. Identify its message and relationship before choosing a chart, timeline, matrix, diagram, card system, or another form.

Do not default to a dashboard, hero metrics, or uniform card grid. Use a dashboard scan layer only when the reader must monitor simultaneous measures and exceptions. Use cards for independently scanned peer units, not generic section containers. Decorative variation is not a report direction.

Keep supplied designs, screens, diagrams, prototypes, demos, interface specimens, and other visual evidence primary when safe. Do not reduce them to filenames or prose. Report composition does not authorize creating or iterating a prototype; treat supplied prototype-like material only as source evidence for the report.

Keep the opening useful without a disclosure. When compatible, include a skip link, title and status, local navigation, governing representation, supporting evidence, limits, resource disclosure, and revision state. Omit empty sections. Link conclusions and recommendations to evidence or source identifiers.

Keep navigation unobtrusive and preserve useful landmarks when adapting the base controls.

While selecting or materially changing an unsettled information design, use these critiques:

- **Purpose counterfactual:** changing purpose changes opening, order, or action layer.
- **Scenario:** the governing representation reveals the unique scenario without the title.
- **Interchangeability:** removing title and subject nouns does not leave a composition suitable for an unrelated report.

These critiques help choose a direction; they do not require redesign of an accepted layout. Repeat them only when changed purpose, scenario, content, or evidence unsettles that direction.

Before delivery, always run these content and evidence checks:

- **Contract and coverage:** required content and human-critical meaning remain present or visibly marked partial, stale, or missing.
- **Entry resource:** composition respects resource authority, shape, and limits.
- **Relationship:** each material visual encodes a supplied claim or relationship.
- **Gap:** missing required content appears as an input gap, not an invented section.
- **Deletion:** each foreground section materially improves decision, action, understanding, verification, or trust.

## Handle logs and evidence

Summarize a log's outcome, time range, entry count, warnings, errors, and last known state when supplied. Keep critical transitions visible beside the affected result. Keep the exact log source-only or archived unless exact inline inspection is required.

When reader-required log excerpts remain in HTML, group them by a supplied boundary such as phase, date, source, or severity. Preserve exact order, timestamps, and text. Do not use one `<pre>`, table cell, or undifferentiated accordion for the full record.

Use an accepted companion evidence bundle when exact evidence is important but too large, repetitive, shared, or context-polluting. Keep an index, summary, critical entries, format, size, cutoff, durability, and stable relative link in HTML. Do not silently omit or rewrite evidence.

Give sources, evidence groups, and retained entries stable identifiers. Mark required print disclosures with `data-print-expand` and embed [report control](../assets/report-control.html). It reveals fragment targets and restores disclosure state after print. Do not print-expand a large raw log when an indexed native source provides coverage.

Use `data-report-section`, `data-table-wrap`, `data-long-text`, and `data-log` for their named foundation behavior. Keep a wide semantic table inside `data-table-wrap`. Give a scrollable wrapper `tabindex="0"` plus an accessible label or description. Tune `--artifact-table-min-inline-size` and the foundation's container query to the actual columns. Do not stack cells into cards or duplicate header text as presentation data.

When one supplied categorical filter materially reduces scanning, embed [collection filter](../assets/collection-filter-control.html). Keep its value tokens, labels, and category membership source-owned. The control owns only the visible subset and result state. It does not own search, compound predicates, sorting, pagination, or URL state.

After a material living update, reconcile title, version, context capsule, summary, navigation, affected detail, recommendations, dispositions, source register, limits, and revision note. Never let new detail silently contradict an earlier headline or status.

## Present candidate decisions

Give each supplied candidate a before-and-after view at a comparable scale and visual grammar. Label changed and unchanged elements. Connect them to supplied evidence, risk, and disposition. A code diff alone is insufficient.

Render one supplied disposition:

- `Build now`
- `Later`, after a named prerequisite
- `Deferred`, after a named trigger
- `Rejected` under current premises
- `Needs evidence` before decision

Do not fill a missing disposition. Mark it as an input gap. For each supplied disposition, present reason, dependencies or blockers, re-entry condition, next action, owner, and change evidence when available. Preserve its meaning and surface inconsistencies instead of resolving them.
