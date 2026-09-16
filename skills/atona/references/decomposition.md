# Delivery decomposition

Turn supplied work into a validated dependency-ordered set of tickets a fresh delivery owner can complete without reconstructing parent narrative. Own decomposition, startability and terminal ticket disposition; the caller owns storage, publication, execution, review and reconciliation.

Use the governing requirements, contract identity and project evidence needed for accurate boundaries. Resolve routine granularity with judgment. Keep a consequential scope, outcome, sequencing, risk or ownership ambiguity visible when authority cannot settle it.

Default to narrow, outcome-complete vertical tickets that cross only the layers needed for an independently verifiable user, operator, stakeholder or system result. Use a non-vertical enabling ticket only when it independently proves a capability that blocks later outcomes or vertical slices cannot remain usable; state the integration boundary it enables. For wide software migrations that cannot remain green vertically, use expand–migrate–contract where it preserves compatibility.

Each ticket contains:

- a short outcome title and what it delivers;
- only stable context and exact source references needed independently;
- observable acceptance, governing behavior identities and the material proof seam;
- exact ticket dependencies or `None`, plus any external prerequisite and owner/trigger;
- a boundary only when it prevents plausible wrong delivery;
- state `Open | Done | Cancelled`; and
- acceptance/proof evidence for `Done`, or authority and reason for `Cancelled`.

Preserve supplied identities and use temporary numbers only while drafting. Ticket identity is semantic: it does not prescribe a commit, branch, candidate, PR/MR, document, deployment unit, proof file or agent session. The caller chooses those containers for integration, review, recovery, ownership and evidence. Avoid guessed paths, copied project rules, layer-only splits and artificial dependencies.

Derive an `Open` ticket as `STARTABLE` only when every ticket dependency is `Done` and no external prerequisite is active; otherwise it is `BLOCKED`. Only `Done` resolves a dependency. A `Cancelled` dependency forces replanning and never silently unblocks dependants. Execution/review progress stays with its owner; do not add ticket states for it.

Validate that tickets are independently verifiable, dependencies genuine and acyclic, external prerequisites real, acceptance observable, and the supplied scope fully covered without overlap. Verify every enabling exception and its named integration boundary. Distinguish inferred decomposition from user-confirmed choices.

Return ungrouped tickets in dependency order, blocked prerequisites first, plus the startable frontier. Do not persist, publish, execute or operate provider state unless the caller separately owns that action.
