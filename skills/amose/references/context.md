# Maintain project domain language

Use the project's existing domain-language record when one exists. Do not create a competing source of truth or rename an established convention merely to match this fallback.

When no equivalent exists, use a visible root `CONTEXT.md` for one domain context. Create it lazily only after the first project-specific term, semantic relationship, or context boundary is confirmed and writing is authorized. Do not use `.context` as the default: canonical project language must remain visible to developers and agents.

For genuinely separate domain contexts, use a root `CONTEXT-MAP.md` that links each context's `CONTEXT.md`, states its purpose and ownership, and records only confirmed relationships between contexts. Do not introduce multiple contexts to organize documentation. If placement depends on an unresolved material boundary decision, return it to `arojinle` before writing.

Keep `CONTEXT.md` implementation-neutral. Include only project-domain language:

- one canonical term with a concise meaning;
- alternatives to avoid when they can cause ambiguity;
- confirmed semantic relationships, distinctions, and context boundaries; and
- short scenarios only when needed to disambiguate a definition.

Exclude generic programming vocabulary, implementation behavior, runtime findings, research notes, task history, specifications, architecture rationale, and temporary proposals. Put evidence-backed operational knowledge in `.learnings`, durable project exclusions in `.nongoals`, and qualifying consequential decisions in ADRs.

When no project format exists, use:

```markdown
# <Context name>

<One or two sentences defining the context and its purpose.>

## Language

**<Canonical term>**:
<One or two sentence meaning.>
_Avoid_: <ambiguous alternatives, or none>
```

Challenge a proposed term against current domain language, code, tests, and confirmed decisions. Code proves behavior, not domain intent. Surface contradictions and require confirmation instead of silently changing the model.

After a term or relationship is confirmed, reconcile the applicable context record immediately when authority exists; do not batch accepted vocabulary for a later retrospective. Re-read the written record, verify context-map links, canonical-term uniqueness, avoided-term conflicts, and separation from `.learnings`, then reissue the final candidate-pinned project-knowledge packet.
