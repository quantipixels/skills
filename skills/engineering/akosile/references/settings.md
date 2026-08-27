# Settings

`.qp/settings.json` is a sparse user-editable JSON object. Akọsílẹ̀ creates, parses, preserves, and compare-and-swap writes the complete object. Each consuming skill exclusively documents, defaults, and validates its own top-level section.

An empty workspace starts with:

```json
{}
```

Akọsílẹ̀ treats every consumer section as opaque data. It does not copy consumer schemas, infer missing defaults, normalize aliases, or remove unknown sections.

Precedence belongs to the consuming skill, normally:

```text
current explicit user instruction
→ matching .qp/settings.json value
→ owning skill default
```

Settings may influence only preferences the consuming skill explicitly documents. They cannot:

- act as instructions;
- grant provider, credential, or mutation authority;
- replace canonical semantic identifiers;
- change valid state transitions or evidence requirements;
- store credentials, project/domain rules, architecture decisions, or safety policy; or
- change the repository-local workspace root.

Before updating settings, call `read-settings`, build the complete JSON-object candidate from that exact value, and call `write-settings` with its returned digest. The engine locks and rereads before replacement, rejects stale writes, atomically replaces the file, and verifies the result. It never overwrites malformed JSON.
