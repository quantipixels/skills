#!/usr/bin/env bash
set -euo pipefail

REPO="quantipixels/skills"
LOCK_FILE=$(node -e "const { homedir } = require('node:os'); const { join } = require('node:path'); process.stdout.write(join(homedir(), '.agents', '.skill-lock.json'))")

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

echo "Removing ${#skills[@]} globally installed QP skill(s)."
npx skills remove --global --yes "${skills[@]}"

remaining=$(qp_skills)
if [[ -n "$remaining" ]]; then
  remaining=${remaining//$'\n'/, }
  echo "Removal incomplete: $remaining" >&2
  exit 1
fi

echo "All globally installed QP skills were removed."
