# Wishbone Golf — Shopify

Version-controlled Shopify theme and store tooling for **wishbone.golf**.

| | |
|---|---|
| Storefront | https://wishbone.golf |
| Shopify store | `k500sw-e1.myshopify.com` |
| Live theme ID | `187794981188` *(observed from the storefront on 2026-09-18 — re-verify with `bin/wb list`)* |
| Primary locale / currency | `en-AT` / EUR |
| Cell | `brand` on devbox — preview port **9292** |

The store is **live and selling**. Everything in this repo defaults to read-only or
draft-only. Nothing here publishes a theme; publishing is a manual action in Shopify admin.

## Layout

```
wishbone/
├── theme/              # the theme — mirror of the live theme at last pull, source of truth for code
├── bin/wb              # one wrapper around the Shopify CLI (loads .env, pins the store)
├── scripts/            # Admin API scripts (catalog/metafields) — added as needed
├── docs/SETUP.md       # credentials + GitHub key setup (owner actions)
├── tasks/changes.md    # log of every change pushed to the store
├── tasks/lessons.md    # corrections worth not repeating
└── shopify.theme.toml  # CLI environments (live / draft)
```

## Setup (once)

See [`docs/SETUP.md`](docs/SETUP.md). Short version:

Credentials are already in place (Dev Dashboard app, client-credentials grant — see
[`docs/SETUP.md`](docs/SETUP.md)). Tokens last 24h and `scripts/token.mjs` mints and
caches them automatically, so there is nothing to refresh by hand.

```bash
bin/wb verify            # proves auth works and lists the store's themes
bin/wb pull              # live theme -> theme/   (read-only on Shopify)
```

The baseline pull is already committed, and `main` is pushed to
`git@github.com:mrehb/wishbone_shopify.git`.

## Daily workflow

```bash
bin/wb pull                 # Git <- Shopify   (refresh from live before you start)
bin/wb dev                  # hot-reloading dev theme -> http://devbox:9292
bin/wb check                # theme-check lint
bin/wb draft "Wishbone QA"  # Shopify <- Git   (new UNPUBLISHED theme; live untouched)
bin/wb push <theme-id>      # Shopify <- Git   (into an existing NON-LIVE theme)
```

Then: review the draft's preview URL → publish in Shopify admin by hand → record it in
[`tasks/changes.md`](tasks/changes.md).

`bin/wb dev` uploads a *development* theme (invisible to shoppers, expired by Shopify when
idle) and serves it at http://devbox:9292.

> Authenticated with the store's **Theme Access** password (`shptka_…`, registered to
> mr@ehb.digital). That matters: the CLI's storefront proxy only works with a Theme Access
> token — with the Dev Dashboard app's Admin token the upload succeeds but `:9292` returns
> 401. `scripts/token.mjs` prefers the Theme Access password and falls back to the client
> credentials.

## Safety

- `bin/wb` never passes `--live` or `--allow-live`, and has no publish command.
- `.claude/hooks/guard.sh` blocks live writes, `theme publish`, theme deletion, `.env`
  staging and force-pushes at the tool level — even in bypass-permissions mode.
- Live-theme code is the store's source of truth for **content** (`config/settings_data.json`,
  `templates/*.json`, `sections/*.json`, `locales/*`) because merchandisers edit it in the
  Shopify editor. Pull before you push, or you will overwrite their work.
