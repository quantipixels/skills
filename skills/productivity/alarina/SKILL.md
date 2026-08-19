---
name: alarina
description: Select the shortest useful route through published QP skills. Focus on one primary outcome owner and only necessary supporting skills.
---

# Alárinà

Select one primary QP skill for the requested outcome. Respect an explicit user selection. Add a supporting skill only when its result is necessary; separate independent outcomes instead of forcing one owner to absorb them. Routing does not grant mutation, provider, credential, publication, or other missing authority.

Engineering, Design, Productivity, and Experimental are install groups, not routing priorities. `olofofo` is experimental and remains opt-in.

## Route

| Starting outcome | Primary skill | Mode |
| --- | --- | --- |
| Select the shortest QP route | `alarina` | — |
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
| Turn supplied work into consumable vertical tickets | `seda-ticket` | — |
| Commit, push, and create or reconcile a ready PR or MR | `seda-pr` | explicit invocation required |
| Monitor an open PR or MR through readiness | `wo-pr` | explicit invocation required |
| Visualize supplied results, purpose-fit reports, analysis, data, decisions, or designs in a portable browser artifact | `html-artifact` | — |
| Prepare a compact handoff for another agent or session | `handoff` | — |
| Draft, revise, or review developer documentation, technical communication, or applicable human-facing artifact copy | `technical-writing` | — |
| Remove AI tells, filler, vague abstraction, or instruction noise from existing prose | `yo-slop` | — |
| Analyze one coding-agent session or bounded corpus | `ayewo-igba-ise` | — |
| Research a question from primary sources into Markdown | `iwadi` | — |
| Select, configure, use, or remove a companion tool | `irinse` | — |
| Maintain quiet continuity for the literal agent session | supporting `olofofo` | — |
| Route an end-to-end visual request | `apere` | specialist route or built-in `logo`, `corporate identity program`, `icons`, `social graphics` |
| Define or reconcile brand identity | `brand` | — |
| Define tokens or component specifications | `eto-apere` | — |
| Implement accessible React/web UI | `asa-oju-ibanisoro` | — |
| Select evidence-backed UI/UX direction | `amoye-ui-ux` | — |
| Design a constrained banner, cover, hero, or ad | `banner-design` | — |
| Create an HTML presentation or pitch deck | `slides` | — |

Use `general` mode in `atunwo` for supplied or local candidates and `provider` mode for an active PR or MR. Default an unqualified code review to `broad`. Use `audit` only for requested behavior parity across a planned, in-progress, or completed stateful refactor or rewrite. Do not invent a mode that its owner does not define.

## Boundaries

- Keep a directly selected artifact specialist primary when it fully owns the result.
- Keep `pare` read-only. It may label a `deep-clean candidate`, but only a delivery owner with explicit opt-in may delete that proof.
- Keep project style, channel conventions, product truth, code conventions, accessibility conformance, localization, brand voice, and publishing with their direct owners; `technical-writing` owns the applicable structural and editorial pass.
- Keep document evidence, technical truth, artifact facts, schema, authority, and acceptance with their direct owners; `yo-slop` follows `technical-writing` as a final prose pass and must preserve their contract.
- Keep portable presentation-style reports with `html-artifact`; route requested slide decks to `slides`.
- Use `atona` while architecture or migration state remains active, `arojinle` for one new or reopened material decision, and `atunwo` in `audit` scope before a stateful refactor that can change lifecycle behavior.
- Keep PR or MR publication with `seda-pr`, monitoring with `wo-pr`, and review verdicts with `atunwo`.
- When another skill owns a code-review outcome but lacks provider access, `atunwo` may support only candidate acquisition and a fixed adapter handoff; this grants no defect, verdict, publication, or provider authority to the owner.
- Keep issue triage supplied-evidence-first. Repository reads, provider reads, and provider writes require their own authority.
- Run `olofofo` only when explicitly requested or activated by a global baseline; it is never the primary owner.

Check the active inventory before returning a route. If the correct owner is unavailable, name it without substituting another skill. Ask one focused question only when the answer selects a materially different owner or mode. Report the primary skill, applicable mode, one concise reason, and necessary supporting skills. Return no QP route when none fits.

When the selected owner disables model invocation, tell the user to invoke it through the host's explicit skill control and stop. Do not reproduce, partially execute, or delegate the hidden workflow.
