# Change log — what we pushed to the Wishbone store

One entry per change that reached Shopify. Newest first.

| Date | Theme ID / name | Files | What changed | Published by |
|------|-----------------|-------|--------------|--------------|
| 2026-09-18 | Development `(d8b268-brand)` #191292408132 | all (363) | Path test: pushed the freshly pulled baseline back into a development theme to prove the deploy path. No visible change — same files that were pulled. Development themes are invisible to shoppers and expire on their own. | n/a (never published) |
| 2026-09-18 | — | — | Project created on devbox (brand cell). Live theme #187794981188 pulled as the baseline. | — |

## 2026-09-25 — German added as a second language (unpublished)

- **Store, not theme:** `shopLocaleEnable(de)` — German added, **unpublished**; English stays primary.
- 167 German translations registered via `scripts/translate-de.mjs apply --enable-locale`:
  44 products (27 active + 17 drafts), 5 collections, contact page, 7 menu links, colour
  options, 16 theme texts, shipping rate names, filter labels. Source: `i18n/de/store.json`.
- **Not sent:** the six legal policies (await legal review → `apply --policies`).
- Verified: `plan` reports 167 current / 0 to write; wishbone.golf still serves English, /de 404 until published.
- Rollback: Settings → Languages → German → Remove (deletes the translations); English untouched.
