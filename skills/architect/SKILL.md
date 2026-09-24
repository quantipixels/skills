---
name: architect
description: Design, survey, review or document technical structure, including ARCHITECTURE.md and a consequential mechanism's fitness for confirmed purpose and domain. Exclude implementation, initiative progression and code-review verdicts.
---

# Architect

Own the technical structure of a software system or consequential module and its canonical architecture overview. Resolve the architecture question at the smallest scale that is materially sufficient: a bounded module question gets a bounded design answer; a system-wide design gets the system depth it actually needs.

Delegate independent boundary assessments or design investigations to subagents when useful. Require concise findings and evidence; integrate them into the architecture judgment.

| Mode | Purpose |
| --- | --- |
| `survey` | read [survey](references/survey.md); stop at ranked friction without designing corrections |
| `design` | create or revise the technical structure |
| `review` | judge one exact architecture/design candidate read-only |
| `document` | read [document](references/document.md); update the canonical overview from established evidence |

Do not turn every design question into a full implementation-ready architecture packet. Use an implementation-readiness result only when the caller explicitly needs a gate, delivery would otherwise have to invent a material technical requirement, or the architecture spans enough consequential concerns that readiness itself is the useful result.

## Understand the architecture question

Pin only what can change the architecture result: subject/candidate, problem or desired outcome, scope/non-goals, material constraints/drivers, current relevant structure, and evidence limits.

Read relevant sections of the project's `ARCHITECTURE.md` or established equivalent as an orientation map, not proof; verify material claims against current evidence.

An existing design does not establish fitness, but sufficient current fitness evidence earns a skip. Assess the consequential mechanism against confirmed purpose, domain and quality drivers; review does not automatically authorize redesign.

When symbol or caller identity controls the design, resolve the relevant declaration, overload and consumers; a spelling match or repository map is not sufficient. Check path coverage, parser support, index freshness and result limits before treating search absence as evidence. Return to the actual interface, invariant or ownership question; a tool result is not an architecture verdict.

Read only evidence capable of changing the architecture: current domain/project knowledge, code/tests/configuration when implementation exists, runtime/deployment/operations evidence, governing decisions, and bounded history/provenance where it explains current structure. Retrieve relevant past decisions and lessons selectively and verify their applicability; no full archive read is required. Observed implementation proves current structure or behavior, not automatic architectural intent.

Use `amose` for material domain meaning or rule applicability, `iwadi` for substantive external facts, and `arojinle` when purpose, success or consequential trade-offs remain unsettled. Return a controlling nontechnical gap to the same caller rather than silently deciding it in the design.

Resolve unknowns that can change the design against current project and authoritative sources.

When reassessing established technology, dependencies, layout or build/test structure, read [architecture evolution](references/architecture-evolution.md). Revisit a choice when changed needs, recurring friction or a concrete new capability challenges its rationale; age or novelty alone is not a reason to migrate.

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

When module/interface/seam shape is material, read [module design](references/module-design.md). Prefer deep modules: small interfaces that hide substantial owned complexity and reduce caller burden. Use CUPID—composable, focused on one coherent purpose, predictable, idiomatic and domain-based—as a design lens, not a scorecard. Preserve locality; do not expose internal seams merely for implementation or tests.

When correctness depends on multiple writers or overlapping transactions over shared mutable state, read [shared-state design](references/shared-state.md).

When the requested system creates or materially changes agent tools, an assistant/automation surface, or agent-accessible product behaviour, read [agent-facing systems](references/agent-native-systems.md). Do not introduce an agent surface for unrelated work.

Apply YAGNI and KISS to the whole system: every element needs a material driver or real boundary. Remove layers only when required responsibilities survive without increasing caller burden or displacing complexity into a worse owner; fewer components alone is not simplification.

### Compare alternatives only when the design is genuinely open

Apply hard constraints first: accepted behavior, security/privacy/trust, required compatibility, ownership/lifecycle, recovery/changeover, and explicit non-goals.

When several credible structures remain and at least two independent criteria can materially change the choice, compare only decision-changing factors such as depth, locality, caller burden, operational load, migration cost, reversibility, compatibility, failure containment, or total system complexity. State the strongest credible alternative and decisive reason for the selected structure. Do not create a universal architecture scorecard.

Select reversible technical choices within accepted constraints. Ask a single already-understood bounded consequential choice directly. Use `arojinle` when desire, consequential trade-offs or latent dependent choices remain unsettled, or an interview is requested. Reuse accepted choices rather than reopening them merely because architecture is active.

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

Keep the canonical overview at its existing location, otherwise repository-root `ARCHITECTURE.md`. Persist question-specific architecture work to the existing project destination; otherwise `.qp/architect/`, using the compact [architecture record](templates/architecture-record.md) when needed. Link the overview rather than maintaining competing system descriptions.
