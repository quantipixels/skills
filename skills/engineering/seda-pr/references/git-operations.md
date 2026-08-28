# Git publication operations for Ṣẹ̀dá PR

Use after scope, branch, remote, base, commit authority, and in-scope paths are settled. Keep commands scoped and inspect their output; do not wrap them in a custom command-policing runtime.

## Candidate preflight

```bash
git status --short --branch
git diff --check
git diff --cached --check
git diff --cached --name-status
```

QP workspace state must not enter publication:

```bash
git ls-files -- '.qp' '.qp/**'
git diff --cached --name-only -- '.qp' '.qp/**'
```

If `.qp` is tracked/staged, stop for cleanup rather than publishing it.

Stage only authorized paths/hunks with native Git, then inspect the staged diff before commit. Do not use `git add -A` when unrelated work is present merely for convenience.

## Remote divergence

When the remote branch exists:

```bash
git fetch "$remote" "$branch"
git rev-list --left-right --count "$remote/$branch...HEAD"
```

Interpret as `<remote-only> <local-only>`. If the remote has new commits, integrate without history rewrite only when the update is clean, intended, and inside authority; otherwise stop with the exact divergence/conflict.

## Publish and verify

```bash
git push --set-upstream "$remote" HEAD
git rev-parse HEAD
git ls-remote "$remote" "refs/heads/$branch"
```

Require the remote branch SHA to equal local `HEAD`. Never force-push. A commit/push request does not authorize amend, rebase, squash, hook bypass, or another history rewrite.
