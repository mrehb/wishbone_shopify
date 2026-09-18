import re, base64, pathlib, json, html
ROOT = pathlib.Path('/workspace/wishbone/design-system')

def datauri(p, mime='image/png'):
    return f"data:{mime};base64," + base64.b64encode((ROOT/p).read_bytes()).decode()

WORD = datauri('assets/wishbone-wordmark.png')
MONO = datauri('assets/wishbone-monogram.png')

def fix_assets(s):
    return (s.replace('../../assets/wishbone-wordmark.png', WORD)
             .replace('../assets/wishbone-wordmark.png', WORD)
             .replace('../../assets/wishbone-monogram.png', MONO)
             .replace('../assets/wishbone-monogram.png', MONO))

# ---- tokens inlined (drop the @import; the page links Google Fonts itself) ----
tokens = ""
for f in ['colors.css','typography.css','geometry.css','layout.css']:
    t = (ROOT/'tokens'/f).read_text()
    t = re.sub(r"@import[^;]+;", "", t)
    tokens += f"\n/* tokens/{f} */\n" + t

# ---- guideline cards ----
guides = []
for p in sorted((ROOT/'guidelines').glob('*.html')):
    src = p.read_text()
    m = re.search(r'<!--\s*@dsCard\s+(.*?)-->', src)
    meta = dict(re.findall(r'(\w+)="([^"]*)"', m.group(1))) if m else {}
    body = re.search(r'<body[^>]*>(.*)</body>', src, re.S).group(1)
    guides.append({
        'file': f'guidelines/{p.name}',
        'group': meta.get('group',''), 'name': meta.get('name', p.stem),
        'subtitle': meta.get('subtitle',''), 'body': fix_assets(body),
    })

# ---- components: strip imports/exports so they can share one babel scope ----
comp_src = ""
order = ['core/Button','core/Input','core/Badge','core/VariantPill',
         'commerce/ProductCard','chrome/SiteHeader','chrome/NewsletterBand','chrome/SiteFooter']
rules = {}
for rel in order:
    jsx = (ROOT/'components'/f'{rel}.jsx').read_text()
    jsx = re.sub(r"^import .*$", "", jsx, flags=re.M)
    jsx = jsx.replace('export function', 'function')
    comp_src += fix_assets(jsx) + "\n"
    prompt = (ROOT/'components'/f'{rel}.prompt.md').read_text()
    paras = [x.strip() for x in prompt.split('\n\n') if x.strip() and not x.startswith('#')]
    rules[rel.split('/')[1]] = ' '.join(paras[-1].split())

tree = "\n".join(sorted(str(p.relative_to(ROOT)) for p in ROOT.rglob('*') if p.is_file()))

DEMO = r"""
const root = ReactDOM.createRoot(document.getElementById('components'));
const row = { display:'flex', gap:12, alignItems:'center', flexWrap:'wrap' };
const Section = ({title, file, rule, children}) => (
  <section style={{marginBottom:34}}>
    <div style={{display:'flex',alignItems:'baseline',gap:12,flexWrap:'wrap',marginBottom:10}}>
      <h3 style={{fontFamily:'var(--font-heading)',textTransform:'uppercase',fontWeight:500,fontSize:21,margin:0}}>{title}</h3>
      <code style={{fontSize:12,color:'var(--text-muted)'}}>{file}</code>
    </div>
    <div style={{border:'1px solid var(--color-border-soft)',padding:'22px 24px',background:'var(--color-ink)'}}>{children}</div>
    <p style={{color:'var(--text-muted)',fontSize:12.5,margin:'10px 0 0',maxWidth:'80ch'}}>{rule}</p>
  </section>
);
root.render(<div>
  <Section title="Button" file="components/core/Button.jsx" rule={RULES.Button}>
    <div style={row}>
      <Button>Add to cart</Button>
      <Button variant="secondary">Learn more</Button>
      <Button variant="white">Find a dealer</Button>
      <Button disabled>Sold out</Button>
      <span style={{background:'var(--color-volt)',padding:10,display:'inline-flex'}}><Button variant="invert">Buy the EON</Button></span>
    </div>
  </Section>
  <Section title="Input" file="components/core/Input.jsx" rule={RULES.Input}>
    <div style={{...row, alignItems:'flex-end'}}>
      <Input label="Email address" placeholder="you@example.com" style={{width:230}} />
      <Input label="Email address" value="you@" error="Add the part after the @ — for example you@example.com." style={{width:320}} />
    </div>
  </Section>
  <Section title="Badge" file="components/core/Badge.jsx" rule={RULES.Badge}>
    <div style={row}><Badge kind="bestseller" /><Badge kind="new" /><Badge kind="soldout" /><Badge kind="spare" /></div>
  </Section>
  <Section title="VariantPill" file="components/core/VariantPill.jsx" rule={RULES.VariantPill}>
    <div style={row}>
      <VariantPill>ONE</VariantPill><VariantPill>TWO</VariantPill><VariantPill>THREE</VariantPill>
      <VariantPill selected>NEO</VariantPill><VariantPill unavailable>EON</VariantPill>
    </div>
  </Section>
  <Section title="ProductCard" file="components/commerce/ProductCard.jsx" rule={RULES.ProductCard}>
    <div style={{display:'grid',gridTemplateColumns:'repeat(3,1fr)',gap:'var(--grid-gap)'}}>
      <ProductCard title="Wishbone EON" type="Electric trolley" price="799,00 €" badge="bestseller" />
      <ProductCard title="Wishbone THREE" type="Manual trolley" price="249,00 €" />
      <ProductCard title="Fast Charger (NEO & EON)" type="Spare part" price="99,90 €" soldOut />
    </div>
  </Section>
  <Section title="Chrome" file="components/chrome/*.jsx" rule={RULES.SiteHeader}>
    <div style={{margin:'-22px -24px'}}>
      <SiteHeader cartCount={2} />
      <NewsletterBand tone="volt" />
      <SiteFooter />
    </div>
  </Section>
</div>);
"""

