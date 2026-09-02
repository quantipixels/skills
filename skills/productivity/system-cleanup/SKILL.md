---
name: system-cleanup
description: Reclaim disk space on macOS by auditing APFS usage, clearing build artifacts and package-manager caches, reviewing stale Git worktrees, and offloading large keepers to an external drive. Use for low storage, a full disk, “out of space” errors, large System Data, and cleanup or offload requests; exclude performance tuning, malware removal, and unapproved deletion of personal or application data.
---

# System cleanup

Audit the disk, clear what is safely regenerable, and confirm before touching anything else.

## Ground rules

- Measure physical free space on the macOS Data volume with `df -h /System/Volumes/Data`; plain `df /`, `du`, Finder categories, and cleaner estimates are supporting evidence rather than the result.
- Prefer a tool's current native cleanup command over deleting its directories. Confirm the installed interface with its own help/current documentation and use a dry run when available; do not preserve a package-manager command catalogue here.
- For direct deletion, use `trash` when available. Accumulate items in Trash and ask once before emptying it. If `trash` is unavailable, obtain confirmation before permanent deletion.
- A general cleanup request authorizes only exact, inactive, regenerable build artifacts and package/language caches.
- Do not clear GUI application data automatically. Report application cache/support-directory sizes unless the user names the app and accepts the risk to logins, cookies, history, or local state.
- Ask before removing personal files, media, applications, projects, backups, model weights, Docker volumes, virtual machines, emulator snapshots, SDKs, runtimes, or toolchains.
- Never bypass SIP, weaken permissions, kill unrelated processes, or delete protected system paths to satisfy a cleanup estimate.

## Workflow

### 1. Assess

Measure the Data volume and inspect mounted volumes. Record initial free space and any external drive. Inspect APFS volumes/snapshots only when their accounting can materially explain the result.

### 2. Survey

Use targeted, filesystem-bounded size scans instead of crawling all of `~`. Check the largest relevant boundary first, then inspect exact candidates. Common classes include:

- inactive build artifacts and dependency/build output in current or linked worktrees;
- package/language caches for installed development tools;
- stale worktrees and their duplicated generated output;
- large media/downloads; and
- large application caches/support directories, for reporting only unless separately authorized.

Check live processes and open handles before touching large temporary directories, worktrees, caches, virtual machines, or current build output. Treat ambiguous data as durable.

### 3. Clear the safe tier

Clear inactive regenerable build artifacts and package/language caches without asking again. For each selected tool, discover and use its current cleanup/prune command from the installed interface/current official documentation rather than deleting internal cache layouts by assumption.

Use application-native cleanup for disposable Docker/Xcode/simulator or equivalent generated state when the active tool clearly owns safe reclamation. Preserve data volumes, compatibility runtimes, user-created images/state, and similar durable assets unless separately authorized.

Run one category at a time and recheck Data-volume free space after each large batch. APFS clones, shared assets, sparse images, and Trash can make logical estimates differ from physical recovery.

### 4. Audit Git worktrees

For every worktree, establish whether it is dirty, has unique commits, is ahead of its upstream, or contains untracked files. Keep and report anything dirty, unique, or unpushed.

Present clean worktrees whose commits are fully merged and pushed as one confirmation batch. After approval, use Git's normal worktree removal and non-forcing branch deletion; never force-delete a branch merely for cleanup.

### 5. Offload keepers

When the user chooses an external-drive offload, confirm the destination is a distinct mounted volume with enough free space. Copy each selected folder with a metadata-preserving method supported by the host; any particular copy tool is an entry point, not proof that every macOS metadata type was preserved.

Verify file counts and sizes; use checksums when the data is irreplaceable. Trash the original only after verification, then create a symlink at its old path when that redirection is appropriate. Symlink individual folders, not broad special directories. Warn that the path will be unavailable while the external drive is unmounted.

### 6. Wrap up

Report initial and current free space, immediate physical gain, items waiting in Trash, cleaned categories, preserved items, failures, and optional next candidates with sizes/trade-offs.

Ask the user to empty Trash when needed. After they approve and Trash is empty, remeasure the Data volume and report final physical gain. Stop after exhausting the authorized safe candidates; report anything that needs separate approval.
