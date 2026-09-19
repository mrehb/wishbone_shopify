#!/usr/bin/env python3
"""Render the v3 "Instrument" system as one page, from the real component source."""
import re, base64, pathlib, json
ROOT = pathlib.Path(__file__).resolve().parent.parent
uri = lambda p: "data:image/png;base64," + base64.b64encode((ROOT/p).read_bytes()).decode()
WORD, MONO = uri('assets/wishbone-wordmark.png'), uri('assets/wishbone-monogram-lime.png')
def fix(s):
    return (s.replace('../../assets/wishbone-wordmark.png', WORD).replace('../assets/wishbone-wordmark.png', WORD)
             .replace('../../assets/wishbone-monogram-lime.png', MONO).replace('../assets/wishbone-monogram-lime.png', MONO))
tokens = "".join("\n" + re.sub(r"@import[^;]+;", "", (ROOT/'tokens'/f).read_text()) for f in ['colors.css','typography.css','geometry.css','layout.css','base.css'])
ORDER = ['primitives/Tile','primitives/Dots','primitives/Pill','primitives/Field','primitives/Readout','primitives/Silhouettes',
         'tiles/HeroTile','tiles/RangeTile','tiles/ProductTile','tiles/PartTile','tiles/CompatTile','tiles/BuyTile','tiles/SpecTile',
         'tiles/CompareTile','tiles/FaqTile','tiles/BoxTile','tiles/TrustTile','chrome/TopBar','chrome/FootBar']
src, rules = "", {}
for rel in ORDER:
    j = (ROOT/'components'/f'{rel}.jsx').read_text()
    j = re.sub(r"^import .*$", "", j, flags=re.M); j = re.sub(r"^export ", "", j, flags=re.M)
    src += fix(j) + "\n"
    pm = ROOT/'components'/f'{rel}.prompt.md'
    if pm.exists():
        paras = [x.strip() for x in pm.read_text().split('\n\n') if x.strip() and not x.startswith('#')]
        rules[rel.split('/')[1]] = ' '.join(paras[0].split())

