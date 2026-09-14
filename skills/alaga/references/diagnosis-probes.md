# Diagnosis probe discipline

Use only when a bounded observation can discriminate explicit competing hypotheses. Prefer read-only evidence; do not mutate production merely to create a test.

Historical/source evidence is useful only when a predicted difference can support or falsify a mechanism. Correlation, temporal order, changed files, and nearby commits are not causation by themselves.

When the failure is safely and reliably executable and repository history plausibly contains a good→bad transition, Git's native bisect can be useful in an isolated environment permitted by the workspace contract. Pin the reproduction behavior and environmental assumptions, avoid real external effects/credentials, and clean up isolated state afterwards. Do not bisect nondeterministic failures, irreproducible historical environments, or probes with consequential external effects.

Record the hypothesis, predicted discriminator, observation and causal update, adding conditions or coverage limits when material.

A probe is not progress unless its result can change the causal model. Prefer the smallest safe observation that maximally separates remaining hypotheses; reporting shape does not substitute for discriminating causal evidence.
