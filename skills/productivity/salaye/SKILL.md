---
name: salaye
description: Explain one subject the user supplies in plain language for someone with no prior knowledge of it. Use when the requested outcome is understanding rather than premise judgment, decision closure, review verdict, research record, or implementation.
---

# Ṣàlàyé

Explain the supplied subject so a capable newcomer can form the right mental model without needing the user to repeatedly specify an explanation style.

- Start with the simplest accurate description of what the thing is and why it exists.
- Define unfamiliar terms before relying on them; preserve exact identifiers/commands/API names when they matter.
- Layer detail progressively: mental model → concrete example → mechanism/important caveat only as needed.
- Prefer one representative example or analogy that clarifies the mechanism; do not add metaphor that distorts it.
- Match depth to the question. A simple “what is X?” should not become a tutorial or exhaustive reference unless the user asks.
- Separate fact from approximation and say when current external verification is needed rather than inventing certainty.

Return the explanation directly. Route to `ro-wo` when the user needs a premise tested, `iwadi` when substantial sourced research is the outcome, or the applicable specialist when implementation/review/decision work is actually requested.
