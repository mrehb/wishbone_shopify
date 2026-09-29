# Change log — what we pushed to the Wishbone store

One entry per change that reached Shopify. Newest first.

| Date | Theme ID / name | Files | What changed | Published by |
|------|-----------------|-------|--------------|--------------|
| 2026-09-29 | Live `German - language switcher in footer` #191587844420 | — (translations) | Theme-text German did not follow the publish: /de homepage was English. Re-registered 26 theme fields on the new live theme; plan = 173/173 current; EN-vs-DE crawl of 36 pages finds only prices, model names, SKUs left identical. | n/a |
| 2026-09-29 | Draft `German - language switcher in footer` #191587844420 | sections/footer-group.json | Footer language selector on (header one was already on, but on phones it only sits at the bottom of the ☰ menu). Verified on the draft preview at 390 px: footer shows Language ▾, Deutsch → /de. Rollback: don't publish / delete the draft. | owner, 2026-09-29 |
| 2026-09-25 | — (store, not theme) | i18n/de/store.json via scripts/translate-de.mjs | German added as a second language, **unpublished**; 167 translations registered (44 products incl. 17 drafts, 5 collections, contact page, 7 menu links, colour options, 16 theme texts, shipping rate names, filter labels). Legal policies not sent (await review). Verified: plan = 167 current / 0 to write; storefront still English, /de 404. Rollback: Settings → Languages → German → Remove. | not published — owner publishes in Settings → Languages |
| 2026-09-18 | Development `(d8b268-brand)` #191292408132 | all (363) | Path test: pushed the freshly pulled baseline back into a development theme to prove the deploy path. No visible change — same files that were pulled. Development themes are invisible to shoppers and expire on their own. | n/a (never published) |
| 2026-09-18 | — | — | Project created on devbox (brand cell). Live theme #187794981188 pulled as the baseline. | — |
