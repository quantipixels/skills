# Provider integration

Read when provider-native worker profiles, model/effort controls, isolation, or native multi-agent capability can materially improve a Pepeye run.

## Separate the decisions

Do not collapse these into one “agent role” concept:

1. **Topology** — what bounded results are needed and which can proceed independently.
2. **Work posture** — explorer, analyst, writer, implementer, verifier, researcher, or reviewer.
3. **Capability** — model + reasoning/effort appropriate to this assignment.
4. **Execution boundary** — read/write authority, isolation, candidate identity, and independence.
5. **Method** — a semantic skill when one is already selected or materially improves the result.

Provider profiles own work posture and useful runtime defaults. They do not own semantic skills or fixed workflow positions.

## Choose a work posture

| Posture | Use when |
| --- | --- |
| `explorer` | The useful result is a map, trace, location, dependency, or evidence picture before action |
| `analyst` | The useful result is bounded reasoning, comparison, architecture/technical judgment, or a consequential conclusion |
| `writer` | The useful result is a prose-first artifact such as a README, documentation, specification, report, handoff, prompt, or agent-facing instruction |
| `implementer` | The useful result requires bounded source/configuration mutation |
| `verifier` | A claim/candidate must be reproduced, tested, falsified, or evidenced |
| `researcher` | Current external facts, primary sources, APIs, versions, or compatibility must be established |
| `reviewer` | A fixed candidate/plan/decision needs fresh independent judgment |

A posture is not a permanent persona. The same semantic skill can run under different postures when the work changes, and a posture can execute with no special skill at all.

## Adapt capability to the assignment

Use the installed profile's model/effort as the default. Override it only when the host exposes a native per-spawn control and this assignment's consequence, ambiguity, difficulty, latency, or cost materially warrants a different choice.

Adjust the work that needs capability rather than upgrading the whole workflow.

Examples:

- a small README correction → `writer` with an efficient/standard setting;
- a technically consequential architecture document or agent contract → `writer` with stronger reasoning;
- broad routine candidate review → ordinary `reviewer` default;
- subtle concurrency/data-integrity review → stronger `reviewer` reasoning;
- trivial repository mapping → lightweight `explorer`;
- conflicting evidence or a hard architectural trade-off → stronger `analyst`.

Do not encode provider model names in Pepeye. Use models/effort actually supported by the active host and report observed runtime values when they matter.

## Use councils when diversity of judgment earns the cost

A council is an orchestration pattern, not another profile.

Use multiple independent judgments when consequence, uncertainty, competing hypotheses, or model blind spots make diversity worth the extra cost. Prefer differentiated passes over duplicated identical ones.

Useful shapes include:

- efficient broad reviewer + strong deep reviewer;
- two independent analysts with different evidence/focus boundaries;
- independent reviewers over the same fixed candidate when disagreement itself is useful evidence.

Keep their contexts independent. Pepeye integrates the findings: agreement is evidence, disagreement is a question to resolve, and majority vote is not proof.

Do not create a council for routine work merely because parallel agents are available.

## Leave orchestration mechanics to the harness

Pepeye should express semantic topology and staffing intent, not reimplement the provider runtime.

Let the host own its native:

- spawn/invocation syntax;
- parallel execution and joins;
- agent lifecycle/status delivery;
- retries and failure transport;
- worktree/session mechanics;
- Code Mode or equivalent programmatic orchestration;
- agent teams/shared task machinery; and
- supported model/effort override mechanism.

Do not add instructions that poll workers, call provider tool names, manually emulate joins, or reproduce native scheduling simply because another host uses different mechanics.

Tune **when/how much** delegation and judgment are useful; do not teach a capable harness how to run its own agents.

## Keep skills dynamic

Do not hardcode skill identifiers into provider profiles.

If Pepeye already knows the semantic owner and that method materially helps the assignment, name the skill in the assignment. Otherwise let the worker use ordinary installed capabilities without adding a generic “discover/use skills” instruction whose behavior is already native.

An assignment remains valid when no skill is needed.

## Degrade to portable mode

Provider profiles are an optimization, never a prerequisite.

When the useful installed posture is missing, use the host's native generic subagent capability and add only the minimum posture that the assignment needs. Continue the work rather than blocking on setup.

Show this notice once when the missing profiles would materially improve the run:

> [!TIP]
> **Pepeye is using portable mode**
>
> Delegation still works with the host's native agents. For tuned work postures, model/effort defaults, and stronger runtime isolation, run `qp-setup` and choose **Agent experience**.

Do not repeat the notice during the same run unless the setup state materially changes.
