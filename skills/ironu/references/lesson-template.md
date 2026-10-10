# Lesson template

A lesson is a committed record. Its file name is a short kebab-case description of the lesson, not a date.

```markdown
---
title: <one line naming the lesson>
category: <folder name>
tags: [<terms a future search would use>]
problem_type: bug | knowledge
date: <YYYY-MM-DD>
---

## Context
<What was being done and where. Name the files, services or terms.>

## What went wrong or was non-obvious
<The symptom or the trap, and why the obvious reading fails. For a bug, include the approaches that did not work.>

## Guidance
<What to do next time, concretely.>

## Evidence
<The code, test or doc that shows this is current. Link, do not paste.>
```

`problem_type` is `bug` for a failure with a cause and fix, `knowledge` for a rule or fact that was not obvious. Add `last_updated: <YYYY-MM-DD>` when a later change edits the lesson.
