---
name: atona
description: Maintain one exact-current initiative plan from early Draft through delivery and closure. Use when an initiative, migration, rollout, feature, or material workstream needs exploration, shaping, lifecycle readiness, coordinated handoffs, proof, and final reconciliation. Exclude specialist design/review, complete decision interviews, delivery execution, workspace infrastructure, and generic routing.
---

# Atọ́nà

Turn unclear intent into one exact-current initiative plan. Own plan meaning, decision coverage, lifecycle sufficiency, delivery integration, current progression gate, and closure; do not absorb specialist design, consequential user decisions, delivery execution, persistence mechanics, or generic routing.

When a confirmed decision or material fact changes, update the affected plan meaning, stale only dependent conclusions/proof, and reopen only lifecycle work whose readiness changed. Never present a partly superseded plan as wholly current.

## 1. Establish the plan

For every material initiative, maintain one semantic plan using [the plan record template](templates/plan-record.md) as a contract rather than a rigid outline.

Keep it in current context when one-session use is sufficient. Persist only when continuity, recovery, independent review, or downstream consumption needs durable identity. Prefer an existing or user-selected destination; when that destination is repository-scoped `.qp` state, use `akosile` for storage mechanics.

For every material initiative beyond a minor bounded fix, maintain an `html-artifact` projection using [human view](references/human-view.md) as the approachable human operating view. The semantic plan and specialist owner results remain authoritative; HTML is a denormalized read model and may be absent or stale without changing semantic truth. Regenerate it after material plan changes, but let `html-artifact` keep verification proportional: structural/source/freshness checks are the default, while browser proof is earned only when rendered or interactive behavior materially controls acceptance.

When supplied context already settles the initiative, synthesize it directly rather than replaying discovery. Separate confirmed context from inference and capture only the problem/outcome, acceptance, confirmed decisions, scope/non-goals, material proof expectations, current progression gate, and evidence identities needed to plan responsibly.

## 2. Maintain lifecycle state

Track one status:

| Status | Meaning |
| --- | --- |
| `Draft` | planning/readiness has a material open gap |
| `Planned` | delivery can start without inventing a material requirement |
| `In Progress` | authorized delivery is active |
| `Backlog` | intentionally inactive with an owner/re-entry trigger |
| `Closed` | planning, delivery, proof, documentation, and any required durable reconciliation obligations are complete |

Atọ́nà alone sets plan status. Supporting results, tickets, provider state, projections, and workspace indexes are evidence only.

Derive a compact delivery summary from current owner results: `Not required | Not started | Active | Blocked | Complete | Stale`.

Keep the **current gate** explicit: the next material progression judgment the human/initiative must satisfy. Do not turn the initiative into a health score. A required gate condition cannot be averaged away by otherwise strong evidence.

## 3. Shape through the Decision Frontier

Pin outcome, scope, constraints, assumptions, non-goals, evidence, risks, and open uncertainties. Read only current project/domain evidence that can materially change the plan.

When unresolved terminology, conceptual boundaries, relationships, or invariants make the initiative itself ambiguous enough that planning would otherwise invent meaning, use `amose` for that independent domain-model clarification and consume its resolved model delta. Reading already-established project vocabulary does not require an `amose` handoff.

When the initiative is too uncertain to state responsibly at full depth, read [progressive shaping](references/progressive-shaping.md). Preserve known-but-not-yet-formulatable territory without inventing future requirements.

Classify material uncertainty by who must resolve it:

```text
FACT
→ discoverable evidence; resolve without asking the user.

PLAN_LOCAL
→ reversible planning detail within accepted authority.

SPECIALIST_RESULT
→ independently useful design/domain/technical/normative result the plan cannot responsibly invent.

MATERIAL_USER_DECISION
→ consequential choice that changes accepted outcome, scope, policy, experience, risk, cost, compatibility, or trade-off; resolve through `arojinle`.
```

Maintain one Decision Frontier state:

```text
EMPTY   — no unresolved material user decision blocks readiness.
OPEN    — at least one material user decision is answerable now.
BLOCKED — material user decisions remain but prerequisite evidence/results are missing.
```

