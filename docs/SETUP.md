# Wishbone Shopify — setup

Two credentials are needed, both created by the owner. Nothing else is outstanding:
the project, tooling, guardrails and Git config are already in place on devbox.

---

## 1. Shopify: a Theme Access token  (≈3 minutes)

The devbox container is headless, so the Shopify CLI's browser login cannot be used.
The supported headless credential for theme work is a **Theme Access** password.

1. Shopify admin for **Wishbone** → **Settings → Apps and sales channels → Shopify App Store**
   → install the free **Theme Access** app (by Shopify).
2. Open Theme Access → **Create password**.
   - Email: your address (the token is mailed there).
   - Name it `devbox brand cell` so it can be revoked on its own later.
3. The mail contains a password starting with `shptka_`. Paste it into
   `/workspace/wishbone/.env`:

   ```
   SHOPIFY_CLI_THEME_TOKEN=shptka_…
   ```

4. Prove it works:

   ```bash
   cd /workspace/wishbone && bin/wb verify
   ```

   That lists every theme in the store with its ID and role, and prints the live theme ID.
   It changes nothing on the store.

A Theme Access token can read and write **themes only** — it cannot touch orders,
customers or products. That is deliberate: it is the smallest credential that does the job.
If this project later needs catalog or metafield scripts, create a separate custom app
(Settings → Apps → Develop apps) and put its `shpat_` token in `ADMIN_API_TOKEN`.

**Revoking:** delete the password in the Theme Access app. Do that if the box is ever
lost or sold.

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
