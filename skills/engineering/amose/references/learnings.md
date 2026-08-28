# Maintain `.learnings`

Use one optional root `.learnings` file for durable, non-obvious knowledge that can change future implementation, review, debugging, operation, or design work. It may contain rules, patterns, conventions, constraints, architectural nuances, operational knowledge, and gotchas. Keep canonical domain terms, definitions, semantic relationships, and context boundaries in the project's existing domain-language record or the applicable `CONTEXT.md`; do not duplicate them here.

Preserve an existing human-readable format. Create the file lazily only when useful knowledge exists and creation is authorized. With no existing format, use lightweight Markdown and include only sections with content.

Require evidence from a confirmed decision, current code, test, configuration, runtime result, ADR, or established repository practice. `.learnings` cannot serve as its own sole proof. When no independent current evidence supports an entry, mark it unverified or remove it instead of perpetuating it.

Keep hypotheses, temporary task state, session history, speculative preferences, obvious code facts, secrets, credentials, and personal data out. Require user or confirmed-decision authority before promoting observed behavior into a business rule, project boundary, or architecture decision.

## Calibration

Good `.learnings` entry:

```text
Provider callbacks can arrive out of order. Reconciliation must compare the provider event sequence/version before applying a state transition. Evidence: callback integration tests and production incident record <id>.
```

Why it belongs: it is durable, non-obvious, operationally relevant, independently evidenced, and changes future implementation/review behavior.

Bad `.learnings` entry:

```text
Use Spring Boot 3 because we like it.
```

Why it does not belong: it is a preference without evidence, consequence, or durable project rule. A confirmed architecture choice belongs with its owning decision/architecture evidence.

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

Keep the file current rather than append-only. Re-read it immediately before writing, make the smallest semantic edit, merge duplicates, replace stale entries, and retain a short supersession or `avoid` note only when it prevents likely recurrence. Remove obsolete detail and use ADRs for consequential rationale. On concurrent or conflicting edits, stop for semantic reconciliation; never overwrite or blindly append.

Compact relevant sections when repetition or stale material impairs use. Do not impose an arbitrary size limit. Consumers may read only relevant sections; passive reading does not require invoking `amose`.
