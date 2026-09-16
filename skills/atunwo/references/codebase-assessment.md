# Existing-system assessment

Use for engineering-quality judgment of an existing system, at the requested light or deep scope. Judge its actual scale, runtime, deployment and change patterns. Trace representative boundaries in light review; cover the agreed boundary systematically in deep review and mark unassessed dimensions.

Inspect the applicable dimensions together, without duplicating findings:

- **Ownership and architecture:** locate privileges, policy, state and failure handling. Check whether callers must coordinate work the owning module should encapsulate.
- **Lifecycle:** trace identity, transitions, retries, idempotency, external effects and recovery through their actual writers. One schema does not prove one lifecycle owner.
- **Modules and abstractions:** ask what knowledge an interface hides and what each layer removes. Challenge pass-through wrappers, speculative variation and duplicated policy by concrete caller or change cost.
- **Language and readability:** judge the actual stack's guarantees and the hardest error, concurrency and lifecycle paths. Preserve names, intermediate values, comments and explicit steps that explain intent; smaller source is not automatically easier to change.
- **Proof and operation:** establish which public outcomes, recovery paths, configuration, startup wiring and deployed boundaries are proved. Retain difficult tests that uniquely protect a required failure signal until another proof owner fully subsumes it.

Report substantiated weaknesses and useful strengths with source locations, mechanism, consequence, counterevidence and the smallest correction. Use [simplification](simplification.md) for unnecessary complexity and `architect` only when a consequential structural question remains unresolved. This assessment does not authorize implementation or certify the whole system.
