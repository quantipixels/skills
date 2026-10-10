---
name: komi
description: Teaches a person a concept, a system or a piece of code until they understand it, at the depth they choose. Use for "teach me", "help me understand", "explain this subsystem or change to me".
---

# Kọ́ mi

Kọ́ mi means "teach me". Output: a lesson after which the reader understands the topic at the depth they chose. Nothing changes in the code. Write it plainly so it reads clearly on the first pass.

Needs: a topic the reader can name or point at (a concept, a file, a diff, a subsystem). If it is too vague to anchor in real code or sources, or the user wants a change or a verdict rather than understanding, return and say what is missing.

## Method

**Workflow** (`asoju`): when the system is bigger than one flow, explore then explain: cheap explorers each trace a slice and you teach from their records.

- Start with a plain definition, in the words a senior engineer would say aloud, with its common name. Then tie it to this project's real code and terms.
- Build from what the reader already knows, read from the conversation rather than quizzed out of them. Spend depth where their question is.
- Give the smallest complete answer first, then stop. The reader controls depth: offer to go deeper or move on. When no one is live, deliver it whole and put the offer at the end.
- Explain the problem a part solves and what happens as someone uses it, not a list of functions and constants.
- Check understanding with one question or small exercise (predict the output, find the bug) only when the topic is hard or the reader is about to act on it. Never quiz by default.
- Keep the confidence of the evidence: say which parts were read in code or a source and which are inferred. Do not present a guess about why something is built a certain way as fact.
- For a diagram or view, ask `fihanmi`, building a flow up in steps (A to B, then redraw with C) rather than one diagram holding every part. A single simple point needs no view.
- When the explanation depends on facts you lack (history, rationale, runtime behaviour), ask `iwadi` to research them and teach from what it returns. Read the code yourself to get oriented; delegate only large research, using `asoju`.

## Done

The reader has the answer at the depth they asked for and knows where to go deeper.

## Return

The lesson. Stop and wait for the reader.
