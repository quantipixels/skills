# Read-only simplification evidence commands

Use only inside Parẹ́'s read-only authority. Commands are investigation evidence, never deletion proof by themselves.

```bash
# Current textual/symbol consumers
git grep -n '<symbol-or-concept>' -- <bounded-paths>

# Candidate surface against upstream
base=$(git merge-base HEAD <upstream>)
git diff --name-status "$base"...HEAD

# Exact-string history
git log -S'<symbol-or-literal>' --all -- <paths>

# Structural/pattern history
git log -G'<pattern>' -p -- <paths>

# File lifetime/renames
git log --follow -- <path>

# Tracked inventory
git ls-files -- <bounded-paths>
```

Use current consumers plus history to challenge dead-code claims. Search absence does not prove deletion safety when reflection, generated code, framework registration, external consumers, data/config references, or platform conventions may own reachability.

Use project-native dependency/task/static-analysis tools when they materially improve evidence; route companion-tool use through `irinse` when its bounded result is needed. Parẹ́ retains the simplification judgment.
