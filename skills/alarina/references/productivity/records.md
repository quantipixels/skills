# Records and working state

Keep information with the owner that will use it. Routine reasoning, a short review, or a result that fits in the reply needs no file. Do not create a second record when the current plan, issue, specification, or project document already carries the work.

Choose a destination by purpose:

- **Human deliverable:** use the requested or established visible project destination. If neither exists, choose a location the reader can open and return its locator. Keep the format the reader needs; a plan or report does not become HTML merely because it is persisted.
- **Shared project knowledge:** update the repository's existing authoritative document, issue tracker, or knowledge location when the information must remain discoverable to collaborators. A private working record does not establish project policy or durable domain truth.
- **Reusable custom workflow:** retain a path supported by real execution under `~/.qp/alarina/ona/` using [learned workflows](learned-workflows.md). Keep project-bound assumptions visible and share through the established project owner when collaborators need it; ordinary task notes do not belong in this library.
- **Disposable scratch:** use the host's temporary storage or an existing project cache for regenerable probes and intermediate output. Retain evidence needed to support a delivered claim, and clean only owned scratch when safe.
- **Resumable private task state:** reuse the task's existing record. If it has no established destination, use a task-scoped directory under `~/.qp/alarina/` in the user's home directory, separated by the actual project, worktree, and task so two checkouts or initiatives cannot overwrite each other. A user or project storage convention overrides this default. Make the record's locator available to the user and next consumer; user-level storage is private working state, not a hidden substitute for a requested deliverable.

Create storage lazily. Identify the project from its canonical repository or common Git directory, and the actual checkout separately; a folder basename or branch name alone is not a unique identity. Keep those locators with the task so resumption and worktree handoff can find the right state. Before cleaning temporary output, move any evidence still needed by a continuing task or delivered claim to its appropriate retained destination and update consumers.

Persist only when resumption, review, or reuse needs it, within the owning command's authority. Keep the current candidate and workspace identity, decisive evidence locators, unresolved obligations, and next action in the existing task record; add other detail only when it changes a decision. Avoid a mandatory schema, registry, background process, or parallel status file.

Existing `.qp/` records remain valid inputs. Read and update an active record there when its ownership and links still work. Move selected records to a new destination only when ownership, dependencies, and consumers are known; preserve working links and provenance. Do not bulk-move or delete historical `.qp/` content merely because the default changed. Publication and deletion retain their own authority boundaries.
