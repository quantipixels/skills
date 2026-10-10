# Evaluator preparation and independent acceptance

Keep this file and frozen probes separate from actor inputs. The actor receives the required behavior and constraints, not a hidden requirement or a preferred implementation. Each case below defines preparation obligations: it cannot yield runtime evidence until those obligations are met. Check the original's intended failure before the actor run and retain an independent probe that rejects a plausible inadequate repair. An unexpected environment failure invalidates the setup; it does not demonstrate the intended defect.

## Framework invocation

Prepare a small project using its actual supported framework and database, preferably the JVM stack needed by the user. Choose one demonstrated defect such as an invocation bypassing transaction advice or a missing validation registration; do not combine unrelated defects. Pin the normal public entry point, required failure response and durable-state contract. Confirm a passing direct test and a failing real-entry-point probe on the original.

Freeze probes that invoke the container-managed path, observe both successful and failing operations, and inspect committed state from a separate transaction/connection. For a commit-time constraint, ensure the test reaches commit rather than relying on test rollback. Acceptance requires nonzero executed framework tests and preserved unaffected behavior. Reject a repair that only changes the direct test or bypasses the container. Do not infer portability to untested databases or framework versions.

## Mixed-version compatibility

Supply independently executable old and candidate versions, a populated snapshot with representative legacy values, and a declared compatibility window and recovery direction. Specify which version combinations must work; incompatible combinations must have an explicit rejection contract. Keep old source/binaries protected. Existing SQLite migration screens remain useful but do not stand in for simultaneous application versions.

Freeze probes for old/new reads and writes before migration, during the supported overlap and after the transition. Include records produced by both writers, unknown/new enum or wire values where relevant, identity preservation and a second migration attempt. Exercise the declared rollback or forward-recovery path after new writes. Reject candidate-only round trips and fixes that silently drop old fields or reinterpret old values. Report each supported pair separately; a passing matrix does not prove compatibility with every historical client.

## Interruption and recovery

Extend the existing settlement semantics with an independently durable provider and a worker process. The provider's effect log must survive worker termination. Add evaluator-controlled barriers to identify the point after provider commit and before local completion; actor-controlled logging alone is not evidence that the boundary was reached. Freeze operation IDs, accepted amounts and provider idempotency semantics.

Terminate the worker at that barrier, reopen persistent state and retry through the public operation. Require one accepted provider effect, the same operation identity and amount, and a correct local completion record. Also probe interruption before the effect, retry after success and conflicting identity reuse. Reject an in-memory deduplication repair. Keep abrupt process death distinct from injected exceptions; this screen does not establish power-loss durability or concurrent linearizability.

## Authorization across entry points

Supply the project's existing policy contract, two tenants, allowed/denied principals, a legitimate privileged identity and the real request/admin/job entry points. State whether background jobs carry user authority or act under a service policy. Include an existing valid path so blanket denial cannot pass. Use synthetic data and local external-effect fixtures.

Freeze allowed, missing-permission and cross-tenant cases across the relevant entry points. Inspect durable records and the external-effect/queue log after denial, including attempts to submit another tenant's resource identifier. Require expected allowed work and preserved privileged behavior. Reject a repair that guards only the public controller or simply disables jobs. Report unsupported principals or entry points as unassessed, not secure.

## Measured resource cost

Supply a deterministic populated workload, actual invocation command, available instrumentation and an explicit acceptance budget justified by the task. Choose a dominant concern such as N+1 queries or bounded batch memory. Freeze dataset sizes, output contract, warm-up conditions and repetition count before comparison; use at least two sizes when a scaling claim matters. A budget is local to this case, not a library-wide quality gate.

Capture baseline and candidate with the same instruments and verify equivalent required outputs. Count real database calls or observe process resources as appropriate; explain whether the measurement includes child processes, database work and caches. Require the stated budget and inspect any shifted work or contention. Reject a repair that drops data, moves cost outside the measured interval or merely edits the benchmark. Retain variability and avoid a latency win claim when noise overwhelms the difference.

## Architecture alternatives

Supply one concrete consumer requirement, the current architecture and relevant history, one plausible library alternative already available or explicitly approved for a disposable spike, and bounded change/measurement constraints. Freeze criteria before viewing candidates: behavior, migration risk, operation and maintenance cost, and consumer/contributor usability. If installation is unavailable, provide a prepared environment or mark the executable alternative blocked; a documentation-only comparison remains a narrower result.

Use the same independent behavioral probes for working alternatives. Review migration/data consequences and whether an apparent code reduction merely hides custom glue, operational burden or an incompatible consumer contract. Include retaining the current design as a valid outcome. Have an independent reviewer distinguish observed results from estimates and evaluate whether decisive trade-offs justify the recommendation. This case yields a reasoned comparison, not an automatic architecture score or a claim about long-term maintenance proven by a short spike.

For component/policy guidance, prepare a concrete co-change, component-cycle or policy/detail problem plus a sound cohesive/framework-native control. Freeze the actual consumer burden and dependency edges; runtime callbacks alone are not a package cycle. Require a concrete consequence rather than principle-name matching, and preserve the sound design when no change earns its cost. Include a replaceable detail whose feasibility constraint must be investigated before deferral.

## Selective test-first development

Prepare separate bounded variants: a reproducible domain defect (the settlement fixture can supply the basic case); a security-configuration defect reachable through a real local HTTP boundary; a mechanical edit already covered by sufficient compilation/tests; and an explicit project test-first requirement. Freeze the accepted behavior and hidden rejection probes, not a preferred implementation. Do not use a file-type exemption for the configuration variant.

When TDD is selected, retain timestamped native commands/results proving nonzero Red before production repair, failure for the intended behavior or required interface, passing candidate behavior and useful refactoring within constraints. Setup/import failures, irrelevant assertions and post-hoc failures are not Red. The mechanical control may pass with existing proof and no added test. Apply the same contract and project rules in both comparison arms.

For consolidation, supply a truly subsumed example, a uniquely protective zero/negative edge, a purported replacement property generator that omits that edge, and an integration check that never exercises its rejection path. Require retention of the unique or complementary proof and permit removal only when the obligation is obsolete or a retained owner rejects its realistic failure at least as well. Inspect source and bounded rejection evidence rather than rewarding fewer tests. Do not add a per-test retention report or suite-wide review gate.
