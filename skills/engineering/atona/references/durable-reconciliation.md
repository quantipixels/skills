# Durable knowledge reconciliation

Read this file before `Closed`. Use it to prevent confirmed knowledge from surviving only in untracked lifecycle records while avoiding a dump of task history into the repository.

## Build the reconciliation candidate

Read the exact-current initiative plan and only the linked specifications, decisions, architecture, research, tickets, delivery results, reviews, and current repository evidence needed to identify material knowledge established or changed during the lifecycle.

Atọ́nà owns the inventory, disposition coverage, and closure judgment. Semantic owners perform their native reconciliation:

- `amose` owns domain context, `.learnings`, `.nongoals`, ADR lifecycle, and authorized local craft;
- the current delivery owner owns ordinary documentation, source-level documentation, and enforceable code, tests, schemas, types, or static rules;
- `seda-spec` owns specification meaning and supersession; and
- `akosile` owns `.qp` path and publication mechanics.

Provider publication remains separately authorized. Do not infer permission to create or update an issue, pull request, wiki, or another external record from plan closure.

Add a reconciliation item when losing it could cause future planning, implementation, review, debugging, operation, migration, or user understanding to repeat a settled mistake or contradict delivered behavior. Add items as they emerge; do not wait until closure when the natural owner can reconcile them safely during delivery.

## Classify every material item

Give each item one disposition:

| Disposition | Meaning | Required evidence |
| --- | --- | --- |
| `PROMOTE` | A durable owner must record the knowledge | destination owner and pending or completed write |
| `ALREADY_REPRESENTED` | Current durable material already expresses it accurately | exact path/symbol/record and candidate identity |
| `LIFECYCLE_ONLY` | The detail is useful history but must not govern future work | retained source identity and reason |
| `NOT_APPLICABLE` | No durable knowledge obligation exists | concise reason |
| `BLOCKED` | Required promotion lacks authority, destination, or current evidence | blocker, owner, and resume trigger |

Use the project's existing source of truth. Common destinations are:

| Knowledge | Natural destination |
| --- | --- |
| user-visible behavior, setup, or usage | README, product documentation, or API documentation |
| durable intent, contract, constraint, or usage attached to a source symbol | inline code comment, doc comment, KDoc, Javadoc, or the language's equivalent through the delivery owner |
| canonical terms, relationships, and domain invariants | existing domain documentation or `CONTEXT.md` through `amose` |
| hard-to-reverse, surprising decision with a genuine trade-off | qualifying ADR through `amose` |
| reusable operational constraint or non-obvious gotcha | `.learnings` through `amose` |
| durable project-wide exclusion | `.nongoals` through `amose` |
| behavior that can be enforced | code, tests, schemas, types, configuration, or static rules through the delivery owner |
| temporary status, abandoned path, or execution transcript | exact lifecycle record only |

Do not promote every record. Summarize only settled knowledge that changes future action. Add a source comment only when the knowledge belongs beside that code and explains intent, contract, constraint, or non-obvious behavior that the code cannot express clearly. Preserve provenance without copying conversations, research transcripts, ticket history, review chatter, or implementation logs into durable documentation or source comments.

An untracked `.qp` resource can remain working memory or historical evidence, but it is not sufficient when knowledge must survive a clone, machine loss, archival gap, or future agent without that workspace. In that case require a versioned repository destination or an explicitly authorized durable provider. Authorized `amose` local craft remains untracked by design; promote clone-critical rules to repository instructions or another visible project authority instead.

## Execute and prove reconciliation

For each `PROMOTE` item:

1. Give the semantic owner the exact source identity, confirmed knowledge, intended destination, and current candidate.
2. Make the smallest update that leaves one source of truth and removes or marks materially stale guidance.
3. Include ordinary documentation, applicable source-level documentation, and enforceable artifacts in the exact delivery candidate before its final review when possible.
4. Re-read every written destination and verify that its meaning, links, lifecycle state, and evidence match the delivered candidate.
5. Record the destination path or provider identity, revision or commit/candidate identity, owner result, and remaining limit in the initiative plan.

Before `Closed`, require no `PROMOTE` item without accepting proof and no `BLOCKED` item. Verify that versioned changes belong to the exact delivered and reviewed candidate, every superseded specification or ADR points to current authority when needed, and retained untracked records are not the sole source of knowledge future work must preserve.
