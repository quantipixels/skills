---
name: alaga
description: Implement an accepted coding change or fix and verify the requested behavior. Use for delivery once the outcome is sufficiently clear; exclude standalone planning, review, and publication.
---

# Alága

Carry the accepted coding outcome through implementation and proportionate verification. Reuse settled scope, decisions, and authorization; a clarification does not restart approval.

Understand the affected behavior and its real owner. Choose the smallest idiomatic change that satisfies the request, preserves unrelated work, and reduces unnecessary state or indirection. Fix the cause rather than accumulating workarounds. Surface consequential scope expansion before taking it on.

Discover commands, APIs, runtime mechanics, and conventions from the current project and authoritative documentation when needed. Use `root-cause` for unresolved diagnosis, `architect` for unresolved technical structure, and `irinse` for a material tool or setup gap.

Verify the changed contract with evidence that could detect a plausible failure. Prefer existing affected checks or a focused probe; add a test when it protects a material regression existing proof would miss. Exercise browser-dependent behavior when acceptance requires it. Remove temporary scaffolding and fix failures caused by the change; rerun only affected checks.

Use `atunwo` when requested or independent judgment is materially useful and within scope. Supply the exact candidate/base, accepted behavior, changed boundaries, verification, and known risks; let `atunwo` choose light or deep unless the user set the depth. Respect a request to skip review. Validate findings, apply warranted corrections within scope, and refresh only affected proof and review conclusions before claiming completion.

Finish when the behavior and necessary documentation are delivered and verified, or a specific gap prevents further progress. Report the change, decisive verification, and limitations. Use `seda-pr` for authorized commit/push/publication; delivery alone does not authorize it.

An explicit `scope-only` request returns the outcome, boundaries, and sufficient proof without implementation.
