---
name: atona
description: Carry an initiative through its requested outcome with a living, human-readable HTML plan. Use for discovery, decisions, planning, coordinated delivery, or resuming that work. Honor exploration-only and planning-only requests; use alaga for settled coding changes needing no initiative coordination.
metadata:
  maturity: experimental
---

# Atọ́nà

Own progression from the idea to the requested outcome. Keep one current plan, invoke specialist skills for their results, and continue authorized work until the outcome is built and verified. A plan, ticket set, or specialist handoff is an intermediate result when the user requested a build.

## Establish the destination and authority

Start at the earliest unresolved step using supplied decisions, existing work, and current evidence. Establish the intended outcome, observable acceptance, scope/non-goals, and requested stopping point. An exploration-only or planning-only request ends at that result; an end-to-end build request carries through delivery without another permission request at each stage. Publication, merge, deployment, and destructive cleanup require applicable authority from the session or governing policy.

Resolve discoverable facts from relevant project knowledge before asking the user. Check source authority and current applicability; carry forward only evidence that changes the work. Surface consequential choices the existing intent cannot settle, using `arojinle` when they need a decision interview. Continue independent authorized work while a dependent choice is unresolved.

## Keep the human in the plan

Use `html-artifact` with [the initiative brief](references/human-view.md) for every plan, including exploration-only and planning-only work. Create and present the living view with the first proposed direction, before delivery; show uncertainty rather than waiting for a finished plan. Scale its detail to the work, not whether it exists. The agent's plan and the human's understanding are both required results.

Maintain one document through decisions, implementation, review, and completion. Give `arojinle` and other contributors its identity and current source revision; consume their results into it rather than commissioning parallel summaries. Keep it understandable to a reader with no prior project or chat context.

Update the plan first, then refresh the view after material decisions, scope changes, delivery/review results, blockers, or verification changes, before asking for dependent decisions or handing off affected delivery. Foreground what changed and its effect on direction, progress, and next action. Chat updates supplement the document; routine tool activity does not require an update.

Presenting the view does not create new approval rounds: honor existing authority and any requested review-before-build boundary. A missing or stale view is a deliverable gap, not permission to claim planning complete. If `html-artifact` or delivery of its result is unavailable, report that gap and continue independent authorized work without treating a chat summary as the required view.

## Explore and settle direction

When credible directions still need generating, read [ideation](references/ideation.md). Use `iwadi` for material evidence gaps, `ro-wo` to challenge a consequential proposal, and `prototype` when a disposable experiment can settle the uncertainty. Preserve the distinction between a promising idea, a confirmed choice, and an accepted requirement.

For a build request, carry the selected direction into shaping and delivery. If no credible direction survives, report why and the evidence or decision needed to proceed. Reuse a settled direction without repeating exploration.

## Shape enough to build

Keep the outcome and acceptance, confirmed decisions and material assumptions, delivery sequence, dependencies, risks, current blocker, and next action in one plan. Match detail to what a fresh contributor would otherwise have to invent; omit empty bookkeeping.

Use `amose` when domain meaning is unresolved, `seda-spec` when behavior needs a normative contract, `architect` when technical structure needs settling, and `seda-ticket` when delivery needs decomposition. Consume their results without copying their methods or requiring every skill on every initiative.

When later work cannot yet be stated responsibly, read [progressive shaping](references/progressive-shaping.md). Resolve prerequisites and build only slices whose acceptance, dependencies, and authority are sufficiently settled. Keep uncertain remaining scope visible; slice readiness does not prove whole-initiative readiness.

For consequential, uncertain, difficult-to-reverse, or materially coordinated work, run a [premortem](references/premortem.md) and reconcile material findings before treating the affected plan as execution-ready.

Use [managed initiatives](references/managed-initiative.md) only when the governing workflow requires named readiness states, coordinated multi-candidate delivery, or a durable lifecycle record. Its formal gates supplement this workflow; size alone does not require them.

## Coordinate delivery and establish completion

Use `alaga` as the builder for each sufficiently settled coding outcome. Supply its acceptance, relevant dependencies, workspace/candidate, and existing authority. Alága owns implementation, verification, and corrections; Atọ́nà owns sequencing and whether the combined results complete the initiative. Consume the returned candidate, evidence, blockers, and scope changes, update the plan, and continue to the next dependency-ready slice.

Let Alága handle review and corrections for its coding change. Use `atunwo` for a separate judgment across the integrated candidate when warranted or requested; reuse applicable review evidence and return accepted coding corrections to `alaga`.

When delivery has multiple work units or candidates, dependencies, owners, or a multi-session handoff, read [delivery tracking](references/delivery-tracking.md). Keep execution and proof details with their owners; Atọ́nà owns whether the combined results satisfy the initiative.

After a material decision, discovery, or delivery result, update the affected plan and reopen only dependent choices and proof. Resolve scope drift before continuing affected work. A partly superseded result is not wholly current.

Assess whether current delivery evidence covers initiative acceptance, including interactions between delivered slices and the real user journey when relevant. Reuse applicable proof. When integration behavior lacks proof or fails, give `alaga` the bounded integration outcome to verify and correct; consume that result before closing the initiative. Task counts, worker completion, isolated passing checks, and provider status do not establish that the build works as a whole. Keep missing proof and blockers visible and resolve them within scope.

Use `seda-pr` for authorized publication and `wo-pr` for requested PR/MR stewardship. Keep implementation, integration, and release state distinct; report an outstanding required stage as incomplete.

## Preserve continuity and close

Keep the plan in context for a short session. When continuity or downstream use needs persistence, update the existing project plan; otherwise use `.qp/atona/`. Record the absolute execution workspace and `branch: <branch-name> [main|worktree]`, plus the main-worktree path for a linked worktree. Update them when execution moves.

Keep ordinary rationale in the plan and living view; read [durable reconciliation](references/durable-reconciliation.md) only when required governing knowledge needs updating.

Before closing a linked-worktree initiative, reconcile required `.qp` state into the accepting workspace, clean only reconciled/disposable state, and record the workspace disposition. Preserve unresolved state. Worktree removal requires user approval; retaining it does not block completion.

Close only when the requested outcome has current accepting proof, required documentation and integration are complete, the living view explains the delivered outcome and remaining limits, and no blocking in-scope obligation remains. For exploration-only or planning-only work, apply that bound to the requested artifacts and state that delivery has not been performed.

Return the living view's locator, outcome, decisive verification, and material limits. If blocked, identify the exact remaining work, prerequisite or human decision, and next action; a recommendation is not completion. Continue authorized executable work instead of ending at a suggested next step.
