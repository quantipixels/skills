# Failure heuristics for `wo-pr`

Use this checklist only after a complete snapshot identifies failed required work. Read the failed job logs before classifying and keep the result against the exact head SHA and provider job ID.

## Branch-related

Prefer branch-related when logs point to changed code or an affected contract: compile, type, lint, static analysis, unit, integration, snapshot, migration, packaging, or compatibility failure in the candidate path. Reproduce or obtain another direct proof when practical. Route the bounded correction to `alaga` with the current head, acceptance, and proof.

## Likely flaky

Prefer likely flaky only when evidence shows a transient runner, network, registry, service, test timing, or known nondeterministic failure and the candidate does not change the failing mechanism. Retry at most once for that exact head and job during the active run. A resumed run does not infer a fresh retry budget; diagnose before another retry. Never modify code to make an unrelated flake disappear.

## Infrastructure or provider

Classify runner provisioning, provider incidents, permission denial, exhausted quota, repository policy failure unrelated to the branch, unavailable dependency service, and persistent rate limits as infrastructure or provider blockers. Do not edit CI configuration, dependency pins, tests, or build scripts without direct candidate causality and separate implementation authority.

## Causally unresolved

Perform one bounded diagnosis attempt. If branch causality remains unclear, return the failed job, log evidence, candidate relation, attempted hypotheses, missing fact, and safest next action. Offer the explicit Experimental `root-cause` route when a causal investigation is the actual missing outcome. Do not spend a retry to avoid diagnosis.

## Review feedback

Act only on published, unresolved feedback against the current head. A provider-side resolution does not prove the issue is fixed. Send the claim to `se-triage`; do not recreate its classifications here. Reply or resolve only after the returned disposition and any required correction are verified against a refreshed head.
