# PR #38 executable-boundary reduction audit

Date: 2026-08-27  
Scope: stacked PR #38 against PR #37 (`feature/akowe-code-quality-system`)  
Result: prune the executable prototypes; keep only the authoring lessons and stack-evidence correction.

## Executive result

The deep-module experiment was useful because it exposed where our executable boundary was too low.

The initial PR #38 candidate added deterministic helpers for Akọ̀wé Code, Àròjinlẹ̀, Atọ́nà, and HTML Artifact. All four helpers worked mechanically, but that is not enough reason to keep them.

The stronger rule is:

> Add executable code when it removes a substantial class of owned implementation or produces an independently useful machine/artifact result. Use instructions when the operation is a short transparent checklist/reasoning step; use native/project tools when they already own the truth.

After applying that bar, none of the four prototype engines belongs in the current PR.

## Disposition summary

| Area | Prototype | Disposition | Replacement |
| --- | --- | --- | --- |
| Akọ̀wé Code | corpus selector + JSON packs + query schema/CLI | `REPLACE_WITH_INSTRUCTIONS` | existing JIT Markdown references, direct context selection, native/project evidence |
| Akọ̀wé Code | stack/project parsing (earlier prototype) | `REPLACE_WITH_NATIVE` | repository files, wrappers, compiler/build/package/framework/IDE tools, Irinṣẹ́ when material |
| Àròjinlẹ̀ | decision-tree/frontier CLI + schema + graph kernel | `REPLACE_WITH_INSTRUCTIONS` | existing frontier algorithm in `SKILL.md`; model maintains the material tree and recomputes the frontier |
| Atọ́nà | Markdown/frontmatter/plan/projection validator + CLI/schema | `REPLACE_WITH_INSTRUCTIONS` | existing lifecycle/readiness/frontier rules and template checks; source/projection readback at handoff |
| HTML Artifact | generic projection JSON IR + renderer + CLI/schema | `REMOVE` | existing direct semantic HTML/artifact workflow until a domain-specific high-boundary renderer is proved |
| Repository CI | `test-deep-capability-kernels.mjs` + dedicated workflow job | `REMOVE` | obsolete when the executable prototypes are removed |
| Source receipt | kernel test receipt JSON | `REMOVE` | no executable behavior remains to justify the receipt |

## Why each executable prototype is being removed

### 1. Akọ̀wé Code corpus selector

The selector took an already-known stack plus semantic signals and returned matching guidance IDs. It was deterministic, but its practical boundary was still:

```text
known context + labels
→ search/filter internal guidance
→ model reasons over result
```

That does not remove a meaningful class of engineering work. The model still has to understand the candidate, identify the mechanism, decide materiality, interpret the guidance, resolve exceptions, research gaps, formulate the Code Craft Brief, and hand it to the delivery owner.

The JSON packs also duplicate information that can live in the existing selectively loaded ecosystem Markdown references. Stable IDs and query fingerprints do not create enough user/agent outcome leverage to justify a second representation, schemas, CLI, engine, tests, and freshness machinery.

**Replacement:** keep the public Akọ̀wé Code skill small. Establish the stack from repository/native evidence, then load only the matching ecosystem/reference material. Research material gaps against owning sources. Do not create a custom internal search product unless a future outcome-level capability genuinely requires it.

### 2. Àròjinlẹ̀ frontier kernel

The frontier algorithm checks dependencies and identifies answerable versus blocked material decisions. That logic is important, but the current kernel only mechanizes a small part of the decision workflow.

The semantic owner still has to create the tree, decide materiality, define options, gather facts, frame trade-offs, recommend, ask the user, interpret answers, reopen stale branches, and obtain final confirmation.

The existing `SKILL.md` already expresses the essential frontier rule clearly enough:

```text
frontier = every material decision whose prerequisites are settled now
```

A transient JSON model, schema, CLI, digests, and graph tests add runtime ceremony without moving the outcome boundary far enough.

**Replacement:** keep the frontier behavior as explicit instructions. Revisit executable support only as part of a complete Decision Studio/decision product where the engine owns a much larger deterministic vertical (history, branch reopening, compare, artifact/runtime, delivery, etc.).

### 3. Atọ́nà plan validator

The validator parses Markdown/frontmatter and checks status/frontier/delivery combinations, headings, local links, and projection revision/status.

These rules are useful, but they are mostly direct translations of the Atọ́nà skill/template contract. The custom parser creates its own Markdown/YAML/HTML assumptions and a second maintenance surface while a passing result still cannot establish the only material outcome: whether the initiative is actually ready or closed.

