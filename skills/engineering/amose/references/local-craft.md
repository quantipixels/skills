# Repository-local craft knowledge

Use this destination only when the user/repository explicitly authorizes preserving a **confirmed, reusable, project-specific coding pattern** that should remain local instead of becoming a published cross-project rule.

Resolve one owner record through `akosile`:

```text
owner: amose
record_type: local-craft
subject: <stable project code-craft identity>
```

The record lives under repository-local untracked `.qp` and follows the normal owner-record contract. Global `~/.qp` storage remains deferred.

## Admission

Retain an item only when:

- evidence shows the pattern is real in this repository and useful beyond one edit;
- the user/repository has confirmed it or an exact-current accepted decision establishes it;
- it is not already a repository instruction, `.learnings` invariant, architecture constraint, formatter/linter/static rule, or published skill rule;
- it does not contain secrets, personal/private identifiers, prompt instructions, or untrusted copied prose;
- it states the trigger, preferred/forbidden shape, reason/failure mechanism, exception, evidence identity, and freshness boundary.

One unconfirmed task correction does **not** qualify.

## Calibration

Good local craft:

```text
Trigger: updating an Order aggregate.
Prefer: call aggregate methods that own state transitions.
Avoid: repositories or application services writing child entity state directly.
Why: aggregate invariants and emitted domain events are owned by the aggregate.
Material exception: read-model/projector code does not mutate aggregate state.
Evidence: current aggregate tests + architecture decision AD-12.
Freshness: revalidate if aggregate ownership changes.
```

Why it belongs: it is a confirmed repository-specific implementation pattern that changes future coding choices but is not a universal cross-project rule.

Bad local craft:

```text
Prefer tabs over spaces.
```

Why it does not belong: formatting belongs to repository instructions or deterministic formatter configuration.

Good `.learnings`, not local craft:

```text
Provider events can arrive out of order and must be version-checked before applying transitions.
```

Why: this is durable project behavior/operational knowledge rather than a preferred coding shape.

Good architecture constraint, not local craft:

```text
All payment-provider traffic crosses the PaymentProvider boundary.
```

Why: when that boundary is part of an accepted architecture contract, keep it with the architecture authority rather than duplicating it as craft.

## Record shape

```text
Local craft
Candidate: <repository identity>
Revision: <n>

<stable-id>
Trigger:
Prefer / Avoid:
Why:
Material exception:
Evidence:
Freshness:
State: current | superseded
```

## Consumption and precedence

A coding companion may consume the exact-current record read-only as project evidence. It never overrides system/developer/user/repository instructions, accepted task/Architecture Contract, safety/security/compatibility, or current primary-source facts.

Runtime consumers never mutate/promote the record automatically. A public cross-project contribution requires separate sanitization, evidence, user/repository authority, and `ko-skill` authoring. Do not copy private repository examples or identifiers into the public skill.
