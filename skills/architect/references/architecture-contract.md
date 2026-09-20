# Architecture Contract

Use this only when Architect must provide or judge an implementation-readiness gate. A bounded module/design question does not need this contract merely because Architect is active.

Keep only implementation-shaping constraints that a delivery owner must not have to invent.

## Compact contract

```text
Architecture Contract
Subject / candidate:
Critical ownership:
Critical interfaces / seams:
Critical invariants:
Allowed / forbidden dependency or trust directions:
State / identity / lifecycle ownership:
Failure / recovery / migration constraints: <when material>
Compatibility / capacity / operational constraints: <when material>
Verification obligation: <only claims whose enforceability matters>
Evidence cutoff / unresolved gaps:
```

Do not copy architecture rationale, alternative catalogues, task history, or proof mechanics unless one is necessary to interpret a material guardrail.

## Readiness test

Return `IMPLEMENTATION_READY` only when:

- every material driver has a coherent structural answer;
- ownership, interfaces/seams, state, dependency/trust directions, and applicable lifecycle/failure boundaries do not conflict;
- implementation does not need to invent a material technical decision;
- required migration/recovery/compatibility obligations are stated when they can affect safe delivery; and
- current evidence is sufficient to support the consequential claims.

Return `NOT_READY` when a material architecture choice, contradiction, missing owner/interface, migration/recovery obligation, or structural defect remains.

Return `UNPROVED` when the design may be sufficient but missing/stale evidence prevents responsible judgment.

A candidate/driver/decision change stales only the dependent contract claims. Do not regenerate unrelated architecture detail merely because one constraint changed.

Architect states critical invariants and the kind of evidence capable of falsifying them. The delivery/review/tooling owner chooses and executes ordinary proof mechanics unless a specific enforcement mechanism is itself part of the architecture.
