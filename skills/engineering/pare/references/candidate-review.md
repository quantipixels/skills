# Candidate review

Perform one finite, read-only maintainability review. Do not change code, tests, documentation, Git state, provider state, or the review target. Keep functional correctness, security, runtime compatibility, behavioral proof, release readiness, and architecture planning outside this review.

## 1. Fix the candidate

Use the target supplied by the user. Otherwise, use the upstream merge-base diff and include working-tree changes when they belong to the requested candidate.

Pin the base and candidate to commits, trees, or a fixed working-tree digest. If more than one credible boundary exists, ask one focused question and stop.

Review the fixed candidate and the minimum surrounding context needed to verify a finding. Exclude unrelated, generated, and vendored code.

Apply repository instructions and adopted language, framework, architecture, and style standards before general engineering principles. Treat external quality models, design principles, metrics, and thresholds as review heuristics unless the repository adopts them as requirements.

Use an exact-current Irinṣẹ result only to prioritize bounded inspection. Treat metrics and static-analysis output as leads, not maintainability findings, and verify each reported maintenance cost in the candidate.

## 2. Review the candidate

Report only actionable maintainability findings. For each finding, give the file, line, summary, applicable repository rule or engineering principle, evidence, concrete maintenance cost, and smallest credible correction direction. A principle name or code smell is not evidence. Do not report style preferences.

### Responsibility and cohesion

Judge a function, class, module, or package by independent change drivers, not size.

- **Good:** a long orchestrator owns one workflow.
- **Bad:** one module owns independently changing billing and support policies, one policy change requires coordinated edits across unrelated locations, or a local special case bypasses its owner.

For a bad case, name the distinct change drivers and the smallest existing or credible seam that keeps each change local. Do not infer a violation from line count, method count, orchestration, or sequential steps alone.

### Coupling and information hiding

Flag a new dependency when it makes one module know another module's private representation, construction, ordering, or policy, or when it creates coordinated changes between otherwise independent concerns. Name the leaked decision and the narrower interface, data shape, or owner that can hide it. Do not seek zero coupling; require each dependency and interface to reduce more maintenance cost than it adds.

### Reuse

Flag new code that re-implements existing knowledge or policy. Search shared or utility modules and files adjacent to the change, and name the existing owner to reuse. Do not merge similar syntax when it serves independent change drivers; a shared abstraction must preserve cohesion instead of coupling unrelated concerns.

### Simplification

Build for proven need — YAGNI. Flag unnecessary complexity the candidate adds, including redundant or derivable state, copy-paste with slight variation, speculative generality, deep nesting, and dead code left behind. Name the simpler form that preserves behavior and the required variation.

Flag values that the candidate passes, stores, or exposes separately only when the owning source can derive them without material cost and the derived form preserves required timing, consistency, lifecycle, and ownership semantics.

### Vocabulary and context independence

Require changed code to make sense to a maintainer who did not see the issue, change review, or development conversation. Flag names and comments whose meaning depends on that history instead of the current domain, behavior, rationale, or constraint.

A stable current specification, architecture decision record, or issue can support the rationale, but it must not replace the minimum current rationale or constraint needed to understand the code.

Prefer one repository term for each concept and one meaning for each term. Flag divergence only when it causes ambiguity or translation cost across the changed code and its consumers. Treat a long compound name as a review clue, not a finding by itself. Recommend a shorter name only when repository context preserves its precise meaning.

When repository sources conflict or no term is adopted, report the ambiguity and translation cost without choosing a canonical term. Name Amọ̀ṣẹ́ as the model owner and state any material decision authority still needed.

Flag a compatibility path for an unshipped signature, data shape, or behavior only when repository history and release evidence prove that it was never released, and a complete search within the stated consumer scope finds no current dependency. State the consumer scope and any external-consumer limitation. Do not infer unshipped status from review discussion or development history alone.

### Efficiency

Flag material wasted work the candidate adds, including redundant computation or I/O, proven-independent operations that run sequentially, blocking work on startup or hot paths, and objects that retain substantially more state than they need. Name the cheaper alternative and the evidence that the cost matters. Do not claim a measured performance or cost improvement without a benchmark or production metric.

### Implementation depth

Check whether the change fixes the owning mechanism or adds a fragile local special case. Prefer a deeper correction only when it reduces repeated policy or future patches without expanding the required behavior.

Treat design patterns as tools, not compliance targets. Recommend a named pattern only when it describes the smallest established structure that resolves the evidenced maintenance cost. Require a real variation, repeated policy, or dependency seam. Do not recommend a pattern, abstraction, configuration option, or extension point only for possible future use.

### Testability and change safety

Review production and test code as maintainable code. Flag hidden dependencies, uncontrolled time or randomness, shared mutable state, oversized fixtures, brittle internal-call assertions, and duplicated test setup only when they make required behavior materially harder to isolate, understand, or verify. Name the observable seam or deterministic input that reduces that cost. Record missing behavioral proof or a correctness concern under `Needs defect review` instead of treating it as a maintainability finding.

### Comments and API documentation

Apply repository documentation rules. Do not require documentation for every declaration.

Require a documentation destination when the candidate changes a public contract, domain policy, operational or configuration procedure, or a non-obvious rationale, invariant, ordering rule, ownership rule, compatibility constraint, or security constraint. A destination can be a local code comment, API documentation, domain documentation, operational documentation, configuration reference, or example. Do not infer a destination from a changed declaration alone.

Report important knowledge that names, types, interfaces, and structure cannot express clearly. Check rationale, invariants, preconditions, side effects, ordering, concurrency, ownership, lifecycle, compatibility, failures, exceptions, and security constraints. Check a supplied documentation-destination record when one exists. When the record says `not applicable`, verify that the cited behavior and relevant repository documentation support that result.

Verify relevant comments, API documentation, domain and operational documentation, configuration references, and examples against the current implementation, callers, tests, links, symbol references, and examples. Report missing important knowledge, inadequate detail, stale or false claims, and harmful redundant comments. Treat tests as behavior proof, not as a substitute for required documentation.

When confirmed project knowledge or decision records are inconsistent with the current candidate or authority, report the drift and its maintenance cost without editing them. Keep their correction with the owning knowledge workflow and ordinary documentation corrections with the outcome owner that changed or verifies the behavior.

List a material behavior, contract, security, or proof concern under `Needs defect review` with its location, bounded scope, reason, evidence, and possible consequence. Treat it as a reference-only, out-of-scope hypothesis, not a maintainability finding or Code Review verdict.

## 3. Reconcile and report

Deduplicate findings and out-of-scope concerns by mechanism. Exclude unsupported concerns, concerns outside the candidate, style preferences, and ungrounded correctness hypotheses.

Verify the candidate identity again. Rebuild the review if it changed.

Return maintainability findings first. Then report `Needs defect review` concerns, the reviewed boundary, candidate identity, and residual limitations. Confirm when no focused maintainability finding remains.
