# Maintain ADRs

Create or offer an ADR only when an unrecorded confirmed decision is all three:

- hard to reverse at meaningful cost;
- surprising without its context; and
- the result of a genuine trade-off between credible alternatives.

When any condition is missing, do not create a new ADR. Keep ordinary implementation choices, reversible portfolio/design changes, naming, refactors, routine dependency choices, and useful rationale in the current plan/spec/PR/history unless another durable destination is independently required.

This threshold governs new records, not lifecycle maintenance of existing records.

## Calibration

Good ADR candidate:

```text
Adopt an outbox-based event publication model instead of direct broker publication from the request transaction because delivery/recovery guarantees and database consistency must survive broker failure.
```

Why it qualifies: it is costly to reverse once integrated, surprising without the failure/recovery context, and reflects a real trade-off against a credible simpler alternative.

Bad ADR candidate:

```text
Rename PaymentDto to PaymentResponse.
```

Why it does not qualify: it is cheap to reverse and does not preserve a consequential trade-off.

Usually not an ADR by itself:

```text
Use PostgreSQL for this new service.
```

It becomes an ADR only when the choice is materially hard to reverse, non-obvious in context, and follows a genuine comparison whose rationale future maintainers need. Otherwise keep it with the ordinary architecture/plan evidence.

Likewise, adding/removing/renaming a skill or changing a reversible portfolio boundary is normally PR/spec/history, not an ADR. Promote it only when the decision itself passes all three gates.

Good `.nongoals`, not ADR:

```text
The project will not operate a third-party plugin marketplace.
```

Why: a durable project exclusion can stand as a boundary without inventing an architectural decision record unless a qualifying trade-off also needs preservation.

Match the repository's existing location, naming, markup, status, and structure. Create the destination and record only when a qualifying decision and write authority exist.

Reconcile an existing ADR whenever its decision changes. Preserve it as history. Do not rewrite a superseded ADR's decision merely to match current names, owners, or behavior; record later truth in lifecycle state, a linked current authority, or a superseding ADR. Create a superseding decision ADR only when the replacement independently passes the threshold; otherwise use the repository's permitted lifecycle mechanism to mark the old record deprecated or no longer current and link to the current authority where practical. A lifecycle-only index or status record may satisfy an immutable-record convention without representing the replacement as a qualifying decision ADR. If the repository permits neither changing the old record nor a lifecycle-only record, return `blocked` and obtain authority for a lifecycle convention instead of violating immutability or the threshold.

## Fallback format

Use this fallback only when the repository has no ADR convention.

Store records in `docs/adr/` with names such as `YYYYMMDD-short-title.md`. Add time only when two independent decisions on the same date would otherwise collide. Create the directory only when the first qualifying ADR is authorized.

The minimum complete record is:

```markdown
# <Short decision title>

<A short paragraph stating the context, what was decided, and why.>
```

Add status, considered options, consequences, or supersession links only when they preserve information a future maintainer will need. Do not add empty sections or boilerplate.
