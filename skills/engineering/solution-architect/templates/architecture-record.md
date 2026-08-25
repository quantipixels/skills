---
owner: solution-architect
record_type: architecture
title: <architecture topic>
updated_at: <offset-aware timestamp>
revision: 1
candidate: <exact subject/candidate, optional>
status: IMPLEMENTATION_READY | NOT_READY | UNPROVED
---

# <Architecture topic>

## Resume

**Problem:** <why this architecture exists>

**Selected design:** <one concise design summary>

**Result:** `IMPLEMENTATION_READY | NOT_READY | UNPROVED`

**Next technical action:** <one exact action and completion condition>

## Problem and outcomes

<problem, affected users/systems, and required outcomes>

## Scope and non-goals

### Scope

- <included boundary>

### Non-goals

- <excluded boundary>

## Constraints and assumptions

- <confirmed constraint or explicit assumption>

## Drivers and scenarios

| Driver | Scenario | Observable response |
|---|---|---|
| <driver> | <normal/failure/misuse/recovery/scale/evolution scenario> | <response> |

## Context and ownership

<actors, external systems, trust boundaries, capabilities, data/state/runtime/deployment/lifecycle owners>

## Decisions and alternatives

### <Decision>

<selected design, alternatives, trade-offs, reversibility, and evidence>

## Implementation design

<modules, interfaces, data/state, flows, integration, authentication, deployment, configuration, observability, and operations>

## Failure, recovery, migration, and deletion

<timeouts, retries, idempotency, backpressure, misuse, compatibility, migration order, rollback, recovery, and old-path deletion>

## Proof

<tests, observability, operational checks, and acceptance for material drivers>

## Risks and gaps

<residual risks, deferrals, evidence gaps, and required owners>

## Linked records and evidence

| Source | Record or locator | Revision/cutoff | Freshness | Role |
|---|---|---|---|---|
| <source> | <record-ref, path, provider identity, or revision> | <revision> | current | <role> |

Keep complete research, code, logs, tests, and provider payloads with their native owners.

## HTML projection

**Audience and purpose:** <reader and outcome>

**Governing question:** <question>

**Central representation:** <context, flow, state, topology, or migration view>

**Foreground:** <selected design, critical flows, material risks, migration, and result>

**Link-only:** <detailed research, code, logs, and supporting records>

## Material history

- r1 — <only a status, scope, decision, evidence, recovery/migration, or ownership change worth retaining>
