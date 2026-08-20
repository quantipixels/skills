# QP lifecycle playbooks

Select one playbook after orientation. A playbook controls task phases; it does not replace the selected leaf owner's instructions.

## Common schema

Every catalog or bespoke playbook must declare:

1. `trigger` — the request or state change that selects the playbook;
2. `match` — the outcome and evidence that make the playbook credible;
3. `entry` — pinned facts, candidate identity, acceptance, constraints, and authority;
4. `phases` — the universal spine plus only necessary inserted phases;
5. `owners` — outcomes to resolve through exact-current `alarina`, including any explicit user selection;
6. `exit proof` — the current evidence required to leave each phase;
7. `skip` — the reason for every omitted universal phase;
8. `recovery` — the owning phase, retry trigger, or safe-pause branch for failure; and
9. `terminal` — the condition for `complete`, `paused`, `unresolved`, or `stopped`.

For multi-step work, add a throughput checkpoint after `shape`: define independently verifiable units, identify the next startable unit, and keep partial units outside task completion.

## Inherited controller contract

Every catalog row inherits these fields:

- `entry` is the oriented task record: outcome, scope, candidate identity, acceptance, constraints, authority, and current evidence.
- `phases` are the universal spine. Place the row's inserted control at the earliest owning phase and keep all other phases visible.
- `owners` are the row's leaf outcomes resolved through exact-current `alarina`; an explicit user-selected owner takes precedence when it can own the outcome.
- `skip` records why a universal phase or listed leaf outcome does not apply to this task.
- `recovery` returns failed proof to the earliest owning phase. Use the safe-pause branch when the retry requires new authority, an external change, or a context transfer.
- `terminal` uses only Pepeye's `complete`, `paused`, `unresolved`, or `stopped` task states.

The selected row and this inherited contract form the playbook declaration. Before `execute`, instantiate them as one task-local record with all nine fields. Replace leaf-outcome labels with the exact identifiers and modes returned by `alarina`, and write the ordered universal and inserted phases explicitly. Do not execute from the summary row alone.

`Pause` is a control branch of the active playbook, not a replacement for its identity. Preserve the suspended playbook's task-local declaration and interrupted phase in the pause receipt. `Pickup` reconstructs that declaration, refreshes its entry conditions, and returns control to the earliest valid phase.

Use this phase-exit proof:

| Phase | Exit proof |
| --- | --- |
| `orient` | Pinned outcome, identity, acceptance, authority, constraints, and evidence |
| `shape` | Credible schema-valid playbook, selected leaf outcomes, and a throughput checkpoint when required |
| `execute` | Current leaf-owner receipts for the requested mutations or results |
| `prove` | Acceptance checked against the real artifact or external state |
| `review` | Applicable review receipt and disposition of every required finding |
| `learn` | One learning disposition and any destination-owner receipt, or `skip: no high-signal candidate` |
| `finish` | One justified terminal state and its retry or pickup trigger when applicable |

## Catalog

| Playbook | Trigger | Match | Inserted control | Leaf outcomes to resolve | Completion emphasis |
| --- | --- | --- | --- | --- | --- |
| Investigation | The user asks a question or evidence is insufficient for the next decision | A question needs evidence, diagnosis, or primary-source research | Acquire evidence before synthesis | research, diagnosis, explanation, companion tooling | Claims trace to current evidence; uncertainty is explicit |
| Decision and design | A material choice or unresolved premise changes the next action | A premise, design, or decision needs closure | Explore and confirm the decision frontier before execution | premise judgment, decision closure, domain reconciliation, visual design | Material choices and consequences are confirmed and durable |
| Bug fix | The user reports wrong behavior or current proof exposes a regression | Reported behavior can be reproduced or credibly isolated | Triage and reproduce before repair | issue triage, diagnosis, bounded delivery, defect review | The failure is fixed at its owner and the original behavior check passes |
| Feature | The user requests a new user-visible or system capability | Acceptance can distinguish the requested capability from unrelated expansion | Establish acceptance before delivery units | architecture when needed, bounded delivery, applicable review | Acceptance passes on the real artifact without unrelated expansion |
| Refactor | Structure must change while specified behavior remains | A baseline and parity boundary can identify preserved behavior | Establish baseline and parity before mutation | simplification audit, architecture, delivery, parity and defect review | Required behavior remains equivalent and the intended structure improves |
| Architecture and migration | Boundaries, ownership, state, or transition must change | The change requires a durable plan across design and delivery | Keep the plan active through reconciliation and delivery | architecture planning, decision closure, project knowledge, delivery, parity review | Decisions, migration state, docs, and proof agree at the new boundary |
| Review | The user supplies a candidate or requests a bounded verdict | Candidate identity and review scope can be pinned | Pin identity and scope before inspection | defect, maintainability, parity, security, or provider-specific review | Findings cite credible mechanisms and the verdict matches the requested scope |
| Publication | A verified local result must cross an external boundary | The destination, current head, authority, and publishable artifact are known | Refresh identity and authority immediately before external writes | changeset or release preparation, `seda-pr`, monitoring | Published state is read back and distinguished from local or attempted state |
| Stewardship | Durable project knowledge, tooling, docs, or portfolio state is stale or incomplete | One existing owner can reconcile the durable source of truth | Reconcile the owning record after the specialist result | project knowledge, companion tooling, docs, skill portfolio maintenance | Exact-current durable state and receipts agree; no parallel source of truth is added |
| Autonomous task | The user authorizes consequential unattended progress | Outcome, stop boundaries, checkpoints, and authority are explicit | Define unattended stop and report checkpoints before execution | the task's native outcome owners plus handoff when needed | Work stops at authority boundaries and every unattended result has proof |
| Program orchestration | Several dependent tasks must converge on one program outcome | Child boundaries, dependencies, receipts, and program acceptance can be named | Track dependency order and child receipts | architecture plan, ticket decomposition, task owners, handoff | All required children and program-level acceptance pass |
| Skill authoring | A QP skill is added, changed, moved, retired, or validated | One skill contract and its integration surfaces form the candidate | Reconcile owner, integration, state, and proof as one portfolio change | `ko-skill`, project knowledge when decisions change, applicable review | Skill contract, group, registry, catalog, metadata, docs, and proof agree |
| Pause | Work reaches a safe boundary but cannot or should not continue now | Current phase, proof, gap, authority, suspended playbook declaration, and first pickup action can be recorded | Branch from the active playbook after its safe boundary; use `skip` for inapplicable review or learning, prove the checkpoint, preserve the interrupted phase, and finish as `paused` without replacing the active playbook identity | `handoff` and the active owner | Pickup receipt names the suspended playbook and phase, exact state, proof, gaps, authority, and first action |
| Pickup | The user resumes a paused task or a handoff crosses context | The suspended playbook declaration, prior receipts, and current candidate state can be reconstructed and refreshed | Reconstruct during `orient`, revalidate during `shape`, then return control to the earliest valid phase of the suspended playbook | `handoff` evidence, active owner, route registry | Candidate, authority, mutable state, and resumed phase are current before work continues |

## Bespoke fallback

Use a `bespoke` playbook only when no catalog row credibly matches. Build it from the common schema and select the smallest necessary leaf-owner set through `alarina`. State why the nearest catalog entries fail. Verify the shaped playbook and authority before execution.

Keep the playbook local to the task. Repeated use is evidence for a later `ko-skill` proposal, not authority to edit this catalog during execution.
