#!/usr/bin/env bash
set -euo pipefail

REPO="quantipixels/skills"
SKILLS_CLI_VERSION=1.5.23
export DISABLE_TELEMETRY=1
dry_run=false
for arg in "$@"; do
  case "$arg" in
    --dry-run) dry_run=true ;;
    --help|-h)
      echo 'Usage: uninstall.sh [--dry-run]'
      echo 'Remove QP-owned names from global Skills CLI targets across hosts.'
      echo 'Preserve independently managed same-name copies before removal.'
      echo 'Native plugins, main-agent profiles, and startup settings are separate.'
      exit 0 ;;
    *) echo "QP uninstall: unknown argument: $arg" >&2; exit 2 ;;
  esac
done
command -v node >/dev/null || { echo 'QP uninstall: Node.js 18+ is required' >&2; exit 1; }
node -e 'if (+process.versions.node.split(".")[0] < 18) process.exit(1)' || exit 1
for name in XDG_STATE_HOME CLAUDE_CONFIG_DIR CODEX_HOME; do
  value=${!name:-}
  [[ -z "$value" || "$value" = /* ]] || { echo "QP uninstall: $name must be absolute" >&2; exit 1; }
done
LOCK_FILE=$(node -e "const { homedir } = require('node:os'); const { join } = require('node:path'); process.stdout.write(process.env.XDG_STATE_HOME ? join(process.env.XDG_STATE_HOME, 'skills', '.skill-lock.json') : join(homedir(), '.agents', '.skill-lock.json'))")

qp_skills() {
  node - "$LOCK_FILE" "$REPO" <<'NODE'
const fs = require('node:fs');
const [lockFile, repository] = process.argv.slice(2);

let lock;
try {
  lock = JSON.parse(fs.readFileSync(lockFile, 'utf8'));
} catch (error) {
  if (error && error.code === 'ENOENT') process.exit(0);
  console.error(`Could not read the global skills lock: ${error.message}`);
  process.exit(1);
}

function normalizeSource(source) {
  return String(source ?? '')
    .trim()
    .replace(/^git\+/, '')
    .replace(/^git@github\.com:/, 'https://github.com/')
    .replace(/^ssh:\/\/git@github\.com\//, 'https://github.com/')
    .replace(/^https?:\/\/github\.com\//, '')
    .replace(/\/+$/, '')
    .replace(/\.git$/, '');
}

const object = value => value !== null && typeof value === 'object' && !Array.isArray(value);
const reject = message => {
  console.error(`Invalid global skills lock: ${message}`);
  process.exit(1);
};
if (!object(lock)) reject('root must be an object');
const entries = lock.skills === undefined ? {} : lock.skills;
if (!object(entries)) reject('skills must be an object');
if (Object.keys(entries).length && lock.version !== 3) reject('unsupported lock version; preserve/migrate it before removal');

const skills = [];
for (const [name, entry] of Object.entries(entries)) {
  if (!object(entry) || typeof entry.source !== 'string') {
    reject('each skill must have an object entry with a string source');
  }
  if (normalizeSource(entry.source) !== repository) continue;
  // Native removal treats wildcards/options specially; never forward them.
  // Validate before newline framing so one lock key stays one argument.
  if (name.length > 64 || !/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(name)) {
    reject('QP skill names must be canonical lowercase ASCII identifiers');
  }
  skills.push(name);
}
skills.sort();

process.stdout.write(skills.join('\n'));
NODE
}

skill_output=$(qp_skills)
skills=()
while IFS= read -r skill; do
  [[ -n "$skill" ]] && skills+=("$skill")
done <<<"$skill_output"

if [[ ${#skills[@]} -eq 0 ]]; then
  echo "No globally installed QP skills found."
  exit 0
fi

if $dry_run; then printf 'Would remove: %s\n' "${skills[@]}"; exit 0; fi
command -v npx >/dev/null || { echo 'QP uninstall: npx is required' >&2; exit 1; }
# The native CLI also checks legacy project-relative paths during global removal.
work=$(mktemp -d)
trap 'rm -rf -- "$work"' EXIT
(cd "$work"; npx --yes "skills@$SKILLS_CLI_VERSION" remove --global --yes "${skills[@]}" </dev/null)

remaining=$(qp_skills)
if [[ -n "$remaining" ]]; then
  remaining=${remaining//$'\n'/, }
  echo "Removal incomplete: $remaining" >&2
  exit 1
fi

echo "All globally installed QP skills were removed."
