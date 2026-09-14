---
name: amose
description: Establish, sharpen, or reconcile one project's canonical domain model and its durable records. Use when project-specific terms, conceptual identities, domain/context boundaries, relationships, ownership, invariants, `.learnings`, `.nongoals`, or ADRs need to be defined, changed, or maintained.
---

# Amọ̀ṣẹ́

Own the project's domain meaning. Make its important concepts precise enough that planning, specifications, architecture, implementation, and review can use the same language without silently inventing different models.

## Clarify the model

Read only evidence capable of settling material meaning: the current domain-language source, governing decisions/policies, relevant code/tests/configuration/runtime behavior, and bounded history when it can resolve a conflict. Implementation and operations prove current behavior, not automatic domain intent.

When an ambiguous, overloaded, synonymous, or conflicting term can change scope, ownership, identity, state, policy, or behavior:

1. state the ambiguity or contradiction;
2. use the smallest concrete scenario that distinguishes the competing concepts;
3. compare it with current domain language and relevant evidence; and
4. propose canonical wording only when evidence or domain authority supports it.

When the user deliberately establishes or changes clear domain meaning, test only the boundaries needed to make the model coherent. Do not manufacture ambiguity to justify an interview.

A useful model clarification may establish or separate:

- canonical terms and avoided synonyms;
- conceptual identity and lifecycle distinctions;
- bounded contexts and cross-context meaning;
- relationships and ownership; and
- semantic invariants or contradictions between stated meaning and current behavior.

Use `yoruba-glossary` for Yorùbá/English technical terminology and glossary maintenance; Amọ̀ṣẹ́ retains project-specific domain meaning.

Ask a single bounded consequential choice directly. Use `arojinle` when the user requests an interview or dependent choices require decision-tree closure. Use `architect` when the missing result is technical structure. Do not turn current implementation shape into domain vocabulary merely because it exists.

## Reconcile canonical language

When a domain-language source already exists, read [domain language](references/context.md) and update that source when the resolved model changed and write authority exists. Do not create a competing project-memory system or generic documentation store.

If no durable domain-language destination is established, return the model delta directly and name the persistence gap only when the result needs to outlive the current work. Let the project or caller choose an intentional project destination rather than inventing `CONTEXT.md`, `.learnings`, `.nongoals`, an ADR, `.qp` record, or another repository convention.

This domain-clarification boundary does not prevent an authorized ADR-creation request from using the [ADR fallback](references/adrs.md) when no project convention exists. Domain clarification alone does not authorize creating an ADR.

A domain-model change may cause another workflow to update specifications, architecture, documentation, tests, or policy. Those artifacts remain owned by their natural workflow. Amọ̀ṣẹ́ maintains the project's canonical domain records and supplies clarified meaning to the other owners.

## Maintain durable domain records

Maintain the project's existing domain records when the request concerns their content or lifecycle:

- `.learnings` → read [learnings](references/learnings.md);
- `.nongoals` → read [non-goals](references/nongoals.md); or
- ADR qualification or lifecycle → read [ADRs](references/adrs.md).

Use the record's existing project destination. Preserve its format and authority boundary. A record change must reflect established domain meaning or an authorized project decision; do not turn task notes, temporary deferrals, or implementation history into durable domain records.

## Return

Return the resolved terms, identities, relationships, ownership, invariants, distinguishing examples when needed, and any remaining semantic conflict or consequential decision with its evidence.

When canonical domain language or a durable domain record was updated, report the destination and verification.
