# Integrating with an existing system

Use only the concerns that can change this implementation or its proof. Reuse the existing discovery and accepted architecture. Resolve unknowns from source, current configuration, relevant history or a discriminating probe; absence from a name search is not proof that an implementation or consumer does not exist.

## Follow the affected behavior

Trace changed contracts through relevant producers, consumers and alternate entry points, including jobs, events, administrative paths and generated clients where present. Locate authoritative inputs for generated code. Check registrations, schemas, mappings and configuration that connect the code; compilation can miss consumers outside the build. Distinguish source, wire and semantic compatibility. Account for each material consumer as updated, compatible or explicitly outside the accepted scope, with any remaining consequence visible.

Use comparable current implementations to recover the intended convention. If they disagree or a workaround controls the decision, inspect the relevant history or governing decision. Preserve an established contract rather than accidental syntax; do not manufacture a universal abstraction from superficially similar code.

## Verify the mechanism being relied on

For framework-managed transactions, validation, authorization, retries, serialization or callbacks, confirm the actual version, configuration, registration and invocation path. An annotation or API name does not establish that interception or enforcement runs. Inspect the effective boundary and use a focused integration probe when source/configuration cannot settle a consequential uncertainty. Preserve existing authorization and tenant checks across new entry points.

Apply design by contract: locate enforcement of relied-on preconditions and reuse established guarantees. A validating-sounding name is not proof; keep unsupported assumptions explicit.

When enforcement is the disputed behavior, drive the framework-managed entry point with a valid control and an input that must be rejected or rolled back. Inspect persisted and external effects, not only the response. A direct method call or a mocked interceptor leaves registration, proxying and lifecycle behavior unproved. Use the project’s actual runner and supported configuration; keep framework-specific commands in project guidance.

Verify least privilege and complete mediation across affected entry points: actor, tenant, resource and operation. Test cross-tenant or insufficient-authority attempts for disclosure and mutation. Distinguish a job’s service authority from delegated user scope.

## Preserve operation during change

Establish the supported deployment and data contract before assuming empty storage, synchronized upgrades or a stopped system. Where applicable, account for existing records, old clients or writers, partial migration and restart. Separate reversible code rollback from irreversible data or external effects. Use `architect` for a consequential unresolved design choice and [stateful proof](stateful-proof.md) when persistence or recovery needs distinguishing evidence.

Follow a material external effect through failure, timeout, retry and cancellation. Locate ownership of identity, atomicity and resource cleanup; do not assume failure means nothing happened. Reuse existing operational signals so the affected failure can be recognized and reconciled without disclosing sensitive data. Add instrumentation only for a concrete missing diagnostic, not a new observability stack.

Check composed failure semantics: retry amplification, exception translation that bypasses recovery, and fallbacks that repeat completed effects.

For changed volume, buffering, parallelism or resource lifetime, verify bounded resource use against the supported workload. Small functional fixtures can miss memory, connection or work amplification. Reuse an applicable limit or bounded measurement; no blanket benchmark is required.

## Close the change

Reconcile implementation and executed proof with the discovered obligations. Check negative and preservation cases that could expose the changed failure mechanism, not every imaginable edge case. Report unresolved consumer, deployment or runtime claims plainly. Passing a narrow test is evidence for that boundary, not permission to claim the whole journey works.
