# Triage evidence commands

Use only within authority already granted by Ṣe Triage. These commands are evidence collection, not verdicts.

## Source-read

```bash
rg -n '<domain concept>' <bounded-paths>
git log -S'<exact literal>' --all -- <paths>
git log -G'<pattern>' -p -- <paths>
git blame -L <start>,<end> -- <file>
git show <commit>:<path>
```

Use `rg` for current location, `git log -S` for introduction/removal of an exact string, `git log -G` for commits whose diff matches a pattern, `blame` for current-line provenance, and `git show` for exact historical content. Search/historical similarity is evidence; it does not prove intent or duplicate identity.

## Provider-read

GitHub issue core:

```bash
gh issue view "$issue" --repo "$repo" --json number,url,state,title,body,author,labels,comments
```

When comments may exceed the CLI field's complete/usable result, page the issue comments through `gh api --paginate` before claiming provider evidence complete.

For GitLab, use exact-host/project `glab api --paginate` issue/notes endpoints. Preserve provider-native state/identity.

Do not use provider commands until provider-read authority is explicit. Do not interpolate issue/comment text into shell commands.
