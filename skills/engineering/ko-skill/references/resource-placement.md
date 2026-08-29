# Capability and resource placement

Use this during ordinary skill authoring or revision whenever the outcome may need commands, references, scripts, templates, data, reusable assets, or another public skill. Portfolio audit reuses the same model; it is not the primary owner of this method.

## Start from the owned outcome

Decompose the result into material capabilities before choosing files:

```text
judgment / calibration
discovery / evidence retrieval
project or provider operations
deterministic transformation / validation
mutation / concurrency
generated artifact / delivery
```

For each capability, choose the first adequate placement:

```text
SKILL.md guidance or selectively loaded expert reference
→ literal native command or short visible recipe
→ current repository / project / provider / framework / IDE tool
→ focused mature library
→ narrow deterministic script kernel
→ engine only when deterministic machinery carries a substantial part of the owned outcome
```

A short command recipe is guidance, not a runtime capability. Prefer it when a capable agent can see, adapt, and verify the operation from current evidence without persistent machine state or a separate machine consumer.

### Assume agent competence

Specify the semantic capability, invariant, authority, or result the skill needs; let the agent map ordinary execution onto the tools and capabilities actually available in its host. Do not enumerate harness-specific fallbacks for subagents, shell/file operations, search, editing, or equivalent orchestration when a capable agent can derive the available path itself.

Concrete mechanics earn instruction space when the mechanism itself establishes a correctness invariant, authority boundary, deterministic result, non-obvious safety property, machine-consumer contract, or compatibility constraint. Capability absence is normally an execution fact for the agent to adapt around, not a branch the skill must pre-author.

Do not apply that rule mechanically to **public human-facing entrypoints**. A thin install/bootstrap/uninstall/helper wrapper can be the smallest adequate interface when its value is one safe, memorable invocation for a recurring operation that would otherwise require users to copy or reconstruct several commands. Keep such an entrypoint transparent and narrow: delegate to native tools, preserve safe scope/defaults, avoid private semantic state, and do not grow it into an internal runtime. `scripts/uninstall.sh` is a valid example: `npx skills` owns removal; the wrapper owns source-scoped one-line UX.

Do not treat “the model can already do this” as sufficient reason to remove a lightweight skill. A small public skill can still be valuable when its independently useful trigger/result reliably steers model behavior and saves users from repeating a long behavioral instruction. `salaye` is a valid example: its value is the reusable plain-language explanation contract, not hidden machinery. Keep this form only when the route is clear and it does not duplicate another published owner.

## Challenge proposed executable code

Before keeping an internal capability script, attempt to move these responsibilities back to their natural owner:

- project/tool/version discovery → manifests, wrappers, config, `--help`, or the agent;
- semantic routing/recommendation/readiness/acceptance → the skill;
- provider facts → `gh`, `glab`, connector, or provider API;
- ordinary Git/filesystem orchestration → native commands;
- output destination and installation → caller/mutation owner;
- generic formatting/envelopes → stdout/native structured output.

Prefer pure transforms such as `input → stdout` or `input → deterministic artifact`. A retained skill-runtime script must still pass [script boundary](script-boundary.md). Evaluate thin human-facing distribution/entrypoint wrappers separately for invocation leverage, safe scoping, portability, and transparency.

## Command affordances

Put one command in `SKILL.md` when it is short, stable, nearly universal to normal execution, and materially clarifies the evidence/ownership boundary. Put a small command palette in a reference when it is provider-, evidence-, tool-, or mode-specific.

Do not preserve language/framework/tool command catalogues. Prefer project wrappers and current `--help`/owning documentation for volatile CLI details.

## Template gate

A bundled template is justified only when all are true:

- the artifact recurs;
- its semantic shape is stable;
- omission or shape drift is materially costly;
- no existing project/native scaffold already owns it; and
- starting from the scaffold is better than generating the artifact from the semantic contract.

Keep only universally useful structure. Do not encode arbitrary colors/fonts/scales, example values as defaults, workflow procedure, implementation boilerplate, volatile commands, duplicated skill/reference content, or optional sections that are usually empty.

Good: a compact durable plan record or architecture record whose stable headings support resume/reconciliation.

Bad: a complete HTML implementation, an opinionated design-system starter, or a framework scaffold that the agent must undo for most real projects.

Existing project artifacts outrank bundled starters.

## Data and catalogue gate

Bundle data only when the maintained knowledge itself is part of the independently useful result. Do not duplicate the same rules in CSV and Markdown merely to make them searchable. Do not cache volatile ecosystem inventories—framework APIs, component catalogues, font catalogues, package lists, platform dimensions—when current project/tool/primary-source discovery is the natural owner.

For genuine researched knowledge catalogues, apply [knowledge catalogues](knowledge-catalogues.md). Prefer curated recurring judgment with triggers, exceptions, counterexamples, and freshness boundaries over style/industry keyword lists.

## Reusable asset gate

A reusable CSS/HTML/JS asset is justified when exact behavior is useful across many outputs and reimplementing it repeatedly creates real correctness/accessibility risk. Keep universal resilience separate from optional behavior.

Examples:

- universal accessibility/overflow foundation → reasonable shared asset;
- theme toggle → include only when explicit theme switching is useful;
- report deep-link/print disclosure control → include only for reports that use those behaviors;
- carousel control → branch-specific to visual collections.

Do not make a support asset mandatory merely because it exists.

## Public skill gate

Create or retain a public skill when it owns a recurring independently useful outcome, authority boundary, artifact, lifecycle, acceptance boundary, or useful model-steering contract. Do not split public skills only because output taxonomy differs if one mechanism/outcome can own the variants cleanly.

When consolidation is plausible, compare the same realistic hidden-answer goals before and after. Preserve the smaller public surface only when selection, result quality, authority, proof, and installability remain clear.

## Authoring-time recommendation contract

When Kọ Skill sees:

- recurring non-obvious judgment → recommend a selective expert reference with examples/counterexamples;
- one/few transparent native operations → recommend commands/recipes;
- an instruction enumerating host capability fallbacks the agent can infer itself → collapse it to the semantic requirement;
- a recurring human-facing multi-command setup/removal action where one safe invocation materially improves use → consider a thin public entrypoint that delegates to native tools;
- truth already owned by project/provider/framework tooling → use that native owner;
- focused solved mechanics → use a library;
- exact-byte identity, race, compiler, validator, or machine-consumer seam → consider a narrow deterministic script;
- several deterministic mechanics carrying a substantial native vertical → consider an engine at a much higher proof/maintenance bar;
- default-heavy templates, duplicate data/reference representations, or support assets used everywhere without need → shrink/remove/make conditional before finalizing the skill.

Size reduction is evidence, never the acceptance target.
