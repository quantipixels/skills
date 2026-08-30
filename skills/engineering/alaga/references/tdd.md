# Test-first implementation

Use test-first work only for a behavior change where a failing test can materially control implementation. Work in vertical behavior slices; complete one slice before starting the next.

## Slice

1. **Establish behavior and seam.** Derive the caller-visible behavior, material success/failure/boundary/recovery cases, the nearest stable behavior-bearing seam, and expected values from a source independent of production logic. Return a material unresolved seam or project-boundary choice to `alaga` before implementation.
2. **Prove red.** Write and run the smallest controlling test set. Confirm it fails because the required behavior is missing or wrong; compilation, fixture, environment, or unrelated failures do not establish the intended red state.
3. **Make it green.** Implement only enough production behavior to satisfy the slice. Run the focused test set and affected proof.
4. **Refactor without changing behavior.** Improve the implementation, rerun invalidated proof, then begin the next slice only if another behavior remains.

## Guardrails

- **Test behavior, not choreography.** Avoid private structure, unstable collaborator calls, incidental steps, and non-contract side channels unless they are themselves the contract.
- **Keep expectations independent.** Use a specification, worked example, known literal, or other independent source; never calculate the expected value with the production logic under test.
- **Prefer vertical slices.** Do not build a horizontal test layer for later behavior before the current slice is green.
- **Use doubles only at useful seams.** Prefer real fast deterministic collaborators. Use a test double when a stable external or nondeterministic boundary must be controlled, or when a narrower unit test has clear value against a stable contract. Framework-specific mocking technique belongs to current project/tool evidence; an active Experimental `akowe` may advise when it materially affects implementation quality.
- **Do not preserve construction history by default.** Smoke tests, probes, one-off harnesses, characterization scaffolding, and very narrow red/green tests are development evidence unless they uniquely protect a durable invariant at a stable seam. Final proof/test-portfolio simplification belongs to `pare` review and the normal review flow, not to a separate TDD compaction phase.
- **Keep proof and documentation honest.** Tests do not replace required API, domain, operational, or configuration documentation. Green TDD proof does not imply delivery acceptance, review, publication, or other work that did not occur.

Preserve unrelated behavior. Keep focused proof current, run broader project-required proof at the appropriate gate or after the candidate stabilizes, and report applicable checks that could not run or pass with their exact limitation.
