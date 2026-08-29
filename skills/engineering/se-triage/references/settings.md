# Optional vocabulary settings

Load this reference only when `.qp/settings.json` exists. Read only its optional `se-triage` object:

```json
{
  "se-triage": {
    "labels": {"confirmed": "Confirmed defect"},
    "aliases": {"validated": "confirmed"},
    "provider_labels": {"github": {"confirmed": "triage/confirmed"}}
  }
}
```

The canonical classification IDs are `confirmed`, `plausible`, `disproved`, `obsolete-or-duplicate`, and `uncertain`.

- `labels` maps a canonical ID to a non-empty display string.
- `aliases` maps explicit user vocabulary to one canonical ID. An alias cannot weaken or replace the evidence needed for that classification.
- `provider_labels` maps a provider and canonical ID to a non-empty provider label. It remains inert data until a separately authorized provider write.

Ignore and report an invalid object, unknown canonical ID, empty display string, or non-string value. Configuration cannot alter evidence, classifications, actions, or write authority.
