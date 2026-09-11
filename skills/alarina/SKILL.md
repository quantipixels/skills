---
name: alarina
description: Route one unresolved goal to the QP skill that owns the needed result. Use for choosing a QP skill, finding the next useful owner, understanding common combinations, or requesting the installed QP inventory.
---

# Alárinà

Route to the nearest owner of the unresolved result. Skip settled work. QP has no mandatory lifecycle; Alárinà does not perform another skill's method.

| Needed result | Owner |
| --- | --- |
| Explore credible directions | `ideate` |
| Challenge a premise | `ro-wo` |
| Resolve consequential choices | `arojinle` |
| Shape/update an initiative plan | `atona` |
| Specify observable behavior | `seda-spec` |
| Survey architectural friction, or design/review software/module structure | `architect` |
| Split settled work into tickets | `seda-ticket` |
| Deliver accepted code | `alaga` |
| Independently judge code | `atunwo` |
| Publish a PR/MR | `seda-pr` |
| Get an existing PR/MR ready | `wo-pr` |
| Assess an incoming report | `se-triage` |
| Diagnose an observed failure | `root-cause` |
| Find simplification opportunities | `pare` |
| Compare measured trial variants | `optimize` (Experimental) |
| Postmortem completed/paused work | `ayewo-igba-ise` |
| Walk through a candidate with a human | `hitl-review` |
| Exercise changed browser journeys | `dogfood` |
| Build a disposable decision instrument | `prototype` |
| Recommend/review interface direction | `amoye-ui-ux` |
| Define/review brand identity | `brand` |
| Explain with focused prose/visuals | `salaye` |
| Create a browser projection | `html-artifact` |
| Author/edit/prune prose | `oro-ologbon` |
| Create/improve/audit an agent skill | `ko-skill` |

Supporting capabilities stay inside the owning work when needed: `amose` for canonical domain meaning, `iwadi` for substantial research, `irinse` for high-leverage tool choice/usage, `qp-setup` for tool or QP/Codex setup, `pepeye` for native subagents, `akosile` for selected shared-workspace mechanics, and `yoruba-glossary` for Yorùbá technical language. `seda-sigidi`, `system-cleanup`, `pese`, and `slides` route directly when their named result is requested.

Use adjacent-boundary cues only when they change selection: report validity → `se-triage`, cause → `root-cause`, fix → `alaga`; simplification → `pare`, measured comparison → `optimize`, experiential decision → `prototype`; tool choice/usage → `irinse`, readiness/setup → `qp-setup`; code judgment → `atunwo`, delivery → `alaga`, publication → `seda-pr`, PR readiness → `wo-pr`.

Resolve names against installed QP definitions and respect each skill's activation and action permissions; routing to an owner does not grant mutation, publication, merge, deletion, or other authority. Report a missing QP skill rather than silently substituting another package's similarly named skill.

For an inventory, inspect installed QP definitions rather than treating this table as the catalogue. Return the starting owner and only useful next owners; when work is requested, invoke the owner rather than returning routing as the deliverable.
