---
name: seda-ticket
description: Break a supplied plan, specification, issue, conversation, or work description into consumable delivery tickets. Use when work needs small vertical slices, explicit dependencies, acceptance criteria, and a clear startable frontier; exclude persistence, publication, implementation, active execution/review tracking, Git, and provider operations.
---

# Ṣẹ̀dá Ticket

Turn supplied work into a confirmed set of tickets that fresh coding agents can implement and verify. Own decomposition, dependency/startability semantics, and terminal ticket disposition only; the caller owns grouping, storage, publication, execution, review progress, and reconciliation from owner results.

## 1. Understand the work

Use the context already supplied. Read a referenced source in full. Inspect the codebase only when current behavior, project vocabulary, constraints, or accurate ticket boundaries require it.

Do not invent a material requirement. Ask for confirmation when decomposition authority is absent or the granularity or dependency structure is ambiguous. A caller can supply an already confirmed breakdown.

When material behavior is not settled enough to slice without invention, use `seda-spec` to establish the normative contract first. Consume its exact identity and behavior references; do not rewrite the specification as ticket-local acceptance.

## 2. Prefer outcome-complete vertical tickets

Default each ticket to one narrow, outcome-complete vertical slice that:

- delivers an independently verifiable user, operator, or system outcome;
- crosses only the layers needed for that outcome;
- fits one fresh agent context and one coherent reviewable change; and
- can stay valid without copied parent narrative or guessed implementation detail.

Do not split one behavior into separate schema, API, UI, or test tickets. Use a non-vertical ticket only for an independently verifiable enabling capability that genuinely blocks later work, or when vertical delivery cannot remain green. Record the exception and its green integration boundary in the ticket context.

For a wide mechanical refactor that cannot stay green as vertical slices, use expand–migrate–contract: add a compatible form, migrate bounded groups, then remove the old form after every migration. State where green integration proof applies.

Each ticket contains:

- **Title** — a short outcome in project vocabulary.
- **What it delivers** — the end-to-end behavior and value.
- **Context** — only required stable facts, constraints, or source references.
- **Acceptance and proof** — observable completion conditions, governing specification behavior identities when present, and how to verify them.
- **Depends on** — exact draft numbers or supplied ticket identities that must be `Done`, or `None`.
- **External prerequisite** — only when a named non-ticket fact/authority/resource prevents starting; include owner/trigger when known.
- **Boundary** — only when an exclusion prevents a plausible wrong implementation.
- **State** — `Open`, `Done`, or `Cancelled`.
- **Terminal evidence** — acceptance/proof result for `Done`; cancellation authority/reason for `Cancelled`.

Use temporary numbers while drafting and preserve identities supplied by the caller. Return an ungrouped dependency-ordered set unless the caller supplies grouping. Do not create synthetic parent tickets or own durable IDs, lifecycle persistence, execution/review states, transition history, assignees, timestamps, lineage, or reconciliation.

Avoid guessed file paths, long snippets, generic implementation checklists, duplicated repository rules, and artificial dependencies. Include an exact stable reference when necessary. Include a short prototype-derived snippet only when prose cannot preserve the decision, and label its source.

## Startability and terminal disposition

Ticket state is deliberately not an execution-progress state machine:

| State | Meaning | Required evidence |
| --- | --- | --- |
| `Open` | delivery remains outstanding | none |
| `Done` | current owner evidence proves the ticket's acceptance/proof | acceptance and proof result |
| `Cancelled` | the ticket is intentionally removed from required delivery | cancellation authority and reason |

Derive startability for an `Open` ticket:

- `STARTABLE` — every ticket dependency is `Done` and no external prerequisite is active;
- `BLOCKED` — at least one ticket dependency or named external prerequisite is unresolved.

Only `Done` resolves a ticket dependency. A `Cancelled` dependency requires re-planning rather than silently unblocking dependants.

Do not add `In Progress`, `In Review`, or runtime `Blocked` ticket states. Active implementation, proof, review, runtime blockers, candidate identity, and recovery live in the native results of `alaga`, `atunwo`, or another current execution/review owner. A caller may reconcile `Open → Done | Cancelled` from those exact-current results without importing their lifecycle into the ticket contract.

The **Startable frontier** is every `Open` ticket currently derived as `STARTABLE`.

## 3. Confirm and return

Check that every ticket is independently verifiable, dependencies are genuine and acyclic, external prerequisites are real, acceptance is observable, and the complete supplied scope or governing specification is covered without overlap. For every non-vertical ticket, verify that its exception is necessary, independently testable, and connected to a named green integration boundary.

When confirmation is required, show the draft and ask whether its granularity and dependencies are correct. Iterate until confirmed.

Return confirmed tickets in dependency order, blocked prerequisites first, with the startable frontier. Return tickets only; do not persist or publish them, operate Git or a provider, implement them, or decide execution/review progress.
