# Maintain domain context

Read the [domain-language method](../references/engineering/domain/context.md) and the [durable record contract](../references/engineering/domain/record-contract.md). Own a project's canonical domain glossary, including a requested migration of domain language from `.learning` or `.learnings`. Return the changed destination and the meaning resolved to the caller.

Use an established domain-language source when one exists. Otherwise, create `CONTEXT.md` at the repository root when the first project-specific term is resolved and writing is authorized. Create no empty file. Capture each resolved term promptly during active modelling rather than deferring all glossary changes to task close. Reading vocabulary alone does not invoke this command or require a write.

`CONTEXT.md` is a glossary: give each canonical term a tight definition of what it **is**, usually one or two sentences, and list avoided synonyms when ambiguity matters. Include only concepts specific to this project's domain. It contains no implementation details, procedure, architecture rationale, decision history, generic lessons, or task notes. Group related terms only when that helps readers locate them.

If a root `CONTEXT-MAP.md` already exists, use it to locate the relevant bounded context's glossary and relationships. For a project with multiple confirmed contexts and no map, create a root `CONTEXT-MAP.md` when a second context's glossary is needed. Point it to the scoped `CONTEXT.md` files, their relationships, and applicable ADR locations; keep definitions in the scoped glossaries. If the correct context is materially unclear, resolve the meaning before placing a term. A single-context project needs only its root `CONTEXT.md`.

For a requested `.learning` or `.learnings` migration, inspect each live entry's meaning and current evidence. Choose its maintained owner:

| Content | Destination |
| --- | --- |
| Confirmed domain terms | Established glossary or applicable `CONTEXT.md`. |
| Durable codebase rules and conventions | Existing project standards, contributor guide or scoped instructions. If none owns the rule, create `CODEBASE_STANDARD.md` only when qualifying content needs that home. |
| Consequential decisions and rationale | Qualified [ADRs](amose-adrs.md). |
| Deliberate project exclusions | [Non-goals](amose-nongoals.md). |
| Technical structure | [Architecture overview](architect-document.md). |
| Procedures, verification pitfalls and workarounds | Owning runbook, verification recipe or method/reference; link from the workflow that needs it. |
| Task history, research and unresolved claims | Existing task or research record, with uncertainty preserved. |

Admit a durable rule only when independent current evidence supports a stable, non-obvious constraint likely to recur and losing it risks a consequential wrong action. Preserve existing filenames such as `CODING_STANDARDS.md`; do not create competing standards or an empty fallback. Keep project policy in its project owner and portable expertise in its owning method; workflows link to those sources. Use [agent-facing writing](oro-sigidi.md) or [documentation reconciliation](akowe-sync.md) for non-domain material within the migration's authorized scope.

Account for each entry as moved, merged, unresolved or retired with a reason. Do not bulk rename, silently discard entries or promote uncertain claims into canonical language. Reconcile reader pointers before removing a legacy file, and remove it only after every live entry has an accounted-for destination and the requested write authority covers removal. An unresolved entry stays recoverable with its existing owner until resolved; migration is not complete while its destination remains unresolved.

When asked to maintain an established `.learnings` source directly, honor that destination for material outside the glossary. Admit an entry only when independent current evidence supports a stable, non-obvious rule likely to recur, losing it risks a consequential wrong action, and no stronger maintained source already owns it. Preserve the existing format and reconcile stale or duplicate entries under the [record contract](../references/engineering/domain/record-contract.md). Do not create a new generic `.learnings` file as a fallback. Report unresolved entries and conflicts so the caller can place them with the correct owner.

For a workaround tied to an upstream bug or version, optionally add a plain-language “Retire when …; check by …” sentence beside the workaround in its destination, identifying the upstream issue or affected version and an observable retirement condition. Preserve that condition when moving an entry. Include a check-by date only when useful; it prompts revalidation, not automatic retirement. Verify the condition against the project's actual version and behavior before retiring the entry. This adds no schema, scheduled refresh or general expiry rule for lessons.
