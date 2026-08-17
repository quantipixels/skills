---
name: alarina
description: Select the shortest useful route through published QP skills. Focus on one primary outcome owner and only necessary supporting skills.
---

# Alarina

Map one user prompt to one primary QP skill and any necessary supporting skills. Alarina owns route selection, not the selected specialist workflow.

## 1. Select the route

Use the task's current state and requested outcome. Respect a QP skill that the user explicitly selected. Recommend an additional QP skill only when a clear gap, conflict, or safety condition requires it.

Choose the shortest route that fully covers the requested outcome. Select one primary skill as the outcome owner. Add supporting skills only when they have a clear role. Do not prescribe a broader process when a direct skill covers the task.

When one prompt contains independent outcomes with different owners, return separate routes. Make a skill supporting only when its result is necessary to complete the primary outcome; do not make one skill own unrelated work.

Keep ordinary documentation with the outcome skill that changes or verifies the behavior. Routing a skill does not grant source, provider, credential, publication, or mutation authority.

### Resolve overlaps

Use `alaga` as the first route for an unqualified supplied build job that needs job-level integration, acceptance, required documentation or project-knowledge reconciliation, or applicable candidate review. The job can contain one or many delivery units. When the requested artifact directly selects one published specialist and no broader job stewardship is needed, keep that specialist primary. Use `tdd` directly when the requested outcome is one bounded feature or bug fix under an explicit test-first implementation loop and no broader build-job stewardship is requested. Within an Alaga code build, TDD can own production-behavior proof as a supporting skill. Keep pure explanation, bare review, monitoring, publication, and provider lifecycle work with their direct owners unless their results are necessary to complete the build.

Route a settled plan artifact to Alaga only when the material decisions and content are supplied and the requested job is to build that exact artifact. Route architecture or migration work to Atona when its decisions, readiness, integration, delivery state, or closure must remain active in a live plan.

Before implementation, a stateful refactor requires an `audit-refactor-behavior` result when it may change transitions, ordering, locking, retries, idempotency, financial ownership, or behavior across entry points. `tdd` or `alaga` owns later implementation only after the audit establishes the baseline and implementation guardrails.

Use `arojinle` to close a new or reopened material decision. Atona remains primary when that decision belongs to its live architecture or migration plan and consumes the exact-current Arojinle result. After confirmation, use `amose` for project-model, project-knowledge, and ADR reconciliation; it does not choose the decision.

Use `ro-wo` for one brief, bounded premise check before agreeing or disagreeing with a material opinion, proposal, assumption, scenario, recommendation, or decision-shaping hypothetical. Keep open-ended conversational exploration with `salaye`, relentless user-requested stress testing with `grilling`, and complete decision closure with `arojinle`.

Treat an unqualified request to review code as broad. Select `qp-code-review` as the primary owner and `simplify` as its supporting maintainability specialist. Select `qp-code-review` alone only when the user explicitly limits the review to defects and excludes maintainability.

Use `unknot` instead when the requested outcome is a read-only simplification audit of the complete repository with explicit subsystem coverage and prioritized opportunities. Keep `simplify` with one bounded changed-code candidate.

Use `skill-portfolio-audit` when the requested unit is a bounded collection of agent skills and the outcome is portfolio-wide inventory, health, state drift, route overlap, or capability-gap analysis. Keep `ko-skill` with one skill and all authorized skill changes.

Use `olofofo` only when a global baseline activates it or the user explicitly asks it to track the literal session. It remains supporting-only; the active task keeps its primary owner.

Use `seda-pr` to commit and push one bounded current-branch change, then create or reconcile its ready-for-review PR or MR narrative and bounded metadata. Use `wo-pr` alone for a bare watch, monitor, babysit, or keep-an-eye-on request. Use `qp-code-review` directly for a bare verdict review. Add code review to monitoring only when the user explicitly requests a verdict or current repository policy requires one.

For `triage-issue`, start with supplied evidence. Repository source reads, provider reads, and one provider comment require separate authority.

| Starting situation | Route |
| --- | --- |
| The user needs help selecting the shortest useful QP route | `alarina` |
| Project terms, relationships, invariants, scenarios, `.learnings`, `.nongoals`, or ADRs need clarification or reconciliation | `amose` |
| An idea, plan, or decision needs complete frontier rounds and a durable record | `arojinle` |
| One bounded feature or bug fix needs an explicit test-first implementation loop without broader build-job stewardship | `tdd` |
| One supplied build job needs job-level integration, acceptance, documentation or knowledge reconciliation, or applicable candidate review | `alaga` |
| Changed code or code-local comments need a read-only maintainability review | `simplify` |
| An entire repository needs a read-only, coverage-complete audit for material simplifications | `unknot` |
| A bounded skill portfolio needs a read-only audit of inventory, health, state drift, routes, or capability gaps | `skill-portfolio-audit` |
| Bounded code or an active PR or MR needs broad or defect-only review | `qp-code-review`, with `simplify` for broad review |
| One bounded current-branch change needs commit, push, and ready-for-review GitHub PR or GitLab MR creation or reconciliation | `seda-pr` |
| One open GitHub PR or GitLab MR needs persistent pipeline and feedback monitoring | `wo-pr` |
| The literal agent session needs quiet continuity, proportionate quality nudges, and reusable cross-session wisdom | supporting `olofofo` |
| One material premise needs an evidence-backed check before agreement or disagreement | `ro-wo` |
| One idea, plan, decision, document, or code candidate needs conversational exploration, explanation, investigation, research, analysis, or evaluation | `salaye` |
| One issue or bug report needs supplied-evidence-first classification and a next action | `triage-issue` |
| Supplied work needs consumable vertical tickets with blockers, acceptance, and lifecycle state | `seda-ticket` |
| A planned or completed refactor needs a parity ledger, or a stateful refactor requires a pre-implementation behavior gate | `audit-refactor-behavior` |
| Supplied content, evidence, decisions, diagrams, or design specifications need translation into one checked, portable HTML artifact or bounded linked variant set | `html-artifact` |
| Architecture or migration work needs one live plan from decisions through delivery, with a clear next action | `atona` |
| Brand voice, identity, assets, or consistency | `brand` |
| Design tokens, CSS variables, component specs, or token migration | `eto-apere` |
| React/web UI, Tailwind, shadcn/ui, responsive behavior, or accessibility implementation | `asa-oju-ibanisoro` |
| UI/UX direction, style, palette, typography, stack, or interaction guidance | `amoye-ui-ux` |
| Social, ad, web-hero, cover, or print banner | `banner-design` |
| HTML presentation, pitch deck, or data-backed slide story | `slides` |
| A visual design request spans multiple deliverables and needs one design owner | `apere` |
| The current conversation needs a safe handoff for another agent | `handoff` |
| One coding-agent session or bounded multi-session corpus needs an evidence-backed friction, recurrence, and durable-improvement assessment | `ayewo-igba-ise` |
| A question needs high-trust research from primary sources, captured in a Markdown file | `iwadi` |
| One portable agent skill needs creation, revision, or validation | `ko-skill` |
| A companion tool needs selection, installation, configuration, integration, bounded use, verification, or removal | `irinse` |

Check the active skill inventory before returning the route. When the correct owner is unavailable, name it as unavailable and do not substitute another skill.

Ask one focused question only when different answers would select materially different owners. Return no QP route when no published skill fits the requested outcome.

## 2. Report the route

If the user asks only which skill owns the prompt, report the primary skill, one concise reason, and any supporting skills.

If the selected primary skill is unavailable, report the route and missing owner.

State the route only when its choice, trade-off, or unresolved decision affects the user.
