# Test-first implementation

Work in vertical behavior slices. Complete one slice before starting the next: write the smallest controlling test set, observe the expected behavior failure, make it pass with the smallest implementation, then improve production code without changing behavior.

TDD proof is construction evidence. It is not automatically the final retained test portfolio.

## 1. Set behavior, seam, and provisional proof owner

Read repository instructions and confirmed domain/architecture/decision/project knowledge. Derive required behavior, applicable success/negative/boundary/recovery/interaction cases, a stable behavior-bearing seam, and independent expected values.

Name the material invariant each new test is meant to protect and the likely cheapest durable proof owner. Return a material unresolved seam/decision to Alága before implementation.

Avoid:

- **Implementation coupling** — assert caller-visible behavior, not private structure, incidental collaborator calls, or unstable steps.
- **Tautological expectations** — derive expected values from a specification/worked example/known literal/independent source, never production logic.
- **Horizontal slicing** — finish one behavior slice before writing tests for later slices.

When the slice needs doubles, read `tdd-mocking.md`.

## 2. Prove red

Write/run the smallest test set controlling the slice. Confirm it fails because required behavior is missing/wrong. Fix compilation, fixture, environment, and unrelated failures before production code. An environment failure is not RED.

## 3. Make the slice green

Write only enough production code for the controlling behavior. Do not speculate about later slices. Run focused and affected proof.

## 4. Refactor production code

Improve names, state representation, ownership, structure, duplication, and implementation depth while preserving behavior. Put durable non-obvious rationale/policy/invariants at the narrowest owner. Tests do not replace required API/domain/operational/configuration documentation.

Treat smoke tests, probes, one-off harnesses, characterization scaffolding, and very narrow red/green tests as development evidence unless they independently protect a durable contract at a stable seam.

## 5. Hand proof to compaction

After the candidate is green/stable, do **not** automatically retain every test created during the slices. Alága applies `proof-compaction.md` across the complete candidate before final review.

Preserve unrelated behavior and current focused proof until compaction is complete. Broader proof runs at required gates or after candidate stabilization, and any proof invalidated by later changes is rerun.

Do not treat green TDD proof as evidence of review/publication or work that did not occur.
