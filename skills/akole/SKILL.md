---
name: akole
description: Akọ́lé. Produces a working coding change with proof. It builds and verifies an accepted change, or fixes a bug once its cause is known. Covers delivery, integration obligations, bug-fix proof, settled-change passes, test-suite improvement, property-based testing and stateful proof.
---

# Akọ́lé

**Output:** a working change with proof that it works. A `scope-only` request returns boundaries and proposed proof without implementation.

**Needs:** a clear outcome and an accepted scope; for a bug fix, a known cause. A clarification does not restart approval or reopen settled decisions. If the request is too thin, the cause of a failure is unknown, or the job is something other than building, return to the caller and say what is missing.

## Method

**Workflows** (`asoju`): start unfamiliar code from a reader's repository record; hand scripted runs (test suites, builds, lints, a verify skill's recipe) to a cheap runner and read its evidence; many independent checks go to a gauntlet.

Implement and verify the accepted coding outcome using [delivery](references/delivery.md), then read the reference that matches the work:

- **Bug fix**: [bug-fix proof](references/bug-proof.md): test first when cheap, a complete cause chain, before and after evidence. Prefer end-to-end checks over unit tests.
- **Change across consumers, stored data, framework behavior, authorization or external effects**: [integration obligations](references/integration-obligations.md).
- **Settled change that works**: [simplify and polish](references/settled-change-passes.md), optional passes.
- **Improving an existing test suite**: [test-suite improvement](references/test-suite-improvement.md).
- **An invariant over many inputs**: [property-based testing](references/property-based-testing.md). **Persistence, concurrency or recovery gaps**: [stateful proof](references/stateful-proof.md).
- **Numbers with units or scale**: call `iwon` for the method.
- **Real-surface proof**: use the project's verification skill to drive the real product. If it is missing, say so and return the gap.

Two rules hold throughout:

- When two fixes that share one premise have both failed, stop fixing. Question the premise and check which parts of the system actually hold the problem before the next attempt.
- Write a code comment only for a non-obvious reason the code cannot show. Let assertion messages and log strings name what a check proves instead of narrating steps.

## Done

The change is implemented, its tests and checks pass, and the proof (including real-surface proof where the change is user-facing) is recorded with what was not run.

## Return

Return the change, the proof and any residual risk to the caller.
