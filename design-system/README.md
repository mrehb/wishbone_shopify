# Wishbone design-system bundle

Ten self-contained previews that make up the Wishbone brand kit in Claude Design
(claude.ai/design). Each file's first line is the `@dsCard` marker Claude Design reads to
build its card index, so the folder *is* the manifest.

```
foundations/  colour · typography · logo · geometry
components/   buttons · variant-pills · product-card · forms · sections · voice
assets/       the two logo PNGs (also inlined into logo.html so previews stand alone)
build.py      regenerates every preview from one shared shell
```

Values come from [`../docs/brand/tokens.css`](../docs/brand/tokens.css) and are documented
in [`../docs/brand/BRAND_KIT.md`](../docs/brand/BRAND_KIT.md). Change a token there, mirror it
in `build.py`, re-run `python3 build.py`, then re-push — the kit and the store stay in step.

## Pushing to Claude Design

Requires design-system authorization, which cannot be done from a Remote Control session:

1. On devbox: `cd /srv/cells/brand && docker compose exec dev claude`
2. In that session: `/design-login`, complete the browser flow, then exit.
3. Back in any brand-cell session, Claude runs DesignSync: list projects → create or pick the
   Wishbone project → finalize a plan → write these files.

The login lands in `/home/dev/.claude`, which is bind-mounted, so it survives a container
rebuild and every later session reuses it.
