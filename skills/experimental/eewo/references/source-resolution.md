# Source resolution

`eewo` combines four source classes while keeping their authority and storage separate.

## Storage scopes

Use `akosile` for both local scopes:

```text
repository: <git-worktree>/.qp/
personal:   ${QP_HOME:-$HOME/.qp}/
```

Repository scope is private generated state for one checkout/project. Personal scope is user-owned cross-project state and must be requested explicitly by `eewo` or the user; the mere existence of `$HOME/.qp` does not authorize reading or writing it.

Never copy records automatically between scopes. A rule can exist independently in both scopes when the user deliberately creates an overlay.

## Source classes

1. **Explicit/project contract** — current user instructions, repository instructions, tracked policy, exact task acceptance, and deterministic tool configuration.
2. **Repository-private patterns** — active `eewo` records in the repository `.qp` scope.
3. **Personal patterns** — active `eewo` records in the explicit personal scope.
4. **Published packs** — read-only patterns shipped with the installed `eewo` skill under `references/packs/`.

All applicable non-conflicting constraints are additive. The ordering is used to resolve authority, not to discard lower sources mechanically.

A lower source may add a stricter rule when it does not contradict a higher contract. It may not silently weaken a higher constraint. A repository-private rule may narrow or supersede a generic published rule only when its evidence and authority establish that project-specific boundary. A personal preference never overrides an explicit repository or user contract.

On a material conflict, stop guard-pack generation for the conflicting rule family and report the smallest decision or evidence required.

## Applicability

Filter before loading full rule bodies. Use available evidence for:

- language;
- framework/runtime;
- version;
- repository identity;
- changed path;
- task/change type; and
- lifecycle phase.

Unknown applicability is not permission to load an entire catalogue. Include a broad rule only when its own scope is intentionally broad.

## Pack identity

A guard pack identifies every input rule by source scope plus semantic id and exact revision/version. When the host can calculate a stable digest, include it. Re-resolve the pack when the implementation candidate, applicability evidence, or source rule revision changes.

Once work begins against a pinned pack, observations discovered during that work belong to a future pack unless the user explicitly reopens the governing candidate.

## Privacy

Personal and repository `.qp` records are local state. Do not stage, publish, attach, or quote private evidence outside its authorized boundary merely because a portable rule is being contributed. Contribution uses the sanitized snapshot contract from `pattern-contract.md`.
