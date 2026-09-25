/**
 * Register the German (de) translations in i18n/de/ with the Wishbone store.
 *
 * English stays the primary language; German is stored as Shopify translations and
 * served at wishbone.golf/de once the language is published. This script never
 * publishes the language — that stays a manual step in Shopify admin
 * (Settings → Languages), after the owner has previewed /de.
 *
 *   node scripts/translate-de.mjs status              scopes + whether de is enabled/published
 *   node scripts/translate-de.mjs plan [--policies]   dry run: what would be written, what is stale or missing
 *   node scripts/translate-de.mjs apply [--policies] [--enable-locale] [--force]
 *
 *   --policies       include the six legal policies (i18n/de/policies/*.html); needs legal sign-off first
 *   --enable-locale  add de to the shop as an UNPUBLISHED language if it is not there yet
 *   --force          overwrite German that already exists in Shopify and differs from ours
 *
 * Every field in i18n/de/store.json pins the English it was translated from. If the live English
 * has changed since, the field is reported as stale and skipped — German is never registered
 * against text it does not translate.
 *
 * Needs the client-credentials app (CLIENT_ID/CLIENT_SECRET) with read_translations,
 * write_translations, read_locales, write_locales, read_products, read_content,
 * read_online_store_navigation, read_shipping (+ read_legal_policies, already granted). The Theme Access
 * password cannot do this, so this script mints its own token and ignores it.
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const API = '2025-10';
const LOCALE = 'de';
const NEEDED = ['read_translations', 'write_translations', 'read_locales', 'write_locales',
  'read_products', 'read_content', 'read_online_store_navigation', 'read_shipping'];

const args = process.argv.slice(2);
const cmd = args[0] || 'plan';
const flag = (f) => args.includes(f);
const fail = (msg) => { console.error(`translate-de: ${msg}`); process.exit(1); };

// ---------------------------------------------------------------- auth
function loadEnv() {
  const file = path.join(root, '.env');
  if (!fs.existsSync(file)) fail('.env not found — see docs/SETUP.md');
  const env = {};
  for (const line of fs.readFileSync(file, 'utf8').split('\n')) {
    const m = line.match(/^\s*([A-Z0-9_]+)\s*=\s*(.*)$/);
    if (m) env[m[1]] = m[2].trim().replace(/^["']|["']$/g, '');
  }
  return env;
}
const env = loadEnv();
const shop = env.SHOP || fail('SHOP is not set in .env');

async function mintToken() {
  const res = await fetch(`https://${shop}/admin/oauth/access_token`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({ grant_type: 'client_credentials', client_id: env.CLIENT_ID, client_secret: env.CLIENT_SECRET }),
  });
  if (!res.ok) fail(`Shopify refused the client credentials (${res.status})`);
  return (await res.json()).access_token;
}
const token = await mintToken();

async function gql(query, variables = {}) {
  for (let attempt = 0; ; attempt++) {
    const res = await fetch(`https://${shop}/admin/api/${API}/graphql.json`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'X-Shopify-Access-Token': token },
      body: JSON.stringify({ query, variables }),
    });
    const j = await res.json();
    const throttled = j.errors?.some((e) => e.extensions?.code === 'THROTTLED');
    if (throttled && attempt < 5) { await new Promise((r) => setTimeout(r, 2000 * (attempt + 1))); continue; }
    if (j.errors) fail(JSON.stringify(j.errors, null, 1));
    return j.data;
  }
}

// ---------------------------------------------------------------- status
async function scopes() {
  const d = await gql('{ appInstallation { accessScopes { handle } } }');
  return d.appInstallation.accessScopes.map((s) => s.handle);
}

async function localeState() {
  const d = await gql('{ shopLocales { locale primary published } }');
  return d.shopLocales.find((l) => l.locale === LOCALE) || null;
}

async function status() {
  const have = await scopes();
  const missing = NEEDED.filter((s) => !have.includes(s));
  console.log('scopes granted :', have.join(', '));
  if (missing.length) {
    console.log('scopes MISSING :', missing.join(', '));
    console.log('\nAdd them to the app in the Dev Dashboard, release a new version and reinstall it on the store.');
    return false;
  }
  const de = await localeState();
  console.log(`language de    : ${de ? (de.published ? 'enabled, PUBLISHED' : 'enabled, unpublished') : 'not added'}`);
  return true;
}

// ---------------------------------------------------------------- source
const SRC = JSON.parse(fs.readFileSync(path.join(root, 'i18n/de/store.json'), 'utf8'));
const POLICY_DIR = path.join(root, 'i18n/de/policies');
// Identify each policy by how its English body starts (the terms also contain the shipping and
// withdrawal wording further down, so only the opening is distinctive).
const POLICY_OPENINGS = [
  ['terms-of-service', 'TERMS AND CONDITIONS'],
  ['refund-policy', 'Right of Withdrawal for Consumer Transactions'],
  ['privacy-policy', 'Privacy Policy'],
  ['shipping-policy', 'For orders to Austria and Germany'],
  ['legal-notice', 'LEGAL NOTICE'],
  ['contact-information', 'Trade name:'],
];
const plain = (html) => (html || '').replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();

// resource type → how to find the German for one translatable field
const THEME_TYPES = ['ONLINE_STORE_THEME_JSON_TEMPLATE', 'ONLINE_STORE_THEME_SECTION_GROUP',
  'ONLINE_STORE_THEME_SETTINGS_DATA_SECTIONS'];
const themeMap = new Map(SRC.theme.map(([en, de]) => [en, de]));
const linkMap = new Map(SRC.links);

function byHandle(table) {
  return (content) => {
    const handle = content.find((c) => c.key === 'handle')?.value;
    const entry = table[handle];
    return (key) => entry?.[key] || null;         // [en, de] or null
  };
}

const RESOURCES = {
  PRODUCT: byHandle(SRC.products),
  COLLECTION: byHandle(SRC.collections),
  PAGE: byHandle(SRC.pages),
  LINK: () => (key, value) => (key === 'title' && linkMap.has(value) ? [value, linkMap.get(value)] : null),
  PRODUCT_OPTION: () => (key, value) => (SRC.option_names[value] ? [value, SRC.option_names[value]] : null),
  PRODUCT_OPTION_VALUE: () => (key, value) => (SRC.option_values[value] ? [value, SRC.option_values[value]] : null),
  ...Object.fromEntries(THEME_TYPES.map((t) => [t, () => (key, value) => (themeMap.has(value) ? [value, themeMap.get(value)] : null)])),
  // no German in store.json yet — listed so `plan` shows what a shopper would still see in English
  SHOP: () => () => null,                          // shop name, homepage SEO title/description
};
// short labels matched by their English value: shipping rate names at checkout, storefront filters
for (const [type, map] of Object.entries(SRC.labels || {})) {
  RESOURCES[type] = () => (key, value) => (map[value] ? [value, map[value]] : null);
}
if (flag('--policies')) {
  RESOURCES.SHOP_POLICY = (content) => {
    const body = content.find((c) => c.key === 'body')?.value || '';
    const hit = POLICY_OPENINGS.find(([, opening]) => plain(body).startsWith(opening));
    if (!hit) return () => null;
    const de = fs.readFileSync(path.join(POLICY_DIR, `${hit[0]}.html`), 'utf8').trim();
    return (key, value) => (key === 'body' ? [value, de] : null);  // policies are matched by opening, not pinned
  };
}

// fields that are never translated: URL handles stay English so no link or redirect changes
const SKIP_KEYS = new Set(['handle']);
// single-variant products carry an option "Title" / "Default Title" that Shopify never shows

async function* translatable(type) {
  let after = null;
  do {
    const d = await gql(`query($type: TranslatableResourceType!, $after: String) {
      translatableResources(first: 100, resourceType: $type, after: $after) {
        pageInfo { hasNextPage endCursor }
        nodes { resourceId
          translatableContent { key value digest }
          translations(locale: "${LOCALE}") { key value outdated } } } }`, { type, after });
    yield* d.translatableResources.nodes;
    after = d.translatableResources.pageInfo.hasNextPage ? d.translatableResources.pageInfo.endCursor : null;
  } while (after);
}

// ---------------------------------------------------------------- plan
async function plan() {
  const writes = [];                               // { resourceId, key, value, digest, label }
  const report = { write: 0, same: 0, differs: 0, stale: [], missing: [] };
  for (const [type, finder] of Object.entries(RESOURCES)) {
    for await (const node of translatable(type)) {
      const lookup = finder(node.translatableContent);
      const existing = new Map(node.translations.map((t) => [t.key, t]));
      const handle = node.translatableContent.find((c) => c.key === 'handle')?.value;
      const where = `${type} ${handle || node.resourceId.split('/').pop()}`;
      for (const c of node.translatableContent) {
        if (!c.value || SKIP_KEYS.has(c.key) || c.value === 'Title' || c.value === 'Default Title') continue;
        const pair = lookup(c.key, c.value);
        if (!pair) {
          // theme resources hold every setting, most of them not text a shopper reads; only
          // report the shopper-facing types as missing
          if (!type.startsWith('ONLINE_STORE_THEME')) report.missing.push(`${where} · ${c.key}: ${plain(c.value).slice(0, 70)}`);
          continue;
        }
        const [en, de] = pair;
        if (en !== c.value) { report.stale.push(`${where} · ${c.key}`); continue; }
        const have = existing.get(c.key);
        if (have && have.value === de && !have.outdated) { report.same++; continue; }
        if (have && have.value !== de && !flag('--force')) { report.differs++; continue; }
        writes.push({ resourceId: node.resourceId, key: c.key, value: de, digest: c.digest, label: `${where} · ${c.key}` });
      }
    }
  }
  report.write = writes.length;
  return { writes, report };
}

function printReport({ writes, report }) {
  for (const w of writes) console.log('  +', w.label);
  console.log(`\nto write: ${report.write} · already current: ${report.same} · existing German left alone: ${report.differs}`);
  if (report.stale.length) console.log(`\nSTALE — live English changed since translation, skipped (${report.stale.length}):\n  ` + report.stale.join('\n  '));
  if (report.missing.length) console.log(`\nno German yet (${report.missing.length}):\n  ` + report.missing.join('\n  '));
  if (!flag('--policies')) console.log('\n(legal policies not included — add --policies once they are signed off)');
}

// ---------------------------------------------------------------- apply
async function apply() {
  let de = await localeState();
  if (!de) {
    if (!flag('--enable-locale')) fail('German is not added to the shop yet. Re-run with --enable-locale (adds it unpublished).');
    await gql(`mutation { shopLocaleEnable(locale: "${LOCALE}") { userErrors { message } shopLocale { locale published } } }`);
    de = await localeState();
    console.log(`added language ${LOCALE} (published: ${de.published})`);
  }
  const p = await plan();
  printReport(p);
  const byResource = new Map();
  for (const w of p.writes) {
    if (!byResource.has(w.resourceId)) byResource.set(w.resourceId, []);
    byResource.get(w.resourceId).push({ locale: LOCALE, key: w.key, value: w.value, translatableContentDigest: w.digest });
  }
  let ok = 0, bad = 0;
  for (const [resourceId, translations] of byResource) {
    const d = await gql(`mutation($id: ID!, $t: [TranslationInput!]!) {
      translationsRegister(resourceId: $id, translations: $t) { userErrors { field message } translations { key } } }`,
    { id: resourceId, t: translations });
    const errs = d.translationsRegister.userErrors;
    if (errs.length) { bad += translations.length; console.error('  !', resourceId, JSON.stringify(errs)); }
    else ok += d.translationsRegister.translations.length;
  }
  console.log(`\nregistered ${ok} German fields${bad ? `, ${bad} failed` : ''}. German is ${de.published ? 'PUBLISHED' : 'still unpublished'}.`);
  if (!de.published) console.log('Preview: Shopify admin → Settings → Languages → German → Preview. Publish there when approved.');
}

// ---------------------------------------------------------------- main
if (cmd === 'status') { await status(); }
else if (cmd === 'plan') { if (await status()) printReport(await plan()); }
else if (cmd === 'apply') { if (!(await status())) process.exit(1); await apply(); }
else fail(`unknown command "${cmd}" — use status, plan or apply`);
