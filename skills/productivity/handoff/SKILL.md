---
name: handoff
description: Create one compact handoff for a fresh agent or session. Focus on the current objective, exact state, evidence, constraints, and next action.
---

# Prepare a Handoff

Write one Markdown handoff file in the operating system's temporary directory, outside the current workspace. Preserve the workspace and do not change source files or existing artifacts.

Use this compact form:

```markdown
## Objective

<objective and user focus>

## Candidate

<repository or source, branch or revision, and dirty state>

## Confirmed

<decisions, constraints, permissions, exclusions, and durable facts not to re-investigate without conflicting evidence>

## Done and proof

<completed work and proof>

## Current state

<remaining work, blockers, uncertainty, unverified claims, and only open questions whose answers can change the next action>

## First action

<one exact action and its checkable completion criterion>

## Evidence and owners

<artifact paths or URLs, material exact-current owner results, and selected owning or supporting skills>
```

Do not select a new skill route. Do not duplicate content from existing artifacts. Reference each artifact and summarize only the state needed to continue.

Serialize exact owner-reported state rather than reconstructing lifecycle meaning. Record observed changes in outcome, owner, candidate/revision, authority, phase, or acceptance when they matter to continuation, but preserve owner-reported freshness/staleness and next-owner decisions as supplied. An identity mismatch may be reported as a freshness risk; do not independently declare another owner's semantic result stale or choose a new owner from the transition alone.

Resolve every source session and artifact before treating it as confirmed. If a required source is unavailable, name the gap, limit `Confirmed` to independently verified facts, and make the first action obtain the smallest recovery bundle: a transcript or prior handoff, candidate identity, completed proof, and the next verifiable action.

When `pepeye` is active, include its exact-current supervision checkpoint and required owner results in the handoff; do not reproduce or advance Pepeye's task supervision.

Include only verified current state. Mark information that may be stale. Remove credentials and unnecessary sensitive information.

Re-read the handoff after writing. Verify that it is readable, contains no exposed credential, and gives a fresh agent the candidate, current state, remaining work, and exact first action.

Report the handoff file path.
