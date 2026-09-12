# Workflow contract

Use for authoring or adapting a Pepeye workflow lane. A workflow declares useful topology between independently owned results; it does not restate or rewrite the methods inside those skills.

## Keep a lane small

A workflow should name:

- **outcome** — the user-visible result the lane advances toward;
- **entry** — when the lane is useful;
- **stages** — semantic result owners, with conditions that make a stage necessary;
- **dependencies** — only real ordering requirements;
- **independence** — stages or judgments whose evidence must come from a separate context;
- **plan review** — any explicit plan that becomes a material workflow artifact must be independently reviewed before it is treated as ready or used to progress work;
- **recovery** — the nearest owner to revisit when later evidence invalidates earlier state;
- **completion** — the evidence that lets delivery progression stop; and
- **closure** — the terminal retrospective plus disposition of any earned learning.

Prefer a readable Markdown lane over a new workflow DSL. Add deterministic parsing/runtime machinery only when repeated real use proves that agents cannot reliably follow the declarative form.

## Dispatch stages through assignments

Each stage names one primary skill. Supporting skills are optional and stay subordinate to that primary result. The workflow decides *what bounded result is needed now*; the selected skill decides *how to produce that result*.

Put workflow-specific constraints in the dispatched assignment, not in the skill definition. The assignment may state the bounded outcome, current evidence/candidate, authority/workspace, required independence, evidence to return, and stop condition. Do not add instructions such as “when running inside Pepeye,” “return to the workflow,” or “do not advance to the next stage” to `alaga`, `atona`, `architect`, `atunwo`, or another skill merely so one workflow can compose it.

A selected skill may delegate to subagents when useful under its own method. The active provider/host harness owns worker instantiation, nesting/capacity, model/effort mapping, and equivalent execution mechanics. The workflow should constrain authority, independence, candidate identity, and result boundaries when those matter; it should not reproduce provider harness mechanics inside skill instructions.

### Review material plans

Plan review is a workflow assignment, not a second planning owner and not a special planner profile.

Whenever an explicit plan becomes a material workflow artifact—because it is the requested deliverable, gates a consequential decision, or will govern downstream delegated/multi-stage execution—dispatch a fresh independent reviewer over that fixed plan before treating it as ready, accepted, or usable for progression. The rule applies regardless of who authored the plan: `atona`, the lead, the user, a persisted artifact, or another workflow.

Pin the exact plan, accepted outcome, current constraints, consequential decisions, and decisive evidence. Keep review read-only where the host can enforce it. Challenge, as applicable, hidden assumptions, unresolved decisions, sequencing/dependencies, ownership, feasibility, architecture/contract gaps, proof strategy, stale evidence, failure handling, migration/rollback/recovery, and credible simpler routes.

The reviewer returns findings, rejected concerns, proof gaps, and a bounded disposition. It does not rewrite the plan or advance the workflow. Route confirmed corrections to the nearest semantic owner; after a material plan change, review the fixed plan again before treating it as ready. Editorial-only changes outside the judgment boundary do not require another pass.

If the work is small enough to proceed directly and no explicit plan exists, do not manufacture a plan or review stage merely to satisfy this rule.

For implementation candidates, `atunwo` remains the independent code-judgment method. Plan review does not replace code review.

Do not use the lane as a mandatory waterfall. Skip a stage when its result is already current and sufficient. Insert an omitted owner when a material unresolved result appears. Parallelize stages only when their evidence/writes are independent or safely isolated.

The workflow lead receives the dispatched assignment's result and decides what semantic result is needed next. That return/continuation behavior is part of the orchestration layer, not a responsibility the selected skill must encode.

## State carried between stages

Carry the smallest cross-stage capsule that can change progression:

- accepted outcome and current non-goals;
- consequential decisions and assumptions;
- current plan/spec/architecture identities when they govern downstream work;
- exact candidate/source identity;
- unresolved blockers/branches;
- authority and workspace boundaries; and
- evidence/proof/review freshness.

Prefer exact locators and summaries over replaying full upstream transcripts.

## Failure and recovery

Route invalidation to the nearest semantic owner:

- missing/current external evidence → `iwadi`;
- consequential choice reopened → `arojinle`;
- delivery sequence/dependencies changed → `atona`;
- technical structure invalidated → `architect`;
- observable behavior/contract changed → `seda-spec`;
- implementation defect or incomplete delivery → `alaga`;
- review evidence stale because candidate/base changed → `atunwo`;
- publication state wrong or missing → `seda-pr` / `wo-pr` as appropriate.

Do not restart the whole workflow when only one downstream dependency is stale.

## Terminal retrospective

Every completed, materially paused, abandoned, or disputed Pepeye workflow/autonomous run closes through `ayewo-igba-ise` after its current result state is fixed. The retrospective judges the bounded run; it does not mutate the surface it is reconstructing.

After Àyẹ̀wò returns, harvest only durable improvements the evidence justifies:

- route each accepted improvement to its natural semantic owner;
- use `amose` `.learnings` maintenance only when the learning is stable, non-obvious, independently evidenced, likely to recur, consequential if forgotten, and not already represented by a stronger maintained source;
- ordinary session history, rationale, one-off discoveries, and speculative advice remain with the postmortem/PR/plan; and
- no qualifying durable learning is a valid outcome.

A workflow is retrospectively closed only when the postmortem is complete and qualifying learnings are harvested or explicitly recorded as pending owner handoffs requiring separate authority.

## Workflow admission

Create a named workflow only when the composition itself recurs or materially improves progression. A one-off sequence can remain an ad-hoc Pepeye workflow. Avoid workflow catalogues that merely enumerate every possible combination of skills.
