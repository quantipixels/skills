---
name: atona
description: Carry an initiative through its requested outcome with a living, human-readable HTML plan, or directly create a behavior contract or delivery decomposition. Use for discovery, decisions, planning, coordinated delivery, behavior contracts, delivery decomposition, or resumed work. Use alaga for settled coding changes needing no initiative coordination.
---

# Atọ́nà

Own progression from the idea to the requested outcome. Keep one current plan, invoke specialist skills for their results, and continue authorized work until the outcome is built and verified. A plan, ticket set, or specialist handoff is an intermediate result when the user requested a build.

For every mode, obtain planning inputs through native readers or applicable document specialists. Use `irinse` only when choosing or interpreting an acquisition capability needs specialist guidance, and `iwadi` for substantive unresolved research. Missing or partially retrieved requirements remain readiness gaps; a source summary does not confirm a requirement.

When the requested stopping point is a behavior contract—including behavior-contract mode or an ordinary request to write or refine a behavior specification—read [behavior contract](references/behavior-contract.md) and return that standalone result. When the requested stopping point is delivery decomposition, read [delivery decomposition](references/decomposition.md) and return that standalone result. Do not start an initiative or require a living HTML plan for either bounded result. These branches remain usable by delivery and review callers.

## Establish the destination and authority

Start at the earliest unresolved step using supplied decisions, existing work, and current evidence. Establish the intended outcome, observable acceptance, scope/non-goals, and requested stopping point. An exploration-only or planning-only request ends at that result; an end-to-end build request carries through delivery without another permission request at each stage. Publication, merge, deployment, and destructive cleanup require applicable authority from the session or governing policy.

Resolve discoverable facts from relevant project knowledge before asking the user. Check source authority and current applicability; carry forward only evidence that changes the work. Surface consequential choices the existing intent cannot settle, using `arojinle` when they need a decision interview. Continue independent authorized work while a dependent choice is unresolved.

## Keep the human in the plan

Use `html-artifact` with [the initiative brief](references/human-view.md) for every plan, including exploration-only and planning-only work. Present the first proposed direction before delivery so the user can judge alignment. Maintain the same view through decisions, implementation, review, and completion; share its locator and source revision with contributors.

Update the plan first, then the view after material changes, before dependent decisions or delivery handoffs. Chat updates supplement this record. Honor existing authority and requested review boundaries without adding approval rounds. If the view is unavailable, report the deliverable gap and continue independent discovery and planning.

## Explore and settle direction

When credible directions still need generating, read [ideation](references/ideation.md). Use `iwadi` for material evidence gaps, use `alarina` in its premise-check branch when a consequential proposal needs challenge, and use `adanwo` in exploration mode when a disposable experiment can settle the uncertainty. Preserve the distinction between a promising idea, a confirmed choice, and an accepted requirement.

For a build request, carry the selected direction into shaping and delivery. If no credible direction survives, report why and the evidence or decision needed to proceed. Reuse a settled direction without repeating exploration.

## Shape enough to build

Keep the outcome and acceptance, confirmed decisions and material assumptions, delivery sequence, dependencies, risks, current blocker, and next action in one plan. Match detail to what a fresh contributor would otherwise have to invent; omit empty bookkeeping.

Use `amose` when domain meaning is unresolved, [behavior contract](references/behavior-contract.md) when behavior needs a normative contract, `architect` when technical structure needs settling, and [delivery decomposition](references/decomposition.md) when delivery needs decomposition. Consume their results without requiring every branch on every initiative.

When later work cannot yet be stated responsibly, read [progressive shaping](references/progressive-shaping.md). Resolve prerequisites and build only slices whose acceptance, dependencies, and authority are sufficiently settled. Keep uncertain remaining scope visible; slice readiness does not prove whole-initiative readiness.

For consequential, uncertain, difficult-to-reverse, or materially coordinated work, run a [premortem](references/premortem.md) and reconcile material findings before treating the affected plan as execution-ready.

When a consequential rollout needs operational acceptance or data recovery, read [rollout readiness](references/rollout-readiness.md). Keep its checks and stop conditions in the current plan or runbook; delivery and live execution retain their existing owners and authority.

Use [managed initiatives](references/managed-initiative.md) only when the governing workflow requires named readiness states, coordinated multi-candidate delivery, or a durable lifecycle record. Its formal gates supplement this workflow; size alone does not require them.

## Coordinate delivery and establish completion

For useful independent work, delegate through native host controls with the current plan/candidate, scope, authority, required evidence and stop condition. Keep one writer per mutable workspace or shared tool, and inspect decisive returned evidence before integrating it.

Use `alaga` as the builder for each sufficiently settled coding outcome. Supply its acceptance, relevant dependencies, workspace/candidate, and existing authority. Alága owns implementation, verification, and corrections; Atọ́nà owns sequencing and whether the combined results complete the initiative. Consume the returned candidate, evidence, blockers, and scope changes, update the plan, and continue to the next dependency-ready slice.

Let Alága handle review and corrections for its coding change. Use `atunwo` for a separate judgment across the integrated candidate when warranted or requested; reuse applicable review evidence and return accepted coding corrections to `alaga`.

When delivery has multiple work units or candidates, dependencies, owners, or a multi-session handoff, read [delivery tracking](references/delivery-tracking.md). Keep execution and proof details with their owners; Atọ́nà owns whether the combined results satisfy the initiative.

After a material decision, discovery, or delivery result, update the affected plan and reopen only dependent choices and proof. Resolve scope drift before continuing affected work. A partly superseded result is not wholly current.

Assess whether current delivery evidence covers initiative acceptance, including interactions between delivered slices and the real user journey when relevant. Reuse applicable proof. When integration behavior lacks proof or fails, give `alaga` the bounded integration outcome to verify and correct; consume that result before closing the initiative. Task counts, worker completion, isolated passing checks, and provider status do not establish that the build works as a whole. Keep missing proof and blockers visible and resolve them within scope.

Use `wo-pr` in publication mode for authorized publication and its stewardship mode for requested PR/MR readiness work. Keep implementation, integration, and release state distinct; report an outstanding required stage as incomplete.

## Preserve continuity and close

Keep the plan in context for a short session. When continuity or downstream use needs persistence, update the existing project plan; for a new plan without a project destination, use `.qp/atona/<datetime>-<slug>/plan.md` and keep its living view beside it as `plan.html`. Set the filename-safe UTC timestamp once at creation (for example, `20260914T153000Z`) and reuse the paths throughout delivery; do not rename existing records to adopt this convention. Record the absolute execution workspace and `branch: <branch-name> [main|worktree]`, plus the main-worktree path for a linked worktree. Update them when execution moves.

Keep ordinary rationale in the plan and living view; read [durable reconciliation](references/durable-reconciliation.md) only when required governing knowledge needs updating.

Before closing a linked-worktree initiative, reconcile required `.qp` state into the accepting workspace, clean only reconciled/disposable state, and record the workspace disposition. Preserve unresolved state. Worktree removal requires user approval; retaining it does not block completion.

Close only when the requested outcome has current accepting proof, required documentation and integration are complete, the living view explains the delivered outcome and remaining limits, and no blocking in-scope obligation remains. For exploration-only or planning-only work, apply that bound to the requested artifacts and state that delivery has not been performed.

Return the living view's locator, outcome, decisive verification, and material limits. If blocked, identify the exact remaining work, prerequisite or human decision, and next action; a recommendation is not completion. Continue authorized executable work instead of ending at a suggested next step.