DEMO = r"""
const MODELS=[{id:'ONE'},{id:'TWO'},{id:'THREE'},{id:'NEO'},{id:'EON'}];
const PARTS=[{title:'Frame (ONE)',fits:['ONE'],price:'89,00 €'},{title:'Rear Wheel Right (ONE)',fits:['ONE'],price:'24,20 €'},{title:'Brake Kit (ONE)',fits:['ONE'],price:'7,30 €'},
 {title:'Front Wheel Kit - Universal fit (ONE & NEO)',fits:['ONE','NEO'],price:'37,40 €'},{title:'Controller (NEO)',fits:['NEO'],price:'62,00 €'},{title:'Drive Train - Motor & Gearbox (NEO)',fits:['NEO'],price:'152,30 €'},
 {title:'Thumb Throttle Kit (NEO)',fits:['NEO'],price:'44,00 €'},{title:'Lithium Battery 27+ Holes (NEO & EON)',fits:['NEO','EON'],price:'369,00 €'},{title:'Fast Charger (NEO & EON)',fits:['NEO','EON'],price:'99,90 €'},
 {title:'Wing Screw for Umbrella Holder (ONE, NEO & EON)',fits:['ONE','NEO','EON'],price:'7,90 €'},{title:'Magnetic Scorecard Holder',fits:['ALL'],price:'29,90 €'},{title:'Umbrella Holder',fits:['ALL'],price:'29,90 €'}];
const Note = ({k}) => <p className="grey" style={{fontSize:'var(--fs-label)',letterSpacing:'.04em',lineHeight:1.5,margin:'8px 0 0',maxWidth:'90ch'}}>{window.RULES[k]||''}</p>;

ReactDOM.createRoot(document.getElementById('store')).render(<div>
  <TopBar cart={2} />
  <Board>
    <HeroTile n="01" label="electric" title="EON" model="EON" copy="A full powered, simple ‘no nonsense’ electric cart." cta="Add to cart · 799 €" secondary="Compare models"
      stats={[{label:'range',value:'27+'},{label:'frame',value:'AL'},{label:'fold size',value:'—'},{label:'parts',value:'05'}]} />
    <RangeTile n="02" models={[{id:'ONE',price:'—'},{id:'TWO',price:'199 €'},{id:'THREE',price:'249 €'},{id:'NEO',electric:true,price:'—'},{id:'EON',electric:true,price:'799 €'}]} />
    <CompatTile n="03" models={MODELS} parts={PARTS} />
    <BuyTile n="04" title="EON" price="799,00 €" colourways={['charcoal-black','charcoal-lime','charcoal-red','white-red']} delivery="2–4 days · AT DE UK" parts={5} />
    <SpecTile n="05" label="range" value="27+" unit="holes" note="lithium, one charge" levels={[1,.9,.8,.7,.6,.45,.3,.2]} />
    <SpecTile n="06" label="charge" pct={.78} value="78" unit="%" note="fast charger" />
    <SpecTile n="07" label="fold size" value="—" />
    <CompareTile n="08" highlight="EON" models={MODELS} rows={[{label:'type',values:{ONE:'manual',TWO:'manual',THREE:'manual',NEO:'electric',EON:'electric'}},
      {label:'price',values:{TWO:'199 €',THREE:'249 €',EON:'799 €'}},{label:'range',values:{NEO:'27+',EON:'27+'}},{label:'fold size',values:{}},{label:'weight',values:{}},{label:'parts listed',values:{ONE:'10',TWO:'2',THREE:'2',NEO:'14',EON:'5'}}]} />
    <ProductTile n="09" model="THREE" title="THREE" type="manual" price="249,00 €" status="in stock" hot />
    <ProductTile n="10" model="NEO" title="NEO" type="electric" price="—" status="sold out" soldOut />
    <PartTile n="11" title="Lithium Battery 27+ Holes (NEO & EON)" price="369,00 €" fits={['NEO','EON']} />
    <FaqTile n="12" items={[{q:'Can I replace the battery myself?',a:'Yes. The Lithium Battery 27+ Holes fits the NEO and the EON and is listed as a spare part at 369 €.'},{q:'Which parts fit my trolley?',a:'Ten are listed for the ONE, fourteen for the NEO and five for the EON. Four accessories fit every model.'},{q:'What is in the box?',a:'The trolley, the charger where applicable, and the bag straps. Holders are separate.'}]} />
    <BoxTile n="13" items={[{name:'EON trolley'},{name:'Fast charger'},{name:'Bag straps — set',qty:'2 ×'}]} note="Ball & tee, scorecard, umbrella and drink holders are sold separately and fit every model." />
    <TrustTile n="14" label="spare parts listed" value="22" hot />
    <TrustTile n="15" label="designed in" value="UK" note="Birthed in Britain" />
    <TrustTile n="16" label="delivery" value="2–4" unit="days" note="AT · DE · UK" />
  </Board>
  <FootBar />
</div>);

ReactDOM.createRoot(document.getElementById('prims')).render(<div>
  <Board>
    <Tile n="01" label="pill"><div style={{display:'flex',gap:8,flexWrap:'wrap'}}>
      <Pill kind="button">Add to cart</Pill><Pill kind="ghost">Compare</Pill><Pill kind="tag">NEO</Pill><Pill kind="status" hot>live</Pill><Pill kind="status">idle</Pill><Pill kind="select" on>EON</Pill><Pill kind="select">ONE</Pill><Pill kind="button" disabled>Sold out</Pill></div><Note k="Pill" /></Tile>
    <Tile n="02" label="dots" span={2}><div style={{display:'flex',gap:22,alignItems:'flex-end',flexWrap:'wrap'}}>
      <Dots {...bars([1,.9,.8,.65,.5,.4,.3,.2],7,.95)} /><Dots {...ring(.66)} /><Dots {...line([.2,.4,.3,.6,.8,1,.7,.6,.65,.5],9)} /><Dots {...steps(5,3)} /><Dots {...wave(30,7)} /></div><Note k="Dots" /></Tile>
    <Tile n="03" label="readout" hot><Readout value="27+" unit="holes" note="one charge" /><Note k="Readout" /></Tile>
    <Tile n="04" label="field" span={2}><div style={{display:'flex',gap:12,alignItems:'flex-end',flexWrap:'wrap'}}>
      <Field label="email address" placeholder="you@example.com" style={{flex:'1 1 200px'}} />
      <Field label="email address" value="you@" error="Add the part after the @ — for example you@example.com." style={{flex:'1 1 280px'}} /></div><Note k="Field" /></Tile>
    <Tile n="05" label="silhouette"><Dots {...silhouette('EON')} size={4} gap={2} /><Note k="Silhouettes" /></Tile>
  </Board>
</div>);
"""

PAGE = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Wishbone v3 — Instrument</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DotGothic16&family=VT323&display=swap" rel="stylesheet">
<style>__TOKENS__
.wrap{max-width:1200px;margin:0 auto;padding:0 20px 100px}
.hd{padding:44px 0 26px;border-bottom:1px solid var(--tile-line);margin-bottom:26px}
.hd img{width:300px;max-width:64%;display:block;margin-bottom:22px}
.sec{margin-top:56px}.sec .label{margin-bottom:14px}
table{width:100%;border-collapse:collapse}th,td{text-align:left;padding:9px 12px;border-bottom:1px solid var(--tile-line);vertical-align:top}
th{font-weight:400}
.tile{background:var(--tile);border-radius:var(--r-tile);padding:var(--pad);box-shadow:inset 0 1px 0 var(--tile-edge)}
footer{border-top:1px solid var(--tile-line);margin-top:56px;padding-top:18px}
</style></head><body><div class="wrap">
<div class="hd"><img src="__WORD__" alt="Wishbone Golf">
  <div class="label"><b>v3</b>&nbsp;&nbsp;instrument · rebuilt from the references · 19 september 2026</div>
  <h1 class="cursor" style="margin-top:14px">One of everything</h1>
  <p style="font-size:var(--fs-lead);max-width:56ch;margin-top:14px">v2 hedged: three typefaces, five radii, a dot device on top of a generic dark UI, and two colours both called "the green". v3 keeps one of each thing and nothing else. Below is the whole store as a board, rendered from the real components.</p></div>

