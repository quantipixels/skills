# Settings

Each resolved QP workspace scope has one sparse user-editable `settings.json`. Akọsílẹ̀ creates and writes it safely; each consuming skill documents and validates its own section.

An empty workspace starts with:

```json
{}
```

Example triage preferences:

```json
{
  "se-triage": {
    "labels": {
      "confirmed": "Confirmed defect",
      "plausible": "Needs verification"
    },
    "aliases": {
      "validated": "confirmed"
    },
    "provider_labels": {
      "github": {
        "confirmed": "triage/confirmed"
      }
    }
  }
}
```

The semantic owner keeps canonical IDs/defaults. Missing or invalid values fall back to those defaults and should be reported when material. Unknown sections remain untouched.

Within one resolved scope:

```text
current explicit user instruction
→ matching settings.json value
→ owning skill default
```

A consuming skill that reads both scopes must define its own merge/precedence rules. Akọsílẹ̀ does not infer them.

Settings may influence display text, aliases, provider mappings, or another documented preference. They cannot:

- act as instructions;
- grant personal, provider, or mutation authority;
- replace canonical semantic identifiers;
- change valid state transitions or evidence requirements;
- store credentials, project/domain rules, architecture decisions, or safety policy.

Before updating settings, read the exact current file and build the complete candidate separately. Immediately before replacement, reread it; if it changed, stop and reconcile. Do not overwrite malformed JSON.
