#!/usr/bin/env bash
# Install the global skill bundle; native plugin/main-agent setup stays separate.
set -euo pipefail

REPO=quantipixels/skills
SKILLS_CLI_VERSION=1.5.23
export DISABLE_TELEMETRY=1
ref=ori
prune=false
dry_run=false
agents=()
usage() {
  cat <<'HELP'
Usage: install.sh [--codex] [--claude] [--ref BRANCH_OR_TAG] [--prune] [--dry-run]

Install all QP skills globally through the pinned Skills CLI. Default: Codex.
  --codex    Use the shared ~/.agents/skills discovery path.
  --claude   Also/instead link skills for Claude Code (not its plugin).
  --ref REF  Published branch or tag; default: ori. Commit SHAs are unsupported.
  --prune    Remove retired QP-owned names across global Skills CLI targets
             only after the installed bundle passes verification.
  --dry-run  Fetch/check the candidate and report changes without installing.
  --help     Show this help.

Requires Node.js 18+, npx, curl, and Git. Updates replace QP-owned copies.
Keep local edits in a checkout. Use `npx skills add .` for uncommitted files.
Pruning uses native name-based removal across hosts, including unselected hosts;
preserve independently managed same-name copies before using --prune.
No hooks, credentials, main-agent profiles, or startup defaults are installed.
Use the native Claude plugin instead for Pepeye; do not use both Claude paths.
HELP
}
fail() { printf 'QP install: %s\n' "$*" >&2; exit 1; }
while [[ $# -gt 0 ]]; do
  case "$1" in
    --codex) agents+=(codex) ;;
    --claude) agents+=(claude-code) ;;
    --ref) [[ $# -ge 2 && -n "$2" && "$2" != -* ]] || fail '--ref requires a branch or tag'; ref=$2; shift ;;
    --prune) prune=true ;;
    --dry-run) dry_run=true ;;
    --help|-h) usage; exit 0 ;;
    *) fail "unknown argument: $1 (see --help)" ;;
  esac
  shift
