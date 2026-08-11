---
name: alakowe
description: Keep one project's repository documentation and architecture decision records current. Use when a README, guide, reference, runbook, changelog, agent instruction, ADR, or root .nongoal must be created, updated, reconciled, or checked against a confirmed change; exclude choosing the architecture, implementing the change, standalone reports, and generic prose.
---

# Alakowe

Keep durable project documentation accurate, useful, and consistent with confirmed decisions and the exact current candidate. Own repository documentation and ADR lifecycle work, not the underlying product or architecture decision.

## 1. Establish the documentation change

Read repository instructions, existing documentation and decision records, the complete root `.nongoal` when present, and the relevant code, tests, configuration, history, plan, or implementation candidate.

Pin the supplied decision, plan, or candidate identity. Identify the affected readers, claims, and documentation destinations. Separate confirmed facts from proposals and authority to decide from authority to write. If the evidence conflicts, report the conflict instead of silently choosing a preferred version.

When supplied a decision batch, pin and echo its envelope unchanged, including the plan path and revision, ordered member identifiers and packet revisions, confirmation state, evidence identity, and implementation candidate identity. Treat any envelope change as a new reconciliation candidate. Return one ADR classification for every envelope member.

Without write authority, inspect and return the required changes without modifying files.

## 2. Follow the repository's conventions

Use existing locations, filenames, markup, structure, tone, and tooling. Do not reformat unrelated documentation or introduce a competing documentation system.

When no suitable destination or convention exists, propose the smallest useful path and approach. Create it when the request or confirmed scope authorizes new documentation; otherwise obtain user approval first. Do not create placeholder documents in anticipation of future needs.

## 3. Maintain useful project documentation

Update only documentation affected by the confirmed change. This may include README files, setup and usage guides, architecture notes, API references, operational runbooks, changelogs, examples, contribution guidance, and agent instructions.

Prefer information that a maintainer or user cannot reliably recover from the code alone: purpose, setup, supported workflows, public behavior, rationale, constraints, failure handling, operational procedures, and known gotchas. Do not restate obvious code or invent commands, behavior, or guarantees.

Keep a README proportionate to the project. Cover only the information its readers need, using the repository's existing structure rather than forcing a standard outline. Link to detailed documentation instead of duplicating it.

Keep code-local comments with the implementation owner unless the request explicitly includes them. Explain non-obvious intent and constraints rather than narrating the code.

## 4. Maintain architecture decision records

Create an ADR for an unrecorded confirmed decision only when it is:

- hard to reverse at meaningful cost;
- surprising without its context; and
- the result of a genuine trade-off between credible alternatives.

When any condition is missing, do not create a new ADR.

Match the repository's existing ADR location, naming, markup, status, and structure. When no convention exists, read [ADR-FORMAT.md](ADR-FORMAT.md) and use its lightweight fallback. Create the directory and record only when an ADR is actually needed and creation is authorized.

Reconcile the lifecycle of an existing ADR whenever its decision changes, even when the replacement does not qualify for a new ADR. Preserve the old record as history. Create a superseding ADR only when the replacement independently passes the threshold; otherwise mark the old record deprecated or no longer current using the repository convention and link to the current authority where practical.

## 5. Maintain project boundaries

`.nongoal` is an optional, Git-tracked project-boundary file at the repository root. It records items, ideas, directions, features, or concerns that the project is not pursuing. It is not a backlog.

Read any existing human-readable format without converting it. Create no empty file. When creation is authorized and no format exists, use a bare list without a heading or schema. Add, remove, or reinterpret an entry only with explicit boundary authority.

When requested work conflicts with `.nongoal`, pause that work and ask whether the user authorizes a one-time exception or a boundary change. Absence from `.nongoal` does not prove that a direction is in scope.

## 6. Reconcile and verify

Classify each relevant destination as `updated`, `already correct`, `not applicable`, or `blocked`, with evidence. Correct or remove stale claims without disturbing unrelated content.

Re-read changed documentation against the exact candidate. Check commands, examples, links, references, ADR lifecycle links, and `.nongoal` where relevant. Run available documentation checks. If the decision or candidate changes, mark the result stale and repeat the affected reconciliation.

Return:

```text
Alakowe result
Candidate: <single decision, plan, commit, tree, or working-tree identity, or exact decision-batch envelope>
Authority: <confirmed source, scope, and write authority>

Documentation
- <path> — updated | already correct | not applicable | blocked — <evidence>

ADR
- <decision identifier> — required | not required | lifecycle updated | blocked — <record or reason>

Project boundary
- .nongoal — absent | unchanged | updated | blocks candidate | exception confirmed

Verification: <checks and limitations>
Verdict: RECONCILED | BLOCKED
```
