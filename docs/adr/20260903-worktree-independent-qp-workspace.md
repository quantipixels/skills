# Store repository workspace state independently of Git worktrees

Status: Accepted

Repository-scoped state belongs to the Git repository's shared state, not to a privileged main worktree. Akọsílẹ̀ therefore uses `<git-common-dir>/qp` as the one physical canonical store and treats each worktree root `.qp` as a reconstructible alias when a worktree-relative view is useful.

This supersedes the canonical-storage topology and bare-repository limitation in `20260828-keep-akosile-scripts-focused.md`; that ADR's stable-subject and deterministic-kernel decisions remain active.

## Why

Git worktrees have private per-worktree administrative state and a shared common repository directory. Records, settings, and artifacts are intended to be shared across the repository's worktrees, so storing their physical home inside one worktree creates unnecessary asymmetry, makes worktree moves/removal more consequential, and rejects bare worktree-hub topologies without semantic reason.

The canonical store remains untracked repository-local state. Worktree aliases provide the familiar `.qp/...` view without making alias topology authoritative.

## Invariant

```text
<git-common-dir>/qp      one real repository store
<worktree>/.qp           derived symlink to the store
bare repository          store valid even without a worktree alias
```

Writers publish through the real canonical root. Aliases are repaired from current Git metadata and are not persisted as semantic state.

## Migration

Legacy physical `.qp` directories in any worktree are authoritative migration inputs until reconciled. Preflight all sources and the canonical destination before destructive mutation; freeze before movement; deduplicate byte-identical authoritative paths; preserve unique content; stop on divergent authoritative content; regenerate derived views; and remove backups only after identity/inventory proof.

Before freezing a live worktree path, establish a bounded quiescence window for workspace readers/writers that may access it. Keep them quiesced until copied authoritative content is verified and the `.qp` alias is restored. If quiescence cannot be established, block migration rather than expose an absent/partial path or permit another writer to recreate an unpreflighted physical store.

A pre-existing common-dir store participates in the same conflict rules; it never silently wins or loses merely because it is the destination.

## Bare repositories and alias capability

Bare repositories may own canonical state and serve as worktree hubs. A repository with no worktree has no `.qp` alias/relative locator. If a host cannot create symlinks, canonical storage remains usable while worktree-relative `.qp` access reports an alias capability gap; replicated physical stores are not created as fallback.

## Rejected alternatives

Do not keep the main worktree as canonical merely because it historically hosted `.qp`, duplicate one physical store per worktree, maintain a separate alias/worktree registry, or add a migration daemon for metadata Git already owns.

## Consequence

Akọsílẹ̀ becomes symmetrical across worktrees, survives worktree movement/removal more naturally, supports bare worktree hubs, and preserves its existing deterministic publication kernels without introducing another storage/runtime layer.