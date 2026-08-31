# Capability and resource placement

Use when authoring/revising a skill that may need references, commands, scripts, templates, data, assets, libraries, or another public owner.

## Choose the smallest adequate surface

Start from the owned outcome and separate material capabilities such as judgment, evidence retrieval, provider/project operation, deterministic transformation, mutation/concurrency, and artifact delivery.

Prefer, in order:

```text
SKILL.md guidance or selective expert reference
→ native/project/provider/framework/IDE capability
→ small operational anchor or short visible recipe when it materially improves discoverability
→ focused mature library/tool
→ narrow deterministic script
→ engine only when deterministic machinery carries a substantial part of the owned outcome
```

A capable agent already knows how to search, inspect files, operate Git/shell/filesystem tools, discover CLI help, edit, or adapt ordinary delegation to its host. State the semantic result/invariant; do not replace deleted runtimes with prose command catalogues or capability-fallback trees. Delegation is not ordinary when bounded independent/noisy work must be isolated to preserve the primary owner's context, focus, continuity, or independent observation; in that case the isolation requirement is behavior-bearing even though the host-specific subagent mechanics remain adaptable.

Concrete mechanics are justified when the mechanism itself protects correctness, authority, deterministic identity/output, concurrency/atomicity, non-obvious safety, an external/machine protocol, or compatibility. Exact-host provider binding, lock-held compare-and-swap, or a compiler interface can qualify; ordinary repository inspection usually does not.

Do not confuse abstraction with simplification. After a **concrete capability is selected**, keep a small operational anchor when removing every concrete entry point would force the agent to rediscover how to enter that same capability on each use. A useful anchor may include the authoritative documentation or discovery surface, the canonical interface/endpoint/protocol, and one representative invocation or discovery command.

Do not use an operational anchor to choose the capability in the first place or to freeze an open-ended discovery space. Lists of inspiration sites, candidate vendors, libraries, frameworks, hosts, products, or sources are not anchors merely because they are convenient starting points. For those spaces, keep durable selection criteria, query/discovery shape, and current evidence. A finite named set is appropriate only when that set is itself part of the owner's explicit compatibility or protocol boundary.

Keep anchors deliberately small: volatile versions, flags, quotas, inventories, installation matrices, and secondary examples remain current-tool evidence to revalidate at use time. The anchor should reduce recurring discovery cost without becoming a QP-owned manual.

## Preserve useful depth

Depth is not synonymous with executable code. A lightweight skill can be deep through curated expert judgment or a native/tool-backed capability.

Keep a selective reference when recurring non-obvious judgment materially improves the result. Prefer examples, counterexamples, triggers, exceptions, and decision criteria over generic advice or cached ecosystem facts.

Use current project/tool/provider/framework truth for volatile APIs, versions, component inventories, commands, and platform behavior. Existing project artifacts outrank bundled starters. An operational anchor may preserve a representative current invocation, but it must point back to authoritative current truth and explicitly leave volatile details open to revalidation.

## Executable boundary

Before keeping internal code, move ordinary discovery, routing, provider facts, Git/filesystem orchestration, destination selection, and installation/publication back to their natural owners. Prefer pure transforms or exact mutation kernels. If code still appears necessary, apply [script boundary](script-boundary.md).

An engine has a much higher bar than “several scripts”: deterministic machinery must carry a meaningful vertical of the skill's native outcome and remove material implementation/defect variance from the agent. Search wrappers, prompt/reference filtering, tiny graph/frontier calculations, generic rendering, provider normalization for the model, and wrappers around native commands are normally below that bar.

## Human-facing entrypoints

A thin public install/bootstrap/uninstall/helper wrapper can still be the smallest interface when one stable safe invocation materially improves recurring user UX. Keep it transparent, conservatively scoped, native-tool-backed, and free of a parallel semantic model or hidden durable state.

## Templates, data and assets

Bundle a template only when its recurring semantic shape is stable, omission/drift is costly, no project/native scaffold owns it, and starting from it is better than generating from the contract. Remove arbitrary defaults, optional-empty sections, workflow procedure, volatile commands, and duplicated skill content.

Bundle data only when maintained knowledge itself is part of the result. Do not duplicate the same rules in CSV/Markdown or cache volatile ecosystem inventories. Use [knowledge catalogues](knowledge-catalogues.md) for a genuine researched corpus.

Keep reusable CSS/HTML/JS assets only when exact shared behavior prevents recurring correctness/accessibility cost. Make optional behavior conditional unless the owner intentionally promises that human-facing representation/control as part of its native result; existence of an asset alone is never reason to include it everywhere.

## Public skill gate

Create or retain a public skill when it owns a recurring independently useful outcome, authority/artifact/lifecycle/acceptance boundary, failure mode, or useful named model-steering contract. Do not split skills merely because output taxonomy differs when one owner can carry the variants cleanly.

Do not remove a lightweight steering skill solely because the base model can perform the underlying behavior. The question is whether the named contract independently improves reliable selection/use without duplicating another owner.

## Placement test

For every material resource ask:

- What outcome does this resource uniquely improve?
- Is the information/mechanic already naturally owned by the agent, project, provider, framework, tool, or a mature library?
- Is this recurring non-obvious judgment, deliberate behavioral override, or merely recoverable procedure?
- Has the concrete capability already been selected, or is this resource quietly choosing/caching candidates for the agent?
- Would removing every concrete pointer make the agent repeatedly rediscover the same selected capability entry point? If so, what is the smallest operational anchor that prevents that?
- If prescribing a mechanism, what invariant, context-isolation need, human-visibility requirement, or external contract requires that exactness?
- If proposing code, what deterministic result cannot be carried as guidance/native tooling?
- If proposing an engine, what substantial portion of the native outcome moves behind it?
- What maintenance, freshness, portability, context, or runtime burden does the resource introduce?
- What proof would show the smaller alternative is insufficient?

Prefer the smallest placement that preserves correctness, judgment quality, authority, discoverability, useful depth, and deliberate behavior. Size reduction alone is not acceptance.
