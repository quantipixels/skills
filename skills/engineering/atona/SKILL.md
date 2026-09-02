---
name: atona
description: Maintain one exact-current initiative plan from early Draft through delivery and closure. Use when an initiative, migration, rollout, feature, or material workstream needs exploration, shaping, lifecycle readiness, coordinated handoffs, proof, and final reconciliation. Exclude specialist design/review, complete decision interviews, delivery execution, workspace infrastructure, and generic routing.
---

# Atọ́nà

Turn unclear intent into one live initiative plan. Keep one exact-current semantic plan and use `html-artifact` to visualise it as the primary human view when a visual artifact materially improves planning, review, or continuity.

Own plan meaning, decision coverage, lifecycle sufficiency, delivery integration, and closure. Keep consequential user-choice closure with `arojinle`, delivery execution with its active owners, repository `.qp` mechanics with `akosile` when that persistence path is used, and route selection with `alarina`. Use a specialist owner only when its independently useful result is actually required; software/system technical architecture belongs to `solution-architect`.

When a confirmed decision or material fact changes, create one scoped amendment map for affected owner results, reopen affected decisions/phases, mark only dependent proof stale, record affected delivery/representation/operational surfaces, and rerun affected decision/readiness/closure checks. Never present a partly superseded result as wholly current.

## 1. Establish the plan

For every material initiative, maintain one exact-current semantic plan using [the plan record template](templates/plan-record.md) as a semantic contract, not a rigid outline.

Keep the plan in current context when one-session use is sufficient. Persist it when continuity, recovery, independent review, or downstream consumption needs a durable identity. Prefer an existing or user-selected destination. When the selected destination is a repository-scoped QP workspace, resolve it through `akosile`:

```text
owner: atona
record_type: initiative-plan
subject: <stable initiative identity>
```

Do not require Git, a repository, or `.qp` merely to admit an initiative. Atọ́nà owns the plan body, revision, native status, decision frontier, delivery summary, decisions, and semantic validity. The selected persistence mechanism owns only its path/publication mechanics; Akọsílẹ̀ owns those mechanics when `.qp` is the selected destination.

Use `html-artifact` to visualise the outcome, status, decision frontier, confirmed decisions, phases, blockers, delivery/proof, and next action when the visual relationship materially improves the human view. Refresh a maintained projection after settled decision rounds or lifecycle transitions; never interrupt an active Àròjinlẹ̀ round for artifact work. Between those boundaries, or when a refresh fails, the semantic plan remains current and an older projection must not be presented as current.

The initiative-plan projection is document-shaped. Routine semantic refreshes use HTML Artifact's structural proof boundary and reuse current render proof while presentation behavior is unchanged.

When material questions are open, the active Àròjinlẹ̀ round is the user-facing handoff: lead with the questions and recommended answers and wait for the user's decisions.

### Synthesize settled context

When a supplied conversation, specification, issue, brief, or other source already contains enough settled context, synthesize it directly into the initiative plan rather than replaying discovery or starting an interview. Capture:

- the current problem or gap and affected actors when material;
- the desired outcome and observable acceptance;
- confirmed decisions;
- proof expectations and existing proof seams;
- scope and non-goals; and
- linked evidence with current identities.

Inspect the current work context only enough to use established vocabulary, behavior, constraints, durable decisions, and proof seams accurately. In a repository this may include instructions, code, tests, configuration, history, ADRs, integrations, and operations; none is required merely because Atọ́nà is active.

Separate confirmed context from inference. When the Decision Frontier is `EMPTY`, do not ask questions merely because this entry began as a conversation. When a material gap remains, classify and resolve it through the normal frontier instead of inventing a complete specification.

Use `seda-spec` when the initiative needs a compact implementation-independent behavior/operating contract beyond concise plan-local outcome and acceptance and that owner fits the subject. When another domain authority owns the normative contract, consume that current result instead. Keep only the lifecycle meaning and identity needed for readiness and delivery rather than copying the full contract into the plan.

## 2. Maintain lifecycle state

Track one status:

| Status | Enter when | Leave when |
| --- | --- | --- |
| `Draft` | planning begins, a material decision/readiness gap opens, or a closed plan is amended | the complete readiness gate passes (`Planned`) or inactive inventory is retained (`Backlog`) |
| `Planned` | the plan is startable, the material decision frontier is empty, and delivery has not begun | delivery starts (`In Progress`), a material gap opens (`Draft`), or closure passes with no delivery (`Closed`) |
| `In Progress` | authorized delivery is active | a material planning/decision gap opens (`Draft`) or delivery and closure pass (`Closed`) |
| `Backlog` | inactive inventory has an owner and reactivation trigger | active planning resumes (`Draft`) |
| `Closed` | every in-scope planning, decision, delivery, proof, documentation, and reconciliation obligation is complete | a material amendment opens (`Draft`) |

The status is Atọ́nà's judgment. Tickets, jobs, reviews, providers, settings labels, workspace indexes, and HTML cannot set it.

Derive one delivery summary from exact-current owner results:

- `Not required` — accepted plan needs no delivery work.
- `Not started` — delivery is required but no owned work has started.
- `Active` — authorized delivery is active and none blocks all safe progress.
- `Blocked` — a current blocker prevents all required safe progress.
- `Complete` — every in-scope delivery obligation has accepting proof.
- `Stale` — changed evidence/identity invalidates a used result.

Recompute it after every relevant result, blocker, dependency, candidate/work-item identity, or evidence change.

## 3. Shape the plan through the Decision Frontier Gate

