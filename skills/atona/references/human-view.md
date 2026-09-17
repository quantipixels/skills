# Living initiative brief

Supply `html-artifact` with the reader’s current decision or concern, the HTML plan's locator and revision, and relevant candidate/evidence identities. Maintain that same HTML as the plan; no equivalent Markdown source or separate source/view synchronization is required. Use one viewpoint unless another reader has a distinct decision.

Establish the problem, affected people, intended outcome, proposed approach, rationale, and unfamiliar project terms for a reader with no prior project or chat context.

For a local operational view, include the plan's current absolute workspace path, `branch: <branch-name> [main|worktree]`, linked main-worktree path when applicable, and closure disposition when set. Omit machine-specific absolute paths from portable/public views unless the caller explicitly wants them.

The opening must expose the problem and direction, current progress and blocker, delivery evidence and limits, next action or user decision, and material change since the previous useful view. Include named plan status, current gate, and Decision Frontier only when the managed lifecycle applies; explain their consequence in ordinary language.

Identify the meaning whose omission could change that judgment: acceptance and scope/non-goals; consequential decisions, alternatives and assumptions; required behavior or architecture conditions; delivery dependencies and cumulative drift; proof limits/freshness; and risk, reversibility or recovery obligations. Supply owner-established uncertainty and counterevidence, not just positive conclusions.

Keep proposed, confirmed, deferred, and superseded choices distinct. Show responsibilities and the delivery sequence where they explain how the outcome will be reached. During delivery, distinguish planned work, implemented behavior, reviewed results, executed tests, and live verification; finish with the actual outcome and remaining limitations. Preserve the reasons for the direction as progress changes.

When traceability matters, include the current chain:

```text
Outcome / acceptance → decision / contract → architecture / owner → delivery candidate → proof
```

Pass owner-established gaps in either direction: accepted obligations without implementation/proof, mechanisms without an accepted basis, or evidence that no longer proves a current claim. Do not infer those gaps from diagram structure.

Preserve the plan’s progression judgment and visibility requirements; `html-artifact` owns presentation and comprehension checks.
