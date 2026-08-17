---
name: unknot
description: Audit an entire codebase for material simplifications in data structures, state, control flow, algorithms, and ownership. Use for a read-only repository-wide review that requires explicit subsystem coverage, independently verified findings, and dependency-aware priorities; exclude bounded change review, defect review, implementation, and architecture planning.
---

# Unknot

Complete one read-only simplification audit of the current repository. Do not edit repository files, run tests, implement recommendations, change Git state, or use provider writes. Read-only inspection commands and host-provided read-only subagents are allowed.

## 1. Establish the coverage contract

Record the repository identity, current revision, worktree baseline, and relevant repository instructions. Inventory the repository from tracked files, entry points, manifests, build configuration, tests, and generated boundaries. Separate every identifiable subsystem that has distinct behavior or ownership; do not use a broad catch-all row as proof of coverage.

Include frontend, backend, shared infrastructure, platform bridges, generated-contract ownership, and test or tooling infrastructure when present and material. Exclude vendored or generated implementation only with an explicit owner and reason.

Give each subsystem a stable ID and record:

- descriptive name and exact, non-overlapping ownership boundary;
- key implementation files;
- public interfaces, major call sites, and relevant tests;
- status: `queued`, `in review`, `recommend`, `skip`, or `not reviewed`.

Use `not reviewed` only when a bounded trial, interruption, or external blocker stops coverage before substantive inspection. State the reason and return the audit as `PARTIAL`. A row marked `not reviewed` cannot satisfy the complete-audit contract.

Maintain one canonical audit record containing the inventory, accepted opportunities, explicit skips, cross-cutting patterns, duplicates and superseded findings, final priorities and dependencies, and a chronological audit log. Keep any persistent scratch file outside the repository in a host-approved temporary location. Treat the inventory as the coverage contract and add a new row when later evidence reveals an omitted boundary.

## 2. Review every subsystem

When the host provides subagents, use fresh read-only agents with one distinct subsystem each. Keep concurrency within the number of results that the coordinator can actively reconcile. Use one consolidated wait, let productive reviews finish, and harvest and close completed workers before opening another bounded batch. The coordinator retains inventory ownership, finding acceptance, prioritization, and the final result.

Give each reviewer the repository identity, exact subsystem boundary, key files, and this brief:

> Review this subsystem for at most two materially useful simplifications in its data structures, state representation, control flow, algorithms, or ownership. Inspect implementation, public interfaces, major call sites, and tests. Stay inside the assigned boundary; report cross-subsystem evidence without expanding scope. Prefer clear local code and return `skip` when no opportunity meets the threshold.

Look for invalid combinations caused by booleans or nullable fields that need a state machine or discriminated union; repeated object-shape assumptions that need one shared typed model; duplicated branching that a small map, registry, reducer, or command model can remove; unclear behavior ownership; repeated scans or transformations; unsuitable collections or indexes; and lifecycle, concurrency, or async state that permits stale or contradictory values.

Accept a recommendation only when the evidence shows a concrete reduction in invalid state, duplicated policy, repeated material work, coordinated change cost, or unclear ownership. Reject stylistic consistency, hypothetical extensibility, minor line-count reduction, speculative abstraction, or a change that only moves branching behind a new type.

For each recommendation, require:

1. verdict: `recommend` or `skip`;
2. exact file and line evidence;
3. current complexity or permitted invalid states;
4. proposed representation and why it is simpler;
5. smallest credible scope, affected files, and interfaces;
6. regression risks and migration concerns;
7. existing proof and additional validation required;
8. confidence: `high`, `medium`, or `low`.

A subsystem-level `skip` must state the inspected boundary and why no candidate met the materiality threshold.

## 3. Verify and reconcile

Independently inspect every submitted finding against the current repository before accepting it. Confirm its lines, interfaces, callers, tests, semantics, and ownership. Reject, narrow, or demote findings that are vague, duplicate another mechanism, misunderstand intentional behavior, cross their assigned boundary without evidence, or relocate complexity.

Deduplicate by underlying mechanism. Assign each accepted finding to one authoritative subsystem; record aliases as duplicates or superseded findings. Record a recommendation or explicit skip for every inventory row, then continue bounded review batches until none remain `queued` or `in review`.

## 4. Audit the audit

After subsystem review is complete, use fresh independent passes when host subagents are available; otherwise perform distinct coordinator passes. Check:

- repository coverage and missing subsystem boundaries;
- duplicate findings and ownership overlap;
- materiality and over-abstraction;
- completeness of every required inventory and finding field;
- priority order and dependency consistency.

If the coverage pass finds an omission, add a separate subsystem row and review it. Do not broaden a completed boundary to conceal the gap.

Rank accepted recommendations by concrete impact, confidence, implementation effort, blast radius, prerequisites, and enabling value. Identify the smallest high-value first implementation slices without implementing them.

## 5. Report and close

Return the canonical audit record with:

1. repository and unchanged-worktree evidence;
2. the completed subsystem inventory;
3. accepted recommendations in priority order with every required field;
4. subsystem skips;
5. cross-cutting patterns, duplicates, and superseded findings;
6. dependencies and best first slices;
7. audit-the-audit results;
8. audit log and residual limitations.

Compare the final worktree state with the recorded baseline. Do not claim that the repository remained unchanged when the evidence differs or concurrent changes prevent attribution.

The audit is complete only when every identifiable subsystem has `recommend` or `skip`, no row remains `not reviewed`, every accepted finding has complete evidence, scope, risk, validation, and confidence, weak or duplicate abstractions are removed, priorities and dependencies are consistent, and unchanged-repository evidence is present.
