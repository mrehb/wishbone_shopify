#!/usr/bin/env python3
"""Build the Wishbone component-library page.

Renders every component from its real source, alongside the storefront audit the
library was designed against and the roadmap of what is still missing.
Regenerate:  python3 tools/build-library.py
"""
import re, base64, pathlib, json

ROOT = pathlib.Path(__file__).resolve().parent.parent
uri = lambda p, m='image/png': "data:%s;base64,%s" % (m, base64.b64encode((ROOT/p).read_bytes()).decode())
WORD, MONO = uri('assets/wishbone-wordmark.png'), uri('assets/wishbone-monogram-volt.png')

def fix(s):
    for a in ('../../assets/wishbone-wordmark.png', '../assets/wishbone-wordmark.png'):
        s = s.replace(a, WORD)
    for a in ('../../assets/wishbone-monogram-volt.png', '../assets/wishbone-monogram-volt.png'):
        s = s.replace(a, MONO)
    return s

tokens = ""
for f in ['colors.css', 'typography.css', 'geometry.css', 'layout.css']:
    tokens += "\n" + re.sub(r"@import[^;]+;", "", (ROOT/'tokens'/f).read_text())

ORDER = ['core/Button', 'core/Input', 'core/Badge', 'core/VariantPill', 'core/DotMatrix', 'core/Stat',
         'commerce/ProductCard', 'commerce/SpecPanel', 'commerce/CompatibilityFinder', 'commerce/PartCard',
         'commerce/ColorwaySelector', 'commerce/BuyBox', 'commerce/ModelCompare',
         'content/Hero', 'content/RangeStrip', 'content/Accordion', 'content/TrustRow', 'content/InTheBox',
         'chrome/SiteHeader', 'chrome/NewsletterBand', 'chrome/SiteFooter']

src, rules = "", {}
for rel in ORDER:
    jsx = (ROOT/'components'/f'{rel}.jsx').read_text()
    jsx = re.sub(r"^import .*$", "", jsx, flags=re.M).replace('export function', 'function')
    src += fix(jsx) + "\n"
    prompt = (ROOT/'components'/f'{rel}.prompt.md').read_text()
    paras = [x.strip() for x in prompt.split('\n\n') if x.strip() and not x.startswith('#')]
    rules[rel.split('/')[1]] = ' '.join(paras[0].split())

