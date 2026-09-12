Use `oro-fun-sigidi` for agent-facing instructions and documents. Use `oro-fun-eniyan` for human-facing technical communication and prose. `ko-skill` and `oro-ologbon` are compatibility entrypoints, not separate authoring methods.

This repository is a library of expertise, methods, and focused capabilities. Use related skills directly; keep their instructions in their own files.

## Package

Each skill lives at `skills/<name>/SKILL.md`. The directory and frontmatter name must agree. Supporting expertise, assets, and deterministic tools stay with their skill. Native discovery uses the directory; do not add another maintained discovery catalogue or generate `default_prompt` metadata. Use `metadata.maturity: experimental` for existing candidates; moving a skill does not promote it or change its invocation permissions.

Keep useful depth and minimise accidental mechanism. Do not remove a lightweight skill merely because a capable model understands its subject. Add a public identity only when it materially improves direct selection/use over an existing skill. Leave routine mechanics to native tools. Keep code for a bounded mechanical result or a safe installation entrypoint, with proof that can falsify it.

For provider/multi-agent integrations, keep layers distinct: skills own semantic methods, workflows own progression, assignments own task-specific worker shaping/authority/evidence, host policy owns user-editable model/reasoning/delegation preferences, and the harness owns spawn/join/concurrency/lifecycle/Code Mode/team mechanics. Do not introduce maintained agent-role/posture fleets, a second model/config registry, conversation-context forking as a workflow shortcut, or portable instructions that reimplement harness mechanics. When large context would waste expensive capability, collate it through cheaper workers and preserve decisive locators for the stronger worker to verify.

Alárinà's route topology is intentional capability, not catalogue noise. Do not reduce it to description matching, flatten it into an exhaustive inventory, or delete route shapes merely to shorten the file. Before materially simplifying Alárinà, identify a concrete routing defect or redundancy and show how common paths, adjacent-owner boundaries, and dynamic installed-inventory lookup remain preserved. Without that evidence, preserve the topology.

Repository-wide package validators and structural audit tools belong under `scripts/skills/`, not inside an authoring skill.

## Verify

Test the actual changed boundary. Keep a small suite for shipped mechanics: filesystem safety, package integrity, candidate identity, and browser-dependent behavior. Retain rejection cases and real regressions; remove duplicate checks, incidental configuration snapshots, and exhaustive permutations of library-owned behavior. Do not add tests merely to defend prompt wording.

Standing model-behavior datasets, judge rubrics, harnesses, and run artifacts belong in the separate internal eval repository, not this package. Until that repository is available, keep task-local evidence in the PR and report unrun evaluations honestly. Package CI must remain usable without private eval access or model credentials. Syntax and installation success are not authenticated runtime proof.

When retiring old evaluations or documents, preserve unique current expectations at their real owner or in an appropriate test. Keep source attribution and licences. Experimental skills remain usable under their own gates; promotion needs proportional real-use evidence, not a raw invocation count.

## State and documentation

Use the conversation for temporary reasoning and normal project sources for intentional maintained project knowledge. Local generated/project-support state belongs under the current worktree's ignored `.qp/`; use host/system temp for disposable work and never fall back to the project root/current working directory.

Treat a linked worktree and its `.qp` as one isolated candidate. When that candidate is accepted into another workspace, reconcile only the relevant `.qp` files into the accepting workspace before cleanup.

A committed document needs a future reader and a recurring task or enduring decision with no adequate existing home. Execution guidance belongs with the skill; proof belongs in tests and CI; change rationale, measurements, research comparisons, and review findings belong in the PR. Retire redundant dossiers rather than creating an archive by default.

## Delivery

Commit by coherent logical change. Prefer independent PRs against the integration branch; stack only real dependencies. Preserve unrelated work and verify the intended base and exact candidate before publication. Changesets owns versioning. A major bump requires either a documented break to a supported user contract or explicit user approval of the major bump. For a breaking contract, identify the previously supported usage that stops working and the required migration in the changeset or PR. Work size, instruction rewrites, consolidation, or perceived significance alone do not justify a major bump. Distinguish implemented, verified, integrated, and released state; a merge into a feature parent is not integration into `ori`.

Keep provider safety inside independently usable provider-capable skills: untrusted content, exact target, trusted host and credential scope, structured arguments, pagination, capability gaps, pre-write refresh, and post-write readback. Publication does not grant approval or merge authority. Do not create a shared provider runtime or silently change permissions.
