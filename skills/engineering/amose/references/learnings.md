# Maintain `.learnings`

Use one optional root `.learnings` file only for **stable, non-obvious project knowledge that future work is likely to encounter again and must apply correctly**. The default is no entry: ordinary implementation rationale, one-off discoveries, task-specific findings, and useful historical context remain in the plan/spec/PR/history.

An entry belongs only when all apply:

- it is evidenced by a confirmed decision, current code/test/configuration/runtime result, ADR, or established repository practice;
- it is stable beyond the current initiative/candidate rather than temporary state or one delivery choice;
- future implementation, review, debugging, operation, or design is likely to encounter the same condition again;
- losing the knowledge creates a credible risk of a consequential wrong action, not merely rediscovery cost; and
- the knowledge is not already represented accurately by a stronger maintained source such as domain context, architecture, policy, configuration, code, or tests.

It may contain recurring rules, patterns, conventions, constraints, architectural nuances, operational knowledge, and gotchas that pass this gate. Keep canonical domain terms, definitions, semantic relationships, and context boundaries in the project's existing domain-language record or applicable `CONTEXT.md`; do not duplicate them here.

Preserve an existing human-readable format. Create the file lazily only when a qualifying entry exists and creation is authorized. With no existing format, use lightweight Markdown and include only sections with content.

`.learnings` cannot serve as its own sole proof. When no independent current evidence supports an entry, remove it or mark it unverified only when retaining that uncertainty itself prevents a consequential mistake.

Keep hypotheses, temporary task state, session history, speculative preferences, obvious code facts, routine implementation choices, secrets, credentials, and personal data out. Require user or confirmed-decision authority before promoting observed behavior into a business rule, project boundary, or architecture decision.

## Calibration

Good `.learnings` entry:

```text
Provider callbacks can arrive out of order. Reconciliation must compare the provider event sequence/version before applying a state transition. Evidence: callback integration tests and production incident record <id>.
```

Why it belongs: it is stable, non-obvious, independently evidenced, likely to recur, and getting it wrong would produce incorrect state transitions.

Bad `.learnings` entry:

```text
This refactor originally used an adapter but we removed it because the direct call was simpler.
```

Why it does not belong: it is useful initiative rationale/history, but future work does not need a durable governing rule; keep it in the PR/spec/history.

Bad `.learnings` entry:

```text
Use Spring Boot 3 because we like it.
```

Why it does not belong: it is a preference without evidence, consequence, or durable project rule. A qualifying architecture decision belongs with its owning architecture/decision evidence.

Good `CONTEXT.md`, not `.learnings`:

```text
Settlement: the final financial transfer after a charge is captured.
```

Why: this is canonical domain meaning rather than an implementation/operational nuance.

Good task/plan note, not `.learnings`:

```text
Retry migration test after staging credentials are restored.
```

Why: this is temporary work state.

Keep the file current rather than append-only. Re-read it immediately before writing, make the smallest semantic edit, merge duplicates, replace stale entries, and retain a short supersession or `avoid` note only when it prevents likely recurrence. Remove obsolete detail. On concurrent or conflicting edits, stop for semantic reconciliation; never overwrite or blindly append.

Compact relevant sections when repetition or stale material impairs use. Do not impose an arbitrary size limit. Consumers may read only relevant sections; passive reading does not require invoking `amose`.
