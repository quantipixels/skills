# Settings

`.qp/settings.json` is a sparse user-editable JSON object. Akọsílẹ̀ creates and safely replaces the complete object; each consuming skill exclusively documents, defaults, and validates its own top-level section.

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

Before updating settings, use `scripts/safe-write.py snapshot` to obtain one exact settings snapshot and its matching digest. Build the complete JSON-object candidate from that snapshot, preserve unknown sections, validate the candidate, and replace it through `safe-write.py write` with the returned digest. For a missing file, the snapshot result is `absent`.

The helper protects only the exact snapshot and atomic compare-and-swap. The consuming skill retains settings semantics and conflict reconciliation.