done
[[ ${#agents[@]} -gt 0 ]] || agents=(codex)
[[ ! "$ref" =~ ^[a-fA-F0-9]{40}$ ]] || fail 'the pinned Skills CLI requires a branch or tag, not a commit SHA'
for tool in node curl git; do command -v "$tool" >/dev/null || fail "$tool is required"; done
git check-ref-format "refs/heads/$ref" >/dev/null || fail 'invalid branch/tag name'
node -e 'if (+process.versions.node.split(".")[0] < 18) process.exit(1)' || fail 'Node.js 18+ is required'
if ! $dry_run; then command -v npx >/dev/null || fail 'npx is required'; fi
# Keep configured locations stable when native commands run outside the caller project.
for name in XDG_STATE_HOME CLAUDE_CONFIG_DIR CODEX_HOME; do
  value=${!name:-}
  [[ -z "$value" || "$value" = /* ]] || fail "$name must be an absolute path"
done
work=$(mktemp -d)
trap 'rm -rf -- "$work"' EXIT
fetch() { curl --fail --silent --show-error --location --proto '=https' --proto-redir '=https' --connect-timeout 10 --max-time 60 "$1" -o "$2"; }
encoded_ref=$(node -e 'process.stdout.write(encodeURIComponent(process.argv[1]))' -- "$ref")
fetch "https://api.github.com/repos/$REPO/commits/$encoded_ref" "$work/commit.json"
sha=$(node -e 'const s=require(process.argv[1]).sha; if(!/^[a-f0-9]{40}$/.test(s)) process.exit(1); process.stdout.write(s)' "$work/commit.json")
fetch "https://raw.githubusercontent.com/$REPO/$sha/.claude-plugin/plugin.json" "$work/manifest.json"
fetch "https://api.github.com/repos/$REPO/git/trees/$sha?recursive=1" "$work/tree.json"

check() {
  node - "$work" "$1" "$ref" "${agents[@]}" <<'NODE'
const fs = require('node:fs');
const path = require('node:path');
const os = require('node:os');
const crypto = require('node:crypto');
const [work, phase, ref, ...agents] = process.argv.slice(2);
const object = v => v !== null && typeof v === 'object' && !Array.isArray(v);
const validName = n => n.length <= 64 && /^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(n);
const normalize = s => s.trim().replace(/^git\+/, '').replace(/^git@github\.com:/, 'https://github.com/')
  .replace(/^ssh:\/\/git@github\.com\//, 'https://github.com/').replace(/^https?:\/\/github\.com\//, '').replace(/\/+$/, '').replace(/\.git$/, '');
const home = os.homedir();
const root = path.join(home, '.agents', 'skills');
const lockPath = process.env.XDG_STATE_HOME ? path.join(process.env.XDG_STATE_HOME, 'skills/.skill-lock.json') : path.join(home, '.agents/.skill-lock.json');
const claude = path.join(process.env.CLAUDE_CONFIG_DIR?.trim() || path.join(home, '.claude'), 'skills');
const stat = p => { try { return fs.lstatSync(p); } catch (e) { if (e.code === 'ENOENT') return null; throw e; } };
const owned = entry => entry && normalize(entry.source) === 'quantipixels/skills';
const json = file => JSON.parse(fs.readFileSync(file, 'utf8'));
try {
  const manifest = json(path.join(work, 'manifest.json'));
  if (!object(manifest) || manifest.name !== 'qp-skills' || !Array.isArray(manifest.skills) || !manifest.skills.length)
    throw new Error('invalid or empty QP manifest');
  const skills = manifest.skills.map(p => {
    const m = typeof p === 'string' && /^\.\/skills\/(engineering|design|productivity|experimental)\/([a-z0-9-]+)$/.exec(p);
    if (!m || !validName(m[2])) throw new Error('invalid manifest skill path');
    return {name: m[2], prefix: p.slice(2) + '/'};
  });
  const names = skills.map(s => s.name).sort();
  if (new Set(names).size !== names.length) throw new Error('duplicate skill names');
  const tree = json(path.join(work, 'tree.json'));
  if (!object(tree) || tree.truncated !== false || !Array.isArray(tree.tree)) throw new Error('incomplete source tree');
  let lock = {};
  try { lock = json(lockPath); } catch (e) { if (e.code !== 'ENOENT') throw e; }
  if (!object(lock) || (lock.skills !== undefined && !object(lock.skills))) throw new Error('invalid skills lock');
  const entries = lock.skills || {};
  if (Object.keys(entries).length && lock.version !== 3) throw new Error('unsupported lock version; preserve/migrate it before installation');
  for (const [name, e] of Object.entries(entries)) {
    if (!object(e) || typeof e.source !== 'string') throw new Error('invalid skills lock entry');
    if (owned(e) && !validName(name)) throw new Error('unsafe QP skill name');
  }
  for (const {name, prefix} of skills) {
    const files = tree.tree.filter(e => e.path?.startsWith(prefix) && e.type === 'blob');
    if (!files.some(e => e.path === prefix + 'SKILL.md')) throw new Error(`missing entrypoint in source: ${name}`);
    const target = path.join(root, name), s = stat(target), alias = path.join(claude, name), a = stat(alias);
    if (phase === 'before') {
      if ((entries[name] && !owned(entries[name])) || (s && !owned(entries[name]))) throw new Error(`unowned skill collision: ${name}`);
      if (s && !s.isDirectory()) throw new Error(`canonical skill is not a directory: ${target}`);
      if (agents.includes('claude-code') && a && !(owned(entries[name]) && a.isSymbolicLink() && path.resolve(claude, fs.readlinkSync(alias)) === target))
        throw new Error(`unmanaged Claude skill: ${alias}`);
    } else {
      if (!owned(entries[name]) || entries[name].ref !== ref || !s?.isDirectory()) throw new Error(`installation incomplete: ${name}`);
      for (const file of files) {
        const relative = file.path.slice(prefix.length);
        if (relative.split('/').some(p => !p || p === '.' || p === '..') || !['100644', '100755'].includes(file.mode))
          throw new Error(`unsupported source path/mode: ${file.path}`);
        const dest = path.join(target, relative);
        if (!stat(dest)?.isFile()) throw new Error(`missing installed file: ${file.path}`);
        const bytes = fs.readFileSync(dest);
        const hash = crypto.createHash('sha1').update(`blob ${bytes.length}\0`).update(bytes).digest('hex');
        if (hash !== file.sha) throw new Error(`installed content differs from selected revision: ${file.path}`);
      }
      if (agents.includes('claude-code') && (!a?.isSymbolicLink() || fs.realpathSync(alias) !== fs.realpathSync(target)))
        throw new Error(`Claude link missing or incorrect: ${name}`);
    }
  }
  const stale = Object.keys(entries).filter(n => owned(entries[n]) && !names.includes(n)).sort();
  if (phase === 'before') {
    fs.writeFileSync(path.join(work, 'names'), names.join('\n') + '\n');
    fs.writeFileSync(path.join(work, 'stale'), JSON.stringify(stale));
    console.log(`Candidate: ${names.length} skills. Retired QP names: ${stale.join(', ') || 'none'}.`);
  } else if (phase === 'installed') {
    const previous = json(path.join(work, 'stale'));
    for (const name of previous) if (entries[name] && !owned(entries[name])) throw new Error(`ownership changed before pruning: ${name}`);
    // A removed lock entry no longer authorizes cleanup of that name.
    fs.writeFileSync(path.join(work, 'remove'), previous.filter(n => owned(entries[n])).join('\n'));
  } else if (stale.length) throw new Error(`pruning incomplete: ${stale.join(', ')}`);
} catch (e) { console.error(`QP install: ${e.message}`); process.exit(1); }
NODE
}
check before
printf 'Source: %s @ %s (%s)\nTargets: %s (global)\n' "$REPO" "$ref" "$sha" "${agents[*]}"
if $dry_run; then printf 'Dry run: refresh managed skills; prune=%s. No installation changes.\n' "$prune"; exit 0; fi
names=()
while IFS= read -r name; do names+=("$name"); done < "$work/names"
(cd "$work"; npx --yes "skills@$SKILLS_CLI_VERSION" add "https://github.com/$REPO#$encoded_ref" --global --agent "${agents[@]}" --skill "${names[@]}" --yes </dev/null)
check installed
if $prune; then
  stale=()
  while IFS= read -r name || [[ -n "$name" ]]; do [[ -n "$name" ]] && stale+=("$name"); done < "$work/remove"
  if [[ ${#stale[@]} -gt 0 ]]; then
    (cd "$work"; npx --yes "skills@$SKILLS_CLI_VERSION" remove --global --yes "${stale[@]}" </dev/null)
  fi
  check pruned
fi
printf 'QP skills verified against %s. Restart the selected host to discover them.\n' "$sha"
