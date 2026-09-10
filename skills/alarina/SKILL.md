---
name: alarina
description: Route a goal through QP skills using their entrypoints, useful combinations, and common work paths. Use for choosing a QP skill, finding the next step, understanding how QP skills fit together, or requesting the QP inventory.
---

# Alárinà

Route through QP skills from the current work state. Skip settled steps and stop at the requested result.

## Idea to delivery

| What is needed now | Use |
| --- | --- |
| Credible directions to explore | `ideate` |
| Challenge a proposal or assumption | `ro-wo` |
| Resolve consequential choices | `arojinle`, which uses `amose` |
| Shape an initiative, migration, or changing plan | `atona` |
| Specify observable behavior | `seda-spec` |
| Design software or module structure | `architect` |
| Split settled work into deliverable tickets | `seda-ticket` |
| Implement a settled change or fix | `alaga` |
| Define coding boundaries without implementation | `alaga` in scope-only mode |
| Commit, push, and open or update a PR/MR | `seda-pr` |
| Watch or get an existing PR/MR ready | `wo-pr` |

A settled change can go straight to `alaga`; an unsettled initiative may use `arojinle` and `atona` first. Add `seda-spec`, `architect`, or `seda-ticket` where those results are missing. `alaga` already includes implementation proof and independent review. Publication and ongoing PR work are separate entrypoints, not automatic tail steps.

## Other starting points

| Situation | QP route |
| --- | --- |
| Incoming report needs assessment | `se-triage` |
| Failure needs a causal explanation | `root-cause`; use `alaga` when the requested next result is a fix |
| Code or refactor needs independent review, or a codebase needs a quality assessment | `atunwo` |
| System needs a read-only simplification audit | `pare` |
| Compare trial variants and decide whether a measured gain merits keeping one | `optimize` (Experimental) |
| Human wants to walk through a candidate | `hitl-review` |
| A completed event or session needs a postmortem | `ayewo-igba-ise` |
| Interface direction, identity, or journey verification | `amoye-ui-ux`, `brand`, or `dogfood` respectively |
| A decision needs something concrete to try | `prototype` |
| Explain with prose, diagrams, code-shape sketches, or focused HTML | `salaye` |
| Standalone browser report or presentation deck | `html-artifact` or `slides` respectively |
| Technical communication, prose editing, or requested pruning | `oro-ologbon` |
| Author or revise an agent skill | `ko-skill` |

Triage assesses a report; diagnosis explains a failure; delivery fixes it. Start with the unresolved question rather than sending every bug through all three. Likewise, a request to review code starts at `atunwo`, not at implementation.

An improvement request is not automatically an experiment. `pare` judges structural simplification; `optimize` compares trial variants for a measured keep/revert/no-improvement decision; `prototype` settles a question through truthful experience. Validate a supplied skill change with `ko-skill`. An unknown implementation does not by itself require optimization: use `alaga` for a supplied improvement job unless comparative trials are needed to establish the requested result. Do not send these owners through each other as mandatory stages.

## Supporting capabilities

Use these within the selected work rather than turning them into stages:

- Meaning and evidence: `amose` for domain modelling, `iwadi` for substantial research, `irinse` for companion tools, `yoruba-glossary` for Yorùbá technical terms.
- Work management: `alaga` for explicit coding scope steering, `pepeye` for supervised native subagents, `akosile` for selected shared workspace storage.
- Specific operations: `qp-setup` for optional Codex instructions and host settings, `seda-sigidi` for an agent identity, `system-cleanup` for macOS cleanup, `pese` for explicitly requested private serving.

Resolve names against the installed QP definitions and respect their activation and action permissions. For an inventory, list the installed QP skills, not every capability in the host. Report a missing skill rather than silently substituting another package's similarly named skill.

For routing advice, give the starting skill and useful next steps. For requested work, use the selected skills; the route is not the deliverable.
