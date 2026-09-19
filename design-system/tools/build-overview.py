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
order = ['core/Button','core/Input','core/Badge','core/VariantPill','core/DotMatrix','core/Stat',
         'commerce/ProductCard','commerce/SpecPanel',
         'chrome/SiteHeader','chrome/NewsletterBand','chrome/SiteFooter']
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
      <h3 style={{fontFamily:'var(--font-display)',fontWeight:500,fontSize:23,margin:0,letterSpacing:'-0.01em'}}>{title}</h3>
      <code style={{fontSize:12,color:'var(--text-muted)'}}>{file}</code>
    </div>
    <div style={{border:'1px solid var(--color-border)',borderRadius:'var(--radius-card)',padding:'22px 24px',background:'var(--surface-card)'}}>{children}</div>
    <p style={{color:'var(--text-muted)',fontSize:12.5,margin:'10px 0 0',maxWidth:'80ch'}}>{rule}</p>
  </section>
);
// Silhouette grid — stands in for a photo-sampled product outline.
const C = 44, R = 26, vals = [], acc = [];
for (let y=0; y<R; y++) for (let x=0; x<C; x++){
  const i=y*C+x;
  const wheel = Math.abs(Math.hypot(x-10,y-18)-5.5)<1.3 || Math.abs(Math.hypot(x-34,y-18)-5.5)<1.3;
  const frame = (y>7 && y<9 && x>9 && x<35) || (Math.abs((x-10)*0.55-(y-18))<0.8 && x>9 && x<23);
  const handle = (Math.abs(x-33)<1 && y>3 && y<9);
  const v = wheel||frame||handle ? 1 : 0;
  vals.push(v); if (v && handle) acc.push(i);
}
root.render(<div>
  <Section title="Button" file="components/core/Button.jsx" rule={RULES.Button}>
    <div style={row}>
      <Button>Add to cart</Button>
      <Button variant="ghost">Compare models</Button>
      <Button variant="quiet">Spare parts →</Button>
      <Button disabled>Sold out</Button>
    </div>
  </Section>
  <Section title="Input & Badge" file="components/core/Input.jsx · Badge.jsx" rule={RULES.Input}>
    <div style={{...row, alignItems:'flex-end', marginBottom:16}}>
      <Input label="Email address" placeholder="you@example.com" style={{width:240}} />
      <Input label="Email address" value="you@" error="Add the part after the @ — for example you@example.com." style={{width:330}} />
    </div>
    <div style={row}><Badge kind="live" /><Badge kind="best" /><Badge kind="soldout" /><Badge kind="spare" /></div>
  </Section>
  <Section title="VariantPill" file="components/core/VariantPill.jsx" rule={RULES.VariantPill}>
    <div style={row}>
      <VariantPill>ONE</VariantPill><VariantPill>TWO</VariantPill><VariantPill>THREE</VariantPill>
      <VariantPill selected>NEO</VariantPill><VariantPill unavailable>EON</VariantPill>
    </div>
  </Section>
  <Section title="DotMatrix · the signature device" file="components/core/DotMatrix.jsx" rule={RULES.DotMatrix}>
    <div style={{display:'flex',gap:28,flexWrap:'wrap',alignItems:'center'}}>
      <DotMatrix values={vals} cols={C} rows={R} accent={acc} />
      <DotBars levels={[1,.95,.85,.75,.6,.5,.4,.3,.2,.12]} />
    </div>
  </Section>
  <Section title="Stat" file="components/core/Stat.jsx" rule={RULES.Stat}>
    <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fit,minmax(230px,1fr))',gap:'var(--grid-gap)'}}>
      <Stat index="01" label="EON · Range" value="27+" unit="holes" note="One charge, lithium"
            footer={[{label:'Price',value:'799 €'},{label:'Fast charge',value:'Yes'}]}>
        <DotBars levels={[1,.95,.9,.8,.7,.6,.5,.4,.3,.2]} />
      </Stat>
      <Stat index="02" label="The range" value="05" note="ONE · TWO · THREE · NEO · EON"
            footer={[{label:'Manual',value:'03'},{label:'Electric',value:'02'}]}>
        <DotBars levels={[.4,.5,.6,.85,1]} />
      </Stat>
    </div>
  </Section>
  <Section title="ProductCard" file="components/commerce/ProductCard.jsx" rule={RULES.ProductCard}>
    <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fit,minmax(215px,1fr))',gap:'var(--grid-gap)'}}>
      <ProductCard title="Wishbone EON" type="Electric trolley" price="799,00 €" badge="best">
        <DotMatrix values={vals} cols={C} rows={R} accent={acc} size={4} gap={2} />
      </ProductCard>
      <ProductCard title="Wishbone THREE" type="Manual trolley" price="249,00 €" badge="best" />
      <ProductCard title="Fast Charger (NEO & EON)" type="Spare part" price="99,90 €" soldOut />
    </div>
  </Section>
  <Section title="SpecPanel" file="components/commerce/SpecPanel.jsx" rule={RULES.SpecPanel}>
    <SpecPanel specs={[
      {label:'Range', value:'27+', unit:'holes', note:'Lithium, one charge', levels:[1,.9,.8,.7,.6,.45,.3,.2]},
      {label:'Frame', value:'AL', note:'Aircraft-grade aluminium'},
      {label:'Fold size', value:'—', note:'Not yet measured'},
    ]} />
  </Section>
  <Section title="Chrome" file="components/chrome/*.jsx" rule={RULES.SiteHeader}>
    <div style={{margin:'-22px -24px'}}>
      <SiteHeader cartCount={2} />
      <div style={{padding:'22px 24px'}}><NewsletterBand /></div>
      <SiteFooter />
    </div>
  </Section>
