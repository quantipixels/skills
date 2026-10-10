#!/bin/sh
# Opt in explicitly: sh scripts/install-hooks.sh. Nothing calls this automatically.
set -eu
root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$root"
current=$(git config --get core.hooksPath || :)
if [ -n "$current" ] && [ "$current" != "scripts/hooks" ]; then
    echo "hooks: core.hooksPath is already set to $current; leaving it unchanged." >&2
    exit 1
fi
git config --local core.hooksPath scripts/hooks
echo "hooks: enabled staged skill validation via scripts/hooks/pre-commit (shared by this repo's worktrees)."
