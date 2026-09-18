/**
 * Print a valid Shopify access token for the Wishbone store.
 *
 * The app is a Dev Dashboard app, so its tokens come from the OAuth
 * client-credentials grant and last 24 hours. This resolves one, caches it in
 * .shopify-token.json (git-ignored, 0600) and reuses it until it is close to
 * expiring, so a session does not mint a new token per command.
 *
 * Resolution order:
 *   1. SHOPIFY_CLI_THEME_TOKEN in .env  — a static Theme Access password, if we ever use one
 *   2. CLIENT_ID + CLIENT_SECRET        — client-credentials grant (the normal path)
 *
 * Usage: node scripts/token.mjs [--force]   (prints the token, nothing else)
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const CACHE = path.join(root, '.shopify-token.json');
const SKEW_MS = 5 * 60 * 1000; // refresh this long before real expiry

function loadEnv() {
  const file = path.join(root, '.env');
  if (!fs.existsSync(file)) fail('.env not found. Copy .env.example to .env — see docs/SETUP.md');
  const env = {};
  for (const line of fs.readFileSync(file, 'utf8').split('\n')) {
    const m = line.match(/^\s*([A-Z0-9_]+)\s*=\s*(.*)$/);
    if (!m) continue;
    env[m[1]] = m[2].trim().replace(/^["']|["']$/g, '');
  }
  return env;
}

const fail = (msg) => { console.error(`token: ${msg}`); process.exit(1); };
const isPlaceholder = (v) => !v || v.includes('xxxx');

const env = loadEnv();
const shop = env.SHOP || fail('SHOP is not set in .env');

// 1. Static token wins if present.
if (!isPlaceholder(env.SHOPIFY_CLI_THEME_TOKEN)) {
  process.stdout.write(env.SHOPIFY_CLI_THEME_TOKEN);
  process.exit(0);
}

const clientId = env.CLIENT_ID;
const clientSecret = env.CLIENT_SECRET;
if (isPlaceholder(clientId) || isPlaceholder(clientSecret)) {
  fail('no credentials in .env — set CLIENT_ID + CLIENT_SECRET (or SHOPIFY_CLI_THEME_TOKEN). See docs/SETUP.md');
}

// 2. Cached token, if it still has comfortable life left.
const force = process.argv.includes('--force');
if (!force && fs.existsSync(CACHE)) {
  try {
    const c = JSON.parse(fs.readFileSync(CACHE, 'utf8'));
    if (c.shop === shop && c.client_id === clientId && c.expires_at - SKEW_MS > Date.now()) {
      process.stdout.write(c.access_token);
      process.exit(0);
    }
  } catch { /* unreadable cache: just mint a new token */ }
}

// 3. Mint a new one.
const res = await fetch(`https://${shop}/admin/oauth/access_token`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
  body: new URLSearchParams({
    grant_type: 'client_credentials',
    client_id: clientId,
    client_secret: clientSecret,
  }),
});

if (!res.ok) fail(`Shopify refused the client credentials (${res.status}): ${await res.text()}`);

const data = await res.json();
if (!data.access_token) fail(`no access_token in Shopify's reply: ${JSON.stringify(data)}`);

fs.writeFileSync(
  CACHE,
  JSON.stringify(
    {
      shop,
      client_id: clientId,
      access_token: data.access_token,
      scope: data.scope,
      expires_at: Date.now() + (data.expires_in ?? 86400) * 1000,
      minted_at: new Date().toISOString(),
    },
    null,
    2
  ),
  { mode: 0o600 }
);

process.stdout.write(data.access_token);
