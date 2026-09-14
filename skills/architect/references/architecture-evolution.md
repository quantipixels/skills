# Architecture evolution

Use for an established choice whose fit is in question. Keep Architect's survey/design/review boundary: survey ranks opportunities; design selects a correction; review judges a supplied candidate. This is not another delivery workflow or a mandatory audit on every feature.

## Recover the decision

Identify the responsibility, original rationale when known, current constraints and what changed: user needs, operating scale, repeated workarounds, a maintenance/support problem, or a newly available language, framework or tool capability. Separate a binding product or compatibility requirement from an incidental implementation choice. Missing rationale is uncertainty, not proof the choice was wrong.

Trace one representative development change through the affected boundary and, when behavior is externally observable, one user journey. Find where callers reconstruct policy, maintainers cross unrelated owners, feedback arrives late, or agents lose the authoritative source. Use observed cost or failure and material counterevidence; a preferred pattern or tidier directory tree is not a finding.

## Keep three outcomes distinct

| Perspective | Relevant evidence |
| --- | --- |
| End user | Can the person complete the intended journey reliably, accessibly and within its response/recovery expectations? API changes must preserve the behavior consumed by real clients. |
| Developer | Can a maintainer locate the owner, understand its contract, make the change, obtain useful feedback and diagnose failure? Include onboarding and operational burden where material. |
| Coding agent | Can the agent discover canonical code, constraints and commands, select affected proof and interpret actual results without guessing or traversing duplicate sources? |

Agent convenience must not degrade end-user experience or developer maintainability. Prefer shared improvements such as coherent ownership, discoverable contracts and reproducible commands. Do not reshape a public API, split cohesive code or duplicate project documentation solely for model context limits. Product capabilities used by agents remain a separate concern under [agent-facing systems](agent-native-systems.md).

## Compare retaining, simplifying and replacing

Include keeping the current choice. Before adding a dependency, service, state store or custom mechanism, check whether an existing language, runtime, framework or provider guarantee already owns the responsibility. Verify the actual version, configuration and semantic limits; familiar names do not establish equivalent behavior.

Inspect the ecosystem's resolved dependency/build graph when it controls the choice, distinguishing direct/transitive and build/test/runtime use. Manifests alone can miss resolution, generated configuration and task-specific inputs. Check locking and reproducibility where the proposed benefit depends on them.

A replacement must explain both what owned work disappears and what new work arrives: integration, transitive dependencies, licensing/support, deployment, configuration, debugging, upgrades and exit cost. A library can reduce maintenance; fewer application lines alone do not establish that. Do not reject a suitable unfamiliar technology, or adopt one merely because it is newer.

For API changes, inspect a realistic consumer: sequencing, identity, errors, pagination or generated-client behavior as applicable. Distinguish source, wire and semantic compatibility. For repository layout, trace where the representative change and its proof belong; prefer locality and explicit dependency direction over a universal folder convention.

For build/test improvements, locate the delayed feedback before choosing a tool or rewrite. Compare equivalent useful work; distinguish clean, incremental and no-change builds, and executed tests from cached results. Use `irinse` for non-obvious tool evidence and `adanwo` when a comparative performance claim controls the choice. Removing required proof is not a speed improvement.

## Make the decision checkable

Return the evidence-backed opportunity or selected change, its user/developer/agent consequences, strongest alternative, compatibility/migration cost and smallest experiment that could overturn the choice. A bounded result may be keep, change, investigate or defer with a concrete re-entry condition. Retain consequential rationale through `amose`; use `atona` only when accepted work needs initiative planning. Report wider opportunities without silently enlarging a delivery assignment.

A stable, consequential architectural invariant may earn an executable fitness check: reuse compiler, build or test enforcement and verify it rejects a representative violation. A one-off preference does not justify a permanent gate.

Sources: [DORA architecture outcomes](https://dora.dev/capabilities/loosely-coupled-teams/), [DevEx framework](https://www.michaelagreiler.com/wp-content/uploads/2024/06/DevEx-WhatDrivesProductivity.pdf), [Google API compatibility](https://google.aip.dev/180), [AX concepts](https://agentexperience.ax/concepts/getting-started/), [Cargo resolved metadata](https://doc.rust-lang.org/cargo/commands/cargo-metadata.html), [ArchUnit incremental rules](https://www.archunit.org/userguide/html/000_Index.html#_freezing_arch_rules).
