# Roadmap

Planned work that is decided in direction but not built yet. Each item says why it waits.

## A learning plugin for shared lessons

Today lessons stay local: `ironu` keeps a project's lessons in its internal docs, hands lessons about the user to `asami` for their defaults, and only mentions lessons about how agents work in general as suggestions. Nothing opens a PR or edits installed skills.

Next: a dedicated internal Quanti Pixels plugin (part of `agent-setup` or `tech-stack`, or a new one) that manages shared learning: it collects generic, scrubbed lessons across projects and carries each to its shared home through its own reviewed process (stack and tooling to `tech-stack`, agent and host setup to `agent-setup`, working method to qp-skills). Proprietary details never leave their project, and the user approves each change.

Why it waits: it needs its own owner, review flow and privacy checks, and the local routing should prove itself first.

## Measured skill retuning

When a new model arrives, cut rules the model no longer needs, but only where an A/B run of old and new skill versions shows no loss above the noise floor.

Why it waits: there is no A/B harness yet. The end-to-end skill test can compare with-skill and no-skill runs, but not two skill versions at scale.

## Shared lesson packs

Rule sets that apply to a group of projects (a stack, a client), selected by where they apply.

Why it waits: lessons stay local for now; the learning plugin above would own this.

## Smaller items

- Recurring feedback intake (issues, chat) like CE's sweep, only when a project has a steady stream to process.
