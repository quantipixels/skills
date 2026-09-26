# Managed initiative lifecycle

Use only when the governing workflow requires named readiness states, coordinated multi-candidate delivery or a maintained lifecycle record. Apply [initiative progression](../../commands/atona.md) for the shared plan, HTML handoff, delivery and workspace rules. These formal gates supplement that method.

## Maintain lifecycle state

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

## Shape through the Decision Frontier

Pin outcome, scope, constraints, assumptions, non-goals, evidence, risks, and open uncertainties. Read only current project/domain evidence that can materially change the plan.

Use [amose](../../commands/amose.md) when material project-specific meaning or applicability—terms, identities, state/lifecycle, policy, boundaries, relationships, ownership, or invariants—is unestablished. Familiar words do not settle applicability; current accepted domain evidence can.

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
→ consequential choice that changes accepted outcome, scope, policy, experience, risk, cost, compatibility, or trade-off; ask a single already-understood bounded choice directly. Use [arojinle](../../commands/arojinle.md) for unsettled purpose, beneficiary, success, consequential trade-offs, latent dependent choices, or a requested interview.
```

Maintain one Decision Frontier state:

```text
EMPTY   — no unresolved material user decision blocks readiness.
OPEN    — at least one material user decision is answerable now.
BLOCKED — material user decisions remain but prerequisite evidence/results are missing.
```

When `OPEN`, ask one already-understood bounded choice directly or use [arojinle](../../commands/arojinle.md) to establish desire and close consequential branches. When `BLOCKED`, resolve the missing prerequisites. Do not reopen settled decisions or manufacture questions for a complete brief.

Use other skills when they improve the plan; keep routine composition out of its lifecycle stages.

## Resolve required results and prove readiness

Before setting `Planned`, ask whether a fresh delivery/review owner would otherwise have to invent a material behavior/rule, technical architecture, consequential user decision, or delivery decomposition.

Use these seams when they are actually required:

- **Normative behavior / operating rules** — require a current [behavior contract](../../commands/seda-spec.md) with `SPEC_READY` when material behavior needs an implementation-independent contract for delivery/review, unless an established domain authority already owns the equivalent contract.
- **Software/system architecture** — require current `architect: IMPLEMENTATION_READY` when delivery would otherwise have to invent material system boundaries, ownership, topology, migration/recovery, compatibility, or another architecture-level decision. Establish consequential mechanism fitness for confirmed purpose/domain/quality drivers; reuse sound current evidence without automatic redesign.
- **Consequential user choice** — keep the Decision Frontier open/blocked; ask one already-understood bounded choice directly or use [arojinle](../../commands/arojinle.md) for unsettled desire, trade-offs or latent dependent choices. Do not bury the decision inside another specialist result.
- **Delivery decomposition** — use [delivery decomposition](../../commands/seda-tickets.md) as needed.

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

## Close the formal record

Before `Closed`, require an empty Decision Frontier, no blocking plan gap, current accepting proof for every in-scope obligation, explicit residual deferrals and no required durable-knowledge gap. Apply the shared initiative's workspace reconciliation and removal authority. Record `reconciled`, `reconciled-retained` or `reconciled-and-removed` when a linked workspace was involved.

Align status, current gate, Decision Frontier, delivery summary, evidence freshness, workspace disposition, remaining limits and next action in the same current plan. Use its requested or established format; a missing or stale required plan does not satisfy its handoff contract.
