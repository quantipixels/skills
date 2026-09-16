# Diagnosis probe discipline

Use only when a bounded observation can discriminate live hypotheses. Choose the tightest available feedback loop: failing test, focused runtime probe, trace replay, browser journey, benchmark or direct observation. Prefer read-only evidence; do not mutate production merely to create a test.

Historical/source evidence is useful only when a predicted difference can support or falsify a mechanism. Correlation, temporal order, changed files, and nearby commits are not causation by themselves.

For a recurring or reopened bug, a targeted tracker/forge search may expose repair history absent from source. Compare any prior attempt's conditions with current code and return only the specific causal update.

Use native bisect only for a reliable safe reproducer and plausible good-to-bad history in permitted isolation. Pin environmental assumptions and clean up owned state; the first bad revision narrows cause but does not establish it.

## Cross-component boundary probe

Use when a failure crosses processes, services, queues, build stages or another boundary without one useful stack trace. Map only the boundaries on the path from trigger to symptom. In one reproduction, correlate safe entry and exit values, identifiers and relevant environmental metadata at each boundary, redacting secrets and sensitive payloads. Locate the first boundary whose output or downstream input diverges from the prediction, then investigate within that component. The first divergence narrows the failing layer; it is not automatically the complete cause.

## Order-dependent test reduction

When a test passes alone but fails in a suite, first pin runner options, order/seed, parallelism, environment and the exact failure. Passing alone does not confirm leaked state: timing, contention, seeds, external resources or other suite conditions may differ. Compare the test alone, its file or nearest group, and the failing suite sequence to distinguish those hypotheses.

If preceding tests are implicated, remove subsets of predecessors and rerun the target while preserving runner conditions and the same failure. Continue until further removal loses the discriminator or the investigation budget is spent. Interactions may require several predecessors, and halving does not guarantee a globally minimal sequence. Inspect the surviving sequence for shared process/module state, mocks, environment, files, database effects and constrained resources. Return a repeatable reduced sequence and the supported mechanism or remaining alternatives.

## Existing repair comparison

When an open pull request or exact commit plausibly repairs the symptom, pin its baseline and patched revisions and compare the artifact before authoring a competing change. Use the same discriminating path, inputs, dependencies, configuration, data basis and permitted environment for both; reset mutable state between runs. Establish that the baseline exhibits the broken state, then check on the patched candidate both that the broken state is absent and that the expected behavior is present. If either half cannot be observed under comparable conditions, return `inconclusive`; if both exhibit the symptom, return `insufficient fix`; otherwise report the bounded before/after evidence.

For verify-only work, make no repair edits, competing patch or publication. Verification does not authorize correction.

Record the hypothesis, predicted discriminator, observation and causal update, adding conditions or coverage limits when material.

A probe is useful only when it can change the causal model. After a reduced reproduction guides a repair, replay the original scenario whenever reduction removed integration conditions. Tag and revert disposable probes; reporting shape does not substitute for causal evidence.
