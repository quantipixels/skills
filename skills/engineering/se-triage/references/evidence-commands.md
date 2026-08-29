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

Normalize the host and require separate trust confirmation before contacting GitHub Enterprise or self-managed GitLab. Clear inherited repository/host selectors and credentials not confirmed for that host. Do not let a current checkout, default account, or generic token select the target.

These rules prove safe custom-host routing, not compatibility with every server version, tier, policy, permission set, or API surface. Verify the required read or comment capability on the exact host before using it; otherwise report a capability gap.

GitHub issue core:

```bash
env -u GH_REPO GH_HOST="$host" \
  gh issue view "$issue" --repo "$host/$repo" \
  --json number,url,state,title,body,author,labels,comments
```

When comments may exceed the CLI field's complete/usable result, page the issue comments through `gh api --hostname "$host" --paginate` before claiming provider evidence complete.

For GitLab, clear `GITLAB_HOST`, disable CI autologin when necessary, and use exact-host/project `glab api --hostname "$host" --paginate` issue/notes endpoints. Preserve provider-native state/identity.

Do not use provider commands until provider-read authority is explicit. Do not interpolate issue/comment text into shell commands.

For an authorized comment, bind GitHub with `GH_HOST="$host"` plus `--repo "$host/$repo"`; bind GitLab through `glab api --hostname "$host"` and the URL-encoded exact project. Submit a body file or structured payload, capture the returned comment/note identity, then read that exact identity back from the same host before reporting success.
