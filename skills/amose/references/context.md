# Maintain project domain language

Use the project's existing domain-language record when one exists. Do not create a competing source of truth or rename an established convention merely to match this fallback.

When no equivalent exists, use a visible root `CONTEXT.md` for one domain context. Create it lazily only after the first project-specific term is resolved and writing is authorized. Do not create it speculatively.

For genuinely separate domain contexts, use a root `CONTEXT-MAP.md` that links each context's `CONTEXT.md`, states its purpose, and records only confirmed relationships between contexts. Do not introduce multiple contexts merely to organize documentation. If the split itself depends on an unresolved consequential boundary decision, resolve that decision before writing the map.

## `CONTEXT.md` is a glossary

Keep `CONTEXT.md` implementation-neutral and intentionally narrow. It contains project-domain language only:

- one canonical project-specific term;
- a one- or two-sentence definition of what the concept **is**; and
- alternatives to avoid when they can cause ambiguity.

Do not store implementation behavior, operating rules, architecture rationale, specifications, research notes, task history, scenarios, generic programming concepts, or a running summary of the conversation. Use scenarios to clarify meaning during reasoning; do not persist them merely because they were useful to the discussion.

A context file may start with one or two sentences identifying the bounded context and its purpose. Relationships between separate contexts belong in `CONTEXT-MAP.md`, not duplicated into each glossary.

When no project format exists, use:

```markdown
# <Context name>

<One or two sentences defining the context and its purpose.>

## Language

**<Canonical term>**:
<One or two sentence definition of what the concept is.>
_Avoid_: <ambiguous alternatives, or none>
```

## Actively challenge the language

When current discussion uses a term that conflicts with the established glossary, surface the contradiction instead of choosing silently. When a term is vague or overloaded, propose a precise canonical term only after the concepts are understood.

Use the smallest concrete scenario that can distinguish the competing meanings. Cross-check relevant code, tests, configuration, or current behavior when they can reveal a contradiction, while preserving the distinction that implementation proves current behavior rather than domain intent.

Example:

```text
CONTEXT.md defines “Cancellation” as cancelling an entire Order,
but the proposed behavior discusses cancelling one line item.
Are these the same domain action, or do we need a distinct term?
```

After a term is resolved and write authority exists, update the glossary immediately rather than batching accepted vocabulary until the end of the session. Re-read the written entry and verify:

- the definition states what the concept is rather than its implementation procedure;
- no competing canonical synonym was introduced;
- avoided terms do not conflict with other current glossary entries; and
- the file did not absorb specification, architecture, operational, or task detail.

When a definition remains disputed, return the conflict instead of persisting confident-sounding lore.
