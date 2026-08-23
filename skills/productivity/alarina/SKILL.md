---
name: alarina
description: Select the shortest useful route through published QP skills. Focus on one primary outcome owner and only necessary supporting skills.
---

# Alárinà

Select one primary QP skill for the requested outcome. Respect an explicit user selection. Add a supporting skill only when its result is necessary; separate independent outcomes instead of forcing one owner to absorb them. Routing does not grant mutation, provider, credential, publication, or other missing authority.

When Pepeye mode is active, act as Pepeye's exact-current leaf-owner registry for the current phase. Return the smallest credible owner route, but do not select, replace, or advance Pepeye's playbook. Outside Pepeye mode, retain direct shortest-route ownership.

Engineering, Design, Productivity, and Experimental are install groups, not routing priorities. `pepeye` is experimental and remains opt-in.

## Route

| Starting outcome | Primary skill | Mode |
| --- | --- | --- |
| Select the shortest QP route | `alarina` | — |
| Drive one task through QP-native playbooks, checkpoints, proof, pause or pickup, and learning | `pepeye` | explicit or authorized-baseline lifecycle mode |
| Clarify or reconcile project terms, rules, knowledge, or decisions | `amose` | — |
| Resolve or stress-test a material decision with a durable record | `arojinle` | — |
| Deliver one bounded feature or fix test-first | `alaga` | `test-first` |
| Deliver a supplied build job through integration and review | `alaga` | `job` |
| Keep an architecture or migration plan active through delivery | `atona` | — |
| Audit behavior parity for a stateful refactor or rewrite | `atunwo` | `audit`; `general` or read-only `provider` target |
| Review bounded code for maintainability only | `pare` | `review`; add `atunwo` as provider adapter only for an active PR or MR |
| Review bounded code for defects and maintainability | `atunwo` | `broad`; `general` or `provider` target |
| Review bounded code only for defects | `atunwo` | `defect-only`; `general` or `provider` target |
| Audit an entire repository for simplifications | `pare` | `audit` |
| Identify unnecessary implementation, dependencies, configuration, support artifacts, or tests | `pare` | `audit` or `review` |
| Implement an accepted bounded `pare` cleanup slice | `alaga` | `job`; deep test deletion also requires explicit opt-in |
| Author or validate one skill, or audit a skill portfolio | `ko-skill` | — |
| Explain a supplied subject to a first-time reader | `salaye` | — |
| Test one material premise before judgment | `ro-wo` | — |
| Assess one supplied issue before implementation | `se-triage` | — |
| Give one AI agent a durable soul or refresh its identity | `seda-sigidi` | — |
| Turn supplied work into consumable vertical tickets | `seda-ticket` | — |
| Commit, push, and create or reconcile a ready PR or MR | `seda-pr` | — |
| Monitor an open PR or MR through readiness | `wo-pr` | — |
| Visualize supplied results, purpose-fit reports, analysis, data, decisions, or designs in a portable browser artifact | `html-artifact` | — |
| Prepare a compact handoff for another agent or session | `handoff` | — |
| Draft, revise, or review developer documentation, technical communication, or applicable human-facing artifact copy | `technical-writing` | — |
| Clean prose or explicitly prune verbosity and repetition without changing its contract | `yo-slop` | — |
| Analyze one coding-agent session or bounded corpus | `ayewo-igba-ise` | — |
| Research a question from primary sources into Markdown | `iwadi` | — |
| Select, configure, use, or remove a companion tool | `irinse` | — |
| Qualify and reconcile reusable learning as the task outcome | `pepeye` | lifecycle mode; use the `learn` phase |
| Route broad, ambiguous, or multi-deliverable design work | `apere` | lightweight route packet |
| Define brand identity, logos, corporate identity, or custom icon language | `brand` | — |
| Create feed posts, carousels, stories, social templates, or social campaign variants | `social-graphics` | — |
| Define tokens or component specifications | `eto-apere` | — |
| Implement accessible React/web UI or product icons | `asa-oju-ibanisoro` | — |
| Select or persist evidence-backed UI/UX direction | `amoye-ui-ux` | — |
| Design a constrained banner, cover, hero, or ad | `banner-design` | — |
| Create a presentation or pitch deck | `slides` | — |

Use `general` mode in `atunwo` for supplied or local candidates and `provider` mode for an active PR or MR. Default an unqualified code review to `broad`. Use `audit` only for requested behavior parity across a planned, in-progress, or completed stateful refactor or rewrite. Do not invent a mode that its owner does not define.

## Boundaries

- Keep a directly selected artifact specialist primary when it fully owns the result.
- Use `apere` only when the design owner is unclear, several design owners/deliverables are involved, or design-specific prerequisites, dependency order, shared constraints, or approval boundaries must be established. Its result is a route packet, not an artifact.
- When an `apere` route packet contains several artifacts that must actually be produced and integrated, give that exact packet to `alaga` as the build job; `apere` does not absorb delivery lifecycle.
- Keep visual/UX direction and its optional MASTER/page record with `amoye-ui-ux`; keep canonical tokens, component specifications, generated configuration, and migrations with `eto-apere`.
- Keep custom icon visual language with `brand` and product UI implementation with `asa-oju-ibanisoro`.
- Keep `pare` read-only. It may label a `deep-clean candidate`, but only a delivery owner with explicit opt-in may delete that proof.
- Keep project style, channel conventions, product truth, code conventions, accessibility conformance, localization, brand voice, and publishing with their direct owners; `technical-writing` owns the applicable structural and editorial pass.
- Keep document evidence, technical truth, artifact facts, schema, authority, and acceptance with their direct owners. `yo-slop` follows the structural owner as a final cleanup or explicit prune pass and must preserve their contract.
- Keep portable presentation-style reports with `html-artifact`; route requested slide decks to `slides`.
- Use `atona` while architecture or migration state remains active, `arojinle` for one new or reopened material decision, and `atunwo` in `audit` scope before a stateful refactor that can change lifecycle behavior.
- Keep PR or MR publication with `seda-pr`, monitoring with `wo-pr`, and review verdicts with `atunwo`.
- When another skill owns a code-review outcome but lacks provider access, `atunwo` may support only candidate acquisition and a fixed adapter handoff; this grants no defect, verdict, publication, or provider authority to the owner.
- Keep issue triage supplied-evidence-first. Repository reads, provider reads, and provider writes require their own authority.
- Activate `pepeye` through explicit invocation or an authorized project or global baseline. While active, Pepeye owns playbook selection and task-level progression; Alárinà supplies current leaf routes, and every specialist retains its native outcome, procedure, proof, and authority gates.

Check the active inventory before returning a route. If the correct owner is unavailable, name it without substituting another skill. Ask one focused question only when the answer selects a materially different owner or mode. Report the primary skill, applicable mode, one concise reason, and necessary supporting skills. Return no QP route when none fits.

When the selected owner disables model invocation, tell the user to invoke it through the host's explicit skill control and stop. Do not reproduce, partially execute, or delegate the hidden workflow.
