# Integration at real boundaries

Load for persistence, framework behavior, authorization, multiple consumers, external effects, migrations or generated/build inputs. Apply only the relevant obligations.

## Atomic state and ownership

Trace every relevant writer, not only the new endpoint. A check followed by a write is unsafe when other writers can invalidate it. Prefer atomic conditional updates, uniqueness constraints or compatible locking/isolation at the actual owner. Check affected-row and conflict behavior. A transaction alone does not remove a race; establish the required isolation across real competing paths.

For repeatable operations establish identity, immutable intent, completion state and uncertain-result handling. Persist or derive stable idempotency keys as the provider contract permits. Reject conflicting intent for one identity. Inspect existing framework/provider retries before adding another layer.

An external effect and local commit are not atomic merely because one method wraps them. Reuse outbox, idempotency or reconciliation contracts where appropriate. Distinguish accepted work from completed effects, exceptions from process death and resumable interruption from permanent failure. Compensation cannot necessarily undo payments, messages or publication.

## Framework and trust boundaries

Exercise framework-managed entry points when advice, validation, injection, serialization or registration controls behavior. Direct calls and mocks can bypass the real mechanism; self-invocation can evade interception. Commit-time failure needs proof reaching commit rather than rollback in a surrounding test transaction.

Trace allowed and denied operations across applicable request, admin and job paths. Check tenant/resource ownership and policy at the protected effect. Denial must leave protected state, queues and external effects unchanged. Preserve legitimate privileged paths; blanket denial is not success. Types and cached decisions do not freeze permissions.

For native/FFI code inspect ownership, lifetime, aliasing, layout, unsafe preconditions and error/panic boundaries through actual callers. A safe wrapper must enforce its preconditions. Use relevant native sanitizers/checks when available and preserve their limits.

## Representations and consumers

Follow new values through mappings, registrations, storage/wire formats, defaults, unknown handling and affected consumers. Inspect a comparable value before choosing an annotation or converter. Semantic reuse is not copying a tolerant external parser into a strict internal boundary. Preserve accepted values and intentional compatibility differences.

Use representative populated migration data, sparse identities and exact relationship mapping. Define old/new readers and writers during rollout, idempotent re-entry and unsupported-version rejection. Candidate-only round trips are not mixed-version proof. Exercise declared rollback/forward recovery after new writes when required.

## Build and operational inputs

For dependency, code-generation or incremental-build changes check resolved inputs and actual consumers. Vary representative inputs and establish recomputation or valid new-input cache retrieval. Warm no-op builds can hide stale output; physical reruns are not always required when valid cached proof exists.

For buffering, retries, batching and concurrency examine relevant resource limits with representative workloads. Preserve cancellation, partial failure, latency and costs outside the measured process. Do not infer throughput from concurrency or call shifted costs an improvement. Restore owned probes and rerun only affected checks.
