# Durable knowledge reconciliation

Use this only when an initiative established or changed **stable governing knowledge that future work must rely on outside the initiative's normal lifecycle artifacts**, or when an existing durable source of truth became materially stale.

The default is **no promotion**. Plans, specifications, tickets, PR/MR discussion, reviews, commits, provider history, and other normal initiative artifacts are sufficient for ordinary implementation choices, rationale, findings, reversible design/portfolio changes, and useful historical context.

## Admit only knowledge that genuinely needs promotion

Promote an item only when all apply:

1. future work materially depends on retaining the knowledge beyond this initiative/candidate;
2. the knowledge is stable enough to govern future work rather than describe a temporary state or one delivery choice;
3. no existing maintained source already represents it accurately;
4. losing or staling it creates a credible risk of a consequential wrong decision, behavior, operation, or boundary—not merely rediscovery cost; and
5. a natural durable owner/destination exists or has been explicitly selected.

If any condition is missing, leave the information in the initiative's normal artifacts/history. Do not create a durable record merely because the information is useful, non-obvious, or expensive to rediscover.

When the gate passes, read only the exact-current initiative result and the durable sources needed to reconcile that knowledge. Semantic owners retain their native contracts; for repository-scoped work this may include:

- `amose` for durable domain/project knowledge, `.learnings`, `.nongoals`, and qualifying ADR lifecycle;
- the current delivery owner for maintained user/operator documentation or enforceable implementation artifacts;
- `seda-spec` for durable behavior-specification meaning when the specification itself must remain authoritative; and
- `akosile` only for `.qp` path/publication mechanics when `.qp` is the selected destination.

External publication remains separately authorized.

## Choose the natural destination

Use the strongest existing source of truth. Examples:

| Knowledge | Natural destination |
| --- | --- |
| maintained user-visible behavior/setup/process | current product/service/process documentation |
| stable canonical terminology, relationship, or invariant | existing domain/project knowledge source |
| stable non-obvious operational/project rule that future work must obey | existing runbook/project knowledge; `.learnings` when that convention applies |
| durable project-wide exclusion | governing project constraints; `.nongoals` when that convention applies |
| enforceable behavior/rule | policy, configuration, schema, type, test/check, automation, code, or another natural control |
| hard-to-reverse surprising decision with a genuine trade-off | existing decision-record convention; qualifying ADR through `amose` in repository technical work |

Prefer updating an existing maintained source over creating a new record. A new destination is not justified merely because knowledge passed the promotion gate.

### ADR gate remains stricter

An ADR is not the generic destination for durable knowledge. Create one only when the decision independently satisfies the ADR contract: **hard to reverse at meaningful cost, surprising without its context, and the result of a genuine trade-off between credible alternatives**.

Skill additions/removals, naming changes, routine refactors, reversible implementation choices, ordinary dependency selections, and portfolio rearrangements normally remain in the PR/spec/history unless they independently meet that threshold.

## Reconcile

For each admitted item:

1. identify the exact stable knowledge and its current evidence;
2. confirm the natural existing destination and authority;
3. make the smallest update that leaves one source of truth;
4. remove or mark materially stale competing guidance when necessary; and
5. re-read the destination and verify it matches the accepted result.

If a required durable source is stale but cannot be updated because authority or destination is missing, return `BLOCKED` with the exact gap. Otherwise do not block initiative closure on knowledge that failed the promotion gate.
