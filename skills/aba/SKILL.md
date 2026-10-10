---
name: aba
description: Àbá (proposal). Produces a short list of real directions with trade-offs and a recommendation the user can pick from. Use for "give me ideas", "what could we do", "which direction", or an outcome the user can see but no route to it.
---

# Àbá

**Output:** the opportunity, the surviving directions with their trade-offs and what each still needs, the rejected ones with one reason each, and a recommendation the user may take or leave. You propose; the user chooses.

**Needs:** a problem or opportunity, who it is for, and what a useful direction would look like. A rough version is enough; mark what you assumed. If the request is too thin, or is really a settled build, a bug, a plan or a spec, or if what the user wants is itself unclear, return to the caller and say what is missing.

## Method

- **Explore directions** ([ideation](references/ideation.md)): when no direction is apparent or the obvious ones are unsatisfying. Produce a small set of different mechanisms, challenge each, keep the credible ones.
- **Shape progressively** ([progressive shaping](references/progressive-shaping.md)): when the outcome is clear but the route is not, or later work cannot be stated yet. Name the destination, find what can be worked now, pick the next step that teaches the most before any backlog is guessed.

Use either or both; do not start with a method the situation does not need.

- Ground claims in evidence. Use `iwadi` for substantial research. A throwaway prototype or a reaction from the user can settle a choice.
- Keep a promising idea, a confirmed choice and an accepted requirement apart. Nothing you propose becomes a requirement until the user picks it.
- For a consequential direction, get a second opinion from the other provider.
- It is valid to say no credible direction exists, with what evidence or decision would change that.
- Do not plan, specify or build.

## Done

Every surviving direction has its trade-offs and what it needs; every rejected one has a reason.

## Return

Return the output to the caller.
