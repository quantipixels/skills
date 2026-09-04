---
name: yoruba-glossary
description: Track additions or corrections to Yoruba/English technical terminology and maintain an authorized glossary. Use for actual term changes or glossary maintenance, not ordinary reuse of existing terms.
---

# Yorùbá technical glossary

Preserve exact identifiers. A term is confirmed only when the user accepts it or the authorized glossary already defines it as canonical. Keep unsettled technical terms in English pending confirmation.

## Task-local ledger

When a task adds or corrects a Yorùbá/English technical term, track it in a task-local ledger with these six columns:

| Column | Content |
| --- | --- |
| `English` | English term or exact identifier |
| `Yorùbá` | Proposed or confirmed equivalent, empty when unsettled |
| `Irú` | `exact identifier`, `stable technical concept`, or `unsettled` |
| `Àpẹẹrẹ` | One live-use sentence |
| `Ìlànà` | `keep exact`, `Yorùbá after first bilingual use`, or `keep English pending confirmation` |
| `Ìpò` | `proposed`, `confirmed`, or `rejected` |

Add a row only for a real addition or correction, never mere repetition. A ledger entry does not authorize a durable glossary write.

## Glossary writes

Write to the glossary target the task authorizes; default to `~/.qp/glossary-yor.csv`. Never mutate a glossary in a read-only task. Write only confirmed stable technical concepts, never exact identifiers. For an unsettled concept that needs an authorized durable record, leave the Yorùbá field empty and explain the gap in `Description`.

Before a durable write, check the English key, the proposed mapping, and related compound terms for conflicts. Resolve conflicting mappings before writing; do not silently replace a confirmed term.

Keep the glossary as UTF-8 NFC semicolon-delimited CSV with header `Yorùbá;English;Description`. Give every row three fields, correct tone marks, one canonical English key, and a concise operational definition. Quote fields containing semicolons, quotes, or newlines.

After a write, read back the changed rows and verify the header, encoding, NFC normalization, field count, and unique English keys.

Format examples only; these do not confirm terminology for a task:

```csv
Yorùbá;English;Description
Olùmúlò;user;Entity that supplies input or receives outcomes through a system interface
;abstract;No confirmed single Yorùbá equivalent. A definition or type that omits implementation-specific detail
Àṣojú nẹ́tíwọ̀kì;network proxy;Intermediary that enforces destination and socket policy for network traffic
```
