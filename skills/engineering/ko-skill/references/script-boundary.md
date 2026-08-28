# Bundled script boundary

Use this whenever a skill proposes, keeps, expands, moves, or replaces executable code. A script is not justified merely because it is useful, tested, short, or deterministic.

## Natural-owner veto first

Before code, ask whether the skill's owner can perform the result directly and reliably from explicit current evidence with concise guidance, a visible command/recipe, an existing project/provider/tool capability, or one focused library.

Use this order for **skill-runtime capability**:

```text
short owner guidance or deep reference
→ literal native command / short recipe
→ readable repository/source/config truth
→ native language/compiler/build/framework capability
→ existing project/provider/IDE/tool capability
→ focused mature library
→ narrow QP script
→ QP engine only when the outcome boundary is genuinely high
```

A visible command recipe is guidance. Do not package it merely to avoid writing the command in Markdown.

### Public entrypoint exception

Do not confuse an internal runtime with a thin human-facing distribution/convenience entrypoint. A public install/bootstrap/uninstall/helper script may be justified even when its internals are ordinary native commands when the **invocation leverage is itself useful**: one stable safe command replaces a fiddly or error-prone multi-command sequence for users.

Such an entrypoint must stay thin:

- native/project tooling still owns the underlying operation;
- scope and defaults are conservative and explicit;
- no parallel semantic model or hidden durable state;
- portability and failure behavior are proportionate to the advertised invocation;
- the wrapper remains understandable enough to audit as an entrypoint, not a private engine.

Example: a source-aware `uninstall.sh` that identifies this repository's globally installed skills and delegates removal to `npx skills` is a valid convenience surface even though the same mechanics can be written as a longer shell recipe.

## Retention gates

A skill-runtime bundled script survives only when all applicable gates pass:

1. **Natural owner** — QP code, rather than the agent/native/project/tool owner, is the smallest credible surface.
2. **Owner** — the owning skill genuinely owns the mechanical result.
3. **Need** — a demonstrated recurrence, correctness, race, portability, machine-consumer, or transformation need exists.
4. **Mechanical boundary** — state the complete operation as `Given X, deterministically produce Y`.
5. **Narrowness** — semantic judgment, routing, acceptance, architecture, recommendation, recovery choice, and authorization remain outside the script.
6. **Leverage** — packaging materially improves correctness/reuse beyond an equivalent visible command/recipe.
7. **State discipline** — persistent state, locks, retries, schemas, or daemons exist only for an observed cross-process need.
8. **Truth boundary** — repository/provider/runtime truth remains authoritative; the script does not maintain a parallel semantic model.
9. **Output** — the next consumer needs the machine result the script actually produces.
10. **Proof** — deterministic tests falsify the exact retained seam.

Line count is never an acceptance rule. Existing tests do not justify retaining obsolete runtime behavior.

## Mandatory compression pass

For every skill-runtime script that passes the first gate, attempt to strip responsibilities that can move back to natural owners:

- discovery/version detection → manifests, wrappers, config, `--help`, agent;
- domain or provider routing → semantic owner;
- provider querying → `gh`, `glab`, connector/API;
- ordinary Git/filesystem operations → native commands;
- output destination/temp-file selection → caller;
- installation/publication → mutation owner;
- generic formatting/result envelopes → stdout/native structured output.

Prefer pure transforms (`input → stdout` or `input → deterministic artifact`) and exact mutation kernels over workflow-shaped CLIs.

Examples:

- custom CSV BM25 wrapper whose rows still require model judgment → `REPLACE_WITH_NATIVE` using direct source selection plus `rg`/`grep`;
- PR provider normalizer that mostly calls `gh`/`glab` and reshapes facts for the model → `REPLACE_WITH_NATIVE` when the skill can reason over provider JSON directly;
- Git candidate fingerprint reconstructed in Python → `REPLACE_WITH_NATIVE` when a temporary index + `git write-tree` provides the exact content-addressed identity;
- validated candidate bytes published iff exact target identity still matches → `KEEP`; the race/atomicity guarantee is a real deterministic seam;
- token graph validation + canonical CSS realization → `KEEP`/`SHRINK`; compiler semantics are the result;
- generic migration workflow over `git worktree`, symlink, copy and compare → guidance/native commands unless an observed transaction guarantee cannot be expressed safely;
- one-line public uninstall wrapper over source lookup + `npx skills remove` → `KEEP ENTRYPOINT` when it materially improves user ergonomics without becoming a runtime abstraction.

## Dispositions

For skill-runtime executable capability, return one:

```text
KEEP
SHRINK
REPLACE_WITH_GUIDANCE
REPLACE_WITH_NATIVE
REPLACE_WITH_LIBRARY
MOVE_TO_OWNER
PROMOTE_TO_ENGINE
REMOVE
NEEDS_EVIDENCE
```

For a repository-level human-facing wrapper, report `KEEP ENTRYPOINT | SHRINK ENTRYPOINT | REPLACE_WITH_COMMAND | REMOVE | NEEDS_EVIDENCE` separately so the runtime deterministic-kernel bar is not misapplied to distribution UX.

For `KEEP`/`SHRINK`, state the exact retained deterministic kernel and which responsibilities were removed. For `REPLACE_WITH_NATIVE`, provide the stable command/recipe when useful or name the native discovery mechanism (`<wrapper> --help`, project task list, provider CLI/API) when exact flags are volatile.
