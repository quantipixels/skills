# Architecture survey

Read [architecture orientation](../references/architect/orientation.md) for evidence and persistence boundaries; preserve this command’s requested stop.

Use `survey` when the question is where architecture work is warranted rather than what the replacement design should be. If the caller already supplied one exact architecture question or candidate, skip the survey and work at that scale.

Bound the search before scanning. Prefer the named subsystem, user pain point, failure area, or change envelope. When no area is supplied and repository history is available, inspect a bounded useful stretch of change history to identify repeatedly changing or tightly co-changing paths, then let those hot areas focus inspection. Widen only when the evidence is scattered or the requested scope requires it; do not equal-weight an entire repository by default.

When an unfamiliar implementation hides the relevant owners or caller paths, use [sawari](sawari.md) for that bounded source map. Consume its locators and coverage limits, then assess architectural friction here; a source map alone is not a survey finding.

When module/interface/seam shape is material, read [module design](../references/architect/module-design.md) and look for friction such as:

- callers repeating sequencing, branching, validation, recovery, mapping, or foreign-system knowledge that one owner could hide;
- one conceptual operation requiring repeated navigation across several shallow modules or files;
- forwarding layers whose interface costs nearly as much to understand as the behavior they hide;
- state, policy, trust, lifecycle, compatibility, or failure invariants spread across several callers or owners;
- internal or provider-specific details leaking through caller-facing interfaces;
- one recurring change requiring shotgun edits across unrelated call sites; and
- durable behavior that is difficult to prove through the current external interface without reaching into private choreography.

Signals are not findings. Apply the deletion test and seek counterevidence: a small layer may still own a real trust/protocol/lifecycle/compatibility boundary, and co-change may reflect a legitimate cohesive slice rather than bad architecture. Distinguish architectural ownership/interface problems from simplification ([atunwo](atunwo.md) with a simplification focus), defects/review findings ([atunwo](atunwo.md)), or missing causal diagnosis ([alaga-diagnose](alaga-diagnose.md)).

Tool output, churn metrics, fan-out, cycles, file size, test count, and complexity scores are leads only; trace the actual caller burden, invariant, or ownership failure before retaining a candidate.

When code judgment belongs to [atunwo](atunwo.md), pass the exact boundary, governing contracts, structural observations, and unresolved claim. Let it select review depth; reuse its current evidence instead of commissioning a second assessment of the same question. Architecture proposals remain proposals until implementation and proof exist.

Rank only evidence-backed candidates. Prefer decision-changing factors such as recurrence/change pressure, caller knowledge, locality, leverage, failure/trust ownership, proof difficulty, blast radius, and reversibility. Do not manufacture a universal architecture score.

For each retained candidate return the affected area, observed friction, likely misplaced responsibility or boundary, evidence, strongest material counterevidence, expected leverage/locality if deepened, and one of `Strong | Worth exploring | Speculative`. End with the top candidate and decisive reason when one stands out.

**Stop at discovery.** Do not propose the final interface, module decomposition, migration plan, or implementation-ready contract in `survey`. Once the user or caller selects a candidate, use [architect-design](architect-design.md) for that exact architecture question.