<div class="sec"><div class="label"><b>01</b>&nbsp;&nbsp;what changed</div>
<table><tr><th class="label">&nbsp;</th><th class="label">v2</th><th class="label">v3</th></tr>
<tr><td>type</td><td class="grey">Space Grotesk + Figtree + Share Tech Mono</td><td><b>DotGothic16</b> — one dot-matrix family, every size</td></tr>
<tr><td>container</td><td class="grey">cards, panels, bands, heroes, wells</td><td><b>the Tile</b> on a <b>Board</b> — nothing else</td></tr>
<tr><td>radius</td><td class="grey">20 · 16 · 10 · 8 · 999</td><td><b>24</b> (tile) · <b>999</b> (pill)</td></tr>
<tr><td>graphic</td><td class="grey">dots + gradients + swatches + icons</td><td><b>dots only</b> — 6px / 3px, photo-sampled silhouettes</td></tr>
<tr><td>green</td><td class="grey">volt #E3FC02 (hue 66°, a yellow-green)</td><td><b>lime #A8FF4A</b> (hue 89° — the hardware's green)</td></tr>
<tr><td>text colours</td><td class="grey">white, muted, error red</td><td><b>white, grey</b>. No red — attention is lime</td></tr>
<tr><td>grid</td><td class="grey">1440 / 72 / 20, mixed spans</td><td><b>1200 · 16px gap · 3/2/1</b>, tiles span 1–3</td></tr>
<tr><td>atmosphere</td><td class="grey">wash + per-card gradients</td><td><b>one lamp</b>, top-left; tiles catch it as a 1px edge</td></tr></table></div>

<div class="sec"><div class="label"><b>02</b>&nbsp;&nbsp;the store, as a board</div>
<div id="store"><p class="grey">loading react from unpkg…</p></div></div>

<div class="sec"><div class="label"><b>03</b>&nbsp;&nbsp;primitives</div>
<div id="prims"></div></div>

<div class="sec"><div class="label"><b>04</b>&nbsp;&nbsp;the marks</div>
<div style="display:grid;grid-template-columns:1.4fr 1fr;gap:var(--grid-gap)">
  <div class="tile" style="display:flex;align-items:center;justify-content:center"><img src="__WORD__" style="width:78%"></div>
  <div class="tile" style="display:flex;align-items:center;justify-content:center"><img src="__MONO__" style="width:62%"></div></div>
<p class="grey" style="font-size:var(--fs-label);letter-spacing:.04em;margin-top:12px">monogram recut: the quarter-circle is now lime #A8FF4A — the same green as the hardware and the accent. still to commission: positive and SVG versions of both marks.</p></div>

<div class="sec"><div class="label"><b>05</b>&nbsp;&nbsp;still open</div>
<table><tr><td>01</td><td>fold size and weight — unmeasured for every model; every readout that needs them prints —</td></tr>
<tr><td>02</td><td>photograph ONE, TWO, THREE, NEO to §light so their silhouettes can be sampled like the EON's</td></tr>
<tr><td>03</td><td>positive + SVG marks</td></tr>
<tr><td>04</td><td>the theme still runs v1 — this is the target, nothing is live</td></tr>
<tr><td>05</td><td>brand book to regenerate for v3</td></tr></table></div>

<footer class="label">wishbone golf · v3 instrument · 19 components · generated from design-system/components by tools/build-v3.py · live theme unchanged</footer>
</div>
<script src="https://unpkg.com/react@18.3.1/umd/react.production.min.js" crossorigin></script>
<script src="https://unpkg.com/react-dom@18.3.1/umd/react-dom.production.min.js" crossorigin></script>
<script src="https://unpkg.com/@babel/standalone@7.29.0/babel.min.js" crossorigin></script>
<script>window.RULES = __RULES__;</script>
<script type="text/babel">
const { useState, useEffect, useRef } = React;
__SRC__
__DEMO__
</script></body></html>"""
out = (PAGE.replace('__TOKENS__', tokens).replace('__WORD__', WORD).replace('__MONO__', MONO)
           .replace('__RULES__', json.dumps(rules)).replace('__SRC__', src).replace('__DEMO__', DEMO))
dest = pathlib.Path('/tmp/wb/kit/wishbone-v3.html'); dest.parent.mkdir(parents=True, exist_ok=True); dest.write_text(out)
print('wrote', dest, round(len(out)/1024), 'KB ·', len(ORDER), 'component files')
