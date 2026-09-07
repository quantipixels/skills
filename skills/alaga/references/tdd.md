# Test-first implementation

Use test-first work only when the user requests it or a material behavior change has a stable behavior-bearing seam, an expectation/oracle independent of production logic, and a failing test that can materially control implementation. Proof is always required; a new test is not.

## Test admission

Before writing a persistent test, establish:

- **material contract** — caller/user-visible behavior or an invariant worth protecting;
- **stable seam** — behavior can be observed without coupling to private choreography;
- **independent oracle** — correct expectations come from a specification, worked example, known literal, external standard, or other source independent of production logic;
- **falsifiability** — a plausible wrong implementation would fail the test for the contract violation rather than an incidental implementation change; and
- **coverage gap** — stronger existing proof does not already protect the same contract sufficiently.

If the first four do not hold, do not manufacture a test. Return to `alaga` and use the smallest sufficient alternative proof.

## Slice

Work in vertical behavior slices; complete one slice before starting the next.

1. **Establish behavior and seam.** Derive the caller-visible behavior, material success/failure/boundary/recovery cases, nearest stable behavior-bearing seam, and independent expected values. When the external module/interface/seam shape itself is a consequential technical-structure question, use `architect` rather than designing production architecture inside this test-first path. Otherwise return a material unresolved local seam/project-boundary choice to `alaga` before implementation.
2. **Prove red.** Write and run the smallest controlling test set. Confirm it fails because the required behavior is missing or wrong; compilation, fixture, environment, mock setup, or unrelated failures do not establish the intended red state.
3. **Make it green.** Implement only enough production behavior to satisfy the slice. Run the focused test set and affected proof. Begin another slice only when another material behavior remains.

Structural refactoring/simplification after the behavior is established belongs to the normal candidate review/convergence flow, where the whole change and test portfolio can be judged together. Do not create a perpetual red-green-refactor expansion loop.

## Guardrails

- **Test behavior, not choreography.** Avoid private structure, unstable collaborator calls, incidental steps, and non-contract side channels unless they are themselves the contract. If durable behavior can only be tested by widening a production interface to expose internals, challenge the proof seam or use `architect` when module shape is materially wrong; do not create public production surface solely for the test.
- **Reject tautologies.** Never compute expected values with production logic, mirror the same algorithm in the assertion, assert configured mocks merely return what they were told, or test a constant against itself. A test must be able to disagree independently with the implementation.
- **Prefer vertical slices.** Do not build a horizontal test layer for later behavior before the current slice is green.
- **Use doubles only at useful seams.** Prefer real fast deterministic collaborators. Use a test double when a stable external or nondeterministic boundary must be controlled, or when a narrower unit test has clear value against a stable contract. Do not create a production interface/factory/dependency-injection layer solely to make mocking convenient unless that layer also owns a real production boundary.
- **Reuse proof surfaces.** Extend the nearest existing behavior/proof owner before adding parallel test files, fixtures, harnesses, or infrastructure. New test infrastructure is a scope-expansion event and needs independent justification.
- **Do not preserve construction history by default.** Smoke tests, probes, one-off harnesses, characterization scaffolding, and very narrow red/green tests are development evidence unless they uniquely protect a durable invariant at a stable seam. Final proof/test-portfolio simplification belongs to `pare` review and the normal review flow.
- **Keep proof and documentation honest.** Green tests do not prove acceptance, architecture quality, publication, or behavior they cannot discriminate. Tests do not replace required API, domain, operational, or configuration documentation.

Preserve unrelated behavior. Keep focused proof current, run broader project-required proof at the appropriate gate or after the candidate stabilizes, and report applicable checks that could not run or pass with their exact limitation.