The highest-value checks are already explicit in Atọ́nà:

- `Planned` requires an empty material decision frontier;
- open/blocked material choices keep the plan in `Draft`;
- record/projection revisions and status must align at handoff;
- delivery/readiness/closure remain Atọ́nà judgments.

**Replacement:** perform these checks as part of the owner workflow and exact-current readback. A future Initiative Console may justify a proper domain model/validator, but a Markdown linter is below that boundary.

### 4. HTML Artifact generic projection engine

The engine accepts generic UI primitives such as:

```text
hero
callout
prose
key-value
table
steps
code
links
flow
```

and emits a standard page shell.

That is a component/page templater, not a domain capability. The model still owns essentially every valuable decision: source selection, thesis, information architecture, representation, hierarchy, interaction, and visual judgment.

It therefore does not capture the important lesson from deeper artifact systems such as Archify, whose engine accepts a domain-specific semantic model and owns a much larger realization/quality/delivery boundary.

**Replacement:** return HTML Artifact to its direct semantic workflow. Do not add a generic IR. The next executable experiment, if any, should begin with one complete domain vertical (for example an Atọ́nà Initiative Console) and only extract shared artifact runtime after that vertical proves itself.

## Script-versus-instruction decision rule

Use instructions when all of these are true:

- the rule is short and transparent;
- the model already has the required exact evidence in context;
- there is no independent machine consumer;
- no persistent state is required;
- edge cases are small enough to state directly;
- failure does not require atomic recovery or provider-level guarantees;
- executable code would mainly encode the same checklist already present in the skill.

Examples from this experiment:

```text
Arojinle frontier calculation
Atọ́nà status/frontier consistency
record/projection revision readback
selecting the matching Akọ̀wé ecosystem reference
```

Use native/tool capability when the operation belongs to another established owner:

```text
dependency resolution
build/project effective configuration
compiler/runtime versions
package graphs
IDE project model
Git/provider state
browser rendering/accessibility/runtime truth
static-analysis metrics
```

Use a small script only when the operation is genuinely mechanical and code materially improves correctness/reproducibility compared with a short instruction.

Use a deep engine only when the boundary rises substantially higher: a domain model enters, and a complete useful result comes out with domain-specific validation, diagnostics, delivery, proof, and reader/machine utility.

## What remains in PR #38

The corrected PR should contain only the durable lessons that improve authoring behavior now:

1. `ko-skill/references/deep-capabilities.md` — raises the deep-module bar from “deep implementation behind a narrow API” to an outcome-level vertical and explicitly prefers instructions/native tools below that bar.
2. `ko-skill/references/script-boundary.md` — adds the natural-owner check and `REPLACE_WITH_INSTRUCTIONS` disposition before executable code.
3. `akowe-code/references/stack-detection.md` — clarifies repository/native-tool evidence and prohibits custom parsers/central command catalogues.
4. This experiment report — records why the prototypes were removed so later work does not repeat the same boundary mistake.
5. One changeset describing the authoring-boundary correction.

No executable runtime, engine, schema, pack/index, dedicated CI job, or generated proof receipt remains in the PR.

## Reduction target

Before pruning, PR #38 had 32 changed files and more than 1,800 additions relative to PR #37.

The corrected target is approximately five changed files, all instruction/evidence surfaces. This removes the maintenance/runtime footprint rather than merely shrinking it.

## Future re-entry bar

Do not rebuild these helpers individually. Re-entry requires a higher outcome boundary.

Examples of boundaries that could justify future executable investment:

```text
Àròjinlẹ̀
Given a semantic decision model, produce a complete decision workbench with dependency/staleness propagation, history/compare, confirmation state, interactive artifact, and delivery proof.

Atọ́nà
Given an exact initiative model and linked receipts, produce a living Initiative Console with phase/decision graphs, current path, blocker/evidence propagation, lifecycle-specific views, revision comparison, and validated delivery.

HTML Artifact
Given a domain-specific semantic artifact model, produce a complete standalone domain instrument—not generic cards—with domain quality diagnostics, reader runtime, compare/export, delivery, and browser evidence.
```

Those are future initiatives, not requirements for this PR.

## Final conclusion

PR #38 should preserve the lesson and delete the premature implementation.

The useful hierarchy is:

```text
instruction/reference
→ native/project/tool capability
→ small script only when exact mechanics genuinely benefit from code
→ deep engine only when it owns a complete high-leverage domain vertical
```

The experiment succeeded by telling us what **not** to institutionalize. The correct fix is deletion, not another round of abstraction around the same low-level helpers.
