Use `oro` for agent-facing instructions and documents or human-facing technical communication and prose; select its branch by the primary reader.

This repository is a library of expertise, methods, and focused capabilities. Use related skills directly; keep their instructions in their own files.

Delegate analysis, research, implementation, and review freely when workers can advance useful parts of the task. Delegation needs no separate user approval or formal overhead justification. Keep assignments bounded, preserve authority, and verify decisive evidence; use native host controls without forking session context.

## Package

Each skill lives at `skills/<name>/SKILL.md`. The directory and frontmatter name must agree. Supporting expertise, assets, and deterministic tools stay with their skill. Native discovery uses the directory; do not add another maintained discovery catalogue or generate `default_prompt` metadata. Use `metadata.maturity: experimental` for existing candidates; moving a skill does not promote it or change its invocation permissions.

Keep useful depth and minimise accidental mechanism. Do not remove a lightweight skill merely because a capable model understands its subject. Add a public identity only when it materially improves direct selection/use over an existing skill. Leave routine mechanics to native tools. Keep code for a bounded mechanical result or a safe installation entrypoint, with proof that can falsify it.

For provider/multi-agent integrations, keep layers distinct: skills own semantic methods, workflows own progression, assignments own task-specific worker shaping/authority/evidence, host policy owns user-editable model/reasoning/delegation preferences, and the harness owns spawn/join/concurrency/lifecycle/Code Mode/team mechanics. Do not introduce maintained agent-role/posture fleets, a second model/config registry, conversation-context forking as a workflow shortcut, or portable instructions that reimplement harness mechanics. When large context would waste expensive capability, collate it through cheaper workers and preserve decisive locators for the stronger worker to verify.

[Pepeye](skills/pepeye/SKILL.md) is the operating entrypoint for this skill system: interpret the requested outcome, select relevant installed skills and conditional routes, coordinate useful work, integrate evidence, and carry authorized work through completion. Specialist skills retain their methods, and workflow skills retain progression within their workflows. [The native agent](agents/pepeye.md) is a thin Claude entrypoint that reads and applies the Pepeye skill; keep operating guidance and the conditional host-policy profile in the skill rather than duplicating them in agent definitions. Model and reasoning choices remain with the user and host policy.

Pepeye's route topology is intentional capability, not catalogue noise. Do not reduce it to description matching, flatten it into an exhaustive inventory, or delete route shapes merely to shorten the file. Before materially simplifying Pepeye, identify a concrete routing defect or redundancy and show how common paths, adjacent-owner boundaries, and dynamic installed-inventory lookup remain preserved. Without that evidence, preserve the topology.

Repository-wide package validators and structural audit tools belong under `scripts/skills/`, not inside an authoring skill.

## Verify

Test the actual changed boundary. Keep a small suite for shipped mechanics: filesystem safety, package integrity, candidate identity, and browser-dependent behavior. Retain rejection cases and real regressions; remove duplicate checks, incidental configuration snapshots, and exhaustive permutations of library-owned behavior. Do not add tests merely to defend prompt wording.

Standing model-behavior datasets, judge rubrics, harnesses, and run artifacts belong in the separate internal eval repository, not this package. Until that repository is available, keep task-local evidence in the PR and report unrun evaluations honestly. Package CI must remain usable without private eval access or model credentials. Syntax and installation success are not authenticated runtime proof.

When retiring old evaluations or documents, preserve unique current expectations at their real owner or in an appropriate test. Keep source attribution and licences. Experimental skills remain usable under their own gates; promotion needs proportional real-use evidence, not a raw invocation count.
