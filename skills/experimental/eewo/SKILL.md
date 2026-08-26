---
name: eewo
description: Apply curated known-bad coding patterns to one implementation or code-review candidate in Rust, Java/JVM, Python, or Elixir. Use when the user explicitly requests Èèwọ̀ guards, anti-pattern prevention, or pattern-based review; optionally record a confirmed local rule. Exclude open-ended pattern mining, generic language teaching, architecture selection, implementation ownership, and final review verdicts.
disable-model-invocation: true
---

# Èèwọ̀

Prevent known failure patterns without prescribing one preferred architecture. This is a guard/reference skill, not a pattern-mining workflow.

`eewo` is Experimental and explicit. `alaga` owns implementation, `atunwo` owns code-review verdicts, `irinse` owns deterministic tools, `amose` owns project knowledge, and `ko-skill` owns changes to published skills.

## Modes

- `guard` — before or during implementation, return the smallest applicable set of prohibitions and safe paths.
- `review` — inspect one exact candidate for applicable pattern violations and return evidence, not a final verdict.
- `record` — with explicit user authority, add, update, supersede, or retire one repository-local or personal pattern.

## 1. Pin the candidate

Record the exact repository or supplied code, candidate identity, language, framework/runtime, relevant version, changed paths, lifecycle phase, and requested mode. Read repository instructions and accepted project constraints first.

A rule match is a hypothesis until the candidate shows the rule's trigger and credible failure mechanism. Do not report style preference, pattern-name matching, or an abstract possibility as a violation.

## 2. Load only relevant references

Always read [general guards](references/general.md). Then load only the applicable language references:

- Rust: [Rust guards](references/rust.md)
- Java/JVM: [Java guards](references/java.md)
- Spring, JPA/Hibernate, jOOQ, or Gradle: [Java framework guards](references/java-frameworks.md)
- Python: [Python guards](references/python.md)
- Elixir/OTP: [Elixir guards](references/elixir.md)

When local patterns are explicitly in scope, read [local patterns](references/local-patterns.md). Do not inspect personal QP records without explicit user authorization for that scope.

Do not load or repeat a complete reference when only a few patterns match the touched constructs.

## 3. Apply the guards

Pattern effects are:

- `BLOCK` — the candidate has a credible correctness, safety, security, resource, or caller-contract failure path. Resolve it or prove the documented exception.
- `WARN` — the pattern indicates a context-dependent maintenance, performance, or design risk. Confirm material impact before requiring change.

For `guard` mode, return the applicable IDs, prohibited behavior, failure mechanism, safe paths, and required proof. Preserve design freedom outside those constraints.

For `review` mode:

1. Pin the exact candidate.
2. Trace each suspected match through the real code path.
3. Check documented exceptions and counterevidence.
4. Report exact locations and the smallest safe correction direction.
5. Continue to state that the catalogue is incomplete; absence of a known pattern is not proof of correctness.

If applicable guards jointly leave no credible safe path, return `CONSTRAINT_CONFLICT` and name the smallest decision required instead of inventing a design.

## 4. Record local knowledge only when asked

Use `record` mode only when the user explicitly says to remember, add, update, supersede, or retire a pattern. Persist through `akosile` using the schema in [local patterns](references/local-patterns.md).

A review finding, community rule, linter signal, or one-off correction does not automatically become local policy. Preserve the observed failure, scope, safe path, and evidence; avoid broadening the rule beyond what is established.

Local records remain separate from the published skill. To contribute or change a shipped reference, use `ko-skill`; use `seda-pr` only for the separately authorized Git publication step.

Maintainers can inspect [pattern provenance](references/provenance.md); ordinary guard and review runs do not load it.

## 5. Return

```text
Eewo result
Mode: guard | review | record
Candidate: <exact identity>
References loaded: <files>
Local scopes read: repository | personal | none
Applicable guards: <id, effect, trigger, safe path>
Violations: <location, failure mechanism, evidence, or none>
Exceptions/counterevidence: <items or none>
Constraint conflicts: <items or none>
Local record changes: <ids/revisions or none>
Coverage limits: <novel/unreviewed areas>
Next owner: alaga | atunwo | akosile | ko-skill | none
```