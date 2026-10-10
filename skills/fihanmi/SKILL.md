---
name: fihanmi
description: Fíhàn mi (Show me). Produces the smallest view that shows a point - pseudocode, a call tree, a component or file tree, a Mermaid diagram (sequence, class, state, ER, flow), a diff, a table or a chart description - with a sentence or two beside it, in chat or Markdown. Use for "show me", diagram, draw, visualize, call flow, "explain visually", or any report, plan, review or explanation for a person that prose alone would make long.
---

# Fíhàn mi (Show me)

## Output

One view per point, each with one or two sentences beside it. Prose that a view replaces is cut. Writes no record.

## Needs

The point to show and the source it comes from (code, spec, numbers). If the point or the source is missing, return to the caller and say which. Use real names, paths and numbers from the source; never invent a value to fill a view.

## Method

For each point take the first row that fits, and keep only the calls, files, fields, states and boundaries that answer the question.

| The point is | Show |
| --- | --- |
| logic, an algorithm, a rule | pseudocode |
| what runs when, in which order | a call tree |
| who talks to whom over time | a Mermaid sequence diagram |
| types and their links, a data model | a Mermaid class or ER diagram |
| a lifecycle, allowed transitions | a Mermaid state diagram |
| UI structure, with state and module boundaries | a component tree with file paths |
| which file owns what, a broad refactor | a shallow file tree, one comment per line |
| what changes in a shape that exists | a `diff` of that same shape |
| numbers that compare | a table, or a described chart |
| most of the block is new, or the reader must copy it | the whole block |
| a layout, or a comparison too dense for Markdown | a page: ask `ojuiwe` for it |

- Put each view next to the sentences it supports, not stacked at the end. Use a second view for one point only when it shows a different thing (structure, then order).
- Lead with the point. Keep a blocker or qualification that could change the reader's choice beside it.
- Mark proposed or inferred edges and unresolved dispatch. A call tree is not evidence of one stack or atomicity; use a sequence diagram when order is the point. Label a conceptual diff as conceptual, not an exact patch. A sketch explains a mechanism; it is not execution evidence.
- In chat, use fenced blocks and Mermaid, and keep prose under 15 lines (views do not count). Give readable text where Mermaid will not render. Keep meaning without colour.
- Worked shapes and the rules for execution semantics and diffs: [visual explanation](references/visual-explanation.md).

## Done

Each point has one view built from real names in the source, with one or two sentences beside it, and nothing a view replaces is repeated in prose.

## Return

Return the views in place. Stop there.
