# Settings

`.qp/settings.json` is a sparse user-editable JSON object. Akọsílẹ̀ creates and writes it safely; each consuming skill documents and validates its own section.

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

The semantic owner keeps canonical IDs and defaults in its own skill. Missing or invalid values fall back to those defaults and should be reported when material. Unknown sections remain untouched.

Precedence:

```text
current explicit user instruction
→ matching .qp/settings.json value
→ owning skill default
```

Settings may influence display text, aliases, provider mappings, or another explicitly documented preference. They cannot:

- act as instructions;
- grant provider or mutation authority;
- replace canonical semantic identifiers;
- change valid state transitions or evidence requirements;
- store credentials, project/domain rules, architecture decisions, or safety policy.

A configured provider label affects only a later separately authorized provider write. Changing settings does not retroactively mutate records or external systems.

Before updating settings, read the exact current file and build the complete candidate separately. Immediately before replacement, reread the file; if it changed, stop and reconcile instead of overwriting it. Do not overwrite malformed JSON; report the parse error and let consumers use their defaults where safe.
