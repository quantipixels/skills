# Store repository workspace state outside individual worktrees

Status: Accepted

## Decision

Repository-scoped QP state uses `<git-common-dir>/qp` as its one physical store. A worktree root `.qp` is only a reconstructible alias when a worktree-relative view is useful. Bare repositories may own the canonical store without any worktree alias.

Akọsílẹ̀ owns the exact path, publication, alias, and migration mechanics. Git metadata remains the authority for repository/worktree topology; QP does not maintain a second worktree registry or replicate one physical store per worktree.

## Why

Repository state must survive worktree movement/removal and be equally available to linked worktrees. Putting the physical store inside one privileged worktree creates avoidable ownership and recovery problems, while Git already provides a shared repository directory.

## Consequences

- worktree deletion cannot remove canonical QP state;
- aliases are derived and repairable rather than semantic state;
- bare worktree hubs remain valid;
- hosts without symlink support report an alias capability gap instead of creating duplicate stores; and
- migration must preserve and reconcile authoritative legacy `.qp` content before replacing it with an alias.
