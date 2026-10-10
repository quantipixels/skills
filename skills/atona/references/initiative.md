# Initiative progression

## Establish the destination

Start at the earliest unresolved step. Reuse supplied decisions, existing work and current evidence. Establish the problem, who it affects, the intended outcome, observable acceptance, scope and non-goals, and where to stop. An exploration-only or planning-only request ends at that result. An end-to-end build request carries through delivery without asking permission again at each stage. Publishing, merging, deploying and destructive cleanup still need the user's go-ahead. For mixed requests, separate the work you may do from the choices the user kept for themselves.

Find discoverable facts in the project before asking the user. Check that a source is current and applies; carry forward only evidence that changes the work. Ask one isolated consequential choice directly. When several consequential choices depend on each other, ask the caller for an interview and pass along the decisions already settled. Reuse complete briefs and accepted decisions. Keep doing independent work while a dependent choice is open.

## Keep the human in the plan

Keep one current plan. Put it where it helps the reader: in chat, in the existing issue or Markdown plan. A person who wants a page can get an HTML page generated from it (by `ojuiwe`). Never keep two plans that are edited separately. Present the first proposed direction before delivery so the user can judge it.

The plan carries what the reader needs to make the current decision: the decision or concern, the plan revision, the candidates and evidence it rests on, and any obligation whose omission would change a decision. This skill owns that content. A generated page is accepted only when those obligations and their limits are visible and current.

Update the plan after material changes and before dependent decisions or handoffs. Respect the user's review points without adding approval rounds. Domain, architecture, research and evidence records keep their own formats; they are not second plans.

## Explore and settle direction

When no direction is apparent, the options are unsatisfying, or other mechanisms need exploring, ask the caller for directions for the user to pick. Treat any evidence gap the same way: name it and ask the caller to fill it. Keep a promising idea, a confirmed choice and an accepted requirement distinct.

Use a known path when it helps, or compose a better one from host and SIGIDI tools, project procedures and the QP skills. A custom path needs no new skill, saved recipe or script. When later steps are uncertain, name the next step that produces evidence.

For a build request, carry the selected direction into shaping and delivery. If no credible direction survives, say why and what evidence or decision would unblock it. Do not repeat exploration for a settled direction.

## Shape enough to build

Keep the outcome and acceptance, confirmed decisions and material assumptions, delivery order, dependencies, risks, current blocker and next action in the one plan. Write the detail a fresh contributor would otherwise have to invent; skip empty bookkeeping.

Include documentation consequences in scope and acceptance. Reuse the builder's documentation evidence; for cross-slice or documentation-only reconciliation, ask the caller for a docs audit (assess) or sync (authorized fixes). Keep its obligations in this plan, not a second audit. Planning-only work names documentation obligations without applying them.

Before implementation, name the checks that prove acceptance and any verification the user deferred. Write acceptance as observable outcomes; keep accepted mechanisms and project constraints listed separately. Keep the project's own checks and the user's division of work. A new finding becomes required work only when it affects acceptance, invalidates evidence or reveals a mandatory obligation; otherwise it is a follow-up.

Keep decision-changing alternatives, rationale, uncertainty and counterevidence, and mark each choice proposed, confirmed, deferred or superseded. When traceability matters, connect acceptance through decisions and owners to delivery and proof. Show missing implementation or proof, mechanisms without an accepted basis, stale evidence and cumulative drift. Keep planned, implemented, reviewed, tested and live-verified distinct; include recovery steps where they matter.

Name what the plan still needs from the caller: settled meaning for domain identity, lifecycle, policy, ownership or invariants; a behavior contract when behavior needs a normative one; a structure decision when structure or a consequential mechanism's fitness is unestablished; tickets when delivery needs splitting. Reuse settled results. Not every initiative needs every branch.

When the route is unclear or later work cannot yet be stated responsibly, use progressive shaping. Choose the next question that produces evidence before guessing a backlog. Build only slices whose acceptance, dependencies and go-ahead are settled. Keep uncertain remaining scope visible; one ready slice does not make the whole initiative ready.

