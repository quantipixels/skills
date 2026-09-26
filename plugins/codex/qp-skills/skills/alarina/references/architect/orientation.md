# Architecture orientation and evidence

Own the technical structure of a software system or consequential module and its canonical architecture overview. Resolve the architecture question at the smallest scale that is materially sufficient: a bounded module question gets a bounded design answer; a system-wide design gets the system depth it actually needs.

Delegate independent boundary assessments or design investigations to subagents when useful. Require concise findings and evidence; integrate them into the architecture judgment.

## Understand the architecture question

Pin only what can change the architecture result: subject/candidate, problem or desired outcome, scope/non-goals, material constraints/drivers, current relevant structure, and evidence limits.

Read relevant sections of the project's `ARCHITECTURE.md` or established equivalent as an orientation map, not proof; verify material claims against current evidence.

An existing design does not establish fitness, but sufficient current fitness evidence earns a skip. Assess the consequential mechanism against confirmed purpose, domain and quality drivers; review does not automatically authorize redesign.

When symbol or caller identity controls the design, resolve the relevant declaration, overload and consumers; a spelling match or repository map is not sufficient. Check path coverage, parser support, index freshness and result limits before treating search absence as evidence. Return to the actual interface, invariant or ownership question; a tool result is not an architecture verdict.

Read only evidence capable of changing the architecture: current domain/project knowledge, code/tests/configuration when implementation exists, runtime/deployment/operations evidence, governing decisions, and bounded history/provenance where it explains current structure. Retrieve relevant past decisions and lessons selectively and verify their applicability; no full archive read is required. Observed implementation proves current structure or behavior, not automatic architectural intent.

Use [amose](../../commands/amose.md) for material domain meaning or rule applicability, [iwadi](../../commands/iwadi.md) for substantive external facts, and [arojinle](../../commands/arojinle.md) when purpose, success or consequential trade-offs remain unsettled. Return a controlling nontechnical gap to the same caller rather than silently deciding it in the design.

Resolve unknowns that can change the design against current project and authoritative sources.

When reassessing established technology, dependencies, layout or build/test structure, read [architecture evolution](architecture-evolution.md). Revisit a choice when changed needs, recurring friction or a concrete new capability challenges its rationale; age or novelty alone is not a reason to migrate.


## Persistence

Keep the canonical overview at its existing location, otherwise repository-root `ARCHITECTURE.md`. Persist question-specific architecture work only when needed, following [records](../records.md) and an existing project destination when present; use the compact [architecture record](templates/architecture-record.md) when helpful. Link the overview rather than maintaining competing system descriptions.
