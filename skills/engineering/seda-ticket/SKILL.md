---
name: seda-ticket
description: Break a supplied plan, specification, issue, conversation, or work description into consumable delivery tickets. Use when work needs small outcome-complete slices, explicit dependencies, acceptance criteria, and a clear startable frontier; exclude persistence, publication, execution, active review tracking, Git, and provider operations.
---

# Ṣẹ̀dá Ticket

Turn supplied work into a confirmed set of tickets that a fresh delivery owner can understand and complete without reconstructing parent narrative. Own decomposition, dependency/startability semantics, and terminal ticket disposition only; the caller owns grouping, storage, publication, execution, review progress, and reconciliation from owner results.

## 1. Understand the work

Use the context already supplied. Read a referenced source in full when it governs the work. Inspect the current project/system only when existing behavior, vocabulary, constraints, or accurate ticket boundaries require it. In software work that may include the codebase; it is not a universal prerequisite.

Do not invent a material requirement. Ask for confirmation when decomposition authority is absent or the granularity/dependency structure is ambiguous. A caller can supply an already confirmed breakdown.

When material behavior or operating rules are not settled enough to slice without invention, use `seda-spec` when its implementation-independent behavior contract fits the need, or consume the current domain's established normative authority. Keep the exact contract identity/reference; do not rewrite the governing specification as ticket-local acceptance.

## 2. Prefer outcome-complete vertical tickets

Default each ticket to one narrow, outcome-complete vertical slice that:

- delivers an independently verifiable user, operator, stakeholder, or system outcome;
- crosses only the functions/layers needed for that outcome;
- is self-contained enough for a fresh delivery owner/reviewer without prescribing candidate, commit, branch, PR/MR, document, proof-file, or agent-session boundaries; and
- can stay valid without copied parent narrative or guessed implementation detail.

Do not split one outcome merely by organizational function, technical layer, artifact type, or proof activity. Use a non-vertical ticket only for an independently verifiable enabling capability that genuinely blocks later work, or when outcome-complete slices cannot remain usable/integrated. Record the exception and the integration/acceptance boundary it enables.

For a software/system-wide migration or mechanical refactor that cannot remain green as vertical slices, an expand–migrate–contract sequence may be appropriate: add a compatible form, migrate bounded groups, then remove the old form after the migration set. This is a software-specific branch, not a universal ticket pattern.

Each ticket contains:

- **Title** — a short outcome in current project/domain vocabulary.
- **What it delivers** — the end-to-end behavior/result and value.
- **Context** — only required stable facts, constraints, or source references.
- **Acceptance and proof** — observable completion conditions, governing specification behavior identities when present, and the proof/evidence obligation or stable seam when material; the execution/proof owner chooses mechanics.
- **Depends on** — exact draft numbers or supplied ticket identities that must be `Done`, or `None`.
- **External prerequisite** — only when a named non-ticket fact/authority/resource prevents starting; include owner/trigger when known.
- **Boundary** — only when an exclusion prevents a plausible wrong delivery.
- **State** — `Open`, `Done`, or `Cancelled`.
- **Terminal evidence** — acceptance/proof result for `Done`; cancellation authority/reason for `Cancelled`.

Use temporary numbers while drafting and preserve identities supplied by the caller. Return an ungrouped dependency-ordered set unless the caller supplies grouping. Do not create synthetic parent tickets or own durable IDs, lifecycle persistence, execution/review states, transition history, assignees, timestamps, lineage, or reconciliation.

Ticket identity is semantic, not operational: a ticket boundary does not imply a commit, candidate, branch, PR/MR, document, proof file, deployment unit, or agent-session boundary. The delivery caller chooses operational containers independently from integration, review, rollback/recovery, ownership, release, and evidence needs.

Avoid guessed file/artifact paths, long snippets, generic implementation checklists, duplicated project rules, and artificial dependencies. Include an exact stable reference when necessary. Include a short prototype-derived snippet only when prose cannot preserve the confirmed decision, and label its source.

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

Do not add `In Progress`, `In Review`, or runtime `Blocked` ticket states. Active execution, proof, review, runtime blockers, candidate/result identity, and recovery remain outside ticket state and with the active execution/review owner. A caller may reconcile `Open → Done | Cancelled` from exact-current owner results without importing another owner's lifecycle into the ticket contract.

The **Startable frontier** is every `Open` ticket currently derived as `STARTABLE`.

## 3. Confirm and return

Check that every ticket is independently verifiable, dependencies are genuine and acyclic, external prerequisites are real, acceptance is observable, and the complete supplied scope/governing specification is covered without overlap. For every non-vertical ticket, verify that its exception is necessary, independently verifiable, and connected to a named integration/acceptance boundary.

When confirmation is required, show the draft and ask whether its granularity and dependencies are correct. Iterate until confirmed.

Return confirmed tickets in dependency order, blocked prerequisites first, with the startable frontier. Return tickets only; do not persist/publish them, operate Git/provider state, execute them, or decide execution/review progress.