For consequential, uncertain, hard-to-reverse or heavily coordinated work, run a [premortem](premortem.md) and resolve material findings before treating the plan as ready to execute.

When a consequential rollout needs operational acceptance or data recovery, read [rollout readiness](rollout-readiness.md). Keep its checks and stop conditions in the plan or runbook.

Use [managed initiatives](managed-initiative.md) only when the workflow requires named readiness states, coordinated multi-candidate delivery or a durable lifecycle record. Size alone does not require them.

## Coordinate delivery and establish completion

Brief each child with the current plan, scope, limits, required evidence and stop condition, and check its returned evidence before you integrate it. Do not run more work than you can integrate and verify.

Each settled coding outcome goes to a builder with the acceptance, dependencies, workspace and the go-ahead you have. The builder owns implementation, verification and corrections; this skill owns order and whether the combined results complete the initiative. Read what comes back (change, evidence, blockers, scope changes), update the plan and continue to the next ready slice. Ask for a separate review of the integrated result when warranted or requested, and send accepted coding fixes back to the builder.

When delivery has several work units, owners, dependencies or a multi-session handoff, read [delivery tracking](delivery-tracking.md).

When you resume, get a material correction, find new evidence, or a child's report disagrees with the files, reconcile the path with the original requirements and accepted decisions. Go back to the source when the plan lacks the deciding detail. Name the affected premise, candidate, proof and next action, and change only what the new evidence invalidates. Routine results need no replanning or rereading of the whole history. Keep accepted evaluations, required reviews and concrete in-scope correctness concerns open until their evidence is checked, they are resolved, or the user drops them. For blocked work, record the exact missing prerequisite.

Resolve scope drift before continuing affected work. Keep work the user asked for or accepted, required checks, and obligations from existing contracts. Drop agent-proposed additions that do not serve acceptance; keep useful ones as optional follow-up. Changing the plan does not authorize deleting code, tests or user files.

Keep progress updates concrete: separate "implemented" from "verified", name the running check and what it settles, and state the real blocker. Report a material scope change promptly. No repeated reassurance or invented estimates.

Check whether the delivery evidence covers the initiative's acceptance, including how slices interact and the real user journey. When integrated behavior lacks proof or fails, give the builder that bounded integration outcome and read its result before closing. Task counts, finished children, isolated passing checks and provider status do not show the build works as a whole.

Choose the smallest check that closes each remaining acceptance gap. After a fix, rerun the affected checks; widen only for a concrete failure, a changed assumption, invalidated evidence or a governing requirement, and say why. Hypothetical adjacent risks do not justify another test campaign.

Publication needs the user's authorization. Keep implemented, integrated and released distinct; report an outstanding required stage as incomplete.

## Preserve continuity and close

Keep the plan in context for a short session. When it must persist, update the existing project plan or issue; otherwise save it as a plan record. Note the workspace and branch the work runs in, and update them when execution moves; leave machine-specific paths out of shared artifacts.

Keep ordinary rationale in the plan; read [durable reconciliation](durable-reconciliation.md) only when governing knowledge needs updating.

Before closing work done in a separate worktree, check that nothing needed exists only in this worktree; working records are shared across worktrees, so only untracked work files in the worktree itself need reconciling. Clean only state you have reconciled or that is disposable. Removing a worktree needs the user's go-ahead; keeping it does not block completion.

Close against the original scope and later decisions, when the outcome has current proof, required documentation and integration are done, the plan explains what was delivered and its limits, and no blocking in-scope obligation remains. For exploration-only or planning-only work, apply this to the requested artifacts and state that nothing was delivered.

Then update the plan and hand over promptly. Optional cleanup, broader review and visual polish are follow-ups; they do not hold accepted delivery open. Link decisive evidence instead of copying raw logs.

Return where the plan lives, the outcome, the decisive verification and its limits. If blocked, name the exact remaining work, prerequisite or user decision, and the next action; a recommendation is not completion. Continue authorized work instead of stopping at a suggested next step.
