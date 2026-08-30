# Keep ticket state to readiness and terminal disposition

Status: Accepted

## Context

`Ṣẹ̀dá Ticket` exists to turn supplied work into portable vertical delivery slices with explicit dependencies, acceptance, and a startable frontier. Its current `Ready → In Progress → Blocked → In Review → Done/Cancelled` lifecycle duplicates active execution and review state already owned by delivery/review results such as Alága and Àtúnwò.

The earlier ticket decision deliberately removed durable graph/persistence ownership and retained a small portable state vocabulary. The remaining execution/review states still make callers reconcile two lifecycles for the same work.

## Decision

1. Keep ticket ownership on decomposition, dependencies, acceptance/proof, startability, and terminal disposition.
2. Use only `Open | Done | Cancelled` as ticket state.
3. Derive `STARTABLE | BLOCKED` for an open ticket from ticket dependencies and named external prerequisites; startability is not persisted execution progress.
4. Remove `In Progress`, `In Review`, and runtime `Blocked` ticket states.
5. Keep implementation progress, candidate identity, runtime blockers, recovery, proof, and review state in the native execution/review owner results.
6. Let callers reconcile `Open → Done | Cancelled` from exact-current owner evidence without importing that owner's lifecycle into the ticket.
7. Only `Done` resolves a dependency; a cancelled dependency requires re-planning.

## Consequences

Tickets remain portable and independently useful without becoming a second delivery tracker. Atọ́nà can derive initiative delivery state from owner receipts while using the ticket set only for decomposition/dependency/startability semantics. Alága and Àtúnwò retain their native progress and review contracts.

This refines the replacement described in `20260813-keep-plan-tickets-local.md`; it does not restore durable ticket graphs, persistence, transition logs, assignees, or provider state.
