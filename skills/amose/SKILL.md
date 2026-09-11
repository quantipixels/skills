---
name: amose
description: Establish, sharpen, or reconcile one project's canonical domain model. Use when project-specific terms, conceptual identities, domain/context boundaries, relationships, ownership, or invariants need to be defined, changed, split, merged, or clarified. Generic project knowledge and record custodianship do not drive selection; explicit legacy `.learnings`, `.nongoals`, or ADR maintenance remains supported as a compatibility path.
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

Use `arojinle` when the unresolved issue is a consequential choice rather than clarification of established meaning. Use `architect` when the missing result is technical structure. Do not turn current implementation shape into domain vocabulary merely because it exists.

## Reconcile canonical language

When a domain-language source already exists, read [domain language](references/context.md) and update that source when the resolved model changed and write authority exists. Do not create a competing project-memory system or generic documentation store.

If no durable domain-language destination is established, return the model delta directly and name the persistence gap only when the result needs to outlive the current work. Let the project or caller choose an intentional project destination rather than inventing `CONTEXT.md`, `.learnings`, `.nongoals`, an ADR, `.qp` record, or another repository convention.

A domain-model change may cause another workflow to update specifications, architecture, documentation, tests, policy, or durable project records. Those artifacts remain owned by their natural workflow. Amọ̀ṣẹ́ supplies the clarified meaning; it does not become their default custodian.

## Compatibility: explicit durable-record maintenance

Existing direct Amọ̀ṣẹ́ requests to maintain one of these records remain supported for a minor release, but this branch does not drive automatic skill selection and is not part of the domain-model result:

- explicit `.learnings` maintenance → read [learnings](references/learnings.md);
- explicit `.nongoals` maintenance → read [non-goals](references/nongoals.md); or
- explicit ADR qualification/lifecycle maintenance → read [ADRs](references/adrs.md).

Explicit legacy record maintenance uses the requested record's existing or selected project destination.

## Return

Return the resolved terms, identities, relationships, ownership, invariants, distinguishing examples when needed, and any remaining semantic conflict or consequential decision with its evidence.

When canonical domain language was updated, also report the destination and verification. For an explicit compatibility-path request, return that record's own required result plus the affected destination, verification/limitations, and `RECONCILED | BLOCKED`; do not pretend the record is part of the domain model.
