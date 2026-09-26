# Maintain canonical domain language

Use the project's existing domain-language source when one exists. Do not create a competing source of truth or rename an established convention merely to match a generic fallback. Otherwise create a root `CONTEXT.md` lazily when a project-specific term is resolved and writing is authorized.

The destination is owned by the project. Amọ̀ṣẹ́ owns the semantic delta. A root `CONTEXT-MAP.md`, when present, locates scoped glossaries and their relationships; add one when a second confirmed bounded context needs a glossary. Include relevant ADR paths in the map without copying decisions into it.

## Keep domain language narrow

A domain-language source should contain the minimum material needed for different humans and agents to mean the same thing:

- canonical project-specific terms and avoided synonyms when ambiguity matters;
- concise definitions of what concepts are;
- conceptual identity and lifecycle distinctions that define the term;
- bounded-context meaning and confirmed cross-context relationships in the context map when applicable.

For a new `CONTEXT.md`, use the context name as the heading, a short description, and a `## Language` section. Give each term a bold name, colon, and one or two sentence definition; add an `_Avoid_:` line only when synonymous wording would confuse the model. Group terms under further headings when natural clusters emerge. A single-context project uses the root file. In a multi-context project, the root map points to each scoped glossary and states only the confirmed relationships needed to navigate them.

Do not absorb implementation procedure, architecture rationale, task history, generic learnings, delivery non-goals, ADR policy, research notes, or a running conversation summary merely because they are useful project knowledge. Those belong to their natural owners and destinations.

## Reconcile meaning, not storage

When current discussion conflicts with established language, surface the contradiction instead of choosing silently. Use the smallest concrete scenario that distinguishes the competing meanings and cross-check code, tests, configuration, or current behavior only when they can expose a semantic contradiction. Current implementation remains evidence of behavior, not automatic authority for domain intent.

After meaning is resolved and write authority exists, update the established domain-language source promptly with the smallest semantic delta. Verify that the resulting definition:

- states what the concept is rather than its implementation procedure;
- does not introduce a competing canonical synonym;
- preserves distinctions needed for identity, ownership, state, or policy; and
- does not absorb specification, architecture, operational, or task detail.

When meaning remains disputed, return the conflict rather than persisting confident-sounding lore.
