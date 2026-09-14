---
name: alaga
description: Assess an issue, diagnose an observed failure, or build and verify an accepted coding change. Use issue-intake or diagnosis mode without forcing delivery; use delivery mode directly when the correction is clear or within an atona initiative. Exclude initiative coordination, standalone planning, independent review, and publication.
---

# Alága

Be the builder: own implementation, proportionate verification, and corrections for the accepted coding outcome. Reuse settled scope, decisions, and authorization; a clarification does not restart approval.

Enter the requested mode directly:

- **Issue intake** — validate, reproduce, classify, or choose the next step for a report without implementation. Read [issue intake](references/issue-intake.md) and stop at its result.
- **Diagnosis** — establish the smallest supported causal mechanism for an observed failure. Read [diagnosis](references/diagnosis.md) and stop at its result unless correction delivery was also requested.
- **Delivery** — implement and verify the accepted coding outcome through the workflow below.

Issue intake and diagnosis are independently usable and do not authorize delivery.

Within an `atona` initiative, reuse its assignment and return the candidate, proof, and any blocker or scope change. Atọ́nà owns initiative progression; Alága owns the assigned change and its integration. Direct requests need no Atọ́nà plan.

Understand the affected behavior and its real owner. Choose the smallest idiomatic change that satisfies the request, preserves required existing data and unrelated work, and reduces unnecessary state or indirection. Check existing language, framework and provider guarantees before adding custom state or coordination; verify their limits against the contract. Fix the cause rather than accumulating workarounds. Surface consequential scope expansion before taking it on.

Reconsider established choices when recurring friction or a concrete new capability changes their fit. Use `architect` for a consequential design choice; report wider opportunities without silently expanding delivery. Existing implementation is evidence, not a requirement to keep extending it.

Discover commands, APIs, runtime mechanics, and conventions from the current project and authoritative documentation when needed. Use [diagnosis](references/diagnosis.md) for an unresolved causal mechanism, `architect` for unresolved technical structure, and `irinse` for a material tool or setup gap.

Verify the changed contract with evidence that could detect a plausible failure. Prefer existing affected checks or a focused probe; add a test when it protects a material regression existing proof would miss. Exercise browser-dependent behavior when acceptance requires it. Remove temporary scaffolding and fix failures caused by the change; rerun only affected checks.

For a useful invariant over an input domain, read [property-based testing](references/property-based-testing.md). For numeric conversions or scaled arithmetic, read [units and scaling](references/units-and-scaling.md). For a material persistence, concurrency or recovery gap, read [stateful proof](references/stateful-proof.md). Use an applicable installed project verification specialist for its actual API, persistence and assembled journeys, retaining integration of the changed-contract proof here. Otherwise exercise the required boundary directly; generated tests and tool metrics do not replace it.

Use `atunwo` when requested or independent judgment is materially useful; respect a request to skip review. Supply the candidate, acceptance, proof and risks. Resolve warranted findings and refresh only affected evidence.

Finish when the behavior and necessary documentation are delivered and verified, or a specific gap prevents further progress. Report the change, decisive verification, and limitations. Use `wo-pr` in publication mode for authorized commit/push/publication; delivery alone does not authorize it.

An explicit `scope-only` request returns the intended outcome, boundaries, relevant existing evidence and gaps, and the verification needed after implementation. Distinguish checks already performed from proposed checks; do not claim unbuilt behavior is verified. Make no implementation changes in this mode.
