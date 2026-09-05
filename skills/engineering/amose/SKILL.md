---
name: amose
description: Establish, sharpen, or reconcile one project's exact-current domain model and exceptional durable project knowledge. Use when project-specific terms, conceptual boundaries, domain relationships, or invariants need to be defined, changed, split, merged, or clarified, or when qualifying durable learnings, exclusions, or decision records must be reconciled; exclude passive vocabulary lookup, material product/architecture decisions, delivery execution, and generic documentation.
---

# Amọ̀ṣẹ́

Actively sharpen the project's domain model when meaning itself is being established, changed, or is unclear. Reading established project/domain language is ordinary capability and does not require `amose`.

## Clarify the model

Read only evidence capable of settling the material meaning: the current domain-language source, governing decisions/policies, relevant code/tests/configuration/runtime behavior, and bounded history/provenance when it can resolve a conflict. Treat implementation and operations as evidence of current behavior, not automatic authority for domain intent.

When an ambiguous, overloaded, synonymous, or conflicting term can change scope, ownership, identity, state, policy, or behavior, do not silently choose a meaning. State the conflict, test it with the smallest concrete scenario that distinguishes the concepts, compare it with current domain language and relevant evidence, and propose canonical wording only when evidence or user/domain authority supports it.

When the user deliberately establishes or changes clear domain meaning, test only the boundaries needed to make that change internally coherent; do not manufacture ambiguity merely to justify an interview.

Challenge the model as concepts crystallize. A useful clarification may establish or separate:

- canonical terms and avoided synonyms;
- conceptual distinctions and identities;
- domain/context boundaries;
- semantic relationships or invariants; and
- contradictions between stated meaning and current behavior.

Use `arojinle` when `amose` is the primary owner and resolving the model requires a consequential user choice rather than clarification. When `amose` is supporting an active `arojinle` interview, return any unresolved consequential choice to that caller instead of recursively invoking `arojinle`.

Use the relevant design owner when an independently useful design result is required; consequential software/system technical structure belongs to `architect`.

For a reusable handoff, return only the compact model delta needed downstream: affected context, resolved terms/distinctions/relationships/invariants, any concrete scenario that materially distinguishes the resolved meaning for a downstream consumer, conflicts or open decisions, and controlling evidence/limits. Do not create a universal project-knowledge packet, freshness lifecycle, or status ceremony for ordinary clarification.

## Reconcile canonical language

Use the project's existing domain-language source or user-selected equivalent; do not create a competing source of truth. In repository work, read [context](references/context.md) when canonical language needs maintenance.

When a term or context relationship is confirmed and write authority exists, reconcile the applicable language source immediately rather than batching accepted vocabulary for a retrospective. Re-read the final text and verify it does not absorb implementation details, temporary scenarios, task history, specifications, or architecture rationale.

## Exceptional durable knowledge

Domain clarification does not imply durable promotion. Ordinary implementation rationale, one-off discoveries, temporary decisions, and useful history stay in their normal plan/spec/PR/history surfaces.

Only when stable governing knowledge independently needs durable reconciliation, use the project's existing destination or user-selected equivalent. Repository-specific conditional contracts are:

- [learnings](references/learnings.md) — stable, non-obvious recurring project knowledge whose loss risks consequential wrong action;
- [nongoals](references/nongoals.md) — durable project-wide exclusions; and
- [ADRs](references/adrs.md) — qualifying hard-to-reverse, surprising software/system decisions that resulted from a genuine trade-off.

Prefer stronger maintained sources such as domain context, architecture, policy, configuration, code, tests, runbooks, or product/service documentation when they already own the truth. Do not create a second durable record merely because information is useful.

When requested durable reconciliation is required but the natural destination, evidence, or write authority is missing, return the exact gap instead of inventing a destination. Use `akosile` only when a selected durable destination is repository-scoped `.qp` state; `akosile` owns path/publication mechanics, not `amose` semantics.

## Return

Return the resolved model delta and material conflicts/open decisions directly. When durable reconciliation was explicitly required, also report affected destination(s), verification/limitations, and `RECONCILED | BLOCKED`.
