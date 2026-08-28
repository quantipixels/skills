# Root-cause probe commands

Use only when a command produces an observation that discriminates between explicit competing hypotheses. Prefer read-only evidence; do not mutate production merely to create a test.

## Historical/source discrimination

```bash
git log -S'<suspected condition/literal>' --all -- <paths>
git log -G'<pattern>' -p -- <paths>
git diff <known-good>..<known-bad> -- <suspected-paths>
git show <candidate-sha> -- <paths>
```

Use these to locate changes correlated with a behavior boundary; correlation/temporal order is not causation. The probe is useful only when a predicted difference supports or falsifies a mechanism.

## Deterministic revision search

When the failure is safely/reliably executable and repository history plausibly contains a good→bad transition, use Git's native bisect only in a disposable/isolated worktree. Pin the exact reproduction command and environmental assumptions, avoid real external effects/credentials, and clean up the disposable worktree afterwards.

Do not use bisect when builds/tests are nondeterministic, history cannot reproduce the environment, or each run has consequential external effects.

## Probe discipline

For every command/probe record:

```text
Hypothesis:
Predicted observation if true:
Predicted observation if false:
Command / bounded scope:
Observed result:
What it rules in/out:
Coverage/limitations:
```

A command is not progress unless its result can change the causal model.
