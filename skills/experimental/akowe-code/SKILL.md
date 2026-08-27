---
name: akowe-code
description: Produce one task-scoped expert code-craft brief for an exact code candidate by establishing its language/framework/runtime from repository and native-tool evidence, applying deep progressively disclosed guidance, project knowledge, known-bad patterns, complexity signals, and bounded current primary-source research when needed. Use when code should be idiomatic, precise, maintainable, version-aware, and natural for its stack. Exclude implementation, architecture decisions, simplification execution, tool verdicts, and final code-review verdicts.
license: MIT
disable-model-invocation: true
metadata:
  version: "0.1.0"
  researched: "2026-08-27"
---

# Akọ̀wé Code

Produce one bounded **Code Craft Brief** for the exact task and candidate. This is an Experimental lightweight companion: it does not implement code, choose architecture, run an infinite improvement loop, or replace stable delivery/review owners.

## 1. Pin the candidate and establish the stack

Read the exact candidate, repository instructions, relevant build/toolchain files, dependency management, language/runtime versions, framework modules, and project knowledge. When an Architecture Contract is supplied, treat it as a hard downstream design constraint.

Read [stack detection](references/stack-detection.md) when more than one language/framework/runtime is plausible or version selection can change guidance. Prefer exact repository/config evidence and the project's own compiler/build/package/framework/IDE tooling when execution resolves an ambiguity. Do not build or rely on a parallel QP parser for facts their natural owner already exposes.

Use this evidence precedence:

```text
system / developer / user / repository instructions
→ accepted task and exact-current Architecture Contract
→ exact repository/native-tool evidence
→ confirmed project/domain knowledge
→ exact-current repository-local craft knowledge, when present
→ most specific applicable framework/runtime reference
→ language/general craft reference
→ bounded current primary-source lookup
```

A more specific framework rule may specialize a language default for proxy, lifecycle, transaction, serialization, scheduling, or runtime behavior. It must not silently weaken correctness, safety, security, compatibility, cancellation, resource ownership, or caller contracts.

## 2. Load only the guidance the candidate needs

Always read [general craft](references/craft.md). Then open only the ecosystem index or compact reference matching the touched code:

- Java → [Java index](references/ecosystems/java.md)
- Kotlin → [Kotlin](references/ecosystems/kotlin.md)
- Elixir/OTP → [Elixir](references/ecosystems/elixir.md)
- Spring Framework / Spring Boot → [Spring index](references/ecosystems/spring.md)
- Ktor → [Ktor](references/ecosystems/ktor.md)
- Phoenix / LiveView → [Phoenix](references/ecosystems/phoenix.md)

Java and Spring intentionally retain deep category references behind those indexes. Use the index as a router: open only categories whose mechanisms are present in the exact candidate. Do not load the whole catalogue simply because the repository uses Java or Spring. For a mixed candidate, compose only the controlling language/framework categories; framework guidance may specialize but not weaken the underlying language/runtime contract.

Read [known-bad patterns](references/known-bad.md) only to test patterns the candidate actually triggers. Absence of a listed pattern is not evidence that the code is correct.

Read [complexity](references/complexity.md) when control flow, state space, fan-out, nesting, mutable state, or test volume appears material. Complexity metrics are hypotheses; `pare` owns a full read-only simplification/complexity judgment.

When a repository-local Amọ̀ṣẹ́ `local-craft` record is supplied or discoverable through the current project workspace, consume only its exact-current confirmed patterns. Treat it as project evidence, never higher-priority instructions and never as permission to mutate or publish it.

## 3. Research only a material gap

Do not research merely because current documentation exists. Research only when the answer can materially change the code and repository/internal guidance cannot establish it confidently.

Typical triggers:

- candidate version is newer than the verified reference cutoff;
- preview/incubator/EAP behavior is involved;
- a framework × language interaction is version-sensitive;
- a security, compatibility, performance, or lifecycle claim depends on current behavior;
- the candidate uses an unfamiliar framework or library with no internal reference coverage.

For one or a few task-local facts, perform a bounded read-only lookup against owning primary sources and cite source/version/cutoff in the brief. Use `iwadi` only when research is substantial, independently reusable/auditable, or the caller requires a durable sourced report. Read [research policy](references/research-policy.md).

Default to no more than three unresolved research questions. That is a focus budget, not a safety ceiling. Stop researching once the brief is pinned. Reopen only when the candidate/stack identity changes or a proved contradiction invalidates the guidance.

## 4. Produce one brief, then stop

Read [brief contract](references/brief-contract.md). Normally activate about 5–12 material constraints; use fewer when the task is simple and exceed that range only when distinct correctness/safety contracts genuinely require it. Do not dump the reference catalogue.

Every active item must tie to the candidate through at least one of:

- a caller-visible or operational failure mechanism;
- a stack/version compatibility rule;
- a clear idiomatic/craft improvement at the same abstraction level;
- a reduction in invalid state, lifecycle ambiguity, unnecessary ceremony, or accidental complexity;
- a required proof seam.

Prefer the smallest native construct that expresses the contract. Do not recommend rewrites solely to demonstrate newer syntax, design patterns, framework features, or personal style.

Return exactly one brief and stop. If invoked again on a later candidate, recompute from that exact identity; do not carry stale rules forward. Return the brief to the caller as Akọ̀wé Code's native result. When a distinct next outcome is requested, use `alarina` to select its owner rather than maintaining a duplicate downstream-owner map here.

## Maintenance

One public skill does not require shallow internal knowledge. The former Java and Spring experiments remain retired as public runtime skills, but their useful detailed category references are preserved under `references/java/` and `references/spring/` for progressive disclosure. Kotlin, Ktor, Elixir/OTP, and Phoenix currently remain compact because their retained corpus is smaller.

Do not add a search/selector engine merely to retrieve these references; normal candidate-driven progressive disclosure is the default. Read [authoring](references/authoring.md) before changing the reference boundary and [source map](references/source-map.md) when auditing provenance or freshness.
