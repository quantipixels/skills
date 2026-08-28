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
    .replace(/\.git$/, '')
    .replace(/\/$/, '');
}

const skills = Object.entries(lock.skills ?? {})
  .filter(([, entry]) => normalizeSource(entry?.source) === repository)
  .map(([name]) => name)
  .sort();

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
