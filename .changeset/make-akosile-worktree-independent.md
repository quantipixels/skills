---
"qp-skills": minor
---

Make Akọsílẹ̀ repository state independent of any privileged Git worktree. Store the canonical workspace under `<git-common-dir>/qp`, treat worktree-root `.qp` entries as reconstructible symlink aliases, support bare repositories as worktree hubs, and define conflict-safe migration from legacy physical `.qp` stores without adding a migration runtime.