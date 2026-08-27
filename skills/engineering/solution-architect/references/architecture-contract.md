# Architecture Contract

Use this reference for implementation-ready `design` and when reviewing a candidate against a current architecture packet. It supplements the rich packet with a compact downstream constraint set.

## Run four sufficiency passes

### Native-platform pass

For each custom abstraction/mechanism, ask whether the detected language/framework/platform already owns the requirement. Prefer the native path when it satisfies the driver; retain custom machinery only for a remaining ownership, policy, lifecycle, integration, compatibility, or proof gap.

### Complexity-budget pass

Every new service, queue, datastore, cache, protocol, dependency, module, abstraction, or deployment unit must pay for itself with a named driver/scenario. Include operational, migration, failure, security, cognitive, and proof burden. Do not introduce a seam only for hypothetical variation.

### Negative-architecture pass

State the important forbidden directions/states: invalid dependency directions, duplicated ownership, trust-boundary leaks, transaction/effect violations, unsafe lifecycle crossings, unbounded work, unsupported compatibility, or forbidden persistence/data flows.

### Fitness/proof-owner pass

For each critical invariant, name one primary complete proof owner at the cheapest stable seam: compiler/type/schema/static rule, focused contract test, integration seam, observability/operational check, or acceptance journey. Duplicate proof only when it detects a distinct failure mode.

## Separate technical choices from material user decisions

Solution Architect owns reversible technical choices when accepted constraints and evidence are sufficient. Do not send every alternative to the user.

When the choice changes accepted outcome, scope, policy, user experience, material cost/risk, compatibility, or a trade-off that requires user authority, do not choose it. Return:

```text
Decision gap
Identity:
Why material:
Prerequisite facts/evidence:
Options/trade-off boundary:
Architecture effect:
Plan effect:
Required owner: arojinle
```

A current material decision gap prevents `IMPLEMENTATION_READY`.

## Derive the compact contract

```text
Architecture Contract
Candidate / packet revision:
Critical invariants:
Allowed dependency directions:
Forbidden directions/states:
Data/state/identity/authority owners:
Lifecycle/failure/recovery obligations:
Resource/capacity/complexity budgets:
Compatibility/migration constraints:
Primary proof seams / fitness owners:
Evidence cutoff/freshness:
```

Keep only implementation-shaping constraints. Do not copy the packet's rationale/alternatives unless needed to interpret one guardrail. A material packet/candidate/decision change stales the contract.
