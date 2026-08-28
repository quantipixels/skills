# Git reconstruction for agent-session retrospectives

Use only when repository history/reflog materially helps reconstruct what happened during the analyzed session/corpus. Current history cannot prove hidden reasoning or content the agent never observed.

```bash
# Local ref/worktree movement where available
git reflog --all --date=iso

# Commit timeline
git log --all --decorate --date=iso \
  --format='%H%x09%ad%x09%d%x09%s'

# One commit/result surface
git show --stat --summary <sha>

# Exact before/after candidate delta
git diff <before>..<after> -- <bounded-paths>

# Current unfinished state when the session ended there
git status --porcelain=v2
```

Correlate Git events with supplied transcripts/tool results/timestamps; do not infer one from the other. Reflog may be unavailable, rewritten, expired, or local to a different clone. State those coverage limits.

Use exact candidate identities from session evidence whenever available; do not substitute today's repository state for what the agent saw then.
