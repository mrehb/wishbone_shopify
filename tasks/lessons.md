# Lessons — Wishbone

Corrections worth not repeating. Add one after any mistake or surprise.

- **2026-09-18 — the store is live from day one.** wishbone.golf has been selling on
  Shopify since before this repo existed (live theme `187794981188`, observed 2026-09-18).
  There is no staging store. Every change goes to a draft or development theme first.
- **2026-09-18 — merchandisers own the content files.** `config/settings_data.json`,
  `templates/*.json`, `sections/*.json` and `locales/*` are edited in the Shopify editor.
  Pull before you push or you silently revert their work.
- **2026-09-18 — `theme dev`'s local preview needs a Theme Access password.** Pull, push,
  list and check all work fine with the Dev Dashboard app's client-credentials token, and
  `theme dev` does upload the development theme — but the proxy at `:9292` answers 401
  (*"The access token provided is expired, revoked, malformed, or invalid"*). Not a broken
  setup: the CLI's storefront proxy wants `shptka_`, not `shpat_`. Preview in the Shopify
  theme editor, or install the Theme Access app and set `SHOPIFY_CLI_THEME_TOKEN`.
- **2026-09-18 — `pkill -f "theme dev"` kills the shell running it.** The pattern matches
  the invoking command line too. Kill by PID.
