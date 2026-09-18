#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# Wishbone guard hook — hard deny-list for Claude Code in this project.
#
# Runs before every Bash command. Exit 2 blocks the command and shows the
# message to Claude Code; exit 0 allows it. This turns the prose rules in
# .claude/CLAUDE.md into rules that hold even in bypass-permissions mode.
#
# Everything is allowed EXCEPT operations that can hurt the live storefront or
# leak credentials. Edit this file if a rule is genuinely in the way — it is a
# safety net for the owner, not a lock imposed on them.
# ---------------------------------------------------------------------------
set -euo pipefail

INPUT="$(cat)"
CMD="$(printf '%s' "$INPUT" | node -e 'let d="";try{d=require("fs").readFileSync(0,"utf8")}catch(e){}try{const j=JSON.parse(d);process.stdout.write(String((j.tool_input&&j.tool_input.command)||""))}catch(e){process.stdout.write("")}')"
[ -z "$CMD" ] && exit 0

block () {
  echo "BLOCKED by Wishbone guardrails: $1" >&2
  echo "wishbone.golf is a live store. Use 'bin/wb draft' and publish by hand in Shopify admin." >&2
  exit 2
}

# 1. Writing to, or publishing, the live theme.
if echo "$CMD" | grep -qE 'theme[[:space:]]+push' && echo "$CMD" | grep -qE -- '(--allow-live|--live|[[:space:]]-l([[:space:]]|$)|[[:space:]]-a([[:space:]]|$))'; then
  block "pushing to the LIVE theme."
fi
if echo "$CMD" | grep -qE 'theme[[:space:]]+push' && echo "$CMD" | grep -qE -- '(--publish|[[:space:]]-p([[:space:]]|$))'; then
  block "publishing a theme as part of a push."
fi
if echo "$CMD" | grep -qE 'theme[[:space:]]+publish|themePublish|"role"[[:space:]]*:[[:space:]]*"main"|role=main'; then
  block "publishing a theme. Publishing to live is a manual action in Shopify admin."
fi

# 2. Deleting themes — irreversible, and a deleted live theme takes the store down.
if echo "$CMD" | grep -qE 'theme[[:space:]]+delete|themeDelete'; then
  block "deleting a theme. Theme deletion cannot be undone; do it in Shopify admin if you mean it."
fi

# 3. Checkout / payment surface.
if echo "$CMD" | grep -qiE 'checkout\.liquid|write_checkouts|paymentsAppConfigure'; then
  block "touching checkout/payment code."
fi

# 4. Credential hygiene.
if echo "$CMD" | grep -qE 'git[[:space:]]+add[^|;&]*\.env([[:space:]]|$)'; then
  block "staging the .env file. Credentials never enter Git."
fi
if echo "$CMD" | grep -qE '(curl|wget)[^|;&]*\.env([[:space:]]|$)'; then
  block "sending the .env file over the network."
fi

# 5. History destruction.
if echo "$CMD" | grep -qE 'git[[:space:]]+push[^|;&]*(--force([[:space:]]|$)|[[:space:]]-f([[:space:]]|$))'; then
  block "force-pushing."
fi

exit 0
