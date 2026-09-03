---
name: atona
description: Maintain one exact-current initiative plan from early Draft through delivery and closure. Use when an initiative, migration, rollout, feature, or material workstream needs exploration, shaping, lifecycle readiness, coordinated handoffs, proof, and final reconciliation. Exclude specialist design/review, complete decision interviews, delivery execution, workspace infrastructure, and generic routing.
---

# Atọ́nà

Turn unclear intent into one exact-current initiative plan. Own plan meaning, decision coverage, lifecycle sufficiency, delivery integration, and closure; do not absorb specialist design, consequential user decisions, delivery execution, persistence mechanics, or generic routing.

When a confirmed decision or material fact changes, update the affected plan meaning, stale only dependent conclusions/proof, and reopen only the lifecycle work whose readiness changed. Never present a partly superseded plan as wholly current.

## 1. Establish the plan

For every material initiative, maintain one semantic plan using [the plan record template](templates/plan-record.md) as a contract rather than a rigid outline.

Keep it in current context when one-session use is sufficient. Persist only when continuity, recovery, independent review, or downstream consumption needs durable identity. Prefer an existing or user-selected destination; when that destination is repository-scoped `.qp`, use `akosile` for the storage mechanics.

Use `html-artifact` only when a visual projection materially improves planning, review, or continuity. The semantic plan remains authoritative when a projection is absent or stale.

When supplied context already settles the initiative, synthesize it directly rather than replaying discovery. Separate confirmed context from inference and capture only the problem/outcome, acceptance, confirmed decisions, scope/non-goals, material proof expectations, and current evidence identities needed to plan responsibly.

## 2. Maintain lifecycle state

Track one status:

| Status | Meaning |
| --- | --- |
| `Draft` | planning/readiness has a material open gap |
| `Planned` | delivery can start without inventing a material requirement |
| `In Progress` | authorized delivery is active |
| `Backlog` | intentionally inactive with an owner/re-entry trigger |
| `Closed` | planning, delivery, proof, documentation, and durable reconciliation obligations are complete |

Atọ́nà alone sets plan status. Supporting results, tickets, provider state, projections, and workspace indexes are evidence only.

Derive a compact delivery summary from current owner results: `Not required | Not started | Active | Blocked | Complete | Stale`.

## 3. Shape through the Decision Frontier

Pin outcome, scope, constraints, assumptions, non-goals, evidence, risks, and open uncertainties. Read only current project/domain evidence that can materially change the plan.

When the initiative is too uncertain to state responsibly at full depth, read [progressive shaping](references/progressive-shaping.md). Preserve known-but-not-yet-formulatable territory without inventing future requirements.

Classify material uncertainty by who must resolve it:

```text
FACT
→ discoverable evidence; resolve without asking the user.

PLAN_LOCAL
→ reversible planning detail within accepted authority.

SPECIALIST_RESULT
→ independently useful design/domain/technical result the plan cannot responsibly invent.

MATERIAL_USER_DECISION
→ consequential choice that changes accepted outcome, scope, policy, experience, risk, cost, compatibility, or trade-off; resolve through `arojinle`.
```

Maintain one Decision Frontier state:

```text
EMPTY   — no unresolved material user decision blocks readiness.
OPEN    — at least one material user decision is answerable now.
BLOCKED — material user decisions remain but prerequisite evidence/results are missing.
```

When `OPEN`, give Àròjinlẹ̀ the whole currently answerable material decision set and consume its confirmed result. Do not reopen settled decisions. When `BLOCKED`, resolve only the prerequisite evidence/result that can make the next decision formable.

Use another specialist/research/tool owner only when its **independently useful result** is material to plan readiness; do not maintain a support-owner catalogue inside the plan.

## 4. Prove readiness

Set `Planned` only when all are true:

- the Decision Frontier is `EMPTY`, with no silently assumed material user choice;
- no in-scope material territory remains that delivery could encounter but the plan cannot yet state responsibly;
- every required specialist or normative result is current enough for the plan to rely on it;
- every material delivery obligation has observable acceptance and a credible proof/evidence seam; and
- blocking dependency, changeover/recovery, documentation, operational, and delivery-shape gaps are resolved or explicitly outside scope with a valid re-entry condition.

Treat coverage, counts, and checklists as evidence rather than readiness by themselves. Approval covers only the confirmed decisions and evidence identity used by the plan.

## 5. Track delivery

When delivery coordination is material, read [delivery tracking](references/delivery-tracking.md). Consume active delivery owners' native results rather than copying their lifecycle/proof mechanics into Atọ́nà.

After a material result changes plan meaning, update the semantic plan first. Keep non-plan-affecting operational detail with its native owner.

## 6. Reconcile and close

Before `Closed`, require the Decision Frontier to remain empty, no blocking plan gap, current accepting delivery/proof for every in-scope obligation, explicit residual deferrals/limits, and completed durable knowledge reconciliation.

Read [durable knowledge reconciliation](references/durable-reconciliation.md) only at the closure boundary or when a durable insight can be reconciled naturally earlier. Preserve only knowledge that changes future work; do not turn lifecycle history into a documentation dump.

Before user-visible handoff, align plan status, Decision Frontier, delivery summary, freshness, remaining work, and next action. Use [suggested direction](references/suggested-direction.md) only when a separate build-direction handoff is actually useful.
