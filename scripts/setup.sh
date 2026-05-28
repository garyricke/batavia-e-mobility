#!/usr/bin/env bash
#
# One-time machine setup for the Batavia "Roll Smart, Ride Safe" end-card workflow.
# Registers the nano-banana image tool with Claude Code using the key from your .env.
#
# Usage:  bash scripts/setup.sh
#
set -euo pipefail

# --- find the project root (the folder that has .env) -------------------------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$ROOT"

say()  { printf "\033[1;34m▸ %s\033[0m\n" "$1"; }
ok()   { printf "\033[1;32m✓ %s\033[0m\n" "$1"; }
die()  { printf "\033[1;31m✗ %s\033[0m\n" "$1" >&2; exit 1; }

say "Setting up the end-card tools…"

# --- 1. prerequisites ---------------------------------------------------------
command -v claude >/dev/null 2>&1 || die "Claude Code isn't installed. Install it first: https://claude.com/claude-code"
command -v node   >/dev/null 2>&1 || die "Node.js isn't installed. Install Node 18+ from https://nodejs.org (the image tool needs it)."
ok "Claude Code and Node.js found."

# --- 2. read the Gemini key from .env ----------------------------------------
[ -f .env ] || die "No .env file in $ROOT. Put the .env you were given in this folder, then re-run."

GEMINI_API_KEY="$(grep -E '^GEMINI_API_KEY=' .env | head -1 | cut -d= -f2- | tr -d '"'\''\r' | xargs)"
[ -n "${GEMINI_API_KEY:-}" ] || die ".env has no GEMINI_API_KEY=… line. Check the .env you were given."
ok "Found GEMINI_API_KEY in .env."

# --- 3. register the nano-banana tool with Claude Code ------------------------
# Remove any prior copy so re-running this is safe.
claude mcp remove nano-banana -s user >/dev/null 2>&1 || true

claude mcp add nano-banana -s user \
  -e GEMINI_API_KEY="$GEMINI_API_KEY" \
  -e GEMINI_MODEL="gemini-3-pro-image-preview" \
  -- npx -y @akashvekariya/nano-banana-mcp

ok "Registered the nano-banana image tool."

# --- 4. done ------------------------------------------------------------------
echo
ok "Setup complete."
echo
say "Next steps:"
echo "  1. Fully quit and reopen Claude Code (so it loads the new tool)."
echo "  2. In Claude Code, type:  check my nano-banana setup"
echo "     You should see: \"Gemini API token is configured and ready to use\""
echo "  3. Then follow end-cards-howto.html to make a card."
