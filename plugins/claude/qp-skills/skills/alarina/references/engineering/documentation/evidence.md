# Documentation evidence and reconciliation

## Bound the document set

Pin the requested change, revision or release, audience and reader task, documentation destinations and write scope. Distinguish working-tree content from a released version. Use a diff to focus discovery, not as proof of completeness; a named document set needs no diff. Keep versioned and historical documentation tied to its intended version.

Follow the project's navigation, documentation/build configuration, source references and relevant reader entry points. Include nested and non-Markdown sources, generated inputs, examples, runbooks and agent guidance when they bear on the changed claim. Follow material references and same-procedure guidance a reader or agent actually uses, including unlinked guidance in the affected area. Do not scan an entire repository or impose a new documentation index by default.

For broad project documentation assessment or improvement, read the [project baseline](project-baseline.md) and check useful missing coverage as well as drift. An audit reports those gaps; authorized improvement establishes the relevant missing documents. Narrow edits do not imply the full baseline.

Resolve the source of generated documentation before editing. Note excluded destinations, external or unavailable sources, unsupported formats and truncated searches. A scope hint matching nothing is a scope gap, not authority to widen. A missing document is not a current one.

## Establish what should change

Read affected claims in context and match evidence to their meaning:

- **Current-state descriptions** follow the relevant implementation, configuration and runtime evidence.
- **Governing requirements or policy** follow independently supported accepted intent. A code disagreement may be a product regression, not obsolete guidance.
- **Historical decisions and versioned records** remain true to their time and version; do not rewrite history as present-day instructions.
- **Planned work** stays visibly planned until implementation and proof establish otherwise.

Check the document set for contradictory instructions as well as stale paths, examples and factual statements. Trace consequential disagreements to the governing evidence; majority agreement, newer timestamps and absent search matches do not settle them. Missing runtime or operational corroboration is a verification gap, not proof of falsity.

For contradictions, generated sources, historical records, consolidation, removal or requested pruning, read [reconciliation boundaries](reconciliation.md). Use [iwadi](../../../commands/iwadi.md) when a substantial external fact controls the correction; reuse sufficient current evidence. Return product defects to [alaga-deliver](../../../commands/alaga-deliver.md) or the calling workflow without silently fixing code or normalizing the defect in documentation.

## Knowledge discoverability

After an authorized knowledge change, apply the shared [knowledge discoverability](../../productivity/knowledge-discoverability.md) check to the affected reader path.