DEMO = r"""
const R = window.RULES;
const Card = ({name, file, children}) => (
  <section style={{marginBottom:30}}>
    <div style={{display:'flex',alignItems:'baseline',gap:12,flexWrap:'wrap',marginBottom:10}}>
      <h3 style={{fontFamily:'var(--font-display)',fontWeight:500,fontSize:21,margin:0,letterSpacing:'-0.01em'}}>{name}</h3>
      <code style={{fontSize:12,color:'var(--text-muted)'}}>{file}</code>
    </div>
    <div style={{border:'1px solid var(--color-border)',borderRadius:'var(--radius-card)',padding:'22px 24px',background:'var(--surface-card)'}}>{children}</div>
    <p style={{color:'var(--text-muted)',fontSize:12.5,margin:'10px 0 0',maxWidth:'82ch'}}>{R[name.split(' ')[0]] || ''}</p>
  </section>
);
const MODELS = [{id:'ONE'},{id:'TWO'},{id:'THREE'},{id:'NEO'},{id:'EON'}];
const PARTS = [
  {title:'Frame (ONE)', fits:['ONE'], price:'89,00 €'},
  {title:'Rear Wheel Right (ONE)', fits:['ONE'], price:'24,20 €'},
  {title:'Brake Kit (ONE)', fits:['ONE'], price:'7,30 €'},
  {title:'Front Wheel Kit - Universal fit (ONE & NEO)', fits:['ONE','NEO'], price:'37,40 €'},
  {title:'Controller (NEO)', fits:['NEO'], price:'62,00 €'},
  {title:'Drive Train - Motor & Gearbox (NEO)', fits:['NEO'], price:'152,30 €'},
  {title:'Lithium Battery 27+ Holes (NEO & EON)', fits:['NEO','EON'], price:'369,00 €'},
  {title:'Fast Charger (NEO & EON)', fits:['NEO','EON'], price:'99,90 €'},
  {title:'Wing Screw for Umbrella Holder (ONE, NEO & EON)', fits:['ONE','NEO','EON'], price:'7,90 €'},
  {title:'Magnetic Scorecard Holder', fits:['ALL'], price:'29,90 €'},
  {title:'Umbrella Holder', fits:['ALL'], price:'29,90 €'},
];
const row = {display:'flex',gap:12,alignItems:'center',flexWrap:'wrap'};
ReactDOM.createRoot(document.getElementById('lib')).render(<div>
  <div className="grouphead"><span className="n">A</span><h2>Commerce</h2>
    <p className="muted">Built against the real catalogue. These are the components the store does not have and most needs.</p></div>

  <Card name="CompatibilityFinder" file="components/commerce/CompatibilityFinder.jsx">
    <CompatibilityFinder models={MODELS} parts={PARTS} />
  </Card>
  <Card name="PartCard" file="components/commerce/PartCard.jsx">
    <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fit,minmax(190px,1fr))',gap:'var(--grid-gap)'}}>
      <PartCard title="Lithium Battery 27+ Holes (NEO & EON)" price="369,00 €" fits={['NEO','EON']} />
      <PartCard title="Drive Train - Motor & Gearbox (NEO)" price="152,30 €" fits={['NEO']} />
      <PartCard title="Brake Kit (ONE)" price="7,30 €" fits={['ONE']} soldOut />
      <PartCard title="Magnetic Scorecard Holder" price="29,90 €" fits={['ALL']} />
    </div>
  </Card>
  <Card name="BuyBox" file="components/commerce/BuyBox.jsx">
    <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:28,alignItems:'start'}}>
      <BuyBox title="Wishbone EON" price="799,00 €" badge="best"
        delivery="2–4 working days · AT, DE, UK" partsNote="5 parts listed for the EON">
        <ColorwaySelector options={['charcoal-black','charcoal-red','white-red']} />
      </BuyBox>
      <SpecPanel specs={[
        {label:'Range', value:'27+', unit:'holes', note:'Lithium, one charge', levels:[1,.9,.8,.7,.6,.45,.3,.2]},
        {label:'Frame', value:'AL', note:'Aircraft-grade aluminium'},
        {label:'Fold size', value:'—', note:'Not yet measured'},
      ]} />
    </div>
  </Card>
  <Card name="ColorwaySelector" file="components/commerce/ColorwaySelector.jsx">
    <div style={{display:'flex',gap:40,flexWrap:'wrap'}}>
      <ColorwaySelector options={['charcoal-black','charcoal-lime','charcoal-red','white-red']} />
      <ColorwaySelector options={['charcoal-lime','white-red']} value="charcoal-lime" />
    </div>
  </Card>
  <Card name="ModelCompare" file="components/commerce/ModelCompare.jsx">
    <ModelCompare highlight="EON" models={MODELS} rows={[
      {label:'Type', values:{ONE:'Manual',TWO:'Manual',THREE:'Manual',NEO:'Electric',EON:'Electric'}},
      {label:'Price', values:{ONE:'—',TWO:'199 €',THREE:'249 €',NEO:'—',EON:'799 €'}},
      {label:'Range', values:{NEO:'27+ holes',EON:'27+ holes'}},
      {label:'Fold size', values:{}},
      {label:'Weight', values:{}},
      {label:'Parts listed', values:{ONE:'10',TWO:'2',THREE:'2',NEO:'14',EON:'5'}},
    ]} />
  </Card>
  <Card name="ProductCard" file="components/commerce/ProductCard.jsx">
    <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fit,minmax(200px,1fr))',gap:'var(--grid-gap)'}}>
      <ProductCard title="Wishbone EON" type="Electric trolley" price="799,00 €" badge="best" />
      <ProductCard title="Wishbone THREE" type="Manual trolley" price="249,00 €" />
      <ProductCard title="Fast Charger (NEO & EON)" type="Spare part" price="99,90 €" soldOut />
    </div>
  </Card>

  <div className="grouphead"><span className="n">B</span><h2>Content</h2>
    <p className="muted">The homepage runs three sections today. These are the blocks a page is actually built from.</p></div>
  <Card name="Hero" file="components/content/Hero.jsx">
    <Hero index="01" eyebrow="Electric" title="Wishbone EON"
      copy="A full powered, simple ‘no nonsense’ electric cart. Aircraft-grade aluminium frame, sealed bearings, magnetic attachments."
      cta="Add to cart · 799 €" secondary="Compare models"
      stats={[{label:'Range',value:'27+'},{label:'Frame',value:'AL'},{label:'Fold size',value:'—'},{label:'Parts',value:'05'}]} />
  </Card>
  <Card name="RangeStrip" file="components/content/RangeStrip.jsx">
    <RangeStrip models={[{id:'ONE',price:'—'},{id:'TWO',price:'199 €'},{id:'THREE',price:'249 €'},
      {id:'NEO',electric:true,price:'—'},{id:'EON',electric:true,price:'799 €'}]} />
  </Card>
  <Card name="TrustRow" file="components/content/TrustRow.jsx">
    <TrustRow items={[{label:'Spare parts listed',value:'22',note:'Across ONE, NEO and EON'},
      {label:'Designed in',value:'UK',note:'Birthed in Britain'},
      {label:'Delivery',value:'2–4 d',note:'AT · DE · UK'},
      {label:'Models',value:'05',note:'Three manual, two electric'}]} />
  </Card>
  <Card name="Accordion" file="components/content/Accordion.jsx">
    <Accordion items={[
      {q:'Can I replace the battery myself?', a:'Yes. The Lithium Battery 27+ Holes fits the NEO and the EON and is listed as a spare part at 369 €.'},
      {q:'Which parts fit my trolley?', a:'Ten are listed for the ONE, fourteen for the NEO and five for the EON. Four accessories fit every model.'},
      {q:'What is in the box?', a:'The trolley, the charger where applicable, and the bag straps. Holders are separate.'}]} />
  </Card>
  <Card name="InTheBox" file="components/content/InTheBox.jsx">
    <InTheBox items={[{name:'Wishbone EON trolley'},{name:'Fast charger'},{name:'Bag straps — set', qty:'2 ×'}]}
      note="Ball & tee, scorecard, umbrella and drink holders are sold separately and fit every model." />
  </Card>

  <div className="grouphead"><span className="n">C</span><h2>Core &amp; chrome</h2>
    <p className="muted">The primitives everything above is assembled from.</p></div>
  <Card name="Button" file="components/core/Button.jsx">
    <div style={row}><Button>Add to cart</Button><Button variant="ghost">Compare models</Button>
      <Button variant="quiet">Spare parts →</Button><Button disabled>Sold out</Button></div>
  </Card>
  <Card name="Stat" file="components/core/Stat.jsx">
    <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fit,minmax(220px,1fr))',gap:'var(--grid-gap)'}}>
      <Stat index="01" label="EON · Range" value="27+" unit="holes" note="One charge, lithium"
        footer={[{label:'Price',value:'799 €'},{label:'Fast charge',value:'Yes'}]}>
        <DotBars levels={[1,.95,.9,.8,.7,.6,.5,.4,.3,.2]} /></Stat>
      <Stat index="02" label="The range" value="05" note="ONE · TWO · THREE · NEO · EON"
        footer={[{label:'Manual',value:'03'},{label:'Electric',value:'02'}]}>
        <DotBars levels={[.4,.5,.6,.85,1]} /></Stat>
    </div>
  </Card>
  <Card name="DotMatrix" file="components/core/DotMatrix.jsx">
    <div style={{display:'flex',gap:28,flexWrap:'wrap',alignItems:'center'}}>
      <DotBars levels={[1,.95,.85,.75,.6,.5,.4,.3,.2,.12]} />
      <DotBars levels={[.2,.35,.5,.65,.8,1,.8,.65,.5,.35,.2]} />
    </div>
  </Card>
  <Card name="Input" file="components/core/Input.jsx">
    <div style={{...row, alignItems:'flex-end'}}>
      <Input label="Email address" placeholder="you@example.com" style={{width:240}} />
      <Input label="Email address" value="you@" error="Add the part after the @ — for example you@example.com." style={{width:330}} />
      <Badge kind="live" /><Badge kind="best" /><Badge kind="spare" />
    </div>
  </Card>
  <Card name="VariantPill" file="components/core/VariantPill.jsx">
    <div style={row}><VariantPill>ONE</VariantPill><VariantPill>TWO</VariantPill><VariantPill>THREE</VariantPill>
      <VariantPill selected>NEO</VariantPill><VariantPill unavailable>EON</VariantPill></div>
  </Card>
  <Card name="SiteHeader" file="components/chrome/*.jsx">
    <div style={{margin:'-22px -24px'}}><SiteHeader cartCount={2} />
      <div style={{padding:'22px 24px'}}><NewsletterBand /></div><SiteFooter /></div>
  </Card>
</div>);
"""
print("staged")

PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Wishbone — component library</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=Figtree:ital,wght@0,400;0,500;0,700;1,400&family=Share+Tech+Mono&display=swap" rel="stylesheet">
<style>
__TOKENS__
*{box-sizing:border-box}
body{margin:0;background:var(--color-carbon);color:var(--color-white);font-family:var(--font-body);
  font-size:15px;line-height:1.65;background-image:radial-gradient(120% 70% at 10% 0%, rgb(242 210 171 / .12), transparent 60%);
  background-attachment:fixed}
.wrap{max-width:1060px;margin:0 auto;padding:0 26px 110px}
h1,h2,h3{font-family:var(--font-display);font-weight:500;letter-spacing:-.02em;margin:0;line-height:1.05}
h1{font-size:52px} h2{font-size:30px}
header{border-bottom:1px solid var(--color-border);padding:52px 0 34px;margin-bottom:20px}
header img{width:290px;max-width:64%;display:block;margin-bottom:26px}
.label{font-family:var(--font-mono);font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--text-muted)}
.label b{color:var(--color-volt);font-weight:400}
.muted{color:var(--text-muted)}
code{font-family:var(--font-mono);font-size:12.5px;background:var(--surface-raised);padding:1px 6px;border-radius:4px}
table{width:100%;border-collapse:collapse;font-size:14px;margin:12px 0}
th,td{text-align:left;padding:9px 12px;border-bottom:1px solid var(--color-border);vertical-align:top}
th{font-family:var(--font-mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--text-muted);font-weight:400}
.sec{margin-top:58px}
.sec-head{display:flex;align-items:baseline;gap:14px;border-top:1px solid var(--color-border);padding-top:16px;margin-bottom:18px}
.num{font-family:var(--font-mono);font-size:12px;letter-spacing:.2em;color:var(--color-volt)}
.grouphead{border-top:1px solid var(--color-border);padding-top:20px;margin:48px 0 24px}
.grouphead .n{font-family:var(--font-mono);font-size:12px;letter-spacing:.2em;color:var(--color-volt)}
.grouphead h2{margin:8px 0 6px}
.block{background:var(--surface-card);border:1px solid var(--color-border);border-radius:20px;padding:22px 24px;margin:16px 0}
.finding{border-left:2px solid var(--color-volt);padding-left:16px;margin:14px 0}
.gap{border-left:2px solid var(--color-error);padding-left:16px;margin:14px 0}
.grid{display:grid;gap:18px}.g2{grid-template-columns:repeat(auto-fit,minmax(290px,1fr))}
ul{padding-left:18px;margin:8px 0}li{margin:5px 0}
footer{border-top:1px solid var(--color-border);margin-top:60px;padding-top:20px;color:var(--text-muted);font-size:13px}
</style></head><body><div class="wrap">

