# Term decisions and glossary maintenance

A term is confirmed when the user accepts the mapping or the authoritative target already defines it. This records project acceptance, not language-wide standardization. Keep unsettled concepts in English pending confirmation.

Track only task-added, corrected, rejected or unsettled terms as `English | Yorùbá | status | optional usage note`, where `status` is exactly one of `proposed`, `confirmed`, `rejected` or `unsettled`. A task-local decision creates no durable-write authority.

Write only to a glossary target identified and authorized by the user or project contract. There is no default global glossary. Preserve its schema, exact identifiers and unrelated records; check the English key, mapping and related compounds, and never silently replace a confirmed mapping.

Use a record-aware parser/writer for structured formats: quoted delimiters/newlines make line search insufficient for identity or uniqueness. Write only confirmed stable concepts unless the schema explicitly supports unsettled entries.

When explicitly creating a new CSV with no project format, use UTF-8 NFC semicolon-delimited `Yorùbá;English;Description`, exactly three fields per row, one canonical English key, and proper quoting for semicolons, quotes or newlines. Read back authorized changes and verify schema, encoding, exact mapping and required key uniqueness.
