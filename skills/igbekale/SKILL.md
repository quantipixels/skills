---
name: igbekale
description: Produces a technical structure design, a ranked survey of structural friction, or an updated ARCHITECTURE.md. Use to design modules, interfaces, boundaries and data ownership, to survey where a codebase's structure hurts, to reassess technology or layout choices, or to document the architecture. Stops at the structure; it does not build it or render a review verdict.
---

# Ìgbékalẹ̀

Output: a selected structure (working record: report or design), ranked survey findings, or an updated canonical architecture overview (committed record: doc). Each carries the decisive trade-offs, critical invariants and unresolved gaps.

Needs: the question or purpose, and the system in scope. If either is missing, or the request is not about structure, return to the caller and say what is missing.

Resolve the question at its useful scale: a bounded module question gets a bounded answer; a system-wide question gets system depth.

## Method

**Workflow** (`asoju`): when the right shape is unsettled, ask for two structurally different designs from different providers (two-shape design) before choosing; start in an unfamiliar repository from a reader's repository record.

| Mode | Purpose |
| --- | --- |
| `design` | create or revise the technical structure; read [design](references/design.md) |
| `survey` | read [survey](references/survey.md); stop at ranked friction without designing corrections |
| `document` | read [document](references/document.md); update the canonical overview from established evidence |

Pin only what can change the result: subject, problem or desired outcome, scope and non-goals, material constraints, the relevant current structure, and evidence limits. Read the relevant parts of the project's architecture overview as an orientation map, not proof; verify material claims against current evidence. An existing design does not establish fitness, but sufficient current fitness evidence earns a skip.

Read only evidence that can change the architecture: domain knowledge, code, tests and configuration, runtime and operations, and the decisions and history that explain the current structure. Observed implementation proves structure and behavior, not intent. When symbol or caller identity controls the design, resolve declarations, overloads and consumers; a search absence needs known path, parser, index freshness and result-limit coverage.

Material domain meaning, substantive external facts and unsettled purpose, success or consequential trade-offs go back to the caller as named gaps; do not decide it silently in the design.

When reassessing established technology, dependencies, layout or build and test structure, read [architecture evolution](references/architecture-evolution.md). Revisit a choice when changed needs, recurring friction or a concrete new capability challenges its rationale; age or novelty alone is not a reason to migrate.

Give implementation readiness only when asked, when delivery would otherwise invent a material technical requirement, or when readiness is itself the useful result. Ask `fihanmi` for a view of substantial findings when it helps.

## Done

The structure covers each material driver with an owner, boundaries and invariants, and names the strongest alternative where the design was open; or the survey is ranked with evidence; or the overview's structural claims and source links are verified at the reviewed revision. Unresolved gaps are listed.

## Return

Return the result with the document path for an updated overview. Keep the canonical overview at its existing location, otherwise the repository root as `ARCHITECTURE.md`; link it rather than maintaining competing system descriptions. Write question-specific design as a record only when a durable one is useful, using the [architecture record](templates/architecture-record.md) when its structure helps.
