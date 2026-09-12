# Durable programs

Use only when a Pepeye workflow must remain correct after the current lead/session disappears or another coordinator must resume without reconstructing material orchestration state from scratch.

## Admission test

Durable orchestration is justified when one or more of these are true and ordinary project artifacts are insufficient:

- work spans sessions or coordinators and has several independently progressing tracks;
- correct resumption depends on queue/frontier state that is not owned by an existing skill;
- workers may finish after the initiating lead is gone and their results must be reconciled safely;
- retries, ownership, integration order, or verification receipts must survive process/machine restart; or
- a human intentionally checks in periodically while the program continues through many bounded units.

Task size, file count, worker count, or multi-day duration alone is not sufficient.

## Minimum durable state

When this threshold is reached, persist only orchestration facts that another lead cannot safely derive:

- program outcome and accepted constraints;
- active/completed/blocked units and dependency frontier;
- exact candidate/workspace identities;
- assignment ownership and authority;
- verification/integration receipts;
- consequential decisions affecting progression; and
- unresolved inbox/handoff events.

Do not duplicate semantic plans, architecture, specifications, reviews, or provider records that already have authoritative owners.

## Escalation discipline

Start with conversation/native worker handles. Promote to a bounded workflow before adding durable state. Add a deterministic bookkeeping seam only after real failures show agent-managed state is insufficient.

Pepeye currently defines this admission boundary but does not ship a scheduler, daemon, orchestration database, or coordinator runtime. A future runtime must earn each mechanism through demonstrated resumability/coordination failures and remain separate from skill semantics.
