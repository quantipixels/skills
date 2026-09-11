# Codebase assessment

Use only for `codebase` mode: a bounded existing-code snapshot needs an engineering-quality judgment rather than a candidate acceptance review.

Assess the actual system at its real scale, runtime, deployment model, trust boundaries, and change patterns. Prefer representative high-leverage boundaries and repeatedly costly seams over equal-weight whole-repository scanning. History, churn, complexity, fan-out, and tool output are leads; trace them to concrete caller burden, failure risk, proof difficulty, or maintenance cost before reporting a finding.

Inspect applicable dimensions without repeating the same observation:

- **Architecture and authority** — do boundaries contain real privileges, failures, policy, or ownership, or do callers still coordinate the hidden work?
- **State and lifecycle** — who owns identity, transitions, retries, idempotency, external effects, and recovery? Do not infer one lifecycle owner from one schema.
- **Modules and composition** — does a small interface hide coherent responsibility? Measure navigation/caller burden rather than file length.
- **Abstractions** — what knowledge does each layer remove? Challenge pass-through wrappers, speculative configurability, duplicated policy, and interfaces that expose internal choreography. Explicit local code can be better than another helper when the helper does not remove real knowledge or policy.
- **Language/runtime design** — judge idioms and guarantees of the actual stack; do not prescribe branded patterns without a concrete mistake they prevent.
- **Readability** — inspect the hardest control-flow, error, concurrency, and lifecycle boundaries. Fewer lines are not automatically simpler. Preserve useful whitespace, named intermediate values, explanatory comments, guard clauses, and explicit lifecycle steps when they make behavior easier to follow. Removing formatting, collapsing statements, or compressing asynchronous control flow is not simplification when comprehension worsens.
- **Tests and operation** — ask which public outcomes, races, recovery paths, composition, configuration, and startup wiring are actually proved. Test count and coverage are not quality verdicts. Do not recommend deleting difficult behavioral proof merely to shrink a suite when it still owns a public, security, money/data-integrity, transaction/locking/idempotency, concurrency/cancellation, recovery/migration, external-adapter, accessibility/interaction, or historically recurrent contract without a stronger complete owner.

When mutable shared state controls authorization, identify the invariant and all relevant writers before alleging a race. When a generic abstraction promises a type/relationship, verify that the implementation actually enforces it rather than trusting a caller-selected generic or unchecked cast.

For each material weakness, state location, mechanism, consequence/change cost, evidence, counterevidence, and smallest correction direction. Also report material strengths worth preserving. Use `pare` only when a deeper independent simplification result is needed and `architect` only when a consequential structural design question must be answered.

Return a bounded assessment, not a codebase certification. Mark dimensions not materially inspected as unassessed. Use grades only when requested and explain the scale:

- **A** — cohesive, well-enforced foundations with only localized weaknesses;
- **B** — sound foundations with meaningful but bounded friction;
- **C** — recurring caller burden, weak contracts, or maintainability costs that materially slow change;
- **D/F** — fundamental ownership, correctness, operability, or structural problems dominate the assessed boundary.

Do not use decimal precision or arithmetic averages that hide a critical weakness. A grade grants no security certification, merge, or deployment authority.
