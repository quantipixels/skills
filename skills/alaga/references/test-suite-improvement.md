# Test-suite improvement

Use when an accepted coding outcome is to make an existing test suite more effective, stable or economical. Alága owns the test changes and their verification. Use `atunwo` when independent judgment about proof retention or adequacy is materially useful, and `irinse` for non-obvious measurement or tool execution. Neither tool output nor review transfers implementation authority.

## Establish the proof baseline

Pin the candidate or revision, suite boundary, governing behaviors and current proof owners. Proof may live in unit, contract, integration, persistence, concurrency, migration, end-to-end or operational checks, as well as compiler, schema, static or runtime guarantees. Identify the realistic failures each material owner can reject before consolidating or removing it.

Execute the scoped existing tests and record the command, environment, actual selection and result. A successful process with no relevant tests is not a baseline. Measure only costs that affect the requested outcome, such as wall time, setup work, external resources or repeated execution, and distinguish observed flakes from suspicions. Cache state, concurrency and shared fixtures can change both cost and reliability; state material conditions rather than treating one run as universal.

Use test count, line or branch coverage, mutation results and complexity scores as leads with their provenance and limits. None is a quality gate. Do not require a mutation campaign, CRAP score, repository-wide sweep or new tool configuration to improve a bounded suite.

## Improve without losing obligations

Trace expensive, flaky, duplicated, over-broad, vacuous or obsolete checks to the behavior they claim to protect. Fix the product, fixture, isolation or assertion mechanism that causes a confirmed failure; do not hide a real defect by weakening, skipping or indefinitely retrying its check.

Consolidate or remove a test only when its obligation is obsolete or a retained proof owner covers that obligation at least as strongly. Preserve valuable proof of public behavior, security, money or data integrity, persistence, transactions, locking, idempotency, concurrency, cancellation, recovery, migration, external adapters, startup composition, accessibility, interaction and recurrent regressions unless a stronger complete owner replaces it. Faster local checks can supplement a realistic boundary, but resemblance to its assertions does not establish equivalent proof.

When retention is uncertain, use a targeted realistic rejection check: demonstrate that the proposed retained proof fails for a controlled defect, invalid value, dropped effect or historically credible regression at the relevant boundary. Use an exact bounded mutation only when it materially resolves the question. Restore temporary changes and distinguish executed rejection evidence from source inference.

Keep the smallest coherent suite shape that still owns the required behaviors. Reuse project-native runners and conventions. A dependency, global configuration change or broad test rewrite requires its own demonstrated need and accepted scope.

## Verify and return

Run the affected suite after the change and confirm the intended tests actually executed. Recheck the changed cost or flake claim under comparable conditions when it is part of acceptance, and exercise targeted rejection evidence where proof ownership changed materially. Do not turn a bounded improvement into a mandatory full-suite campaign.

Report the suite boundary and candidate, changes, retained proof owners, executed baseline and final evidence, observed cost or stability difference, rejection evidence, and unproved or environment-limited obligations. A lower test count or higher coverage percentage alone is not a successful result.
