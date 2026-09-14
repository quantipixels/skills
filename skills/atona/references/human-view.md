# Living initiative brief

Use `html-artifact` for the required living plan view, from the first proposed direction through completion. Reuse the same document and stable locator; retain its identity and source revision in the current plan so resumed work updates it.

Supply the reader's decision, current concern, exact plan revision, and relevant owner-result/candidate/evidence identities. Use one viewpoint unless another reader's distinct decision requires a separate view.

Supply enough context for a person with no prior project or conversation knowledge to understand the problem, who it affects, desired outcome, proposed approach, why it is preferred, and what will change. Explain unfamiliar project terms before relying on them. The human must be able to judge alignment and consequences, not merely inspect agent statuses.

For a local operational view, include the plan's current absolute workspace path, `branch: <branch-name> [main|worktree]`, linked main-worktree path when applicable, and closure disposition when set. Omit machine-specific absolute paths from portable/public views unless the caller explicitly wants them.

The opening must expose the problem and direction, current progress and blocker, delivery evidence and limits, next action or user decision, and material change since the previous useful view. Include named plan status, current gate, and Decision Frontier only when the managed lifecycle applies; explain their consequence in ordinary language.

Identify the meaning whose omission could change that judgment: acceptance and scope/non-goals; consequential decisions, alternatives and assumptions; required behavior or architecture conditions; delivery dependencies and cumulative drift; proof limits/freshness; and risk, reversibility or recovery obligations. Supply owner-established uncertainty and counterevidence, not just positive conclusions.

Keep proposed, confirmed, deferred, and superseded choices distinct. Show responsibilities and the delivery sequence where they explain how the outcome will be reached. During delivery, distinguish planned work, implemented behavior, reviewed results, executed tests, and live verification; finish with the actual outcome and remaining limitations. Preserve the reasons for the direction as progress changes.

When traceability matters, include the current chain:

```text
Outcome / acceptance → decision / contract → architecture / owner → delivery candidate → proof
```

Pass owner-established gaps in either direction: accepted obligations without implementation/proof, mechanisms without an accepted basis, or evidence that no longer proves a current claim. Do not infer those gaps from diagram structure.

Preserve the plan's progression judgment and visibility requirements in the view. A Markdown dump, unexplained skill-name map, attractive dashboard, or source link alone does not establish comprehension. Check that the reader can explain what is proposed, why, what remains undecided, what has actually happened, and what comes next from the view itself.
