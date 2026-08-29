# Git publication invariants for Ṣẹ̀dá PR

Use after scoped work, current branch, remote/base, commit authority, and in-scope paths are settled. Native Git owns the mechanics; this reference defines the publication invariants.

## Candidate boundary

The commit must contain exactly the authorized work. Keep ambient/unrelated changes, secrets, and QP `.qp` state out of the staged candidate. Inspect the exact staged result before commit and do not create an empty commit when the intended work is already committed.

Repository state never authorizes amend, rebase, squash, force-push, hook bypass, or another history rewrite.

## Remote divergence

Refresh the exact remote branch before publication. If it contains commits absent from the local branch, do not push through the divergence blindly. Integrate without rewriting history only when the update is clean, intended, and within authority; otherwise stop with the exact divergence/conflict.

## Push identity

Push only the intended current branch without force. Read the remote branch back and require its SHA to equal the exact local commit intended for publication. A successful push command without matching remote identity is not publication proof.

If the local candidate or remote branch changes after validation, refresh the dependent publication evidence before provider narrative/state mutation.
