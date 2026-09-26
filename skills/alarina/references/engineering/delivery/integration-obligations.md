# Integrating with an existing system

Use only concerns that can change this implementation or proof. Resolve unknowns from source, effective configuration, history or a discriminating probe; search absence does not prove no consumer exists.

## Follow the affected behavior

Trace changed contracts through relevant producers, consumers and alternate entry points, including jobs, events, administrative paths and generated clients where present. Locate authoritative inputs for generated code. Check registrations, schemas, mappings and configuration that connect the code; compilation can miss consumers outside the build. Distinguish source, wire and semantic compatibility. Account for each material consumer as updated, compatible or explicitly outside the accepted scope, with any remaining consequence visible.

Use comparable implementations and governing decisions to recover the contract rather than copying accidental syntax or abstracting superficial similarity.

## Verify the mechanism being relied on

Identify the decisive facts on which the change's safety depends and the evidence capable of disproving them. Concentrate investigation there rather than expanding a speculative risk list. For example, removing an API may depend on every supported consumer having migrated; compiling the producer alone cannot establish that. Reuse sufficient current proof and carry each unresolved controlling claim into the handoff.

For framework-managed transactions, validation, authorization, retries, serialization or callbacks, confirm the actual version, configuration, registration and invocation path. An annotation or API name does not establish that interception or enforcement runs. Inspect the effective boundary and use a focused integration probe when source/configuration cannot settle a consequential uncertainty. Preserve existing authorization and tenant checks across new entry points.

Apply design by contract and complete mediation: locate enforcement of relied-on preconditions across every relevant entry point. A validating name is not proof.

When enforcement is the disputed behavior, drive the framework-managed entry point with a valid control and an input that must be rejected or rolled back. Inspect persisted and external effects, not only the response. A direct method call or a mocked interceptor leaves registration, proxying and lifecycle behavior unproved. Use the project’s actual runner and supported configuration; keep framework-specific commands in project guidance.

Verify least privilege across actor, tenant, resource and operation. Test cross-tenant and insufficient-authority attempts for disclosure and mutation; distinguish service authority from delegated user scope.

## Preserve operation during change

Establish the supported deployment and data contract before assuming empty storage, synchronized upgrades or a stopped system. Where applicable, account for existing records, old clients or writers, partial migration and restart. Separate reversible code rollback from irreversible data or external effects. Use [architect-design](../../../commands/architect-design.md) for a consequential unresolved design choice and [stateful proof](../verification/stateful-proof.md) when persistence or recovery needs distinguishing evidence.

Follow a material external effect through failure, timeout, retry and cancellation. Locate ownership of identity, atomicity and resource cleanup; do not assume failure means nothing happened. Reuse existing operational signals so the affected failure can be recognized and reconciled without disclosing sensitive data. Add instrumentation only for a concrete missing diagnostic, not a new observability stack.

Check composed failure semantics: retry amplification, exception translation that bypasses recovery, and fallbacks that repeat completed effects.

For changes to workload, buffering, concurrency or resource lifetime, use backpressure and bounded concurrency where downstream capacity requires them; define overload behavior. Measure relevant memory, connection and work amplification against the supported workload. Reuse existing limits; no blanket benchmark is required.

## Close the change

Reconcile implementation and executed proof with the discovered obligations. Check negative and preservation cases that could expose the changed failure mechanism, not every imaginable edge case. Report unresolved consumer, deployment or runtime claims plainly. Passing a narrow test is evidence for that boundary, not permission to claim the whole journey works.
