# Lessons — Wishbone

Corrections worth not repeating. Add one after any mistake or surprise.

- **2026-09-18 — the store is live from day one.** wishbone.golf has been selling on
  Shopify since before this repo existed (live theme `187794981188`, observed 2026-09-18).
  There is no staging store. Every change goes to a draft or development theme first.
- **2026-09-18 — merchandisers own the content files.** `config/settings_data.json`,
  `templates/*.json`, `sections/*.json` and `locales/*` are edited in the Shopify editor.
  Pull before you push or you silently revert their work.
- **2026-09-18 — `theme dev`'s local preview needs a Theme Access password; RESOLVED.**
  Pull, push, list and check all work with the Dev Dashboard app's client-credentials token,
  and `theme dev` uploads fine with it — but the proxy at `:9292` answered 401 (*"The access
  token provided is expired, revoked, malformed, or invalid"*). The CLI's storefront proxy
  wants `shptka_`, not `shpat_`. Fixed the same day by installing the Theme Access app and
  putting its password in `.env`; `:9292` then served the storefront at 200. If a future
  token is ever swapped back to client credentials, expect the 401 to return.
- **2026-09-18 — `pkill -f "theme dev"` kills the shell running it.** The pattern matches
  the invoking command line too. Kill by PID.
