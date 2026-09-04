# Durable knowledge reconciliation

Read this file before `Closed`. Use it to prevent confirmed knowledge from surviving only in transient lifecycle context while avoiding a dump of task history into repositories, documents, or organizational knowledge stores.

## Build the reconciliation candidate

Read the exact-current initiative plan and only the linked specifications, decisions, research, delivery results, reviews, current durable sources, and other evidence needed to identify material knowledge established or changed during the lifecycle.

Atọ́nà owns the inventory, disposition coverage, and closure judgment. Semantic owners perform their native reconciliation. Use the active domain/project owner when one exists; in repository-scoped work:

- `amose` owns domain context, `.learnings`, `.nongoals`, ADR lifecycle, and authorized local craft;
- the current delivery owner owns ordinary documentation and enforceable implementation artifacts within its result;
- `seda-spec` owns behavior-specification meaning and supersession; and
- `akosile` owns `.qp` path and publication mechanics when `.qp` is the selected destination.

External publication remains separately authorized. Do not infer permission to create or update an issue, pull request, wiki, shared drive, policy store, knowledge base, or another external record from plan closure.

Add a reconciliation item when losing it could cause future planning, delivery, review, diagnosis, operation, changeover, or user understanding to repeat a settled mistake or contradict the accepted result. Add items as they emerge; do not wait until closure when the natural owner can reconcile them safely during delivery.

## Classify every material item

Give each item one disposition:

| Disposition | Meaning | Required evidence |
| --- | --- | --- |
| `PROMOTE` | A durable owner/destination must record the knowledge | destination owner and pending or completed write |
| `ALREADY_REPRESENTED` | Current durable material already expresses it accurately | exact source/record identity and current revision/candidate |
| `LIFECYCLE_ONLY` | The detail is useful history but must not govern future work | retained source identity and reason |
| `NOT_APPLICABLE` | No durable knowledge obligation exists | concise reason |
| `BLOCKED` | Required promotion lacks authority, destination, or current evidence | blocker, owner, and resume trigger |

Use the active domain's existing source of truth. Possible destinations include:

| Knowledge | Natural destination |
| --- | --- |
| user-visible behavior, setup, process, service, or usage | current product/service/process documentation |
| durable intent, contract, constraint, or rationale attached to a maintained artifact | the artifact's own documented authority: source comment, specification note, operating instruction, procedure, design record, or equivalent |
| canonical terms, relationships, and domain invariants | existing domain/project documentation or the current knowledge owner |
| hard-to-reverse surprising decision with a genuine trade-off | the domain's existing decision record; in repository technical work, a qualifying ADR through `amose` |
| reusable operational constraint or non-obvious gotcha | existing runbook/playbook/project knowledge; `.learnings` through `amose` when that repository convention is the natural destination |
| durable project-wide exclusion | the project's governing constraints; `.nongoals` through `amose` when that repository convention applies |
| behavior/rule that can be enforced | the strongest natural control: policy, configuration, schema, type, test/check, automation, code, checklist, or other domain mechanism through its owner |
| temporary status, abandoned path, or execution transcript | exact lifecycle record only |

Do not promote every record. Summarize only settled knowledge that changes future action. Preserve provenance without copying conversations, research transcripts, ticket history, review chatter, or execution logs into durable guidance.

Do not require a repository destination when the initiative is not repository-bound. A temporary file, chat-only state, or untracked `.qp` resource can remain working memory or historical evidence, but it is insufficient when knowledge genuinely must survive the current context. In that case require an existing/user-selected durable destination or return `BLOCKED` with the missing destination/authority. Do not invent a new knowledge system merely to satisfy closure ceremony.

## Execute and prove reconciliation

For each `PROMOTE` item:

1. Give the semantic owner the exact source identity, confirmed knowledge, intended destination, and current result/candidate.
2. Make the smallest update that leaves one source of truth and removes or marks materially stale guidance.
3. Reconcile durable material at its natural delivery boundary when possible rather than creating a separate end-of-initiative documentation phase.
4. Re-read every written destination and verify that its meaning, links, lifecycle state, and evidence match the accepted result.
5. Record the destination identity/revision, owner result, and remaining limit in the initiative plan.

Before `Closed`, require no `PROMOTE` item without accepting proof and no `BLOCKED` item. Verify that durable changes belong to the exact accepted result, superseded specifications/decisions point to current authority when needed, and transient records are not the sole source of knowledge future work must preserve.