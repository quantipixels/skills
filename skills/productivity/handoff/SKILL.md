---
name: handoff
description: Create one compact handoff for a fresh agent or session. Focus on the current objective, exact state, evidence, constraints, and next action.
---

# Prepare a Handoff

Create one compact handoff packet that a fresh agent/session can use immediately. The handoff content is the native result; a file is only a transport when the active host or user needs one.

When a durable/portable file materially improves transfer and the host supports it, write one Markdown handoff to the host's temporary or user-selected output surface without changing the source workspace or existing artifacts. Otherwise return the complete handoff inline or through the host's native transferable artifact surface.

Use this compact form:

```markdown
## Objective

<objective and user focus>

## Subject / candidate

<exact current work/result identity: source, artifact, revision, event, branch, candidate, or equivalent when applicable>

## Confirmed

<decisions, constraints, permissions, exclusions, and durable facts not to re-investigate without conflicting evidence>

## Done and proof

<completed work and current proof/evidence>

## Current state

<remaining work, blockers, uncertainty, unverified claims, and only open questions whose answers can change the next action>

## First action

<one exact action and its checkable completion criterion>

## Evidence and owners

<artifact paths/URLs/identities, material exact-current owner results, and selected owning or supporting skills/capabilities>
```

Do not select a new skill route. Do not duplicate content from existing artifacts. Reference each artifact/result and summarize only the state needed to continue.

Serialize exact owner-reported state rather than reconstructing lifecycle meaning. Record observed changes in outcome, owner, candidate/revision, authority, phase, or acceptance when they matter to continuation, but preserve owner-reported freshness/staleness and next-owner decisions as supplied. An identity mismatch may be reported as a freshness risk; do not independently declare another owner's semantic result stale or choose a new owner from the transition alone.

Resolve every source session and artifact before treating it as confirmed. If a required source is unavailable, name the gap, limit `Confirmed` to independently verified facts, and make the first action obtain the smallest recovery bundle: prior transcript/handoff or equivalent context, current subject/candidate identity, completed proof, and the next verifiable action.

When `pepeye` is active, include its exact-current supervision checkpoint and required owner results in the handoff; do not reproduce or advance Pepeye's task supervision.

Include only verified current state. Mark information that may be stale. Remove credentials and unnecessary sensitive information.

Re-read the final packet after writing/composing. Verify that it is readable, contains no exposed credential, and gives a fresh agent the subject/candidate, current state, remaining work, and exact first action.

Return the handoff content plus its direct-access locator when one exists. Do not invent a filesystem path when the host did not create a file.
