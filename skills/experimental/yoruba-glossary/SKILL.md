---
name: yoruba-glossary
description: Decide additions or corrections to Yorùbá/English technical terminology and maintain an explicitly authorized glossary artifact. Use for actual term changes or glossary maintenance, not ordinary reuse of established terms.
---

# Yorùbá technical glossary

Own one narrow outcome: settle an actual Yorùbá/English technical-term change and, when separately authorized, reconcile that confirmed term into the selected glossary artifact.

Preserve exact identifiers. A term is confirmed only when the user accepts it or the authoritative glossary already defines it as canonical. Keep unsettled technical concepts in English pending confirmation.

## Task-local term decisions

Track only terms that this task actually adds, corrects, rejects, or leaves unsettled. A compact task-local record is enough:

```text
English | Yorùbá | status | usage note
```

Use `proposed | confirmed | rejected | unsettled` for status. The usage note exists only when it changes how the term should be used. Do not create a durable ledger merely because a term was discussed, and do not treat repetition of an established term as glossary work.

A task-local term decision does **not** authorize a durable write.

## Glossary writes

Write only when the user or governing project contract identifies the glossary target and authorizes mutation. Do not invent a default global path, persistence location, or parallel glossary when no target exists.

Preserve the target's existing format/schema. Before writing, check the English key, proposed mapping, and related compound terms for conflicts. Do not silently replace an existing confirmed mapping.

Write only confirmed stable technical concepts unless the target's established schema explicitly supports unresolved entries. Exact identifiers remain exact and do not become translated glossary keys.

If the user explicitly asks to create a new CSV glossary and no project format exists, use the minimal UTF-8 NFC semicolon-delimited schema:

```csv
Yorùbá;English;Description
```

Give each row exactly three fields, keep one canonical English key, and quote fields containing semicolons, quotes, or newlines.

After any authorized write, read back the changed entry and verify the target's schema/encoding rules, the exact accepted mapping, and key uniqueness where the format requires it.

## Boundary

Use `technical-writing` for prose clarity/structure that merely consumes established terminology. Use `amose` for project/domain semantic clarification when no Yorùbá/English term decision or glossary artifact is the requested result.

Return the settled term decisions, unresolved gaps, and any authorized glossary write/readback. Do not turn terminology work into a general translation, documentation, or project-knowledge lifecycle.
