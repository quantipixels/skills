# ADR format

Use this fallback only when the repository has no ADR convention.

Store records in `docs/adr/` with sequential names such as `0001-short-title.md`. Create the directory only when the first qualifying ADR is authorized. Scan existing records and increment the highest number.

## Minimum record

```markdown
# <Short decision title>

<A short paragraph stating the context, what was decided, and why.>
```

That can be the complete ADR. Add status metadata, considered options, or consequences only when they preserve information a future maintainer will need. Do not add empty sections or boilerplate.
