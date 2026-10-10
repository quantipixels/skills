# Working records live outside the repo

Specs, tickets, plans, prototypes and reports used to sit in `.qp/` inside each checkout. They were lost when a worktree was deleted, differed between worktrees of the same repo, and were easy to commit by mistake. We decided they live in `~/.qp/<owner>/<repo>/`, shared by every worktree and never committed, and that each checkout gets a `.qp` symlink to that folder, listed in `.git/info/exclude` rather than `.gitignore`. Only records meant to last with the code are committed: lessons in `docs/internal/solutions/`, decisions in `docs/internal/decisions/`, guides for users in `docs/user/`, and the README's Non-goals. A project can move specs, tickets or plans into git with `qp.yaml`.

Consequences: working records are per machine, not shared through the repo. `alarina` ships `scripts/qp_records.py` to create or repair the link before any record is written.
