# Codebase assessment

Use when the subject is a bounded existing-code snapshot. Match coverage to light or deep review; this scope needs engineering-quality judgment rather than a candidate acceptance verdict.

Assess the actual system at its real scale, runtime, deployment model, trust boundaries, and change patterns. Prefer representative high-leverage boundaries and repeatedly costly seams over equal-weight whole-repository scanning. History, churn, complexity, fan-out, and tool output are leads; trace them to concrete caller burden, failure risk, proof difficulty, or maintenance cost before reporting a finding.

Inspect applicable dimensions without repeating the same observation:

- **Architecture and authority** — do boundaries contain real privileges, failures, policy, or ownership, or do callers still coordinate the hidden work?
- **State and lifecycle** — who owns identity, transitions, retries, idempotency, external effects, and recovery? Do not infer one lifecycle owner from one schema.
- **Modules and composition** — does a small interface hide coherent responsibility? Measure navigation/caller burden rather than file length.
- **Abstractions** — what knowledge does each layer remove? Challenge pass-through wrappers, speculative configurability, duplicated policy, and interfaces that expose internal choreography. Explicit local code can be better than another helper when the helper does not remove real knowledge or policy.
- **Language/runtime design** — judge idioms and guarantees of the actual stack; do not prescribe branded patterns without a concrete mistake they prevent.
- **Readability** — inspect the hardest control-flow, error, concurrency, and lifecycle boundaries. Flag compressed formatting when it obscures intent or departs from established project style.
- **Tests and operation** — assess evidence for public outcomes, failure and recovery paths, concurrency, configuration, and startup wiring. Test count and coverage are not quality verdicts. Preserve tests that uniquely protect required behavior or known regressions; recommend removal only when the obligation is obsolete or retained evidence covers it at least as strongly.

Use [boundary failures](boundary-failures.md) when authorization depends on shared state or generic abstractions promise type guarantees that need scrutiny.

For each material weakness, state location, mechanism, consequence/change cost, evidence, counterevidence, and smallest correction direction. Also report material strengths worth preserving. Use [simplification](simplification.md) when deeper analysis is needed and [architect-design](../../commands/architect-design.md) only for an unresolved consequential structural design question.

Return a bounded assessment, not a codebase certification. Mark dimensions not materially inspected as unassessed. Use grades only when requested and explain the scale:

- **A** — cohesive, well-enforced foundations with only localized weaknesses;
- **B** — sound foundations with meaningful but bounded friction;
- **C** — recurring caller burden, weak contracts, or maintainability costs that materially slow change;
- **D/F** — fundamental ownership, correctness, operability, or structural problems dominate the assessed boundary.

Do not use decimal precision or arithmetic averages that hide a critical weakness. A grade grants no security certification, merge, or deployment authority.
