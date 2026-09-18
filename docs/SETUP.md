# Wishbone Shopify — setup

Two credentials are needed, both created by the owner. Nothing else is outstanding:
the project, tooling, guardrails and Git config are already in place on devbox.

---

## 1. Shopify: app credentials — DONE (2026-09-18)

The store is reached with a **Dev Dashboard app** using the OAuth client-credentials
grant, the same pattern as the BIG MAX US/UK stores. The owner supplied the credentials
on 2026-09-18 and they are in `/workspace/wishbone/.env` (mode 0600, git-ignored):

```
SHOP=k500sw-e1.myshopify.com
CLIENT_ID=…
CLIENT_SECRET=shpss_…
```

Granted scopes, read back from Shopify: `write_themes`, `write_theme_code`,
`write_legal_policies`. Themes only — the app cannot see orders, customers or products.
If this project later needs catalog or metafield scripts, add scopes to the app in the
Shopify Dev Dashboard (or create a second app) rather than reusing this one blindly.

Since 2026-09-18 the **Theme Access** app is also installed and its password
(`SHOPIFY_CLI_THEME_TOKEN`, registered to mr@ehb.digital) is what `bin/wb` actually uses —
the client credentials stay as the fallback. Both work for pull/push/list/check, but only
the Theme Access password makes `bin/wb dev`'s preview on `:9292` work. Revoke it in the
Theme Access app if this box is ever lost.

Access tokens from the client-credentials grant live **24 hours**. `scripts/token.mjs` mints one on demand,
caches it in `.shopify-token.json` (0600, git-ignored) and refreshes it 5 minutes before
expiry, so nothing long-lived is stored and no command ever needs a manual refresh.
`bin/wb` calls it for you; `node scripts/token.mjs --force` mints a fresh one.

Proof it works:

```bash
cd /workspace/wishbone && bin/wb verify
```

**Rotating:** regenerate the client secret in the Shopify Dev Dashboard and replace
`CLIENT_SECRET` in `.env`. Worth doing if the box is ever lost — and note these values
were pasted into a chat session, so they exist in that transcript too.

---

## 2. GitHub: repository and deploy key — DONE (2026-09-18)

- Repository: **`git@github.com:mrehb/wishbone_shopify.git`** (note the underscore).
- Key: `~/.claude/ssh/mrehb__wishbone_shopify.key`, selected by this repo's
  `core.sshCommand`. Public key also in `docs/deploy-key.pub`.
- `main` is pushed and tracking `origin/main`.

Deploy keys are per repository by design: this cell cannot reach any other repo, and no
other cell can reach this one. `ERROR: Repository not found.` means the key is not on that
repo (or the repo name is wrong) — `ssh -i <key> -T git@github.com` answers with the repo
the key actually belongs to, which is how the `wishbone-shopify` / `wishbone_shopify`
naming mismatch was found.

CI (`.github/workflows/ci.yml`) runs theme-check on pull requests and on `main`. It never
contacts the store, and no Shopify credentials are stored in GitHub — deploys run from
devbox. A deploy key cannot read the Actions API, so check the run's result in the GitHub
UI.

---

## 3. First real step after the credentials land

```bash
cd /workspace/wishbone
bin/wb pull                                   # live theme -> theme/
git add theme && git commit -m "Baseline: live theme"
bin/wb check                                  # see what the theme lints like
```

That first commit is the baseline every future diff is read against. Until it exists,
there is no record of what the live store actually contains.
