# Implementation cleanup

Use this workflow only after Parẹ́ selects `clean` for implementation, dependencies, configuration, or support artifacts. Preserve required behavior. Send behavior-changing work to Alaga and stateful parity analysis to Audit Refactor Behavior.

## 1. Fix the scope and proof floor

Record the repository identity, revision, worktree baseline, selected paths or artifact classes, exclusions, required behavior, proof floor, and mutation authority. Preserve unrelated work. Treat a supplied audit or review result as a hypothesis until it matches the current candidate.

Inventory the candidate implementation, entry points, callers, public interfaces, dynamic registration, reflection, feature flags, optional platforms, generated ownership, scripts, configuration, build integration, direct dependencies, tests, and known external consumers. Use exact-current Irinṣẹ evidence only to direct inspection.

## 2. Classify candidates

Classify every proposed removal as `retain`, `delete-safe`, or `blocked`. Use `delete-safe` only when current source and repository-native proof show that no required interface, behavior, policy, migration, compatibility, security, compliance, or operational owner remains.

For a dependency, verify that owned imports, runtime loading, platform variants, build integration, lockfile ownership, configuration, and support scripts no longer require it. Import search alone is insufficient.

Stop when dynamic reachability, generated ownership, external consumers, optional platforms, security or compliance impact, migration state, or required behavior is uncertain. Do not use human approval as proof that production code is unreachable.

## 3. Delete and prove

Apply the smallest coherent removals. Remove tests, fixtures, configuration, and dependencies only when their complete owned use is gone or the applicable test-cleanup policy authorizes removal. Do not change production behavior to make proof pass.

After each coherent batch, run the narrowest affected static and behavior proof. At completion, run the applicable repository-native format, lint, typecheck, build, surviving tests, integration checks, and final-diff inspection. A passing proof set supports only the behavior and platforms it exercises.

Compare the final worktree with the baseline. Check for accidental behavior changes, dangling imports, orphaned configuration, missing generated steps, stale documentation, and unrelated edits.

## 4. Report

Report the scope, baseline and final candidate, deleted and retained interfaces, removed implementation, dependencies, configuration, and support artifacts, proof commands and results, blocked candidates, ambient changes, and residual reachability, platform, external-consumer, and acceptance risks.
