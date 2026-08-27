# Bundled-script boundary

Read this reference when a skill adds, keeps, expands, moves, replaces, or consolidates executable code. The skill owns judgment/workflow. Executable code must earn its maintenance/runtime cost; repetition alone is not enough.

## 1. Apply the natural-owner veto

Before writing code, ask:

> Who naturally owns this fact, query, transformation, validation, or rendering mechanic today?

Check in order:

1. readable repository/source/config state;
2. host/native language/compiler/build/package/framework capability;
3. provider/project/IDE/tooling already present;
4. one focused mature library/tool;
5. only then a residual QP-owned executable seam.

Use `REPLACE_WITH_NATIVE` when the ecosystem already exposes the necessary truth. Do not build a QP parser around Maven/Gradle/Mix/package-manager/project-model facts, and do not move the same duplication into a static command catalogue.

## 2. Ask whether instructions are enough

Before a script, test the instruction-only shape:

> Can the owner perform this operation directly and reliably from explicit current evidence, with a short transparent rule/checklist, no persistent state, and no independent machine consumer?

If yes, prefer instructions/reference guidance.

Typical `REPLACE_WITH_INSTRUCTIONS` candidates:

- a small frontier/dependency checklist;
- a few lifecycle/status consistency checks;
- selecting one applicable reference from an already-established context;
- comparing explicit record/projection fields;
- ordinary HTML composition where the model still owns nearly all useful structure;
- thin normalization whose only consumer is the next model reasoning step.

Do not retain code merely because tests now exist for it. Delete obsolete tests with obsolete executable behavior.

## 3. Require one mechanical contract for a small script

For residual executable code, state:

> Given X, deterministically produce Y.

A small script may parse/normalize an owned structured input, validate explicit mechanical invariants, fingerprint an exact supplied candidate, calculate a non-trivial deterministic result, or transform one owned representation into another.

Reject it when the sentence requires semantic judgment, routing, authorization inference, readiness/acceptance, lifecycle ownership, or another skill's workflow.

A small script is justified only when code is materially safer/cheaper than repeating the operation as instructions—for example because edge cases are numerous, exact reproducibility is externally consumed, or failure needs machine-enforced handling.

## 4. Hold deep engines to a higher bar

A deep engine is not “several scripts in a directory.” Read [deep capability modules](deep-capabilities.md) before using `PROMOTE_TO_ENGINE`.

The engine boundary must be outcome-level and independently useful. Search/filter helpers, tiny graph calculators, Markdown validators, generic page renderers, and wrappers around native tools are below that bar by default.

Narrowness applies to the public machine interface, not line count—but internal depth is justified only when it removes a substantial class of owned implementation from the agent.

## 5. Preserve semantic and truth boundaries

Executable code must not own:

- recommendations, architecture, design direction, materiality, priority, or severity;
- user-intent interpretation or skill selection;
- mutation authority or permission inference;
- readiness, acceptance, plan status, or semantic completion;
- another skill's lifecycle/recovery/orchestration;
- a second source of truth duplicating repository/provider/native-tool state.

Source/repository/provider/tool state remains authoritative. Script output is derived evidence or an exact transformed artifact.

## 6. Review gates

For every executable addition, record:

1. **Natural owner** — alternatives checked first.
2. **Instruction test** — why a short instruction/checklist is insufficient.
3. **Skill owner** — who owns the residual deterministic operation.
4. **Mechanical boundary** — exact X → Y contract.
5. **Leverage** — what meaningful repeated work/defect class the code removes.
6. **State discipline** — stateless by default; persistence needs observed cross-process need.
7. **Truth boundary** — authoritative state remains outside the helper unless the helper produces the owned artifact itself.
8. **Output** — compact evidence or exact transformed result.
9. **Proof** — deterministic tests cover credible edge/failure cases proportionately.
10. **Fallback** — unsupported runtime/tooling fails explicitly.

## 7. Choose one disposition

- `KEEP` — necessary, correctly owned, proportionately proved.
- `SHRINK` — valid operation but implementation absorbs avoidable behavior.
- `REPLACE_WITH_INSTRUCTIONS` — transparent operation is better expressed as owner guidance/checklist.
- `REPLACE_WITH_NATIVE` — host/provider/project/ecosystem tool already owns it.
- `REPLACE_WITH_LIBRARY` — focused dependency removes substantial custom mechanics.
- `MOVE_TO_OWNER` — operation belongs elsewhere.
- `PROMOTE_TO_ENGINE` — several necessary QP-owned seams form a complete high-boundary domain capability.
- `REMOVE` — no justified executable capability remains.
- `NEEDS_EVIDENCE` — necessity/ownership/leverage/portability is unproved.

Default toward deletion and directness. Executable machinery is valuable when it moves the capability boundary upward, not when it merely codifies a checklist the agent can already follow.
