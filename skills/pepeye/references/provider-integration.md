# Provider integration

Read when provider-native agents, reusable agent definitions, model/effort controls, isolation, or native multi-agent capability can materially improve a Pepeye run.

## Separate the decisions

Do not collapse these into one “agent” concept:

1. **Topology** — what bounded results are needed and which can proceed independently.
2. **Work posture** — how this worker should approach the bounded assignment.
3. **Execution context** — native host agent, existing user definition, QP-managed definition, or generic native subagent.
4. **Capability** — the model + reasoning/effort appropriate to this assignment using controls the host actually exposes.
5. **Execution boundary** — requested read/write authority, isolation, candidate identity, and independence.
6. **Method** — a semantic skill when one is already selected or materially improves the result.

The work posture is Pepeye's staffing vocabulary. It does not imply that a QP agent definition exists.

## Use the Yorùbá work postures

| Work posture | ASCII id | Use when |
| --- | --- | --- |
| **Àṣàwárí** | `asawari` | The useful result is a map, trace, location, dependency, or evidence picture before action |
| **Olùtúpalẹ̀** | `olutupale` | The useful result is bounded analysis, comparison, architecture/technical judgment, or a consequential conclusion |
| **Akọ̀wé** | `akowe` | The useful result is a prose-first artifact such as a README, documentation, specification, report, handoff, prompt, or agent-facing instruction |
| **Olùṣe** | `oluse` | The useful result requires bounded source/configuration mutation |
| **Olùdánilójú** | `oludaniloju` | A claim/candidate must be reproduced, tested, falsified, or evidenced |
| **Olùwádìí** | `oluwadi` | Current external facts, primary sources, APIs, versions, or compatibility must be established |
| **Olùyẹ̀wò** | `oluyewo` | A fixed candidate/plan/decision needs fresh independent judgment |

A posture is not a permanent persona. The same semantic skill can run under different postures when the work changes, and a posture can execute with no special skill at all.

## Prefer existing capability before QP definitions

Choose the execution context in this order:

1. a suitable **native host agent/capability**;
2. a suitable **existing user agent definition**;
3. a **QP-managed agent definition** only when it adds durable reusable value the first two do not provide;
4. a **generic native subagent** shaped through the assignment.

Judge suitability by actual behavior/capability, not file/name matching. `Àṣàwárí` may be implemented by Codex's native explorer, Claude's native Explore agent, a user's custom definition, or a generic worker depending on the host and assignment.

Do not install/use a QP definition merely for symmetry. Do not shadow a native agent to obtain a Yorùbá name. The Yorùbá posture is how Pepeye describes the worker's job; it is not proof of which provider primitive implements it.

QP definitions are additive. Existing user definitions remain user-owned. Setup may offer **keep**, **replace**, or **add separately** when a material overlap requires a choice; it must not merge QP instructions into a user definition.

## Mould the worker through the assignment

The reusable execution context should stay small. Shape the actual worker on demand with the assignment capsule:

- **outcome** — the bounded result needed now;
- **scope/candidate** — exact code, artifact, source, or question boundary;
- **execution boundary** — requested read-only/write-capable/isolated behavior and mutation authority;
- **independence** — whether fresh context/separate judgment is required;
- **evidence** — what the worker must return to support integration;
- **stop condition** — what makes this assignment complete; and
- **method** — the selected semantic skill only when it materially helps.

This is what turns a general/native agent into the worker Pepeye needs for this particular job. Do not move task-specific scope, acceptance criteria, or workflow position into the reusable agent definition.

## Adapt capability to the assignment

Capability is independent of work posture. A small README correction and a consequential architecture document can both use **Akọ̀wé** while deserving different model/reasoning capability; an ordinary review and a subtle concurrency review can both use **Olùyẹ̀wò** with different depth.

Use the current host's real model/effort controls and precedence. Do not encode provider model names or a fake cross-provider `efficient / balanced / strong` contract in Pepeye.

Prefer the current/native default when it is sufficient. Increase or reduce capability only for the assignment that warrants it rather than upgrading the entire workflow.

A definition-level model/effort value may be stronger than a default on some providers. Treat it according to the installed host's actual semantics; do not promise a spawn-time override that the provider will not honor.

## Use councils when diversity earns the cost

A council is an orchestration pattern, not an agent definition.

Use multiple independent judgments when consequence, uncertainty, competing hypotheses, or model blind spots make diversity worth the extra cost. Prefer differentiated passes over duplicated identical ones, for example:

- a lighter broad **Olùyẹ̀wò** plus a stronger deep **Olùyẹ̀wò**;
- two independent **Olùtúpalẹ̀** workers with different evidence/focus boundaries;
- independent reviewers over the same fixed candidate where disagreement itself is useful evidence.

Keep their contexts independent. Pepeye integrates the findings: agreement is evidence, disagreement is a question to resolve, and majority vote is not proof.

Do not create a council for routine work merely because parallel agents are available.

## Leave orchestration mechanics to the harness

Pepeye expresses semantic topology and staffing intent, not a replacement provider runtime.

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

Tune **when/how much** delegation, independence, capability, and judgment are useful; do not teach a capable harness how to run its own agents.

## Keep skills dynamic

Do not hardcode skill identifiers into agent definitions.

If Pepeye already knows the semantic owner and that method materially helps the assignment, name the skill in the assignment. Otherwise let the worker use ordinary installed capabilities without adding a generic “discover/use skills” instruction whose behavior is already native.

An assignment remains valid when no skill is needed.

## Treat definitions as optional enhancement

Missing QP definitions are not degraded mode when the host already provides adequate capability. Continue through native/user/generic agents without ceremony.

Only call out setup when a concrete missing configuration/definition materially limits the current work and `qp-setup` could improve it. Show that notice once per run; do not repeatedly advertise setup merely because no QP definition exists.
