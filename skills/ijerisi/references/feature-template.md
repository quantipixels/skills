# Feature recipe template

Use this shape for a new map entry, or preserve an equivalent established format. Replace the fields with project facts; the generated file must not contain placeholders. The title describes the user's goal, not an internal module.

```markdown
# <Feature title>

<What the user can accomplish and the observable outcome.>

## Sub-features

- <Stable journey ID>: <behavior and expected result>.

## How a user reaches it

- <Entry-point ID>: <menu, route, shortcut, public command or API operation>.
- <Other supported entry point and its distinct prerequisites>.

## How to drive it

Prerequisites: <fixture state, identity/access, instance readiness and reset requirements>.

For each listed entry point and sub-feature:

1. <Exact public action or driver command using a stable handle>.
2. <Next action and observable result, including when the operation is complete>.
3. <Independent observation of material persisted or external effects>.
4. <Evidence to retain, its destination, and the path ID recorded with it>.
5. <Owned fixture reset needed before the next journey>.

Coverage: <executed paths with actual evidence pointers, plus unexecuted, blocked or failing paths and their reasons>.

## Gotchas

- <A project-specific condition that changes reachability or invalidates proof>.
- <A recovery action that restores an owned baseline without deleting evidence>.
```

A path is not covered because another path reaches the same screen. Keep entry-point and sub-feature identities distinct enough to report which combinations ran. An inaccessible prerequisite needs the attempted operation and missing condition, not a passing label. Expected failures and empty states can be valid journeys when the accepted contract requires them.

The `features/README.md` names the intended surface/build, shared prerequisites, baseline/reset procedure, driver conventions and evidence root, then links each feature entry once. Put shared setup there and feature-specific setup in the entry. Record executable evidence only after running it; source-backed recipes can be useful while still unverified. Update coverage when the build or recipe changes so an old receipt does not imply current proof.
