---
name: seda-pr
description: Commit scoped changes, push the current branch, and create or update its ready or draft GitHub pull request or GitLab merge request for a third-party reader with no project context. Draft creation/ready-to-draft transitions require explicit user request. Exclude code implementation, review, monitoring, approval, merge, and close operations.
compatibility: Requires Git, network access, and an authenticated provider interface that can prove exact-host/repository reads, writes, pagination, and readback; supported transport may be a connected provider API/connector or authenticated gh/glab CLI.
---

# Ṣẹ̀dá PR

Publish one scoped current branch as one ready-for-review or explicitly requested draft PR/MR. Own scoped commit/push plus provider narrative/state publication; do not implement or review the code.

## Authority

Invocation authorizes staging/committing the scoped work, non-force pushing the current branch, creating/updating one item with title/body, and applying existing high-confidence labels.

New items default to ready. Create or transition to draft only when explicitly requested; otherwise preserve an existing item's publication state.

Invocation does **not** authorize source edits outside the supplied scope, empty commits, history rewrite, hook bypass, force-push, reviewer/assignee notifications, approval, merge/close, or issue-closing effects without separate authority.

## Publish

1. Resolve canonical provider/host/repository/current branch/remote/base from explicit input, then unambiguous repository evidence. For an existing PR/MR, pin current item number and publication state.
2. Apply [Git publication invariants](references/git-operations.md) to produce and prove the exact authorized commit on the remote branch. Native Git owns ordinary mechanics; ambient work, unauthorized history rewrite, and unproved remote identity are hard boundaries.
3. Read [provider operations](references/provider-operations.md). Use the available provider interface that can preserve exact-host trust, credential isolation, complete reads/pagination, capability checks, identity refresh, structured writes, and post-write readback.
4. Reuse an open item with the same canonical repository/head/base rather than creating a duplicate. Stop if the base-to-head diff is empty.
5. Write the title/body directly for a third-party reader with no project context. Ground them in the exact base-to-head change and material proof, docs, ownership, risks, gaps, and review focus. Preserve useful accurate human content; do not strengthen a claim or add an effect not supported by the candidate.
6. Refresh target/head before every provider write. Reconcile only explicitly requested publication state and read the written state back. On unknown/partial write, stop dependent writes and report `PARTIAL` until current evidence proves the effect.

Preserve existing labels; apply only existing high-confidence labels. Reviewer suggestions are not assignments.

## Report

Return commit SHA when created, remote/readback SHA, canonical PR/MR URL, requested/observed publication state, applied/suggested labels, verification, capability gaps, issue-link effects, and next action. Do not claim merge readiness or approval.