<header>
  <img src="__WORD__" alt="Wishbone Golf">
  <div class="label"><b>V2</b>&nbsp;&nbsp;COMPONENT LIBRARY · 19 SEPTEMBER 2026</div>
  <h1>Built for this catalogue</h1>
  <p class="muted" style="max-width:690px;margin-top:14px">Twenty-one components, all rendered below from their real
  source with real catalogue data. The commerce set was designed against what wishbone.golf actually sells — which,
  once you look, is mostly spare parts.</p>
</header>

<section class="sec">
  <div class="sec-head"><span class="num">01</span><h2>What the store has today</h2></div>
  <table>
    <tr><th>Reading</th><th>Value</th><th>What it means for the library</th></tr>
    <tr><td>Homepage sections</td><td class="readout" style="font-family:var(--font-mono)">3</td><td>Two image-with-text blocks and a paragraph. No hero, no range, no proof, no FAQ.</td></tr>
    <tr><td>Products</td><td style="font-family:var(--font-mono)">27</td><td>5 trolleys · <b>22 spare parts &amp; accessories</b></td></tr>
    <tr><td>Parts with no photograph</td><td style="font-family:var(--font-mono);color:var(--color-error)">15</td><td>Why <code>PartCard</code> falls back to a dot-matrix plate instead of a grey box</td></tr>
    <tr><td>Products with no description</td><td style="font-family:var(--font-mono);color:var(--color-error)">8</td><td>Components must read well with a title and a price alone</td></tr>
    <tr><td>Parts per model</td><td style="font-family:var(--font-mono)">ONE 10 · NEO 14 · EON 5 · TWO 2 · THREE 2</td><td>The compatibility finder's whole reason to exist</td></tr>
    <tr><td>Colourways</td><td style="font-family:var(--font-mono)">4</td><td>charcoal-black · charcoal-lime · charcoal-red · white-red — two-tone, so swatches are split circles</td></tr>
    <tr><td>Templates already per model</td><td style="font-family:var(--font-mono)">7</td><td><code>product.trolley_eon</code>, <code>collection.spare_one</code>, <code>collection.spare_neo</code>… the structure exists, the components did not</td></tr>
  </table>
  <div class="finding"><b>The catalogue is a parts business wearing a trolley shop's clothes.</b>
  Twenty-two of twenty-seven products are spare parts, the theme already carries per-model spare collections, and every
  part is named <code>Component (MODEL)</code>. Nothing on the storefront helps a customer use that — so the first
  component in this library is the one that does.</div>
  <div class="gap"><b>Two data gaps worth fixing before design work.</b> Fifteen parts have no photograph, and TWO and
  THREE have almost no parts listed — either they share the ONE's parts and the catalogue does not say so, or there is a
  genuine hole in what is offered. The components surface both rather than hiding them.</div>