When `OPEN`, give `arojinle` the whole currently answerable material decision set and consume its confirmed result. Do not reopen settled decisions. When `BLOCKED`, resolve only prerequisite evidence/results that can make the next decision formable.

Use another skill only when its independently useful result is material to plan readiness. Do not turn supporting capabilities into plan stages.

## 4. Resolve required results and prove readiness

Before setting `Planned`, ask whether a fresh delivery/review owner would otherwise have to invent a material behavior/rule, technical architecture, consequential user decision, or delivery decomposition.

Use these seams when they are actually required:

- **Normative behavior / operating rules** — require current `seda-spec: SPEC_READY` when material behavior needs an implementation-independent contract for delivery/review, unless an established domain authority already owns the equivalent contract.
- **Software/system architecture** — require current `architect: IMPLEMENTATION_READY` when delivery would otherwise have to invent material system boundaries, ownership, topology, migration/recovery, compatibility, or another architecture-level decision.
- **Consequential user choice** — keep the Decision Frontier open/blocked and resolve through `arojinle`; do not bury the decision inside another specialist result.
- **Delivery decomposition** — use `seda-ticket` when several semantic work units need explicit dependency/startability structure before delivery can begin safely. Do not require tickets for one coherent job merely because it has several implementation steps or independently checkable acceptance.

For other material specialist needs, use the relevant skill when its independent result is required. Keep only the result identity/readiness needed by the plan; do not copy another skill's procedure or lifecycle.

When delivery coordination or decomposition can affect planning readiness, read [delivery tracking](references/delivery-tracking.md) before declaring `Planned`; loading it does not authorize delivery.

Set `Planned` only when all are true:

- the Decision Frontier is `EMPTY`, with no silently assumed material user choice;
- no in-scope material territory remains that delivery could encounter but the plan cannot state responsibly;
- every required independent/normative result is present, accepting, current, and exact enough for the plan to rely on;
- every material delivery obligation has observable acceptance and a credible proof/evidence seam;
- required delivery decomposition/startability is established when the initiative needs it; and
- blocking dependency, changeover/recovery, documentation, operational, and delivery-shape gaps are resolved or explicitly outside scope with a valid re-entry condition.

Treat coverage, counts, rubric scores, and checklists as evidence rather than readiness by themselves. When several viable planning choices remain, compare only the criteria that can change the decision and apply hard gates first; do not let an aggregate score obscure a decisive constraint.

If a required result is absent, stale, blocked, or not ready, keep the plan `Draft` and make that gap visible when it controls progression.

## 5. Track delivery

When delivery coordination is material, read [delivery tracking](references/delivery-tracking.md). Consume active delivery owners' native results rather than copying their lifecycle/proof mechanics into Atọ́nà.

After a material result changes plan meaning, update the semantic plan first. Recompute the current gate, weakest limiting claim/gap, stale dependencies, and any maintained human projection. Keep non-plan-affecting operational detail with its native owner.

## 6. Reconcile and close

Before `Closed`, require the Decision Frontier to remain empty, no blocking plan gap, current accepting delivery/proof for every in-scope obligation, explicit residual deferrals/limits, and no unresolved durable-knowledge obligation that actually meets the promotion threshold below.

Treat the initiative's normal artifacts and history—plan, specification, tickets, PR/MR, review, commits, and provider history—as sufficient for ordinary implementation choices, rationale, findings, and reversible portfolio/design changes. Read [durable knowledge reconciliation](references/durable-reconciliation.md) only when the initiative established or changed stable governing knowledge that future work must rely on outside those normal lifecycle artifacts, or when an existing durable source of truth became materially stale.

Before user-visible handoff, align plan status, current gate, Decision Frontier, delivery summary, evidence/projection freshness, weakest material claim or blocker, remaining work, and next action. When a maintained human projection applies, require the current [human-view](references/human-view.md) visibility/assurance contract before presenting it as the current view. Use [suggested direction](references/suggested-direction.md) only when a separate build-direction handoff is actually useful.
