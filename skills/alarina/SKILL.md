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

Use `alaga` for a supplied build job that needs job-level integration, acceptance, knowledge reconciliation, or candidate review. Keep one directly selected specialist primary when it fully owns the artifact. Use `tdd` directly for one bounded test-first feature or fix without broader job stewardship.

Use `atona` while architecture or migration decisions, readiness, delivery state, or closure must remain active. Use `arojinle` for one new or reopened material decision. Before implementing a stateful refactor that can change lifecycle behavior, require `audit-refactor-behavior`.

For code review, use `qp-code-review` with supporting `simplify` by default; omit `simplify` only for an explicitly defect-only review. Use `simplify` alone for one changed-code candidate, `pare` for a complete-repository simplification audit, and `skill-portfolio-audit` for a bounded skill portfolio. Use `ko-skill` for one skill and its authorized changes.

Keep explanation with `salaye`, premise judgment with `ro-wo`, requested stress testing with `grilling`, and complete decision closure with `arojinle`.

Use `seda-pr` for bounded commit, push, and ready PR or MR reconciliation; `wo-pr` for monitoring; and `qp-code-review` for a verdict. Add a verdict to monitoring only when requested or required by repository policy. `triage-issue` starts from supplied evidence; repository reads, provider reads, and provider comments require separate authority.

`olofofo` is supporting-only and runs only when explicitly requested or activated by a global baseline.

| Starting situation | Route |
| --- | --- |
| The user needs help selecting the shortest useful QP route | `alarina` |
| Project terms, `CONTEXT.md`, relationships, invariants, scenarios, `.learnings`, `.nongoals`, or ADRs need clarification or reconciliation | `amose` |
| An idea, plan, or decision needs complete frontier rounds and a durable record | `arojinle` |
| One bounded feature or bug fix needs an explicit test-first implementation loop without broader build-job stewardship | `tdd` |
| One supplied build job needs job-level integration, acceptance, documentation or knowledge reconciliation, or applicable candidate review | `alaga` |
| Changed code or code-local comments need a read-only maintainability review | `simplify` |
| An entire repository needs a read-only, coverage-complete audit for material simplifications | `pare` |
| A bounded skill portfolio needs a read-only audit of inventory, health, state drift, routes, or capability gaps | `skill-portfolio-audit` |
| Bounded code or an active PR or MR needs broad or defect-only review | `qp-code-review`, with `simplify` for broad review |
| One bounded current-branch change needs commit, push, and ready-for-review GitHub PR or GitLab MR creation or reconciliation | `seda-pr` |
| One open GitHub PR or GitLab MR needs persistent pipeline and feedback monitoring | `wo-pr` |
| The literal agent session needs quiet continuity, proportionate quality nudges, and reusable cross-session wisdom | supporting `olofofo` |
| One material premise needs an evidence-backed check before agreement or disagreement | `ro-wo` |
| One user-supplied subject needs a plain-language explanation for a first-time reader | `salaye` |
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
