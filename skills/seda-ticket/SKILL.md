---
name: seda-ticket
description: Break a supplied plan, specification, issue, conversation, or work description into consumable delivery tickets. Use when work needs small vertical slices, explicit blockers, acceptance criteria, and a clear startable frontier; exclude persistence, publication, implementation, review, Git, and provider operations.
---

# Seda Ticket

Turn supplied work into a confirmed set of tickets that fresh coding agents can implement and verify. Own decomposition and the portable lifecycle semantics only; the caller owns grouping, storage, publication, execution, and lifecycle transitions.

## 1. Understand the work

Use the context already supplied. Read a referenced source in full. Inspect the codebase only when current behavior, project vocabulary, constraints, or accurate ticket boundaries require it.

Do not invent a material requirement. Ask for confirmation when decomposition authority is absent or the granularity or dependency structure is ambiguous. A caller can supply an already confirmed breakdown.

## 2. Draft vertical tickets

Make each ticket one narrow, complete behavior slice that:

- delivers an independently verifiable user, operator, or system outcome;
- crosses only the layers needed for that outcome;
- fits one fresh agent context and one coherent reviewable change; and
- can stay valid without copied parent narrative or guessed implementation detail.

Do not split one behavior into separate schema, API, UI, or test tickets. Use an enabling ticket only when it delivers a verifiable capability or genuinely blocks later work.

For a wide mechanical refactor that cannot stay green as vertical slices, use expand–migrate–contract: add a compatible form, migrate bounded groups, then remove the old form after every migration. State where green integration proof applies.

Each ticket contains:

- **Title** — a short outcome in project vocabulary.
- **What it delivers** — the end-to-end behavior and value.
- **Context** — only required stable facts, constraints, or source references.
- **Acceptance and proof** — observable completion conditions and how to verify them.
- **Blocked by** — exact draft numbers or supplied ticket identities that prevent starting, or `None`.
- **Boundary** — only when an exclusion prevents a plausible wrong implementation.
- **State** — `Ready` for every newly confirmed ticket.
- **Allowed next** — derived from the current state.
- **State evidence** — only when the current state requires it.

Use temporary numbers while drafting and preserve identities supplied by the caller. Return an ungrouped dependency-ordered set unless the caller supplies grouping. Do not create synthetic parent tickets or own durable IDs, lifecycle persistence, transition execution, lineage, or reconciliation.

Avoid guessed file paths, long snippets, generic implementation checklists, duplicated repository rules, and artificial dependencies. Include an exact stable reference when necessary. Include a short prototype-derived snippet only when prose cannot preserve the decision, and label its source.

Use this lifecycle:

| State | Allowed next | Required state evidence |
| --- | --- | --- |
| `Ready` | `In Progress`, `Cancelled` | none |
| `In Progress` | `Blocked`, `In Review`, `Cancelled` | none |
| `Blocked` | its recorded `resume_to`, `Cancelled` | reason, unblock owner or trigger, and `resume_to` set to either `In Progress` or `In Review`; retain exact candidate and proof summary when resuming review |
| `In Review` | `In Progress`, `Blocked`, `Done`, `Cancelled` | exact candidate and proof summary |
| `Done` | none | acceptance and proof result |
| `Cancelled` | none | cancellation authority and reason |

Only `Done` resolves a dependency. Keep a dependant `Ready` until every dependency is `Done`; a `Cancelled` dependency requires re-planning. The **Startable frontier** is every `Ready` ticket whose dependencies are all `Done`. Remove stale state evidence when a transition no longer requires it. Do not add lifecycle history, timestamps, assignees, or an event log.

## 3. Confirm and return

Check that every ticket is independently verifiable, blockers are genuine and acyclic, acceptance is observable, and the complete supplied scope is covered without overlap.

When confirmation is required, show the draft and ask whether its granularity and blockers are correct. Iterate until confirmed.

Return confirmed tickets in dependency order, blockers first, with the startable frontier. Return tickets only; do not persist or publish them, operate Git or a provider, implement them, or decide review status.
