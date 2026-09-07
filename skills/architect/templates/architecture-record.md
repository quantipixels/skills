---
owner: architect
record_type: architecture
subject: <stable architecture subject>
title: <architecture topic>
updated_at: <offset-aware timestamp>
revision: 1
# Include only when readiness itself is the record result:
# status: IMPLEMENTATION_READY | NOT_READY | UNPROVED
---

# <Architecture topic>

## Question and result

**Architecture question:** <the technical structure this record resolves>

**Selected structure:** <concise design summary>

**Readiness:** <omit unless implementation readiness is the requested/required result>

## Material drivers

<only constraints/scenarios that materially shape the structure>

## Structure and ownership

<system/subsystem/module ownership, interfaces/seams, data/state/identity, and integrations>

Include trust, deployment/runtime, operations, failure/recovery, compatibility, migration, rollback, or deletion only when they materially shape this architecture.

## Critical invariants

<implementation-shaping rules and forbidden dependency/trust/state directions>

## Decisions and alternatives

<selected technical choices, decisive trade-offs, and strongest credible alternatives worth retaining>

## Gaps and evidence

<unresolved architecture gaps, evidence limits, and exact linked sources needed for review/recovery>
