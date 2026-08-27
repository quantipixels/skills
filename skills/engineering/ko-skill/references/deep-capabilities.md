# Deep capability modules

Use this pattern only when a skill can hide a substantial, outcome-level deterministic capability behind a small semantic interface. The lesson is not “put more scripts in skills”; it is “raise the machine boundary high enough that the skill stops rebuilding a whole class of work.”

## Classify two independent dimensions

```text
Control shape:    lightweight | workflow
Capability shape: native | reference-backed | engine-backed | tool-backed
```

Control shape describes lifecycle/orchestration. Capability shape describes where execution depth comes from. A lightweight skill may be engine-backed, but implementation depth is not valuable by itself.

- `native` — host/model/repository capabilities already express the result adequately.
- `reference-backed` — the depth is semantic guidance loaded just in time.
- `tool-backed` — an existing project/provider/ecosystem tool owns the mechanics.
- `engine-backed` — the skill owns a substantial deterministic vertical that produces a useful domain result, not merely helper metadata.

## Apply the natural-owner veto first

Before adding executable code, identify who already owns the fact or transformation:

```text
readable repository/source/config truth
→ language/compiler/build/package/framework/provider capability
→ existing project/IDE/tool capability
→ focused mature library/tool
→ only then consider QP-owned executable code
```

Repetition is not ownership. Do not reimplement dependency resolution, effective build configuration, package graphs, compiler/runtime reporting, Git/provider state, browser truth, static-analysis metrics, or other mechanics their natural tools already expose.

Do not replace custom code with a permanent command catalogue in prose. Discover the current project/tool command from wrappers, help/task output, current official documentation, or `irinse` when selecting/configuring/operating the tool is itself material.

## Prefer instructions before a helper script

Use instructions/reference guidance when the operation is small, transparent, local to one reasoning step, and can be performed reliably from current evidence without persistent state or a standalone machine consumer.

Typical instruction-owned work includes:

- applying a short decision/frontier checklist;
- checking a handful of plan lifecycle invariants;
- selecting the relevant existing reference from an already-known stack;
- composing ordinary HTML directly when no domain renderer owns the representation;
- reading source/provider state and comparing a few explicit fields.

Do not create executable code merely to make these checks feel more deterministic. A script adds runtime, portability, maintenance, tests, schemas, and another failure surface.

## Require an outcome-level boundary for an engine

A deep engine should remove an entire class of repeated implementation from the agent. State its contract at the level of a useful domain outcome, for example:

> Given a valid domain specification, produce a complete validated artifact/workbench with domain diagnostics, delivery proof, and reader utility.

A candidate is **below the deep-module bar** when its main result is only:

- a search/filter over prompt/reference content;
- a small graph/frontier calculation;
- frontmatter/heading validation;
- generic card/table/section rendering;
- normalization that exists only to feed another model step;
- a thin wrapper around one native command/tool.

Those may still be legitimate tiny scripts in exceptional cases, but they are not deep capability modules and should default to instructions or native/tool composition.

## Gates for a justified engine

Require all of these:

1. **Natural owner** — existing repository/native/provider/tool capability does not already own the result.
2. **Outcome owner** — one skill genuinely owns the complete vertical.
3. **High boundary** — the machine result is independently useful, not merely helper metadata for another reasoning step.
4. **Substantial mechanics** — the engine hides enough recurring implementation to materially reduce model work, variance, or defects.
5. **Domain model** — inputs express domain meaning rather than generic presentation widgets or tool arguments.
6. **Quality model** — the capability has domain-specific validation/diagnostics, not only syntax/schema checks.
7. **Delivery/use** — the result can be consumed after generation: artifact, workbench, exact transformation, or durable machine product.
8. **Proof** — deterministic tests cover credible success/failure boundaries; visual/runtime proof stays with the natural browser/tool owner where applicable.
9. **Fallback** — unsupported environments degrade explicitly without silently changing semantics.

## Authoring loop for a real deep capability

A mature vertical will often expose some bounded equivalent of:

```text
guide → author semantic model → validate → diagnose/repair → compare/inspect → deliver → verify
```

Do not add commands just to match this shape. Each operation must earn its place from the domain capability.

## Script disposition

When reviewing executable code, choose one:

- `KEEP` — small deterministic seam is necessary, correctly owned, and proportionately proved.
- `SHRINK` — valid seam, avoidable implementation remains.
- `REPLACE_WITH_INSTRUCTIONS` — the model can perform the transparent operation directly from explicit evidence; executable leverage is too low.
- `REPLACE_WITH_NATIVE` — repository/provider/ecosystem capability already owns it.
- `REPLACE_WITH_LIBRARY` — a focused mature dependency removes substantial custom mechanics.
- `MOVE_TO_OWNER` — the operation belongs to another skill/tool owner.
- `PROMOTE_TO_ENGINE` — several justified QP-owned mechanics form one complete high-boundary domain vertical.
- `REMOVE` — no useful distinct capability remains.
- `NEEDS_EVIDENCE` — ownership, leverage, portability, or proof is not established.

The default should remain the smallest boundary that preserves correctness: instruction first, native/tool second, small script when truly necessary, and a deep engine only when the outcome-level vertical earns it.
