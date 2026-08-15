# ADR format

Use this fallback only when the repository has no ADR convention.

Store records in `docs/adr/` with names such as `YYYYMMDD-short-title.md`. Add time only when two independent decisions on the same date would otherwise collide. Create the directory only when the first qualifying ADR is authorized.

## Minimum record

```markdown
# <Short decision title>

<A short paragraph stating the context, what was decided, and why.>
```

That can be the complete ADR. Add status, considered options, consequences, or supersession links only when they preserve information a future maintainer will need. Do not add empty sections or boilerplate.
