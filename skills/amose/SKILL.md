---
name: amose
description: "Establish or reconcile project domain language, identity, lifecycle, policy and invariants, including existing ADRs, learnings and non-goals."
---

# Amọ̀ṣẹ́

Own project-specific meaning, not technical structure or a generic memory system. Shared words can conceal distinct bounded-context models. Code proves behavior, not necessarily intended policy.

Read governing domain sources, applicable decisions and the smallest relevant implementation, tests or history. Verify applicability before reusing a familiar rule. When meaning changes behavior or ownership, state the ambiguity and use a concrete distinguishing scenario. Ask only for meaning/authority that evidence cannot settle; do not manufacture an interview around a clear decision.

Establish the terms, conceptual identity, lifecycle/transitions, relationships, bounded contexts, owners and material invariants needed by the work. Distinguish internal identifiers, wire/storage values and user-visible labels. Synonyms are not automatically interchangeable domain values.

Use [atona](../atona/SKILL.md) for unsettled outcomes and consequential choices, [architect](../architect/SKILL.md) for technical shape and [yoruba-glossary](../yoruba-glossary/SKILL.md) for language-wide terminology. Return clarified meaning to the same caller.

Maintain the established canonical destination when authorized. Do not invent another context file, knowledge database or plan. Without a durable destination return the model delta and name the persistence gap only when it matters. Discussion and term acceptance do not authorize arbitrary writes.

For existing `.learnings`, retain reusable evidenced knowledge and applicability, not session history. For `.nongoals`, distinguish deliberate exclusions from deferrals and preserve re-entry conditions. For ADR work follow the project convention; record decision, context, alternatives, consequences, status and supersession. Use a simple `docs/adr/` destination only when ADR creation is authorized and no convention exists. Changed needs can invalidate old decisions.

Architecture, types, schemas and constraints may enforce an invariant; interpretation stays here. Return meaning, source/authority, resolved contradictions, outstanding decisions and actual durable writes. Hand implementation and proof to their owners.
