# Failure heuristics for `wo-pr`

Use this checklist only after a snapshot identifies failed required work. Read the failed job logs before classifying.

## Branch-related

Prefer branch-related when logs point to changed code or an affected contract: compile, type, lint, static analysis, unit, integration, snapshot, migration, packaging, or compatibility failure in the candidate path. Reproduce or obtain another direct proof when practical. Use the smallest owning implementation workflow and rerun affected proof.

## Likely flaky

Prefer likely flaky when evidence shows a transient runner, network, registry, service, test timing, or known nondeterministic failure and the candidate does not change the failing mechanism. Retry only when the watcher recommends it and `retry-ci` authority exists. Never modify code to make unrelated flakes disappear.

## Infrastructure or provider

Classify runner provisioning, provider incident, permission denial, exhausted quota, repository policy failure unrelated to the branch, unavailable dependency service, and persistent rate limit as infrastructure or provider blockers. Do not edit CI configuration, dependency pins, tests, or build scripts without direct candidate causality and separate implementation authority.

## Ambiguous

Perform one bounded diagnosis attempt. If branch causality remains unclear, stop with the failed job, log evidence, candidate relation, attempted diagnosis, missing fact, and safest next action. Do not spend a retry to avoid making the classification.

## Review feedback

Act only on published, unresolved, actionable feedback. Check the exact current code and head; a provider-side resolution does not prove the issue is fixed. Do not reply as the human user. Do not resolve a thread involving unapproved participants. Record an item `handled` only after its required code and provider effects are verified.
