# Test quality and suite improvement

Use the behavioral-test principles when designing or judging tests. Apply the suite-improvement procedure below only when an accepted outcome changes an existing suite's effectiveness, stability or cost. Alága owns edits and executed proof; [atunwo](../../commands/atunwo.md) owns independent judgment. Neither measurements nor review transfer implementation authority.

## Behavioral-test principles

Test observable contracts through the smallest faithful stable interface. Prefer an existing seam shared with real callers; do not expose internals merely to make an assertion easy. An internal invariant can merit focused proof, but assertions about private call order or implementation shape need a contractual reason. A refactor preserving behavior should normally preserve these tests.

Choose expected results independently of the implementation: a confirmed acceptance example, worked calculation, authoritative fixture or independent oracle. Repeating the same algorithm on both sides of an assertion can preserve the same defect. Name the realistic wrong result the assertion would reject; test count, snapshots and green status alone do not establish signal.

Use real owned collaborators when practical. Substitute external effects, nondeterminism or costly dependencies at a justified seam, and preserve the relevant adapter contract. Mock choreography proves the expectation configured in the mock, not necessarily the assembled behavior. Prefer a real local substitute when it faithfully exercises the disputed contract; supplement with integration evidence where it cannot.

During Red → Green delivery, let one completed slice inform the next test. After the working change, review whether tests still describe the accepted behavior and whether a proposed refactor preserves their evidence. A review finding should identify the weak oracle or coupled assertion and consequence, not demand blanket rewrites or a universal test style.

These principles adapt Matt Pocock's [TDD test and mocking guidance](https://github.com/mattpocock/skills/tree/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/tdd) while retaining Alárinà's contextual proof and authority boundaries.

## Improve an existing suite

## Establish the proof baseline

Pin the candidate or revision, suite boundary, governing behaviors and current proof owners. Proof may live in unit, contract, integration, persistence, concurrency, migration, end-to-end or operational checks, as well as compiler, schema, static or runtime guarantees. Identify the realistic failures each material owner can reject before consolidating or removing it.

Execute the scoped existing tests and record the command, environment, actual selection and result. A successful process with no relevant tests is not a baseline. Measure only costs that affect the requested outcome, such as wall time, setup work, external resources or repeated execution, and distinguish observed flakes from suspicions. Cache state, concurrency and shared fixtures can change both cost and reliability; state material conditions rather than treating one run as universal.

Use test count, line or branch coverage and complexity scores as leads with their provenance and limits. None is a quality gate. Do not require a repository-wide sweep or new tool configuration to improve a bounded suite.

## Improve without losing obligations

Trace expensive, flaky, duplicated, over-broad, vacuous or obsolete checks to the behavior they claim to protect. Fix the product, fixture, isolation or assertion mechanism that causes a confirmed failure; do not hide a real defect by weakening, skipping or indefinitely retrying its check.

Consolidate or remove a test only when its obligation is obsolete or a retained proof owner covers that obligation at least as strongly. Preserve valuable proof of public behavior, security, money or data integrity, persistence, transactions, locking, idempotency, concurrency, cancellation, recovery, migration, external adapters, startup composition, accessibility, interaction and recurrent regressions unless a stronger complete owner replaces it. Faster local checks can supplement a realistic boundary, but resemblance to its assertions does not establish equivalent proof.

When retention is uncertain, use a targeted realistic rejection check: demonstrate that the proposed retained proof fails for a controlled defect, invalid value, dropped effect or historically credible regression at the relevant boundary. Restore temporary changes and distinguish executed rejection evidence from source inference.

Keep the smallest coherent suite shape that still owns the required behaviors. Reuse project-native runners and conventions. A dependency, global configuration change or broad test rewrite requires its own demonstrated need and accepted scope.

## Verify and return

Run the affected suite after the change and confirm the intended tests actually executed. Recheck the changed cost or flake claim under comparable conditions when it is part of acceptance, and exercise targeted rejection evidence where proof ownership changed materially. Do not turn a bounded improvement into a mandatory full-suite campaign.

Report the suite boundary and candidate, changes, retained proof owners, executed baseline and final evidence, observed cost or stability difference, rejection evidence, and unproved or environment-limited obligations. A lower test count or higher coverage percentage alone is not a successful result.
