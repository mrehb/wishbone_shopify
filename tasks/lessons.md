# Lessons — Wishbone

Corrections worth not repeating. Add one after any mistake or surprise.

- **2026-09-18 — the store is live from day one.** wishbone.golf has been selling on
  Shopify since before this repo existed (live theme `187794981188`, observed 2026-09-18).
  There is no staging store. Every change goes to a draft or development theme first.
- **2026-09-18 — merchandisers own the content files.** `config/settings_data.json`,
  `templates/*.json`, `sections/*.json` and `locales/*` are edited in the Shopify editor.
  Pull before you push or you silently revert their work.
