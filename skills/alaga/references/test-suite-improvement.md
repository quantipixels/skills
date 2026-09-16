# Test-suite improvement

Use when an accepted coding outcome is to make an existing test suite more effective, stable or economical. Alága owns the test changes and their verification. Use `atunwo` when independent judgment about proof retention or adequacy is materially useful, and `irinse` for non-obvious measurement or tool execution. Neither tool output nor review transfers implementation authority.

## Establish the proof baseline

Pin the candidate or revision, suite boundary, governing behaviors and current proof owners. Proof may live in unit, contract, integration, persistence, concurrency, migration, end-to-end or operational checks, as well as compiler, schema, static or runtime guarantees. Identify the realistic failures each material owner can reject before consolidating or removing it.

Execute the scoped existing tests and record the command, environment, actual selection and result. A successful process with no relevant tests is not a baseline. Measure only costs that affect the requested outcome, such as wall time, setup work, external resources or repeated execution, and distinguish observed flakes from suspicions. Cache state, concurrency and shared fixtures can change both cost and reliability; state material conditions rather than treating one run as universal.

Counts, coverage, mutation and complexity are leads with provenance, never quality gates. A bounded improvement requires no campaign or new tool by default.

## Improve without losing obligations

Trace expensive, flaky, duplicated, over-broad, vacuous or obsolete checks to the behavior they claim to protect. Fix the product, fixture, isolation or assertion mechanism that causes a confirmed failure; do not hide a real defect by weakening, skipping or indefinitely retrying its check.

Consolidate or remove a test only when its obligation is obsolete or a retained proof owner subsumes its material failure signal. Preserve public behavior, security/integrity, persistence/concurrency/recovery, migration, external adapter, composition, accessibility/interaction and recurrent-regression proof without a stronger complete owner. Similar assertions do not establish proof equivalence.

When retention is uncertain, use a targeted realistic rejection check: demonstrate that the proposed retained proof fails for a controlled defect, invalid value, dropped effect or historically credible regression at the relevant boundary. Use an exact bounded mutation only when it materially resolves the question. Restore temporary changes and distinguish executed rejection evidence from source inference.

Keep the smallest coherent suite shape that still owns the required behaviors. Reuse project-native runners and conventions. A dependency, global configuration change or broad test rewrite requires its own demonstrated need and accepted scope.

## Verify and return

Run the affected suite after the change and confirm the intended tests actually executed. Recheck the changed cost or flake claim under comparable conditions when it is part of acceptance, and exercise targeted rejection evidence where proof ownership changed materially. Do not turn a bounded improvement into a mandatory full-suite campaign.

Report the boundary, changes, retained proof owners, comparable baseline/final evidence, targeted rejection evidence and limits. A lower count or higher coverage alone is not success.
