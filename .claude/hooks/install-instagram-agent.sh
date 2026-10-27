#!/bin/bash
# Installs the instagram-agent plugin (provides /ig-reel and friends) in cloud
# sessions. Pinned to a reviewed commit; bump IG_REF after reviewing upstream.
set -euo pipefail

[ "${CLAUDE_CODE_REMOTE:-}" = "true" ] || exit 0

IG_REPO=https://github.com/Jakeschincariol/instagram-agent-skill
IG_REF=d03c56bb598be770c60b201f94237e5d1a4268a6
IG_DIR="$HOME/.cache/instagram-agent-skill-$IG_REF"

if claude plugin list </dev/null 2>/dev/null | grep -q 'instagram-agent@instagram-agent-skill'; then
  exit 0
fi

if [ "$(git -C "$IG_DIR" rev-parse HEAD 2>/dev/null)" != "$IG_REF" ]; then
  rm -rf "$IG_DIR"
  git init -q "$IG_DIR"
  git -C "$IG_DIR" fetch -q --depth 1 "$IG_REPO" "$IG_REF"
  git -C "$IG_DIR" checkout -q FETCH_HEAD
fi

claude plugin marketplace add "$IG_DIR" </dev/null >/dev/null
claude plugin install instagram-agent@instagram-agent-skill </dev/null >/dev/null
