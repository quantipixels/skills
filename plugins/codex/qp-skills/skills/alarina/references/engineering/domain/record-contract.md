# Durable record contract

Own the project's domain meaning and ubiquitous language across planning, specifications, architecture, implementation and review. Preserve bounded-context distinctions; shared wording must not conceal different models.

Check material rules' applicability even when their words are familiar. Reuse current settled meaning; do not treat stale records as immutable intent or invent business rules to reconcile a conflict.

Use the record's existing project destination. Preserve its format and authority boundary. A record change must reflect established domain meaning or an authorized project decision; do not turn task notes, temporary deferrals, or implementation history into durable domain records.

Check a record's claim against independent current evidence before promoting or retiring it; the record alone is not its own proof. Distinguish descriptive behavior from independently supported intent. A policy does not become obsolete merely because current code stopped enforcing it, and missing evidence is not proof that a claim is false. Surface unresolved conflicts rather than silently replacing intent with implementation.

Before editing, re-read the affected record. Make the smallest semantic change, merge duplicates and stale entries, and preserve useful lifecycle history. Reconcile concurrent or conflicting edits rather than overwriting or blindly appending. Read only relevant sections when a large existing store permits scoped retrieval; a truncated or failed search does not establish that no relevant record exists.

After a record change, check [knowledge discoverability](../../productivity/knowledge-discoverability.md) and return any unresolved reader-path gap with the changed destination.
