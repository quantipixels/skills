---
name: seda-pr
description: Produces a PR/MR description, a published PR/MR, or a PR/MR kept moving through CI, conflicts and feedback, up to the requested stopping point. Use to create, describe, publish or babysit a GitHub PR or GitLab MR.
compatibility: Live provider operations require authenticated access; commits and fixes also require Git and project verification tools. A description can use supplied changes and evidence.
---

# Seda PR

**Output:** a PR/MR (description, published item, or stewarded item) from its requested entry point to its requested stopping point, easy for a reviewer to inspect. Optimize the reviewer's understanding, not a changelog of agent activity.

**Needs:** a change on a branch (or an existing PR/MR) and the stopping point wanted. If there is no change to publish, or the user did not ask to publish, return to the caller and say what is missing.

## Method

**Workflows** (`asoju`): a large PR's description starts from a change record; a body many reviewers rely on gets draft, critique, revise.

## Scope the operation

- **Description:** return a draft, or update an existing body when explicitly requested. This grants no commit, push, PR creation, state change or babysitting authority.
- **Publication:** commit scoped work, push and create or update the item. Stop after verified publication unless babysitting was also requested.
- **Stewardship / babysitting:** investigate CI, conflicts and feedback, make justified in-scope corrections, verify, commit, push normally and reply/resolve with evidence. Babysitting covers replies on this item's review threads; other messages (new issues, pings, other PRs) need separate authority. A watch/status-only request remains read-only, including the body.

Use the explicit target; otherwise reuse the current branch's unambiguous open item. Before publishing, read the branch's item state: a branch whose item is merged or closed is spent, so start a new branch from the updated integration branch and carry over any unmerged commits. For publication with no item, use the task branch or create a feature branch from the established integration branch or specified stack parent. Ask only for genuinely ambiguous targets or authority. Supplied descriptions/diffs need no live PR.

Publication, approval and merge are separate user decisions. A publication or babysitting request authorizes neither approval nor merge. Preserve unrelated work, human content and the repository template. Approval, merge/close/reopen, draft-state changes, retargeting, history rewrite, force-push, hook bypass, reviewer/assignee changes and unrelated edits need separate authority.

Use `gh` or `glab`, falling back to the provider API; discover uncertain mechanics from current help/docs.

## Describe and publish

Use [reviewer brief](references/reviewer-brief.md) for composing or materially refreshing a body. Reuse the task, actual diff, applicable domain meaning and current proof; gather surrounding context only where needed to explain behavior or ownership.

For authorized publication, verify the target, commit coherent changes and push normally. Create or update the existing item, ready by default for creation unless draft was requested; preserve the state of an existing item. Never publish an empty diff. A body update does not create another PR.

Read back the published head, base, state and body. Confirm that claims and evidence describe that candidate and that evidence locations are usable by the reviewer. Verify uncertain writes before retrying. Return draft text without a saved sidecar unless the caller or project needs one.

## Babysit the same item

Establish current head/base, mergeability, required checks and all unresolved feedback; incomplete coverage is unknown, not ready. Read [stewardship](references/stewardship.md) for the full procedure (feedback assessment, corrections, waiting on SIGIDI or elsewhere, stop conditions), plus [stacked PRs](references/stacked-prs.md) when dependencies affect the target and [failure guidance](references/failure-heuristics.md) to judge failures and feedback against code. Read-only watching reports findings without fixing, replying or resolving them.

## Done

Provider-ready means open/not draft, positively mergeable, required checks passed or explicitly absent, feedback disposed with evidence and no unresolved published threads, no blocking review, complete current evidence and no changing ancestor. Keep `PROVIDER_READY` or `STACK_PROVIDER_READY` for callers; neither means low risk, independent approval or integrated delivery acceptance.

Before finishing SIGIDI PR work, check `list_thread_pull_requests` and link any PR you worked on that is missing. Report linking or watching failures.


## Return

For a description, return the usable body and material gaps, or verify the requested live-body update. Otherwise return the URL, consequential change/corrections, current readiness, risk/recovery and the blocker or next action. Include candidate identities when needed to substantiate or resume the work. Stop before approval or merge.
