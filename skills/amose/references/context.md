# Maintain canonical domain language

Use the project's existing domain-language source when one exists. Do not create a competing source of truth or rename an established convention merely to match a QP fallback.

The destination is owned by the project. Amọ̀ṣẹ́ owns the semantic delta, not a repository layout. If no durable destination is established, return the clarified model in the conversation and name the persistence gap only when future work actually needs a durable source.

## Keep domain language narrow

A domain-language source should contain the minimum material needed for different humans and agents to mean the same thing:

- canonical project-specific terms and avoided synonyms when ambiguity matters;
- concise definitions of what concepts are;
- conceptual identity and lifecycle distinctions;
- bounded-context meaning and confirmed cross-context relationships;
- ownership or semantic invariants when they are part of the domain model.

Do not absorb implementation procedure, architecture rationale, task history, generic learnings, delivery non-goals, ADR policy, research notes, or a running conversation summary merely because they are useful project knowledge. Those belong to their natural owners and destinations.

## Reconcile meaning, not storage

When current discussion conflicts with established language, surface the contradiction instead of choosing silently. Use the smallest concrete scenario that distinguishes the competing meanings and cross-check code, tests, configuration, or current behavior only when they can expose a semantic contradiction. Current implementation remains evidence of behavior, not automatic authority for domain intent.

After meaning is resolved and write authority exists, update the established domain-language source with the smallest semantic delta. Verify that the resulting definition:

- states what the concept is rather than its implementation procedure;
- does not introduce a competing canonical synonym;
- preserves distinctions needed for identity, ownership, state, or policy; and
- does not absorb specification, architecture, operational, or task detail.

When meaning remains disputed, return the conflict rather than persisting confident-sounding lore.
