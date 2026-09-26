# Maintain ARCHITECTURE.md

Read [architecture orientation](../references/engineering/architecture/orientation.md) for evidence and persistence boundaries; preserve this command’s requested stop.

With write authority, use `document` to create or refresh the project's canonical architecture overview from established evidence, without redesigning the system. Reuse its existing location and format, including scoped module documents. When creation is requested or authorized architecture work needs a durable overview and none exists, use repository-root `ARCHITECTURE.md`; do not create a competing copy just to enforce that name.

The overview should let a new contributor locate and safely change the system: major components and their source paths, responsibilities and dependency direction, key runtime/data flows, and the boundaries and invariants that constrain change. Include state ownership, integrations, trust and deployment only where material. Explain non-obvious rationale; link README/setup, domain records and ADRs rather than duplicating them. [amose](amose.md) retains domain meaning and ADR lifecycle.

Ground the current-state map in code/tests/configuration and relevant runtime evidence. Distinguish observed implementation, accepted but unimplemented design, proposals and unknowns. For a greenfield system, label the overview as planned. A stale document does not authorize changing code to match it.

Reconcile affected sections when authorized work changes the documented structure; preserve unaffected content. Survey/review-only requests report missing documentation or drift without creating or editing the overview. Routine changes with no architectural impact need no document churn.

Before returning, verify affected structural claims and source links at the reviewed revision. Report the document path, updated scope and unresolved drift or evidence gaps; writing the file alone is not completion.
