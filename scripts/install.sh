#!/usr/bin/env bash
set -euo pipefail

REPO="quantipixels/skills"
REF="ori"
GROUP_ROOT="https://github.com/$REPO/tree/$REF/skills"
RETIRED_SKILLS=(
  alakowe
  product-delivery
  qp-setup
  simplify
  skill-portfolio-audit
  tdd
  tunmo-pr
  unknot
)

usage() {
  cat <<'EOF'
Usage: install.sh [--all|--engineering|--design|--productivity|--experimental]

  --all           Install all stable skills. This is the default.
  --engineering   Install engineering skills.
  --design        Install design skills.
  --productivity  Install productivity skills.
  --experimental  Install experimental skills.
EOF
}

if [[ $# -gt 1 ]]; then
  usage >&2
  exit 2
fi

mode=${1:---all}
case "$mode" in
  --all)
    groups=(engineering design productivity)
    ;;
  --engineering)
    groups=(engineering)
    ;;
  --design)
    groups=(design)
    ;;
  --productivity)
    groups=(productivity)
    ;;
  --experimental)
    groups=(experimental)
    ;;
  --help|-h)
    usage
    exit 0
    ;;
  *)
    echo "Unknown install mode: $mode" >&2
    usage >&2
    exit 2
    ;;
esac

retired_qp_skills() {
  # JavaScript is intentionally single-quoted.
  # shellcheck disable=SC2016
  npx skills list --global --json | node -e '
    const [repository, ...retiredSkills] = process.argv.slice(1);
    let input = "";

    function normalizeSource(source) {
      return String(source ?? "")
        .trim()
        .replace(/^git\+/, "")
        .replace(/^git@github\.com:/, "https://github.com/")
        .replace(/^ssh:\/\/git@github\.com\//, "https://github.com/")
        .replace(/^https?:\/\/github\.com\//, "")
        .replace(/\.git$/, "")
        .replace(/\/$/, "");
    }

    process.stdin.setEncoding("utf8");
    process.stdin.on("data", chunk => { input += chunk; });
    process.stdin.on("end", () => {
      let result;
      try {
        result = JSON.parse(input);
      } catch (error) {
        console.error(`Could not parse the global skills list: ${error.message}`);
        process.exit(1);
      }

      const retired = new Set(retiredSkills);
      const skills = Array.isArray(result) ? result : result.skills ?? [];
      const installed = skills
        .filter(skill => retired.has(skill.name) && normalizeSource(skill.source) === repository)
        .map(skill => skill.name)
        .sort();

      process.stdout.write(installed.join("\n"));
    });
  ' "$REPO" "${RETIRED_SKILLS[@]}"
}

for group in "${groups[@]}"; do
  echo "Installing QP $group skills globally."
  npx skills add "$GROUP_ROOT/$group" --global --all --full-depth
done

retired_output=$(retired_qp_skills)
retired=()
while IFS= read -r skill; do
  [[ -n "$skill" ]] && retired+=("$skill")
done <<<"$retired_output"

if [[ ${#retired[@]} -eq 0 ]]; then
  echo "Selected QP skills are installed. No retired QP skills were found."
  exit 0
fi

echo "Removing ${#retired[@]} retired QP skill(s): ${retired[*]}"
npx skills remove --global --yes "${retired[@]}"

remaining=$(retired_qp_skills)
if [[ -n "$remaining" ]]; then
  remaining=${remaining//$'\n'/, }
  echo "Retired QP skill removal incomplete: $remaining" >&2
  exit 1
fi

echo "Selected QP skills are installed and retired QP skills were removed."
