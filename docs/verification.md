# Verification boundaries

## Package checks

Keep tests beside the shipped mechanics they protect: package discovery and resource integrity, installer ownership and interruption recovery, exact publication, parsers, and delivered browser controls. Prefer a representative rejection case or real regression over duplicate fixtures, configuration snapshots, and broad input permutations. CI owns the concrete commands and supported platform checks.

Before deleting a test, identify the failure it detects and any remaining proof that covers it. Fewer test functions alone do not establish a useful reduction. Do not weaken production validation or make a failed check advisory to obtain a smaller suite.

## Model evaluations

Use [Kọ Skill's behavior-check contract](../skills/ko-skill/SKILL.md#check-behavior) for evaluating a changed skill. The separate internal eval repository is the intended home for task corpora, rubrics, harnesses, and model-comparison runs; it is not yet provisioned by this change. Do not mirror that corpus here or make public package checks depend on it.

Keep task-local evidence in the PR until the internal destination is available. Record exact skill and eval revisions when available, host/model settings, observed results, and limitations. Keep evaluator expectations out of the tested skill's instructions. An unavailable evaluation remains `NOT_RUN`, not a package failure or a verified behavioral result.

[Compatibility](compatibility.md) distinguishes mechanical, structural, and authenticated-runtime claims. A green package check does not establish better model behavior, and an eval cannot replace safety tests for executable code.
