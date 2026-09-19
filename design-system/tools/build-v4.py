#!/usr/bin/env python3
"""Render the v4 "Studio" system as one page, from the real component source."""
import re, base64, pathlib, json
ROOT = pathlib.Path(__file__).resolve().parent.parent
uri = lambda p: "data:image/png;base64," + base64.b64encode((ROOT/p).read_bytes()).decode()
A = {n: uri(f'assets/{n}.png') for n in ['wishbone-wordmark','wishbone-wordmark-ink','wishbone-monogram-lime','wishbone-monogram-ink']}
def fix(s):
    for n, u in A.items(): s = s.replace(f'../../assets/{n}.png', u).replace(f'../assets/{n}.png', u)
    return s
tokens = "".join("\n" + re.sub(r"@import[^;]+;", "", (ROOT/'tokens'/f).read_text()) for f in ['colors.css','typography.css','geometry.css','layout.css','base.css'])
ORDER = ['primitives/Eyebrow','primitives/Display','primitives/Button','primitives/Stat','primitives/Field','primitives/Tag','primitives/Price','primitives/Dots','primitives/Silhouette',
         'sections/Hero','sections/Stats','sections/Lineup','sections/Feature','sections/Trust','sections/Inquiry','sections/Buy','sections/Specs','sections/Compare','sections/Parts','sections/Faq',
         'chrome/Header','chrome/Footer']
src, rules = "", {}
for rel in ORDER:
    j = (ROOT/'components'/f'{rel}.jsx').read_text()
    j = re.sub(r"^import .*$", "", j, flags=re.M); j = re.sub(r"^export ", "", j, flags=re.M)
    src += fix(j) + "\n"
    pm = ROOT/'components'/f'{rel}.prompt.md'
    paras = [x.strip() for x in pm.read_text().split('\n\n') if x.strip() and not x.startswith('#')]
    rules[rel.split('/')[1]] = ' '.join(paras[0].split())
data = pathlib.Path('/tmp/wb/demo-data.js').read_text()
# the two page cards, body only
def card_body(rel):
    t = (ROOT/'components'/rel).read_text()
    b = t.split("const ns = window.WishboneGolfDesignSystem_4d0e77 || {};")[1].split("</script>")[0]
    b = b[b.index("const { Header"):]  # drop the demo data; the page includes it once
    return fix(b).replace("ReactDOM.createRoot(document.getElementById('root'))", "ReactDOM.createRoot(document.getElementById('__ID__'))")
# the components are already in scope on the page, so the cards' destructuring lines are dropped
HOME = re.sub(r"^const \{[^}]*\} = ns;\n", "", card_body('sections/sections.card.html'), flags=re.M).replace('__ID__', 'home')
PROD = re.sub(r"^const \{[^}]*\} = ns;\n", "", card_body('sections/commerce.card.html'), flags=re.M).replace('__ID__', 'prod')
PRIMS = r"""
const Row = ({label, k, children}) => <div style={{display:'grid',gridTemplateColumns:'160px 1fr',gap:24,padding:'24px 0',borderTop:'1px solid var(--hair)'}}><div><div className="label">{label}</div><p className="grey" style={{fontSize:13,lineHeight:1.5,marginTop:8}}>{window.RULES[k]}</p></div><div style={{display:'flex',gap:16,flexWrap:'wrap',alignItems:'center'}}>{children}</div></div>;
ReactDOM.createRoot(document.getElementById('prims')).render(<div>
  <Row label="eyebrow" k="Eyebrow"><Eyebrow n="01">The lineup</Eyebrow><div className="band--ink" style={{padding:'10px 14px'}}><Eyebrow n="03">Battery</Eyebrow></div></Row>
  <Row label="display" k="Display"><Display lines={['Light.','Simple.','British.']} size="s" /></Row>
  <Row label="button" k="Button"><Button kind="lime" arrow>Shop EON</Button><Button kind="ink" arrow>Compare</Button><Button kind="outline" arrow>Watch film</Button><Button kind="text" arrow>All parts</Button><Button kind="lime" disabled>Sold out</Button></Row>
  <Row label="stat" k="Stat"><div style={{width:'100%'}}><StatRow items={[{value:'27+',unit:'holes',label:'range'},{value:'5',label:'models'},{value:'22',label:'spare parts'},{value:null,label:'weight'}]} /></div></Row>
  <Row label="field" k="Field"><Field label="Email" placeholder="you@example.com" style={{flex:'1 1 240px'}} /><Field label="Email" value="you@" error="Add the part after the @ — for example you@example.com." style={{flex:'1 1 280px'}} /></Row>
  <Row label="tag" k="Tag"><Tag on>NEO</Tag><Tag>ONE & NEO</Tag><Tag>ALL</Tag></Row>
  <Row label="price" k="Price"><Price value="799,00 €" /><Price value="199,00 €" from /><Price value="—" /><Price value="24,20 €" compare="29,90 €" /></Row>
  <Row label="photo" k="Silhouette"><Photo src={IMG.EON} model="EON" style={{width:180}} /><Photo model="EON" style={{width:180}} /><Photo model="ONE" style={{width:180}} /><Photo model="NEO" tone="paper" style={{width:180}} /></Row>
</div>);
"""
PAGE = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Wishbone v4 — Studio</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600&family=DotGothic16&display=swap" rel="stylesheet">
<style>__TOKENS__
.doc{max-width:1200px;margin:0 auto;padding:0 32px}
.hd{padding:48px 0 32px;border-bottom:1px solid var(--hair);margin-bottom:8px}
.hd img{height:16px;width:auto;margin-bottom:28px}
.sec{padding:56px 0 0}.sec>.eyebrow{margin-bottom:20px}
table{width:100%;border-collapse:collapse;font-size:14px}th,td{text-align:left;padding:10px 12px 10px 0;border-bottom:1px solid var(--hair);vertical-align:top}th{font-weight:500}
.frame{border:1px solid var(--hair);margin-top:24px}
.frame .container{max-width:1136px}
footer.doc{border-top:1px solid var(--hair);margin-top:64px;padding-top:20px;padding-bottom:80px}
</style></head><body>
<div class="doc"><div class="hd"><img src="__WORD__" alt="Wishbone Golf">
  <div class="eyebrow"><b>v4</b>Studio · rebuilt to the new reference · 19 September 2026</div>
  <h1 class="display display--hero" style="margin-top:20px">White.<br>Measured.<br>One lime.</h1>
  <p class="lead grey" style="max-width:58ch;margin-top:20px">v3 was too dark and had too many dots. The new reference is a white, product-led page with a light sans, hairlines, one dark band and a lime button used once. And the store already photographs everything on white — so the site is white. The dot voice stays in one place: the small numbered label above each headline.</p></div>