page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Wishbone Golf Design System — what was shipped</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600&family=Figtree:ital,wght@0,500;0,700;1,500&display=swap" rel="stylesheet">
<style>
{tokens}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--color-ink);color:var(--color-white);font-family:var(--font-body);font-weight:500;font-size:15px;line-height:1.6}}
.wrap{{max-width:1040px;margin:0 auto;padding:0 24px 90px}}
h1,h2,h3,h4{{font-family:var(--font-heading);font-weight:500;text-transform:uppercase;margin:0;line-height:1.05}}
h1{{font-size:50px}} h2{{font-size:31px}}
header{{border-bottom:1px solid var(--color-border-soft);padding:52px 0 34px;margin-bottom:46px}}
header img{{width:300px;max-width:66%;display:block;margin-bottom:30px}}
.eyebrow{{font-size:11px;letter-spacing:var(--tracking-eyebrow);text-transform:uppercase;color:var(--text-muted)}}
.muted{{color:var(--text-muted)}}
.sec-head{{display:flex;align-items:baseline;gap:14px;border-top:1px solid var(--color-border-soft);padding-top:16px;margin:56px 0 22px}}
.num{{font-family:var(--font-heading);font-size:13px;color:var(--color-volt);letter-spacing:.1em}}
code{{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12.5px;background:var(--surface-panel);padding:1px 6px}}
.card{{border:1px solid var(--color-border-soft);margin-bottom:26px}}
.card .label{{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;padding:12px 16px;border-bottom:1px solid var(--color-border-soft);background:var(--surface-panel)}}
.card .label b{{font-family:var(--font-heading);text-transform:uppercase;font-weight:500;font-size:15px}}
.card .render{{padding:20px 22px;overflow-x:auto}}
table{{width:100%;border-collapse:collapse;font-size:14px}}
th,td{{text-align:left;padding:8px 12px;border-bottom:1px solid var(--color-border-soft);vertical-align:top}}
th{{font-family:var(--font-heading);text-transform:uppercase;font-weight:500;font-size:13px;color:var(--text-muted)}}
pre{{background:var(--surface-panel);border:1px solid var(--color-border-soft);padding:16px 18px;overflow-x:auto;font-size:12px;line-height:1.5;color:#d8dade}}
.note{{border-left:3px solid var(--color-cyan);background:var(--surface-panel);padding:14px 18px;margin:18px 0}}
footer{{border-top:1px solid var(--color-border-soft);margin-top:60px;padding-top:18px;color:var(--text-muted);font-size:13px}}
</style></head><body><div class="wrap">

<header>
  <img src="{WORD}" alt="Wishbone Golf">
  <div class="eyebrow">Claude Design · project 4d0e779c · 19 September 2026</div>
  <h1>Wishbone Golf Design System</h1>
  <p class="muted" style="max-width:680px">54 files, pushed and verified. This page renders what is
  actually in the project — the guideline cards below are the files themselves, and the components are
  their real JSX running in your browser. Built to the same convention as your BIG MAX Golf system.</p>
</header>

<div class="sec-head"><span class="num">01</span><h2>Foundations &amp; guidelines</h2></div>
<p class="muted" style="margin-top:-8px">Ten specimen cards. Each carries an <code>@dsCard</code> marker, which is what Claude Design indexes on.</p>
{"".join(f'''
<div class="card">
  <div class="label"><span class="eyebrow" style="color:var(--color-volt)">{g['group']}</span><b>{g['name']}</b>
    <span class="muted" style="font-size:12.5px">{g['subtitle']}</span>
    <code style="margin-left:auto">{g['file']}</code></div>
  <div class="render">{g['body']}</div>
</div>''' for g in guides)}

<div class="sec-head"><span class="num">02</span><h2>Components</h2></div>
<p class="muted" style="margin-top:-8px">Eight components, each shipped as <code>.jsx</code> + <code>.d.ts</code> + <code>.prompt.md</code>.
Rendered here from the exact source that was pushed; the note under each is from its prompt file.</p>
<div id="components"><p class="muted">Loading React from unpkg to render the components…
If this stays here, the page is offline — the design system itself is unaffected.</p></div>

<div class="sec-head"><span class="num">03</span><h2>What is in the project</h2></div>
<table>
  <tr><th>Path</th><th>What it holds</th></tr>
  <tr><td><code>tokens/</code></td><td>colors · typography · geometry · layout · base — every value has an address in the theme</td></tr>
  <tr><td><code>guidelines/</code></td><td>the ten specimen cards above</td></tr>
  <tr><td><code>components/core/</code></td><td>Button, Input, Badge, VariantPill</td></tr>
  <tr><td><code>components/commerce/</code></td><td>ProductCard</td></tr>
  <tr><td><code>components/chrome/</code></td><td>SiteHeader, NewsletterBand, SiteFooter</td></tr>
  <tr><td><code>assets/</code></td><td>wordmark + monogram PNGs</td></tr>
  <tr><td><code>uploads/</code></td><td>BRAND_KIT.md, tokens.css/json, logo originals — the raw extraction</td></tr>
  <tr><td><code>SKILL.md</code></td><td>agent entry point, invocable as <code>wishbone-design</code></td></tr>
  <tr><td><code>readme.md</code></td><td>the brand brief: content fundamentals, visual foundations, open decisions</td></tr>
</table>

<details style="margin-top:22px"><summary class="muted" style="cursor:pointer;font-size:13px">Full file list (54)</summary>
<pre>{html.escape(tree)}</pre></details>

<div class="note">
  <b style="font-family:var(--font-heading);text-transform:uppercase;font-weight:500">Open the project once</b>
  <p style="margin:6px 0 0">Claude Design compiles <code>_ds_bundle.js</code> from the JSX the first time the project is
  opened. Until then the three component cards inside Claude Design show a “bundle not loaded” placeholder — the guideline
  cards render immediately. Nothing to fix; it just needs one visit.</p>
</div>

<div class="note" style="border-left-color:var(--color-volt)">
  <b style="font-family:var(--font-heading);text-transform:uppercase;font-weight:500">Still assumed, not decided</b>
  <p style="margin:6px 0 0">The system treats volt <code>#E3FC02</code> as the brand green. The monogram ships
  <code>#C8D645</code> and the hardware photographs around <code>#B4FA6E</code>. If you pick a different one, say so and I
  update the tokens and re-push rather than you editing swatches by hand.</p>
</div>

<footer>
  Claude Design project <code>4d0e779c-652a-4fef-bd5b-6bd8de45e03d</code> · same files committed at
  <code>github.com/mrehb/wishbone_shopify</code> under <code>design-system/</code> · derived from the live store 2026-09-19
</footer>
</div>

<script src="https://unpkg.com/react@18.3.1/umd/react.production.min.js" crossorigin></script>
<script src="https://unpkg.com/react-dom@18.3.1/umd/react-dom.production.min.js" crossorigin></script>
<script src="https://unpkg.com/@babel/standalone@7.29.0/babel.min.js" crossorigin></script>
<script>window.RULES = {json.dumps(rules)};</script>
<script type="text/babel">
const {{ useState }} = React;
{comp_src}
{DEMO}
</script>
</body></html>
"""
out = pathlib.Path('/tmp/wb/kit/wishbone-design-system.html')
out.write_text(page)
print("wrote", out, round(len(page)/1024), "KB", "| guidelines:", len(guides), "| components:", len(order))
