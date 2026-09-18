# Wishbone Golf — Shopify project rules

**wishbone.golf is a live, selling store** (`k500sw-e1.myshopify.com`, live theme
`187794981188` as of 2026-09-18). There is no staging store. Read
[`../README.md`](../README.md) and [`../docs/SETUP.md`](../docs/SETUP.md) first.

## Live-store safety (highest priority)

- **Default to read-only.** Explore and report before changing anything.
- **Never write to the live theme.** Deploys go to a draft (`bin/wb draft`) or a
  development theme (`bin/wb dev`). Publishing is the owner's manual action in Shopify
  admin — never automated, never scripted.
- **Pull before you push.** Merchandisers edit `config/settings_data.json`,
  `templates/*.json`, `sections/*.json` and `locales/*` in the Shopify editor. Those
  files are theirs; the live store is the source of truth for them. Liquid, CSS and JS
  are code, and Git is the source of truth for those.
- **One change at a time**, with a stated rollback (usually: re-pull, or publish the
  previous theme back in admin).
- **Never touch checkout or payment code.** Blocked by the guard hook as well.

`.claude/hooks/guard.sh` enforces the above at the tool level, including in
bypass-permissions mode. If it blocks you, explain why to the owner rather than
working around it.

## How to do things here

| Task | Command |
|------|---------|
| Check credentials / see themes | `bin/wb verify` |
| Refresh from live | `bin/wb pull` |
| See a change against real data | `bin/wb dev` → http://devbox:9292 |
| Lint | `bin/wb check` |
| Hand the owner something to review | `bin/wb draft "<what it is>"` → give them the preview URL |

Never start an ad-hoc web server for theme work — `bin/wb dev` renders the theme against
the real store. Port **9292** is this cell's Shopify theme port; **3002** is the generic
preview port.

## Session habits

- Record anything pushed to the store in `tasks/changes.md` (date, theme, files, why).
- Record corrections in `tasks/lessons.md`.
- Reports and audits for the owner get published with
  `~/.claude/bin/artifact <file>.html --title "…" --project wishbone`, and the printed
  `TFF ▸` line goes into the reply. Theme files are not artifacts.
- Work on a branch and open a pull request for anything non-trivial; `main` should
  always match what is deployable.