Pin outcome, affected capabilities, scope, constraints, assumptions, non-goals, evidence, risks, and open uncertainties. Read the current domain/project constraints and durable decisions that can materially affect the plan. When working in a repository, include relevant `.learnings`, complete `.nongoals`, architecture/ADRs, code, tests, history, integrations, and recovery paths as applicable. When a repository direction conflicts with `.nongoals`, require an authorized `amose` exception or boundary update before planning past it.

When a material `Draft` initiative is too large or uncertain for its whole planning surface to be stated responsibly at once, read [progressive shaping](references/progressive-shaping.md). Use it to preserve known-but-not-yet-formulatable territory, explore breadth before depth, and re-chart only what new evidence makes formable. It does not add a lifecycle state, ticket system, owner, or Decision Frontier value.

Classify each material uncertainty that can be stated responsibly before assigning an owner:

```text
FACT
→ discoverable evidence; resolve directly or through iwadi/irinse when their owned result is needed.

PLAN_LOCAL
→ reversible plan detail that does not require user authority; Atọ́nà may recommend/settle it from current evidence.

SPECIALIST_DESIGN
→ independently useful domain/technical design result owned by the current specialist when one exists. Software/system architecture → solution-architect. If QP has no fitting owner, keep the need explicit rather than forcing it through a software owner.

MATERIAL_USER_DECISION
→ consequential choice that changes accepted outcome, scope, policy, user experience, risk, cost, compatibility, or trade-off; owned by arojinle.
```

Maintain one explicit frontier state in the plan:

```text
EMPTY   — every material user decision is confirmed, already confirmed with current evidence, non-blocking deferred with a re-entry contract, or not applicable.
OPEN    — one or more currently answerable material user decisions remain. OPEN takes precedence when other material decisions are blocked but at least one independent question can be asked now.
BLOCKED — unresolved material decisions remain, but none can currently be asked because prerequisite facts or specialist results are missing.
```

Do not invoke `arojinle` merely to reopen settled decisions. When the frontier is `OPEN`, give it the whole currently answerable material decision set and caller context, then let Àròjinlẹ̀ own the user question round. When some branches remain blocked, continue independent answerable branches and resolve missing prerequisites without suppressing the current open frontier. When `BLOCKED`, resolve the prerequisite fact/evidence first. When `EMPTY`, record why no interview is required.

Use `amose` for project/domain knowledge only when its native result can materially change the plan/frontier. Use `iwadi` for substantial reusable research, `irinse` for bounded tool evidence, and the current specialist only when its independently useful result is material. Delegate bounded independent/noisy planning work when inline exploration would materially pollute the plan context; consume only the compact result needed to continue.

Supporting skills return compact exact-current results. Keep detailed packets with their native owners and link them instead of copying them.

## 4. Prove readiness

Before `Planned`:

1. Re-read the exact plan as its delivery owner.
2. Recompute the Decision Frontier Gate. Require `EMPTY`; no open, blocked, stale, silently assumed, or blocking-deferred material decision may cross the gate.
3. When progressive shaping was needed, require no material not-yet-specifiable territory that delivery could encounter inside accepted scope. Exclude it, settle it, or give a genuine non-blocking re-entry contract rather than inventing the question.
4. If `arojinle` was used for the current decision set, require its exact-current final confirmation. If it was not required, record the current evidence proving why.
5. Verify every required specialist result against the exact plan/current identity. Require current `solution-architect: IMPLEMENTATION_READY` only when software/system architecture is material; require another specialist's native readiness/result only when that owner actually governs the needed design.
6. Treat coverage as an index, not proof: trace the top credible normal, failure, misuse, recovery, compatibility, migration/changeover, and operational mechanisms that apply to this initiative.
7. For each material obligation, require either current `seda-spec: SPEC_READY` when its implementation-independent behavior contract fits and a separate normative contract is needed, another domain authority's current contract when it does not, or plan-local observable acceptance with a named proof/evidence seam.
8. When delivery coordination is material, apply [delivery tracking](references/delivery-tracking.md)'s cumulative delivery-shape envelope before `Planned`. Require current expectations for delivery owners/workstreams or affected systems/surfaces, proof/evidence owners, new dependencies/contracts, handoff/review topology, and material replan triggers; counts may inform judgment but cannot become quotas.
9. Resolve every blocking dependency, recovery/changeover, proof, documentation, and operational gap.
10. Write the `Planned` revision and refresh any maintained primary human view.

Set `Planned` only when delivery can begin without inventing a material requirement. Approval covers only the listed decisions and exact evidence identity.

## 5. Track delivery

When multiple work units/candidates, dependencies, implementers, multi-session handoff, or delivery authority apply, read [delivery tracking](references/delivery-tracking.md). It owns delivery integration, handoffs, result reconciliation, and completion proof. Atọ́nà retains plan identity, decision/frontier integration, delivery-summary derivation, and closure.

After a material owner result changes plan meaning, update the semantic plan first and refresh any maintained human view at the next settled boundary. Keep non-plan-affecting operational detail outside the plan.

When a lifecycle result establishes knowledge that may outlive the initiative, add it to the plan's durable reconciliation inventory and reconcile it at the natural delivery boundary when possible.

## 6. Reconcile and close

Before `Closed`, verify the decision frontier remains empty; no blocking decision/gap remains; delivery/review match the exact current result/candidate; proof gaps/deferrals are explicit; and freezes hold.

Read [durable knowledge reconciliation](references/durable-reconciliation.md). Require every material lifecycle insight to have a proved disposition, no obsolete guidance to remain, and no knowledge needed by future work to survive only in transient lifecycle context.

Update the plan with final results/material semantic history and refresh any maintained human view.

Before every user-visible handoff, align plan status, decision frontier, delivery summary, plan freshness, remaining work, and next action, then apply [suggested direction](references/suggested-direction.md).