<div class="sec"><div class="eyebrow"><b>01</b>What changed</div>
<table><tr><th></th><th>v3 Instrument</th><th>v4 Studio</th></tr>
<tr><td>ground</td><td class="grey">#0F1014, one warm lamp</td><td><b>paper #FFFFFF / mist #F4F4F5</b>; ink once per page</td></tr>
<tr><td>type</td><td class="grey">DotGothic16 for everything</td><td><b>Manrope</b> 300 caps headlines, 400 body, 500 labels, 600 price</td></tr>
<tr><td>the dots</td><td class="grey">every string, plus charts, gauges, rings, waves</td><td><b>the eyebrow</b> in DotGothic16, and silhouettes for unphotographed parts</td></tr>
<tr><td>container</td><td class="grey">the Tile, on a Board</td><td><b>bands</b>, full bleed, 5 : 7 halves, hairline tables</td></tr>
<tr><td>radius</td><td class="grey">24 / 999</td><td><b>0</b></td></tr>
<tr><td>lime</td><td class="grey">one element per tile, on dark</td><td><b>one button per view</b> + small marks; never text on paper</td></tr>
<tr><td>photography</td><td class="grey">warm lamp, dark ground — none existed</td><td><b>the store's white studio shots</b>, multiplied onto mist — all of them usable today</td></tr></table></div>
</div>

<div class="doc sec"><div class="eyebrow"><b>02</b>Home</div></div>
<div class="frame" id="home"><p class="grey doc" style="padding:24px 32px">loading react from unpkg…</p></div>

<div class="doc sec"><div class="eyebrow"><b>03</b>Product, compare, parts</div></div>
<div class="frame" id="prod"></div>

<div class="doc sec"><div class="eyebrow"><b>04</b>Primitives</div><div id="prims"></div></div>

<div class="doc sec"><div class="eyebrow"><b>05</b>Marks</div>
<div style="display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:16px;margin-top:8px">
  <div style="border:1px solid var(--hair);padding:48px;display:flex;align-items:center;justify-content:center"><img src="__WORDINK__" style="width:78%"></div>
  <div style="border:1px solid var(--hair);padding:32px;display:flex;align-items:center;justify-content:center"><img src="__MONOINK__" style="width:60%"></div>
  <div style="background:var(--ink);padding:32px;display:flex;align-items:center;justify-content:center"><img src="__MONO__" style="width:60%"></div></div>
<p class="grey" style="font-size:13px;margin-top:12px">positive marks cut for paper; the quarter-circle stays lime #A8FF4A on both. SVG masters still to commission.</p></div>

<div class="doc sec"><div class="eyebrow"><b>06</b>Still open</div>
<table><tr><td>01</td><td>fold size and weight — unmeasured for every model; every table that needs them prints —</td></tr>
<tr><td>02</td><td>fifteen parts and the NEO have no photograph; they draw silhouettes until they do</td></tr>
<tr><td>03</td><td>SVG masters of the marks; ™ vs ®</td></tr>
<tr><td>04</td><td>the theme still runs v1 — this is the target, nothing is live</td></tr>
<tr><td>05</td><td>a lifestyle photograph for the About band: overcast course, grey sky, the trolley the only saturated thing</td></tr></table></div>

<footer class="doc label grey">wishbone golf · v4 studio · 22 components · generated from design-system/components by tools/build-v4.py · live theme unchanged</footer>
<script src="https://unpkg.com/react@18.3.1/umd/react.production.min.js" crossorigin></script>
<script src="https://unpkg.com/react-dom@18.3.1/umd/react-dom.production.min.js" crossorigin></script>
<script src="https://unpkg.com/@babel/standalone@7.29.0/babel.min.js" crossorigin></script>
<script>window.RULES = __RULES__;</script>
<script type="text/babel">
const { useState, useEffect, useRef, useId } = React;
__SRC__
__DATA__
__HOME__
__PROD__
__PRIMS__
</script></body></html>"""
out = (PAGE.replace('__TOKENS__', tokens).replace('__WORD__', A['wishbone-wordmark-ink']).replace('__WORDINK__', A['wishbone-wordmark-ink'])
           .replace('__MONOINK__', A['wishbone-monogram-ink']).replace('__MONO__', A['wishbone-monogram-lime'])
           .replace('__RULES__', json.dumps(rules)).replace('__SRC__', src).replace('__DATA__', data).replace('__HOME__', HOME).replace('__PROD__', PROD).replace('__PRIMS__', PRIMS))
dest = pathlib.Path('/tmp/wb/kit/wishbone-v4.html'); dest.parent.mkdir(parents=True, exist_ok=True); dest.write_text(out)
print('wrote', dest, round(len(out)/1024), 'KB ·', len(ORDER), 'component files')
