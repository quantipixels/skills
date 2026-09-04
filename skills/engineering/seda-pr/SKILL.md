---
name: seda-pr
description: Commit scoped changes, push the current branch, and create or update its ready or draft GitHub pull request or GitLab merge request, including one layer in a stacked review. Draft creation/ready-to-draft transitions require explicit user request. Exclude code implementation, review, monitoring, stack reconciliation, approval, merge, and close operations.
compatibility: Requires Git, network access, and an authenticated provider interface that can prove exact-host/repository reads, writes, pagination, and readback; supported transport may be a connected provider API/connector or authenticated gh/glab CLI.
---

# Ṣẹ̀dá PR

Publish one scoped current branch as one ready-for-review or explicitly requested draft PR/MR. Own scoped commit/push plus provider narrative/state publication. When the branch is one layer in a stack, preserve and report that layer's exact base/stack relationship; do not implement, review, or reconcile the whole stack.

## Authority

Invocation authorizes staging/committing the scoped work, non-force pushing the current branch, creating/updating one item with title/body, observing its stack context, and applying existing high-confidence labels.

New items default to ready. Create or transition to draft only when explicitly requested; otherwise preserve an existing item's publication state.

Creating the current item against its confirmed parent branch is part of publication. Invocation does **not** authorize source edits outside the supplied scope, empty commits, history rewrite, hook bypass, force-push, retargeting an existing item or neighboring stack layer, restructuring/dissolving a stack, reviewer/assignee notifications, approval, merge/close, or issue-closing effects without separate authority.

## Publish

1. Resolve canonical provider/host/repository/current branch/remote/base from explicit input, then unambiguous repository evidence. For an existing PR/MR, pin current item number, publication state, current base, and current head.
2. Resolve publication topology before writing. Prefer provider-native stack membership when available; otherwise derive only from exact open PR/MR source-target relationships. Record `standalone`, `stacked`, or `unknown`, plus the current layer's trunk/parent/position/dependants only to the extent provider evidence proves them. Never infer stack membership from branch names. If an existing item's observed base conflicts with the intended relationship, stop unless retargeting is explicitly authorized.
3. Apply [Git publication invariants](references/git-operations.md) to produce and prove the exact authorized commit on the remote branch. Native Git owns ordinary mechanics; ambient work, unauthorized history rewrite, and unproved remote identity are hard boundaries.
4. Read [provider operations](references/provider-operations.md). Use the available provider interface that can preserve exact-host trust, credential isolation, complete reads/pagination, capability checks, identity refresh, structured writes, stack-context reads, and post-write readback.
5. Reuse an open item with the same canonical repository/head/base rather than creating a duplicate. Stop if the exact current base-to-head diff is empty.
6. Write the title/body directly for a third-party reader with no project context. Ground them in the exact base-to-head change and material proof, docs, ownership, risks, gaps, review focus, and stack parent/trunk context when it changes how the candidate should be read. Preserve useful accurate human content; do not strengthen a claim or add an effect not supported by the candidate.
7. Refresh target/head/base and the current base-ref SHA before every provider write. When stacked, also refresh the parent relationship/stack membership. A changed base can stale the diff/narrative even when the head SHA is unchanged. Reconcile only explicitly requested publication state and read the written state back. On unknown/partial write, stop dependent writes and report `PARTIAL` until current evidence proves the effect.

Preserve existing labels; apply only existing high-confidence labels. Reviewer suggestions are not assignments.

## Report

Return commit SHA when created, remote/readback SHA, canonical PR/MR URL, requested/observed publication state, base and base-ref identity, stack context (`standalone`, `stacked`, or `unknown`) with parent/trunk/position when proved, applied/suggested labels, verification, capability gaps, issue-link effects, and next action. Do not claim merge readiness or approval.
