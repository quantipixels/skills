---
name: architect
description: Design, survey, or review the technical structure of a software system or consequential module at the smallest scale needed to resolve the architecture question. Use for architectural friction, technology/dependency fit, system boundaries, module/interface/seam shape, data/state ownership, integrations, deployment, quality scenarios, trade-offs, migration/recovery, or architecture sufficiency; exclude initiative lifecycle planning, user-decision closure, implementation, workspace infrastructure, and code-review verdicts.
---

# Architect

Own the technical structure of a software system or consequential module. Resolve the architecture question at the smallest scale that is materially sufficient: a bounded module question gets a bounded design answer; a system-wide design gets the system depth it actually needs.

Delegate independent boundary assessments or design investigations to subagents when useful. Require concise findings and evidence; integrate them into the architecture judgment.

| Mode | Purpose |
| --- | --- |
| `survey` | find and rank evidence-backed architectural friction without designing the correction |
| `design` | create or revise the technical structure |
| `review` | judge one exact architecture/design candidate read-only |

Do not turn every design question into a full implementation-ready architecture packet. Use an implementation-readiness result only when the caller explicitly needs a gate, delivery would otherwise have to invent a material technical requirement, or the architecture spans enough consequential concerns that readiness itself is the useful result.

## Understand the architecture question

Pin only what can change the technical design: subject/candidate, problem or desired outcome, scope/non-goals, material constraints/drivers, current relevant structure, and evidence limits.

Across modes, use `irinse` when structural, resolved dependency, flow, history, rule, runtime, database or build evidence materially controls the architecture decision and needs specialist acquisition or interpretation. Return to the actual interface, invariant or ownership question; a tool result is not an architecture verdict.

Read only evidence capable of changing the architecture: current domain/project knowledge, code/tests/configuration when implementation exists, runtime/deployment/operations evidence, governing decisions, and bounded history/provenance where it explains current structure. Observed implementation proves current structure or behavior, not automatic architectural intent.

Use `amose` and `iwadi` as needed.

Resolve unknowns that can change the design against current project and authoritative sources.

When reassessing established technology, dependencies, layout or build/test structure, read [architecture evolution](references/architecture-evolution.md). Revisit a choice when changed needs, recurring friction or a concrete new capability challenges its rationale; age or novelty alone is not a reason to migrate.

## Survey mode

Use `survey` when the question is where architecture work is warranted rather than what the replacement design should be. If the caller already supplied one exact architecture question or candidate, skip the survey and work at that scale.

Bound the search before scanning. Prefer the named subsystem, user pain point, failure area, or change envelope. When no area is supplied and repository history is available, inspect a bounded useful stretch of change history to identify repeatedly changing or tightly co-changing paths, then let those hot areas focus inspection. Widen only when the evidence is scattered or the requested scope requires it; do not equal-weight an entire repository by default.

When module/interface/seam shape is material, read [module design](references/module-design.md) and look for friction such as:

- callers repeating sequencing, branching, validation, recovery, mapping, or foreign-system knowledge that one owner could hide;
- one conceptual operation requiring repeated navigation across several shallow modules or files;
- forwarding layers whose interface costs nearly as much to understand as the behavior they hide;
- state, policy, trust, lifecycle, compatibility, or failure invariants spread across several callers or owners;
- internal or provider-specific details leaking through caller-facing interfaces;
- one recurring change requiring shotgun edits across unrelated call sites; and
- durable behavior that is difficult to prove through the current external interface without reaching into private choreography.

Signals are not findings. Apply the deletion test and seek counterevidence: a small layer may still own a real trust/protocol/lifecycle/compatibility boundary, and co-change may reflect a legitimate cohesive slice rather than bad architecture. Distinguish architectural ownership/interface problems from simplification (`atunwo` with a simplification focus), defects/review findings (`atunwo`), or missing causal diagnosis (`alaga` in diagnosis mode).

Tool output, churn metrics, fan-out, cycles, file size, test count, and complexity scores are leads only; trace the actual caller burden, invariant, or ownership failure before retaining a candidate.

