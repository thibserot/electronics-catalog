#!/usr/bin/env bash
# scripts/install-git-hooks.sh
# Installs a pre-commit hook that runs `make registry_stickers`
# and auto-adds generated files to the current commit.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
HOOK_DIR="${REPO_ROOT}/.git/hooks"
HOOK_FILE="${HOOK_DIR}/pre-commit"

mkdir -p "${HOOK_DIR}"

cat > "${HOOK_FILE}" <<'HOOK'
#!/usr/bin/env bash
set -euo pipefail

# Ensure we are at repo root
REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "${REPO_ROOT}"

# Regenerate registry + stickers/QR before committing
echo "[pre-commit] Running: make registry_stickers"
make registry_stickers

# Stage generated artifacts so they are included in the commit
git add \
  docs/components/stickers/id_registry.yaml \
  docs/components/stickers/id_registry_simple.yaml \
  docs/registry/index.md \
  docs/components/stickers/*.png \
  docs/components/stickers/index.csv \
  docs/components/stickers/sheets.csv \
  docs/components/stickers/sheet_*.png \
  docs/qr/

# Optionally: fail if there are unformatted or unexpected changes elsewhere
# Uncomment to enforce a clean tree (excluding the staged artifacts above)
# if ! git diff --quiet; then
#   echo "[pre-commit] Unstaged changes remain. Please review and stage them." >&2
#   exit 1
# fi

echo "[pre-commit] OK"
HOOK

chmod +x "${HOOK_FILE}"
echo "Installed pre-commit hook at ${HOOK_FILE}"
