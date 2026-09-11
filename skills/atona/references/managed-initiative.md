# Managed initiative lifecycle

Use this branch only when the governing workflow needs named readiness states, coordinated multi-candidate delivery, or a maintained lifecycle record. Ordinary plans use the main skill directly. These gates preserve formal consumers; they are not mandatory stages of every task.

# Atọ́nà

Turn unclear intent into one exact-current initiative plan. Own plan meaning, decision coverage, lifecycle sufficiency, delivery integration, current progression gate, and closure; do not absorb specialist design, consequential user decisions, delivery execution, persistence mechanics, or generic routing.

When a confirmed decision or material fact changes, update the affected plan meaning, stale only dependent conclusions/proof, and reopen only lifecycle work whose readiness changed. Never present a partly superseded plan as wholly current.

## 1. Establish the plan

For every material initiative, maintain one semantic plan using [the plan record template](../templates/plan-record.md) as a contract rather than a rigid outline.

Keep it in current context when one-session use is sufficient. Persist only when continuity, recovery, independent review, or downstream consumption needs durable identity. Prefer an existing intentional project destination; otherwise use `.qp/atona/` in the current workspace.

When execution is bound to a concrete working directory, persist its absolute path and branch as `<branch-name> [main|worktree]`. For a linked worktree, also persist the absolute main-worktree path. Treat that workspace and its `.qp` as the current initiative candidate; update the workspace fields when execution moves.

Use `html-artifact` as needed with [the initiative brief](human-view.md). Update the plan before refreshing a maintained view; a stale view is not current evidence.

When supplied context already settles the initiative, synthesize it directly rather than replaying discovery. Separate confirmed context from inference and capture only the problem/outcome, acceptance, confirmed decisions, scope/non-goals, material proof expectations, current progression gate, and evidence identities needed to plan responsibly.

## 2. Maintain lifecycle state

Track one status:

| Status | Meaning |
| --- | --- |
| `Draft` | planning/readiness has a material open gap |
| `Planned` | a current premortem supports readiness and delivery can start without inventing a material requirement |
| `In Progress` | authorized delivery is active |
| `Backlog` | intentionally inactive with an owner/re-entry trigger |
| `Closed` | accepted outcome/proof are complete and required local candidate state has been reconciled |

Atọ́nà alone sets plan status. Supporting results, tickets, provider state, and projections are evidence only.

Derive a compact delivery summary from current owner results: `Not required | Not started | Active | Blocked | Complete | Stale`.

Keep the **current gate** explicit: the next material progression judgment the human/initiative must satisfy. Do not turn the initiative into a health score. A required gate condition cannot be averaged away by otherwise strong evidence.

## 3. Shape through the Decision Frontier

Pin outcome, scope, constraints, assumptions, non-goals, evidence, risks, and open uncertainties. Read only current project/domain evidence that can materially change the plan.

Use `amose`.

When the initiative is too uncertain to state responsibly at full depth, read [progressive shaping](progressive-shaping.md). Preserve known-but-not-yet-formulatable territory without inventing future requirements.

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

When `OPEN`, use `arojinle` on the answerable decision frontier. When `BLOCKED`, resolve the missing prerequisites. Do not reopen settled decisions.

Use other skills when they improve the plan; keep routine composition out of its lifecycle stages.

## 4. Resolve required results and prove readiness

Before setting `Planned`, ask whether a fresh delivery/review owner would otherwise have to invent a material behavior/rule, technical architecture, consequential user decision, or delivery decomposition.

Use these seams when they are actually required:

- **Normative behavior / operating rules** — require current `seda-spec: SPEC_READY` when material behavior needs an implementation-independent contract for delivery/review, unless an established domain authority already owns the equivalent contract.
- **Software/system architecture** — require current `architect: IMPLEMENTATION_READY` when delivery would otherwise have to invent material system boundaries, ownership, topology, migration/recovery, compatibility, or another architecture-level decision.
- **Consequential user choice** — keep the Decision Frontier open/blocked and resolve through `arojinle`; do not bury the decision inside another specialist result.
- **Delivery decomposition** — use `seda-ticket` as needed.

Retain the identities and readiness of required specialist results, not their procedures.

When delivery coordination or decomposition can affect planning readiness, read [delivery tracking](delivery-tracking.md) before declaring `Planned`; loading it does not authorize delivery.

Run the [plan premortem](premortem.md) against this candidate plan, or verify that an existing premortem still applies. Reconcile its material findings before assessing the gate.

Set `Planned` only when all are true:

- the premortem is current, its material readiness threats are resolved, and any residual risk is justified within accepted constraints and the responsible decision-maker's authority;
- the Decision Frontier is `EMPTY`, with no silently assumed material user choice;
- no in-scope material territory remains that delivery could encounter but the plan cannot state responsibly;
- every required independent/normative result is present, accepting, current, and exact enough for the plan to rely on;
- every material delivery obligation has observable acceptance and a credible proof/evidence seam;
- required delivery decomposition/startability is established when the initiative needs it; and
- blocking dependency, changeover/recovery, documentation, operational, and delivery-shape gaps are resolved or explicitly outside scope with a valid re-entry condition.

Treat coverage, counts, rubric scores, and checklists as evidence rather than readiness by themselves. When several viable planning choices remain, compare only the criteria that can change the decision and apply hard gates first; do not let an aggregate score obscure a decisive constraint.

If the premortem or another required result is absent, stale, blocked, or not ready, keep the plan `Draft` and make that gap visible when it controls progression.

## 5. Track delivery

When delivery coordination is material, read [delivery tracking](delivery-tracking.md). Consume active delivery owners' native results rather than copying their lifecycle/proof mechanics into Atọ́nà.

After a material result changes plan meaning, update the semantic plan first. Recompute the current gate, weakest limiting claim/gap, stale dependencies, and the brief for any maintained view. Keep non-plan-affecting operational detail with its native owner.

## 6. Reconcile and close

Before `Closed`, require the Decision Frontier to remain empty, no blocking plan gap, current accepting delivery/proof for every in-scope obligation, explicit residual deferrals/limits, and no unresolved durable-knowledge obligation required by the governing contract or owning result.

When the initiative ran in a linked worktree, inspect that worktree's `.qp`, reconcile only the material state needed by the accepting workspace, then clean reconciled/disposable local state while preserving anything not safely reconciled. Do not mirror the directory wholesale. Record one workspace disposition: `reconciled`, `reconciled-retained`, or `reconciled-and-removed`.

After local-state cleanup, offer to remove the completed linked worktree. Removal requires explicit user approval; declining removal does not block `Closed`. Approval to remove the worktree does not authorize force-deleting unrelated dirty or untracked project files; if Git reports unresolved state, surface it.

Keep ordinary rationale in normal initiative artifacts. Read [durable knowledge reconciliation](durable-reconciliation.md) only when stable governing knowledge must survive beyond them or an existing durable authority is materially stale; the knowledge owner decides admission and reconciliation.

Before user-visible handoff, align plan status, workspace/disposition when relevant, current gate, Decision Frontier, delivery summary, evidence/projection freshness, weakest material claim or blocker, remaining work, and next action. When a human view is required, consume HTML Artifact's current result against the initiative brief; a missing or stale view does not satisfy that deliverable. Use [suggested direction](suggested-direction.md) only when a separate build-direction handoff is actually useful.
