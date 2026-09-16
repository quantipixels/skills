# Managed initiative lifecycle

Use this opt-in overlay only when a governing workflow needs named readiness states, coordinated multi-candidate delivery, or a durable lifecycle record. Ordinary plans use the main Atọ́nà workflow. Atọ́nà alone owns plan status and current progression; supporting results are evidence.

Maintain one exact-current semantic plan using the [plan record](../templates/plan-record.md) as a contract, not a rigid outline. Persist it only for continuity, recovery, independent review, or downstream consumption, preferring an established destination and otherwise `.qp/atona/`. Record the current execution workspace and branch form; for a linked worktree also record its main-worktree path. Update semantic truth before the required living view.

## State and gates

| Status | Meaning |
| --- | --- |
| `Draft` | planning or readiness has a material gap |
| `Planned` | a current premortem supports readiness without invented material requirements |
| `In Progress` | authorized delivery is active |
| `Backlog` | intentionally inactive with an owner and re-entry trigger |
| `Closed` | accepted outcome and proof are complete and required candidate state is reconciled |

Derive delivery separately as `Not required | Not started | Active | Blocked | Complete | Stale`. Keep the current gate and weakest material gap explicit; counts and aggregate scores cannot satisfy a missing mandatory condition.

Classify uncertainty by its actual owner:

- `FACT` — discoverable evidence; resolve without asking the user.
- `PLAN_LOCAL` — reversible planning detail within accepted authority.
- `SPECIALIST_RESULT` — independently useful result the plan cannot responsibly invent.
- `MATERIAL_USER_DECISION` — consequential choice affecting outcome, scope, policy, experience, risk, cost, compatibility, or trade-off.

Maintain one Decision Frontier: `EMPTY` when no unresolved material user choice blocks readiness, `OPEN` when one is answerable, or `BLOCKED` when prerequisite evidence is missing. Ask one bounded choice directly or use `arojinle` for dependent choices. Progressive shaping may track not-yet-formulatable territory, but it does not add another Decision Frontier state.

## Readiness

Use the main workflow's owner seams only when needed: a current `SPEC_READY` behavior contract for material normative behavior, `architect: IMPLEMENTATION_READY` for architecture delivery would otherwise invent, consequential user-choice closure, and delivery decomposition/startability for materially coordinated work. Retain identities and readiness, not copied procedures.

Before `Planned`, require:

- a current premortem with material threats resolved or retained within the responsible authority;
- an `EMPTY` Decision Frontier and no in-scope territory delivery could encounter but the plan cannot yet state responsibly;
- every required specialist result to be current, accepting and exact enough to rely on;
- observable acceptance and a credible proof seam for each delivery obligation; and
- resolved dependency, recovery, documentation, operational and delivery-shape gaps, or a valid out-of-scope re-entry condition.

Keep the plan `Draft` when a controlling result is absent, stale, blocked, or not ready. Delivery authority still comes from the request or governing policy; `Planned` does not grant it.

## Delivery and closure

Run authorized delivery through the main workflow and [delivery tracking](delivery-tracking.md) when coordination is material. After a material result, update plan meaning, stale only dependent conclusions and proof, recompute the gate, and refresh the living view. Work-in-progress limits follow actual integration and verification capacity, never a headcount quota.

Before `Closed`, require the Decision Frontier to remain empty, no blocking plan gap, current accepting proof for every in-scope obligation, explicit residual limits, and completion of any required durable-knowledge obligation. For linked worktrees, reconcile only needed `.qp` state into the accepting workspace and record `reconciled`, `reconciled-retained`, or `reconciled-and-removed`; preserve unresolved state. Worktree removal requires user approval and declining it does not block closure.

Align the final status, workspace/disposition, gate, frontier, delivery summary, freshness, blocker, remaining work, next action, and living view. When blocked or intentionally inactive, name the owner and exact re-entry trigger; otherwise continue authorized executable work.