</section>

<section class="sec">
  <div class="sec-head"><span class="num">02</span><h2>The library</h2></div>
  <p class="muted" style="margin-top:-6px">Live, from the pushed source. Notes under each component are the first line of
  its <code>prompt.md</code>.</p>
  <div id="lib"><p class="muted">Loading React from unpkg to render the components… if this stays, the page is offline.</p></div>
</section>

<section class="sec">
  <div class="sec-head"><span class="num">03</span><h2>What to build next</h2></div>
  <div class="grid g2">
    <div>
      <h3 style="font-size:20px">Fits content that exists</h3>
      <ul class="muted">
        <li><b>PartsDiagram</b> — an exploded trolley with hotspots to each listed part. The highest-value thing this
        catalogue could have, and it works without part photography.</li>
        <li><b>CollectionGrid + filters</b> — filter by model, by type, by in-stock. The tags are already there.</li>
        <li><b>CartDrawer</b> — with a "parts that fit your trolley" slot.</li>
        <li><b>ProductGallery</b> — trolleys average 2.5 images; the gallery should not pretend there are ten.</li>
        <li><b>SearchResults</b> — part-number and model-aware.</li>
        <li><b>StockNote</b> — restock date, not "currently unavailable".</li>
      </ul>
    </div>
    <div>
      <h3 style="font-size:20px">New directions</h3>
      <ul class="muted">
        <li><b>FoldSequence</b> — three frames, one camera, the fold. The most persuasive thing the product does and it
        is nowhere on the site.</li>
        <li><b>RangeCalculator</b> — holes per charge against course and load; turns "27+" into a personal answer.</li>
        <li><b>ServiceGuide</b> — step-by-step fitting for each part, with the tool needed. Sells parts and prevents returns.</li>
        <li><b>DealerFinder</b> — if there is a stockist network, it belongs on the site.</li>
        <li><b>Reviews</b> — none exist today; a repairability brand should be collecting them.</li>
        <li><b>RegistrationFlow</b> — register a trolley, get its parts list. Ties the catalogue to an owner.</li>
      </ul>
    </div>
  </div>
  <p class="muted" style="margin-top:14px">Each of these is a component plus content. The content can follow — the
  library is built so a block renders honestly with a title, a number and an em dash where a value is missing.</p>
</section>

<footer>
  21 components · pushed to the Claude Design project <em>Wishbone Golf Design System</em> ·
  source <code>design-system/components/</code>, generator <code>tools/build-library.py</code> ·
  data read from wishbone.golf on 19 September 2026 · the live theme is unchanged
</footer>
</div>

<script src="https://unpkg.com/react@18.3.1/umd/react.development.js" crossorigin></script>
<script src="https://unpkg.com/react-dom@18.3.1/umd/react-dom.development.js" crossorigin></script>
<script src="https://unpkg.com/@babel/standalone@7.29.0/babel.min.js" crossorigin></script>
<script>window.RULES = __RULES__;</script>
<script type="text/babel">
const { useState, useEffect, useRef } = React;
__SRC__
__DEMO__
</script>
</body></html>
"""

out = (PAGE.replace('__TOKENS__', tokens).replace('__WORD__', WORD)
           .replace('__RULES__', json.dumps(rules))
           .replace('__SRC__', src).replace('__DEMO__', DEMO))
dest = pathlib.Path('/tmp/wb/kit/wishbone-library.html')
dest.parent.mkdir(parents=True, exist_ok=True)
dest.write_text(out)
print('wrote', dest, round(len(out)/1024), 'KB ·', len(ORDER), 'components')
