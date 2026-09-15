# Term decisions and glossary maintenance

A term is confirmed when the user accepts its mapping or the authoritative target glossary already defines it as canonical. This records project acceptance, not language-wide standardization. Keep unsettled technical concepts in English pending confirmation.

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

Use a format-aware reader/writer for structured glossaries. Text search can locate candidates, but quoted delimiters or newlines make line matches insufficient to establish records or key uniqueness. Parse the relevant records before changing them and for read-back verification; preserve unrelated entries.

Write only confirmed stable technical concepts unless the target's established schema explicitly supports unresolved entries. Exact identifiers remain exact and do not become translated glossary keys.

If the user explicitly asks to create a new CSV glossary and no project format exists, use the minimal UTF-8 NFC semicolon-delimited schema:

```csv
Yorùbá;English;Description
```

Give each row exactly three fields, keep one canonical English key, and quote fields containing semicolons, quotes, or newlines.

After any authorized write, read back the changed entry and verify the target's schema/encoding rules, the exact accepted mapping, and key uniqueness where the format requires it.
