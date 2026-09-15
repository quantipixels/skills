# Diagnosis probe discipline

Use only when a bounded observation can discriminate explicit competing hypotheses. Prefer read-only evidence; do not mutate production merely to create a test.

Historical/source evidence is useful only when a predicted difference can support or falsify a mechanism. Correlation, temporal order, changed files, and nearby commits are not causation by themselves.

For a recurring, reopened or otherwise nontrivial bug, a targeted tracker and forge search can expose work absent from source history. When existing read access is available, query a few variants of the symptom, stable error text and affected area. Inspect an open matching repair before duplicating it; inspect a merged attempt and its discussion for the intended mechanism and conditions. A failed earlier approach constrains the present hypothesis only after comparing those conditions with the current code and environment. Return the links and the specific causal update; do not turn this probe into a global sweep or a ticket-writing task.

When the failure is safely and reliably executable and repository history plausibly contains a good→bad transition, Git's native bisect can be useful in an isolated environment permitted by the workspace contract. Pin the reproduction behavior and environmental assumptions, avoid real external effects/credentials, and clean up isolated state afterwards. Do not bisect nondeterministic failures, irreproducible historical environments, or probes with consequential external effects.

## Cross-component boundary probe

Use when a failure crosses processes, services, queues, build stages or another boundary without one useful stack trace. Map only the boundaries on the path from trigger to symptom. In one reproduction, correlate safe entry and exit values, identifiers and relevant environmental metadata at each boundary, redacting secrets and sensitive payloads. Locate the first boundary whose output or downstream input diverges from the prediction, then investigate within that component. The first divergence narrows the failing layer; it is not automatically the complete cause.

## Order-dependent test reduction

When a test passes alone but fails in a suite, first pin runner options, order/seed, parallelism, environment and the exact failure. Passing alone does not confirm leaked state: timing, contention, seeds, external resources or other suite conditions may differ. Compare the test alone, its file or nearest group, and the failing suite sequence to distinguish those hypotheses.

If preceding tests are implicated, remove subsets of predecessors and rerun the target while preserving runner conditions and the same failure. Continue until further removal loses the discriminator or the investigation budget is spent. Interactions may require several predecessors, and halving does not guarantee a globally minimal sequence. Inspect the surviving sequence for shared process/module state, mocks, environment, files, database effects and constrained resources. Return a repeatable reduced sequence and the supported mechanism or remaining alternatives.

## Existing repair comparison

When an open pull request or exact commit plausibly repairs the symptom, pin its baseline and patched revisions and compare the artifact before authoring a competing change. Use the same discriminating path, inputs, dependencies, configuration, data basis and permitted environment for both; reset mutable state between runs. Establish that the baseline exhibits the broken state, then check on the patched candidate both that the broken state is absent and that the expected behavior is present. If either half cannot be observed under comparable conditions, return `inconclusive`; if both exhibit the symptom, return `insufficient fix`; otherwise report the bounded before/after evidence.

For an explicit verify-only request, make no edits to the repair, no competing patch and no publication. Verification supplies evidence about the pinned artifact; it does not authorize correction. Use existing project isolation without overwriting unrelated work, and keep all runtime effects within the already authorized test boundary.

Record the hypothesis, predicted discriminator, observation and causal update, adding conditions or coverage limits when material.

A probe is not progress unless its result can change the causal model. Prefer the smallest safe observation that maximally separates remaining hypotheses; reporting shape does not substitute for discriminating causal evidence.
