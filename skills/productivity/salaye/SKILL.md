---
name: salaye
description: Explain one subject the user supplies in plain language for someone with no prior knowledge of it. Use when the requested outcome is understanding rather than premise judgment, decision closure, review verdict, research record, or implementation.
---

# Ṣàlàyé

Explain the supplied subject so a capable newcomer can form the right mental model without repeatedly specifying an explanation style.

- Start with the simplest accurate description of what the thing is and why it exists.
- Define unfamiliar terms before relying on them; preserve exact identifiers, commands, API names, and domain terms when they matter.
- Layer detail progressively: mental model → concrete example → mechanism or important caveat only as needed.
- Prefer one representative example or analogy that clarifies the mechanism; do not add metaphor that distorts it.
- Match depth to the question. A simple “what is X?” should not become a tutorial or exhaustive reference unless the user asks.
- Separate fact from approximation and say when current external verification is needed rather than inventing certainty.

When structure materially shortens the explanation, use the smallest inline representation that exposes the relationship: pseudocode for logic, a call tree for execution/order, a component or shallow file tree for composition/ownership, a shape-aware diff for before/after, or a small diagram when two-dimensional relationships are genuinely clearer. Show the whole block/shape when omission would hide ownership or order. Keep the representation adjacent to the explanation it replaces or supports.

Return the explanation directly. `html-artifact` becomes the owner only when the requested result is a standalone browser information projection rather than conversational understanding. Do not turn an explanation request into research, decision closure, review, or implementation unless that outcome is separately requested.