When code judgment belongs to `atunwo`, pass the exact boundary, governing contracts, structural observations, and unresolved claim. Let it select review depth; reuse its current evidence instead of commissioning a second assessment of the same question. Architecture proposals remain proposals until implementation and proof exist.

Rank only evidence-backed candidates. Prefer decision-changing factors such as recurrence/change pressure, caller knowledge, locality, leverage, failure/trust ownership, proof difficulty, blast radius, and reversibility. Do not manufacture a universal architecture score.

For each retained candidate return the affected area, observed friction, likely misplaced responsibility or boundary, evidence, strongest material counterevidence, expected leverage/locality if deepened, and one of `Strong | Worth exploring | Speculative`. End with the top candidate and decisive reason when one stands out.

**Stop at discovery.** Do not propose the final interface, module decomposition, migration plan, or implementation-ready contract in `survey`. Once the user or caller selects a candidate, re-enter `design` mode for that exact architecture question.

## Design the smallest sufficient structure

Design from owned responsibilities and real boundaries inward. Specify only the concerns material to the question:

- ownership and system/subsystem boundaries;
- modules, interfaces, seams, and adapters;
- data/state/identity ownership and consistency;
- dependencies and integrations, including failure semantics;
- trust/security/privacy boundaries;
- deployment/runtime/configuration/operations when they shape the design;
- compatibility, migration, rollback, recovery, or deletion when material; and
- critical invariants implementation must preserve.

When module/interface/seam shape is material, read [module design](references/module-design.md). Prefer deep modules with small high-leverage interfaces and strong locality. Do not expose internal seams merely because implementation or tests use them.

When correctness depends on multiple writers or overlapping transactions over shared mutable state, read [shared-state design](references/shared-state.md).

When the requested system creates or materially changes agent tools, an assistant/automation surface, or agent-accessible product behaviour, read [agent-facing systems](references/agent-native-systems.md). Do not introduce an agent surface for unrelated work.

Apply YAGNI and KISS to the whole system: every element needs a material driver or real boundary. Remove layers only when required responsibilities survive without increasing caller burden or displacing complexity into a worse owner; fewer components alone is not simplification.

### Compare alternatives only when the design is genuinely open

Apply hard constraints first: accepted behavior, security/privacy/trust, required compatibility, ownership/lifecycle, recovery/changeover, and explicit non-goals.

When several credible structures remain and at least two independent criteria can materially change the choice, compare only decision-changing factors such as depth, locality, caller burden, operational load, migration cost, reversibility, compatibility, failure containment, or total system complexity. State the strongest credible alternative and decisive reason for the selected structure. Do not create a universal architecture scorecard.

Select reversible technical choices within accepted constraints. Ask a single bounded consequential choice directly. Use `arojinle` when the user requests an interview or dependent choices require decision-tree closure.

## Verify architectural sufficiency

Architecture must be coherent and falsifiable, but `architect` does not own delivery proof mechanics. State the critical invariants and ensure there is a credible way to verify the consequential claims. Name a specific enforcement/proof mechanism only when that mechanism materially shapes the architecture.

For a bounded design question, return the selected technical structure, decisive trade-offs, critical invariants, and unresolved gaps directly.

When implementation readiness is the requested or required result, read [architecture contract](references/architecture-contract.md) and return one:

- `IMPLEMENTATION_READY` — every material driver is covered, ownership/interfaces/invariants are coherent, and implementation needs no invented material technical requirement;
- `NOT_READY` — a material technical decision, conflict, migration/recovery obligation, or architecture defect remains; or
- `UNPROVED` — missing/stale evidence prevents responsible judgment.

Keep confidence separate from readiness when evidence strength materially helps interpretation. Confidence never converts `UNPROVED` into readiness.

## Review mode

In `review`, pin the exact architecture/design candidate and stay read-only. Judge the design at its existing scale rather than expanding it into a larger architecture exercise. Trace material drivers and invariants to the structure, challenge missing ownership/interfaces as well as unnecessary layers, and return the smallest evidence-backed correction or unresolved gap.

Use `html-artifact` as needed.

## Persistence

Persist to the existing project destination; otherwise `.qp/architect/`. Use the compact [architecture record](templates/architecture-record.md) when persistence is needed.
