#!/bin/sh
# Run the CI checks in a uv environment, without installing into system Python.
set -eu

if ! command -v uv >/dev/null 2>&1; then
    echo "check: uv is required; install it from https://docs.astral.sh/uv/getting-started/installation/ and rerun npm run check." >&2
    exit 127
fi

root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$root"
exec uv run --no-project --isolated --python 3.12 \
    --with-requirements "$root/requirements-dev.txt" \
    python "$root/scripts/check.py" "$@"
