# Reference quality

Use this when adding, expanding, splitting, moving, or removing a skill reference. Judge the reference by the expert judgment it carries when its branch is relevant, not by raw line count or file count.

A healthy reference is not a private encyclopaedia. It is a selectively loaded part of one owner that helps a capable agent make a recurring non-obvious decision more reliably.

## Reference or catalogue?

A **reference** belongs to one skill outcome and is loaded when a bounded branch of that outcome needs deeper judgment, vocabulary, examples, counterexamples, stable decision rules, or an authoritative conceptual anchor.

A **catalogue** maintains a reusable body of language, framework, platform, standards, or domain knowledge because that knowledge is itself necessary to the skill's public result. Apply [researched knowledge catalogues](knowledge-catalogues.md) only for that shape.

Good reference: a Solution Architect module-depth guide explaining when an adapter owns enough lifecycle/policy to justify a seam.

Bad disguised catalogue: a hidden Java/Spring/Kotlin best-practice corpus inside an execution companion.

## Keep decision-bearing depth

A reference earns its place when most of these are true:

- **Owner fit** — the knowledge can materially change this owner's native result.
- **Non-obvious judgment** — a capable agent can plausibly get the distinction wrong without calibration.
- **Recurrence** — it applies across multiple plausible invocations or protects one owner-wide high-consequence boundary.
- **Selective trigger** — the owner can load it only when the branch matters.
- **Stable basis** — it is durable enough to preserve, or it states the evidence/freshness boundary that requires revalidation.
- **Calibration value** — examples, counterexamples, a named reasoning model, or stable vocabulary materially sharpen the rule.
- **Bounded output** — the reference improves the native result without being dumped into that result.

Do not keep a reference merely because it is informative. Move, research, or remove material that:

- duplicates current official documentation or discoverable repository facts;
- restates formatter, compiler, linter, schema, or static-tool output that a deterministic owner can provide more reliably;
- mirrors a subject taxonomy without an owner-specific decision consequence;
- freezes volatile framework/platform behavior better read from current owning sources;
- records one task's temporary state, rationale, or history; or
- cannot change the skill's judgment, action, proof, safety, authority, or completion result.

### Preserve useful named models

Do not remove a named model, standard, or concept merely because its currently selected rules can be paraphrased. Keep the name when it provides material conceptual compression, stable vocabulary, authoritative scope, or a retrieval anchor that helps the agent handle cases not enumerated in local bullets.

When keeping one, bind it explicitly:

```text
named model/standard
→ QP-relevant reasoning job
→ selected behavior-bearing subset
→ boundary: the name does not import the whole framework
```

Prefer current owning sources for volatile or normative detail. Remove names that add only prestige, generic ceremony, canned templates, or latent rules QP does not intend to adopt.

When compressing or removing a reference, check the residual material decision surface: a smaller representation is worse if the deleted depth merely turns a consequential constraint or distinction into model inference.

## Use examples as calibration

Examples are first-class when they teach a material boundary. Use concise forms such as `Good / Bad`, `Prefer / Avoid`, `Use when / Avoid when`, or one strong counterexample.

Good:

```text
Deep module
Good: a small interface owns retries, lifecycle, provider quirks, and failure translation.
Bad: an interface mirrors every implementation method and exists only for hypothetical variation.
Exception: a thin adapter is valid when it owns a real external integration or trust boundary.
```

Bad:

```text
Good: clean code.
Bad: messy code.
```

Do not require examples to replace prose. Keep them when they make a recurring judgment more precise than prose alone. Remove cosmetic variants that teach no new distinction.

## Split by retrieval boundary, not aesthetics

Do not impose an arbitrary maximum reference size or file count. Prefer one cohesive reference when its sections normally load together. Split only when branches can be selected independently enough to save material context or carry materially different freshness/evidence boundaries.

Good: one cohesive `module-depth.md` loaded for module/interface design.

Bad: seven tiny files that must all be opened for every module-boundary decision.

Use headings, local examples, and retrieval cues so a substantial reference remains navigable.

## Mature shared guidance deliberately

Task-local findings do not automatically become shared skill guidance. When evidence suggests a durable gap:

```text
observed recurring or owner-wide misjudgment
→ exact-current retrospective/evidence when needed
→ identify the earliest owning skill
→ author the smallest durable principle/reference through Kọ Skill
→ prove the changed judgment against a realistic boundary
```

Recurrence is not a numeric quota. One strong owner-wide failure can justify a reference when the consequence and generality are clear. One unconfirmed task correction does not.

Project-specific confirmed patterns stay with the project's existing owner such as Amọ̀ṣẹ́ local craft rather than being promoted automatically.

## Return one disposition

For each material reference under review, use one disposition:

- `KEEP` — coherent, selectively useful expert depth.
- `DEEPEN` — the owner is correct but recurring non-obvious judgment is under-specified.
- `SPLIT` — independently selectable branches currently force unnecessary context.
- `MOVE` — another owner or deterministic mechanism is the correct source.
- `RESEARCH` — the guidance is useful but evidence/freshness is insufficient.
- `REMOVE` — duplicate, obvious, stale, task-local, or result-irrelevant material.

Every `DEEPEN`, `SPLIT`, `MOVE`, or `REMOVE` finding must name the decision consequence. Reference length alone is never a finding.
