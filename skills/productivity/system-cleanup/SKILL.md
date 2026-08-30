---
name: system-cleanup
description: Reclaim disk space on macOS by auditing APFS usage, clearing build artifacts and package-manager caches, reviewing stale Git worktrees, and offloading large keepers to an external drive. Use for low storage, a full disk, “out of space” errors, large System Data, and cleanup or offload requests; exclude performance tuning, malware removal, and unapproved deletion of personal or application data.
---

# System cleanup

Audit the disk, clear what is safely regenerable, and confirm before touching anything else.

## Ground rules

- Measure with `df -h /System/Volumes/Data`, not plain `df /`. Treat `du`, Finder categories, and cleaner estimates as leads; the Data volume’s physical free-space change is the result.
- Prefer a tool’s cleanup command over deleting its directories. Check the installed command’s help and use its dry run when available.
- For direct deletion, use `trash` when available. Accumulate items in Trash and ask once before emptying it. If `trash` is unavailable, obtain confirmation before permanent deletion.
- A general cleanup request authorizes only exact, inactive, regenerable build artifacts and package or language caches.
- Do not clear GUI application data automatically. Report `~/Library/Caches/<App>` and `~/Library/Application Support/<App>` sizes unless the user names the app and accepts the risk to logins, cookies, history, or local state.
- Ask before removing personal files, media, applications, projects, backups, model weights, Docker volumes, virtual machines, emulator snapshots, SDKs, runtimes, or toolchains.
- Never bypass SIP, weaken permissions, kill unrelated processes, or delete protected system paths to satisfy a cleanup estimate.

## Workflow

### 1. Assess

Run `df -h /System/Volumes/Data` and inspect `/Volumes`. Record initial free space and any mounted external drive. Inspect APFS volumes or snapshots only when their accounting matters.

### 2. Survey

Use targeted, filesystem-bounded `du` scans instead of crawling all of `~`. Check the largest boundary first, then inspect exact candidates. Common targets are:

- build artifacts such as Rust `target/`, `node_modules/`, Gradle output, Xcode DerivedData, and artifacts in linked worktrees;
- package and language caches for Homebrew, Go, pnpm, npm, pip, Cargo, and similar tools;
- stale worktrees and their duplicated build output;
- large media in editing apps, `~/Movies`, and `~/Downloads`; and
- large application caches or support directories, for reporting only.

Check live processes and open handles before touching large temporary directories, worktrees, caches, virtual machines, or current build output. Treat ambiguous data as durable.

### 3. Clear the safe tier

Clear inactive build artifacts and package or language caches without asking again. Prefer current native operations such as `go clean -cache`, `brew cleanup --prune=all`, `pnpm store prune`, `npm cache clean --force`, and `cargo clean`.

Use application-native cleanup for unused Docker images or build cache, Xcode shared caches, and unavailable simulator devices. Preserve Docker volumes and compatibility runtimes unless separately authorized.

Run one category at a time and recheck Data-volume free space after each large batch. APFS clones, shared assets, sparse images, and Trash can make logical estimates differ from physical recovery.

### 4. Audit Git worktrees

For every worktree, establish whether it is dirty, has unique commits, is ahead of its upstream, or contains untracked files. Keep and report anything dirty, unique, or unpushed.

Present clean worktrees whose commits are fully merged and pushed as one confirmation batch. After approval, use `git worktree remove` and then `git branch -d`; never use `git branch -D` for cleanup.

### 5. Offload keepers

When the user chooses an external-drive offload, confirm the destination is a distinct mounted volume with enough free space. Copy each selected folder with a metadata-preserving method supported by the host. `rsync -a` is a starting point, not proof that every macOS metadata type was preserved.

Verify file counts and sizes; use checksums when the data is irreplaceable. Trash the original only after verification, then create a symlink at its old path. Symlink individual folders, not special directories such as `~/Movies`. Warn that the path will be unavailable while the external drive is unmounted.

### 6. Wrap up

Report initial and current free space, immediate physical gain, items waiting in Trash, cleaned categories, preserved items, failures, and optional next candidates with sizes and trade-offs.

Ask the user to empty Trash. After they approve and Trash is empty, re-run `df -h /System/Volumes/Data` and report the final physical gain. Stop after exhausting the authorized safe candidates; report anything that needs separate approval.
