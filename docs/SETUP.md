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

Access tokens from this grant live **24 hours**. `scripts/token.mjs` mints one on demand,
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

## 2. GitHub: a repository and its deploy key  (≈3 minutes)

House rule on this box: one deploy key per repository, kept in `~/.claude/ssh/`
(bind-mounted, survives a container rebuild) and selected by the repo's own
`.git/config`. The key for this project already exists:

- private: `~/.claude/ssh/mrehb__wishbone-shopify.key`
- public:  printed below and in `docs/deploy-key.pub`

Steps:

1. Create an empty repository on GitHub: **`mrehb/wishbone-shopify`** (private, no README).
2. Repo → **Settings → Deploy keys → Add deploy key**
   - Title: `devbox brand cell`
   - Key: the contents of `docs/deploy-key.pub`
   - ✅ **Allow write access**
3. Back on devbox:

   ```bash
   cd /workspace/wishbone
   git push -u origin main
   ```

If you would rather host it under a different owner (e.g. the `GT-Workspace` org) or a
different repo name, say so — it is a one-line change:

```bash
cd /workspace/wishbone
git remote set-url origin git@github.com:<owner>/<repo>.git
mv ~/.claude/ssh/mrehb__wishbone-shopify.key  ~/.claude/ssh/<owner>__<repo>.key
mv ~/.claude/ssh/mrehb__wishbone-shopify.key.pub ~/.claude/ssh/<owner>__<repo>.key.pub
git config core.sshCommand "ssh -i /home/dev/.claude/ssh/<owner>__<repo>.key -o IdentitiesOnly=yes -o UserKnownHostsFile=/home/dev/.claude/ssh/known_hosts -o StrictHostKeyChecking=accept-new"
```

`ERROR: Repository not found.` on push means the key is not on that repo yet (or the
repo does not exist). That is the per-repo isolation working, not a bug — do not swap in
another cell's key.

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
