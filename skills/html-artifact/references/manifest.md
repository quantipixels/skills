# Compact artifact manifest

Use for a substantial or maintained artifact when stable identity and source-cut retrieval are useful. Keep existing capsules readable as historical inputs; this format is not a retroactive requirement for all artifacts.

```html
<script type="application/json" id="qp-artifact-manifest">
{"schemaVersion":1,"artifactId":"retry-review","revision":"1","sourceCut":[{"id":"candidate","revision":"abc123"}],"delivery":"connected","interactionState":"transient","dependencies":[]}
</script>
```

Required fields in v1: `schemaVersion: 1`, nonempty `artifactId` and `revision`, `sourceCut` (array of nonempty `id`/`revision` pairs), `delivery` (`portable`, `connected` or `host`), `interactionState` (`transient` or explicitly requested `persistent`) and `dependencies` (array of `name`, exact `version`, `url` entries). Empty source/dependency arrays are valid when genuinely absent. Optional `purpose`, `status`, `evidenceCutoff`, `blockers` and `nextAction` remain concise owner-established meaning. Do not encode live reader choices here.

Manifest delivery must match `html[data-artifact-delivery]` when both are present. A persistent declaration documents scope; it does not grant authority. State retention needs the user's request and a separate named lifetime, destination and reset contract.

## Serialize for the actual context

Use JSON serialization, then replace `<` with `\u003c` before embedding in a script data block. Do not HTML-escape JSON quotes into `&quot;`: script data is raw text, so that makes invalid JSON. Avoid hand-built JSON and keep `</script>` from terminating the block.

```python
payload = json.dumps(manifest, ensure_ascii=False).replace("<", r"\u003c")
```

Use HTML escaping for ordinary HTML text/attributes, not for this JSON block. `JSON.parse(element.textContent)` should round-trip the object.

## Mechanical verification

Run `python3 <html-artifact-skill-directory>/scripts/verify_artifact.py path/to/report.html`. Exit 0 means its bounded structural checks passed; exit 1 reports definite violations, and exit 2 reports unreadable input. Review warnings are not acceptance or security certification. The script never executes document JavaScript or contacts remote hosts.

Checks cover metadata, duplicate IDs, fragment and explicit control targets, manifest shape, explicit active external resources and common inline state/network calls. Dynamic expressions, imported code, CSS behaviour, all possible exfiltration and semantic source truth are outside static coverage. Browser evidence must establish the default no-save behaviour of shipped controls. A quoted API name is a review lead, not proof it executes.

Native document fragments are valid. Reject implicit history/URL writes that persist reader selections by default; distinguish them from a link the reader intentionally follows.
