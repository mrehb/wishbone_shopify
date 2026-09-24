# German storefront (wishbone.golf/de)

English stays the primary language. German is added as a second language and stored as
Shopify translations; no English content is overwritten. Nothing here is live until the
owner publishes German in Shopify admin.

- `store.json` — products (27), collections (5), the contact page, menu links, colour
  option names/values and the 16 theme texts (homepage, product templates, password page).
  Each field pins the English it translates, so edits made in admin later show up as *stale*
  instead of being overwritten with old German.
- `policies/*.html` — the six legal policies. **Need legal review before `--policies`.**
- Theme interface strings come from `theme/locales/de.json` (complete, 382/382 keys).
- The contact form (forms.bigmaxgolf.com) gets German from bigmax-forms
  branch `feat/wishbone-contact-de`.

## Going live

1. Dev Dashboard → the store's app → add scopes `read_translations write_translations
   read_locales write_locales read_products read_content read_online_store_navigation
   read_shipping`, release a version, reinstall on the store.
2. `node scripts/translate-de.mjs plan` — dry run.
3. `node scripts/translate-de.mjs apply --enable-locale` — adds German unpublished, writes it.
4. Preview in admin (Settings → Languages → German → Preview), then publish there and assign
   German to the AT/DE markets as their default if wanted.

## Decisions taken while translating

- *Sie* throughout, Austrian legal terms (Rücktritt, FAGG, KSchG, UID-Nr., Impressum).
- Product names stay as they are (Wishbone ONE/TWO/THREE, NEO, EON); "Wishbone Three" in
  body copy became "Wishbone THREE" per the 2026-09-20 naming ruling.
- URL handles are not translated, so no links or redirects change.
- Colours: charcoal → Anthrazit, lime → Limette (e.g. `charcoal-lime` → Anthrazit-Limette).

## Found in the English while translating (not changed)

- The THREE's "User manual" link points to the **TWO** manual PDF.
- ONE copy claims "under 4 kg … lightest in its class" — never weighed (see brand v5 notes).
- EON "folding dimensions 102 × 94 × 57 cm" look like unfolded dimensions.
- The refund policy and terms refer to a withdrawal form "Appendix A" that is not published.
- Announcement bar (disabled) still says shipping resumes 17 November 2025.
- `page.about` template holds Shopify placeholder text; no page uses it.
