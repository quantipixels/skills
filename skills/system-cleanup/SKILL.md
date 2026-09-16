---
name: system-cleanup
description: Reclaim disk space on macOS by auditing APFS usage, clearing build artifacts and package-manager caches, reviewing stale Git worktrees, and offloading large keepers to an external drive. Use for low storage, a full disk, “out of space” errors, large System Data, and cleanup or offload requests; exclude performance tuning, malware removal, and unapproved deletion of personal or application data.
disable-model-invocation: true
---

# System cleanup

Measure physical free space on the macOS Data volume with `df -h /System/Volumes/Data`; Finder categories, `du`, logical sizes and cleanup estimates are supporting evidence. Inspect mounted volumes and APFS snapshots only when they can explain the result. Scan targeted filesystem boundaries from largest relevant areas inward rather than crawling the whole home directory.

A general cleanup request authorizes exact, inactive, regenerable build artifacts and package/language caches within scope. Prefer each tool's current native cleanup/prune command, confirmed from its installed interface or official docs. Check live processes and open handles first. GUI application data, ambiguous state, personal files, apps, projects, backups, model weights, Docker volumes, VMs, emulator snapshots, SDKs, runtimes and toolchains need explicit selection and risk acceptance.

Use Trash when available and ask once before emptying it; permanent deletion needs confirmation. Never weaken permissions/SIP, kill unrelated processes or delete protected system paths. Application-native cleanup may remove clearly disposable generated state, but preserve durable volumes, images, compatibility runtimes and user-created state.

Clear one safe category at a time and remeasure the Data volume after large batches. APFS clones/shared blocks, sparse images, live handles and Trash can make logical removal differ from physical gain.

For selected Git worktrees, inspect dirty state, unique commits, upstream divergence and untracked files. Preserve anything dirty, unique, unpushed or unreconciled. Batch clean, fully merged/pushed worktrees for confirmation, then use non-forcing Git removal and branch deletion.

For an authorized offload, verify a distinct mounted destination with capacity, copy by a metadata-preserving host method, and verify counts/sizes plus checksums for irreplaceable data. Tool success does not prove every metadata type survived. Trash the source only after verification; create a narrow symlink only when appropriate and state that it fails while the drive is unmounted.

Report initial/current Data-volume free space, measured physical gain, categories cleared, Trash awaiting approval, preserved candidates, failures and optional next actions. After approved Trash emptying, remeasure final gain. Stop when authorized safe candidates are exhausted.