</div>);
"""

page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Wishbone Golf — v2 Telemetry</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=Figtree:ital,wght@0,400;0,500;0,700;1,500&family=Share+Tech+Mono&display=swap" rel="stylesheet">
<style>
{tokens}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--color-carbon);color:var(--color-white);font-family:var(--font-body);font-weight:500;font-size:15px;line-height:1.6}}
.wrap{{max-width:1040px;margin:0 auto;padding:0 24px 90px}}
h1,h2,h3,h4{{font-family:var(--font-display);font-weight:500;letter-spacing:-.02em;margin:0;line-height:1.05}}
h1{{font-size:50px}} h2{{font-size:31px}}
header{{border-bottom:1px solid var(--color-border);padding:52px 0 34px;margin-bottom:46px}}
header img{{width:300px;max-width:66%;display:block;margin-bottom:30px}}
.eyebrow{{font-size:11px;letter-spacing:var(--tracking-label);text-transform:uppercase;color:var(--text-muted)}}
.muted{{color:var(--text-muted)}}
.sec-head{{display:flex;align-items:baseline;gap:14px;border-top:1px solid var(--color-border);padding-top:16px;margin:56px 0 22px}}
.num{{font-family:var(--font-display);font-size:13px;color:var(--color-volt);letter-spacing:.1em}}
code{{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12.5px;background:var(--surface-card);padding:1px 6px}}
.card{{border:1px solid var(--color-border);margin-bottom:26px}}
.card .label{{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;padding:12px 16px;border-bottom:1px solid var(--color-border);background:var(--surface-card)}}
.card .label b{{font-family:var(--font-display);text-transform:uppercase;font-weight:500;font-size:15px}}
.card .render{{padding:20px 22px;overflow-x:auto}}
table{{width:100%;border-collapse:collapse;font-size:14px}}
th,td{{text-align:left;padding:8px 12px;border-bottom:1px solid var(--color-border);vertical-align:top}}
th{{font-family:var(--font-display);text-transform:uppercase;font-weight:500;font-size:13px;color:var(--text-muted)}}
pre{{background:var(--surface-card);border:1px solid var(--color-border);padding:16px 18px;overflow-x:auto;font-size:12px;line-height:1.5;color:#d8dade}}
.note{{border-left:3px solid var(--color-cyan);background:var(--surface-card);padding:14px 18px;margin:18px 0}}
footer{{border-top:1px solid var(--color-border);margin-top:60px;padding-top:18px;color:var(--text-muted);font-size:13px}}
</style></head><body><div class="wrap">

<header>
  <img src="{WORD}" alt="Wishbone Golf">
  <div class="eyebrow"><b style="color:var(--color-volt);font-weight:400">V2</b>&nbsp;&nbsp;TELEMETRY · CLAUDE DESIGN 4d0e779c · 19 SEPTEMBER 2026</div>
  <h1>The rebrand</h1>
  <p class="muted" style="max-width:690px">Green kept, everything else moved. Carbon ground under a warm
  raking light, volt as the only accent, soft geometry, three typefaces with one job each, and a dot matrix
  as the signature device. 67 files pushed. Everything below is rendered from the real files — the guideline
  cards are the files themselves, the components are their actual JSX.</p>

  <table style="margin-top:26px">
    <tr><th>&nbsp;</th><th>v1 — as found</th><th>v2 — this</th></tr>
    <tr><td>Ground</td><td class="muted">#1F1F21 cold ink</td><td><b>#0F1014 carbon</b> + warm wash</td></tr>
    <tr><td>Accent</td><td class="muted">volt + cyan</td><td><b>volt only</b> — cyan retired</td></tr>
    <tr><td>Monogram</td><td class="muted">olive #C8D645</td><td><b>reissued in volt</b></td></tr>
    <tr><td>Geometry</td><td class="muted">radius 0, pills the exception</td><td><b>20px cards / 10px controls</b></td></tr>
    <tr><td>Display face</td><td class="muted">Oswald 500 UPPERCASE</td><td><b>Space Grotesk</b>, sentence case</td></tr>
    <tr><td>Values</td><td class="muted">body type</td><td><b>Share Tech Mono</b> readouts</td></tr>
    <tr><td>Signature</td><td class="muted">—</td><td><b>the dot matrix</b></td></tr>
    <tr><td>Volt share</td><td class="muted">10 %</td><td><b>4 %</b> — one per screen</td></tr>
    <tr><td>Shadows</td><td class="muted">none</td><td>none — <b>unchanged</b></td></tr>
  </table>
</header>

<div class="sec-head"><span class="num">01</span><h2>Foundations &amp; guidelines</h2></div>
<p class="muted" style="margin-top:-8px">Twelve specimen cards, including the two new ones — <code>dot-matrix</code> and <code>light</code>. Each carries an <code>@dsCard</code> marker, which is what Claude Design indexes on.</p>
{"".join(f'''
<div class="card">
  <div class="label"><span class="eyebrow" style="color:var(--color-volt)">{g['group']}</span><b>{g['name']}</b>
    <span class="muted" style="font-size:12.5px">{g['subtitle']}</span>
    <code style="margin-left:auto">{g['file']}</code></div>
  <div class="render">{g['body']}</div>
</div>''' for g in guides)}

<div class="sec-head"><span class="num">02</span><h2>Components</h2></div>
<p class="muted" style="margin-top:-8px">Eleven components, each shipped as <code>.jsx</code> + <code>.d.ts</code> + <code>.prompt.md</code>.
Rendered here from the exact source that was pushed; the note under each is from its prompt file.</p>
<div id="components"><p class="muted">Loading React from unpkg to render the components…
If this stays here, the page is offline — the design system itself is unaffected.</p></div>

<div class="sec-head"><span class="num">03</span><h2>What is in the project</h2></div>
<table>
  <tr><th>Path</th><th>What it holds</th></tr>
  <tr><td><code>tokens/</code></td><td>colors · typography · geometry · layout · base — every value has an address in the theme</td></tr>
  <tr><td><code>guidelines/</code></td><td>the ten specimen cards above</td></tr>
  <tr><td><code>components/core/</code></td><td>Button, Input, Badge, VariantPill, <b>DotMatrix/DotBars</b>, <b>Stat</b></td></tr>
  <tr><td><code>components/commerce/</code></td><td>ProductCard, <b>SpecPanel</b></td></tr>
  <tr><td><code>components/chrome/</code></td><td>SiteHeader, NewsletterBand, SiteFooter</td></tr>
  <tr><td><code>assets/</code></td><td>wordmark, monogram, <b>monogram in volt</b></td></tr>
  <tr><td><code>uploads/</code></td><td>BRAND_KIT.md, tokens.css/json, logo originals — the raw extraction</td></tr>
  <tr><td><code>SKILL.md</code></td><td>agent entry point, invocable as <code>wishbone-design</code></td></tr>
  <tr><td><code>readme.md</code></td><td>the brand brief: content fundamentals, visual foundations, open decisions</td></tr>
</table>

<details style="margin-top:22px"><summary class="muted" style="cursor:pointer;font-size:13px">Full file list (54)</summary>
<pre>{html.escape(tree)}</pre></details>

<div class="note">
  <b style="font-family:var(--font-display);text-transform:uppercase;font-weight:500">Open the project once</b>
  <p style="margin:6px 0 0">Claude Design compiles <code>_ds_bundle.js</code> from the JSX the first time the project is
  opened. Until then the three component cards inside Claude Design show a “bundle not loaded” placeholder — the guideline
  cards render immediately. Nothing to fix; it just needs one visit.</p>
</div>

<div class="note" style="border-left-color:var(--color-volt)">
  <b style="font-family:var(--font-display);font-weight:500">The theme still runs v1</b>
  <p style="margin:6px 0 0">This system is the target, not the storefront. wishbone.golf is untouched — nothing reaches
  customers until a draft theme is built from these tokens and published by hand. Two catalogue gaps are worth closing
  first: <b>fold size and weight</b> are missing, and they are exactly the proof a telemetry brand runs on.</p>
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
const {{ useState, useEffect, useRef }} = React;
{comp_src}
{DEMO}
</script>
</body></html>
"""
out = pathlib.Path('/tmp/wb/kit/wishbone-design-system.html')
out.write_text(page)
print("wrote", out, round(len(page)/1024), "KB", "| guidelines:", len(guides), "| components:", len(order))
