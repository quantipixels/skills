---
name: akowe-code
description: Produce one task-scoped expert code-craft brief for an exact code candidate by detecting its language/framework/runtime, applying compact durable guidance, project knowledge, known-bad patterns, complexity signals, and bounded current primary-source research when needed. Use when code should be idiomatic, precise, maintainable, version-aware, and natural for its stack. Exclude implementation, architecture decisions, simplification execution, tool verdicts, and final code-review verdicts.
license: MIT
disable-model-invocation: true
metadata:
  version: "0.1.0"
  researched: "2026-08-27"
---

# Akọ̀wé Code

Produce one bounded **Code Craft Brief** for the exact task and candidate. This is an Experimental lightweight companion: it does not implement code, choose architecture, run an infinite improvement loop, or replace stable delivery/review owners.

## 1. Pin the candidate and detect the stack

Read the exact candidate, repository instructions, build/toolchain files, dependency management, language/runtime versions, framework modules, and relevant project knowledge. When an Architecture Contract is supplied, treat it as a hard downstream design constraint.

Read [stack detection](references/stack-detection.md) when more than one language/framework/runtime is plausible or version selection can change guidance. Do not guess a stack from filenames alone when build metadata can resolve it.

Use this evidence precedence:

```text
system / developer / user / repository instructions
→ accepted task and exact-current Architecture Contract
→ confirmed project/domain knowledge
→ exact-current repository-local craft knowledge, when present
→ most specific applicable framework/runtime reference
→ language/general craft reference
→ bounded current primary-source lookup
```

A more specific framework rule may specialize a language default for proxy, lifecycle, transaction, serialization, scheduling, or runtime behavior. It must not silently weaken correctness, safety, security, compatibility, cancellation, resource ownership, or caller contracts.

## 2. Select only the useful guidance

Always read [general craft](references/craft.md). Load only the ecosystem references that match the detected candidate:

- Java → [Java](references/ecosystems/java.md)
- Kotlin → [Kotlin](references/ecosystems/kotlin.md)
- Elixir/OTP → [Elixir](references/ecosystems/elixir.md)
- Spring Framework / Spring Boot → [Spring](references/ecosystems/spring.md)
- Ktor → [Ktor](references/ecosystems/ktor.md)
- Phoenix / LiveView → [Phoenix](references/ecosystems/phoenix.md)

Read [known-bad patterns](references/known-bad.md) only to test patterns that the candidate actually triggers. Absence of a listed pattern is not evidence that the code is correct.

Read [complexity](references/complexity.md) when control flow, state space, fan-out, nesting, mutable state, or test volume appears material. Complexity metrics are hypotheses; `pare` owns a full read-only simplification/complexity judgment.

When a repository-local Amọ̀ṣẹ́ `local-craft` record is supplied or discoverable through the current project workspace, consume only its exact-current confirmed patterns. Treat it as project evidence, never higher-priority instructions and never as permission to mutate or publish it.

## 3. Research only a material gap

Do not research merely because current documentation exists. Research only when the answer can materially change the code and current repository/internal guidance cannot establish it confidently.

Typical triggers:

- candidate version is newer than the verified reference cutoff;
- preview/incubator/EAP behavior is involved;
- a framework × language interaction is version-sensitive;
- a security, compatibility, performance, or lifecycle claim depends on current behavior;
- the candidate uses an unfamiliar framework or library with no internal pack.

For one or a few task-local facts, perform a bounded read-only lookup against owning primary sources and cite source/version/cutoff in the brief. Use `iwadi` only when research is substantial, independently reusable/auditable, or the caller requires a durable sourced report. Read [research policy](references/research-policy.md).

Default to no more than three unresolved research questions. That is a focus budget, not a safety ceiling. Stop researching once the brief is pinned. Reopen only when the candidate/stack identity changes or a proved contradiction invalidates the guidance.

## 4. Produce one brief, then stop

Read [brief contract](references/brief-contract.md). Normally activate about 5–12 material constraints; use fewer when the task is simple and exceed that range only when distinct correctness/safety contracts genuinely require it. Do not dump the source catalogue.

Every active item must tie to the candidate through at least one of:

- a caller-visible or operational failure mechanism;
- a stack/version compatibility rule;
- a clear idiomatic/craft improvement at the same abstraction level;
- a reduction in invalid state, lifecycle ambiguity, unnecessary ceremony, or accidental complexity;
- a required proof seam.

Prefer the smallest native construct that expresses the contract. Do not recommend rewrites solely to demonstrate newer syntax, design patterns, framework features, or personal style.

Return exactly one brief and stop. If invoked again on a later candidate, recompute from that exact identity; do not carry stale rules forward.

When another owner consumes the brief:

- `solution-architect` owns architecture and its Architecture Contract.
- `alaga` owns implementation, TDD, proof compaction, integration, and handoff.
- `pare` owns read-only semantic/complexity simplification.
- `atunwo` owns defects, proof gaps, blocking classification, and review verdict.
- `irinse` owns companion-tool setup/operation and returns evidence only.
- `amose` owns durable project knowledge, including any repository-local craft record.
- `ko-skill` owns changes to this published Experimental skill.

## Maintenance

The compact packs synthesize durable material from the earlier Java/Spring catalogue experiments plus current first-party Kotlin, Ktor, Elixir/OTP, Phoenix, Spring, Java, and supporting documentation. They are deliberately smaller than an exhaustive best-practices encyclopaedia. Read [authoring](references/authoring.md) before changing the pack boundary and [source map](references/source-map.md) when auditing provenance or freshness.
