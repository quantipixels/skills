# Project-knowledge history evidence

Use when current code/docs disagree, terminology provenance matters, or a durable learning/ADR/non-goal may reflect historical intent rather than current behavior.

```bash
# Current occurrences
rg -n '<term-or-invariant>' <bounded-paths>

# When an exact term/value appeared or disappeared
git log -S'<exact term>' --all -- <paths>

# Commits whose diff matches old/new vocabulary or a structural pattern
git log -G'<old-term|new-term|pattern>' -p -- <paths>

# Current-line provenance
git blame -L <start>,<end> -- <file>

# Exact historical artifact
git show <commit>:<path>
```

History proves what changed and when, not automatically why or which semantic intent should control. Treat commit messages/old docs as evidence. Current code proves current behavior; confirmed domain decisions/ADRs/user authority control intended meaning where they conflict.

Use the smallest history slice that can resolve the knowledge conflict. Do not mine unrelated history merely to accumulate context.
