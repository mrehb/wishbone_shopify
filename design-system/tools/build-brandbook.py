#!/usr/bin/env python3
"""Wishbone Golf brand book v3 "Instrument" — one self-contained HTML document,
set in the system it documents. Regenerate after any token change."""
import base64, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parent.parent
uri = lambda p: "data:image/png;base64," + base64.b64encode((ROOT/p).read_bytes()).decode()
WORD, MONO, MONO_OLD = uri('assets/wishbone-wordmark.png'), uri('assets/wishbone-monogram-lime.png'), uri('assets/wishbone-monogram.png')
tokens = "".join("\n" + re.sub(r"@import[^;]+;", "", (ROOT/'tokens'/f).read_text()) for f in ['colors.css','typography.css','geometry.css','layout.css','base.css'])

def card(name):  # inline a guideline specimen's body so the book shows the real card
    src = (ROOT/'guidelines'/f'{name}.html').read_text()
    body = re.search(r'<body[^>]*>(.*)</body>', src, re.S).group(1)
    return body.replace('../assets/wishbone-wordmark.png', WORD).replace('../assets/wishbone-monogram-lime.png', MONO)

CH = []
def ch(n, slug, title, lede, body):
    CH.append((n, slug, title))
    return f'<section class="ch" id="{slug}"><div class="label"><b>{n}</b>&nbsp;&nbsp;{title}</div><h2 class="t">{title}</h2><p class="lede">{lede}</p>{body}</section>'

T = lambda inner, extra='': f'<div class="tile" {extra}>{inner}</div>'
def table(rows, head=None):
    h = f"<tr>{''.join(f'<th class=label>{c}</th>' for c in head)}</tr>" if head else ''
    return "<table>" + h + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</table>"

B = []
B.append(ch('01','brand','The brand',
 'Wishbone makes golf trolleys that are measured objects: light, simple, British. The brand reports what the product is.',
 T('<div class="label"><b>1.1</b>&nbsp;&nbsp;the statement</div><p style="font-size:var(--fs-h);line-height:1.15;margin-top:14px" class="cursor">Birthed in Britain, Wishbone Golf merges exquisite design with unwavering quality</p><p class="grey" style="margin-top:12px">The brand\'s own words. Nothing in this book replaces them.</p>')
 + '<h3 class="t">1.2 pillars</h3><div class="board">'
 + T('<div class="label"><b>01</b>&nbsp;&nbsp;engineered light</div><p style="margin-top:12px">Aircraft-grade aluminium, no bulk. Every claim provable by picking the thing up.</p>')
 + T('<div class="label"><b>02</b>&nbsp;&nbsp;no nonsense</div><p style="margin-top:12px">The brand\'s own phrase, from the EON copy. It governs the product, the site and this book.</p>')
 + T('<div class="label"><b>03</b>&nbsp;&nbsp;british design</div><p style="margin-top:12px">Stated once — “Birthed in Britain” — then demonstrated by the object, never repeated as an adjective.</p>')
 + '</div><h3 class="t">1.3 architecture</h3>'
 + table([['Company','<b>Wishbone Golf</b>','prose and legal'],['Family','<b>Wishbone</b>','“a Wishbone trolley”'],['Manual','<b>ONE · TWO · THREE</b>','Wishbone ONE — caps, always'],['Electric','<b>NEO · EON</b>','Wishbone EON'],['Parts','<code>Component (MODEL)</code>','Fast Charger (NEO & EON) — never trimmed']], ['level','name','written as'])
 + '<h3 class="t">1.4 the range</h3>'
 + table([['ONE','manual, 3 wheel','—','10 parts listed'],['TWO','manual','199 €','2'],['THREE','manual','249 €','2'],['NEO','electric','—','14'],['EON','electric, flagship','799 €','5']], ['model','type','price','parts'])
 + '<p class="grey">27 products live; 22 are spare parts. One is still published under vendor <em>My Store</em>.</p>'))

B.append(ch('02','voice','Voice',
 'Report the value, then stop. The voice did not change in any version — the design finally matches it.',
 '<div class="board">'
 + T('<div class="label"><b>do</b></div><ul><li>Say the number — 27+ holes, 799 €, 05 models</li><li>Name the material — aircraft-grade aluminium, sealed bearings</li><li>One idea per sentence</li><li>Print — for a value you do not have</li><li>British spelling</li></ul>','style="grid-column:span 1"')
 + T('<div class="label">don\'t</div><ul class="grey"><li>innovative · premium · game-changing</li><li>exclamation marks, emoji</li><li>invent a spec to fill a tile</li><li>bury shipping or returns in an accordion</li><li>“aluminum” in British copy</li></ul>')
 + T('<div class="label"><b>the cursor</b></div><p style="margin-top:12px">A statement may end with <span class="lime">_</span> — the hero title and the footer line only. It marks the brand as an instrument that is still running, not a slogan that is finished.</p>')
 + '</div><h3 class="t">2.1 house style</h3>'
 + table([['Models','caps: ONE, TWO, THREE, NEO, EON'],['Numbers','digits; tile numbers two-digit: 01'],['Prices','799,00 € on the storefront, 799 € in prose'],['Unknown','<b>—</b> with <em>not yet measured</em>. Never estimate, never hide the row'],['Buttons','sentence case, verb first: Add to cart · Compare models'],['Headings','sentence case; labels uppercase, tracked 0.14em'],['Case of the brand','Wishbone Golf · Wishbone · WISHBONE only in the mark']], ['item','rule'])
 + '<h3 class="t">2.2 microcopy</h3>'
 + table([['status line','All systems operational · Spare parts ship same day'],['sold out','Sold out — back on <em>date</em>'],['field error','▸ Add the part after the @ — for example you@example.com.'],['empty cart','Nothing in the cart. Five models, 22 spare parts.'],['newsletter','New models, spare-part restocks, firmware notes. Nothing else.'],['404','No page at this address. The range, the spare parts, or contact.']], ['context','copy'])))

B.append(ch('03','marks','The marks',
 'A white wordmark and a wb monogram. The monogram was recut so its cut is the brand green — the same green as the hardware.',
 T(card('marks'))
 + '<h3 class="t">3.1 specification</h3>'
 + table([['Wordmark','<code>wishbone-wordmark.png</code> 800 × 64 · header 200px · min 120px / 30 mm · clear space = height of the W'],['Monogram','<code>wishbone-monogram-lime.png</code> 600 × 307 · min 24px · favicon, app icon, packaging'],['Backgrounds','ground, dark photography (< 25 % luminance behind the mark), or a lime tile with the mark in ground colour'],['Never','white or grey backgrounds · recolour · stretch · outline · shadow · box · lock the two marks together · rebuild GOLF in DotGothic16']], ['item','rule'])
 + '<h3 class="t">3.2 the green in the mark</h3><div class="board">'
 + T(f'<div class="label">v1 as shipped</div><img src="{MONO_OLD}" style="width:70%;margin:14px auto 0;display:block"><p class="grey" style="margin-top:12px">olive #C8D645 — hue 66°</p>')
 + T(f'<div class="label"><b>v3</b>&nbsp;&nbsp;recut</div><img src="{MONO}" style="width:70%;margin:14px auto 0;display:block"><p style="margin-top:12px">lime #A8FF4A — hue 89°, the hardware</p>')
 + T('<div class="label">to commission</div><ul><li>positive (dark-on-light) versions of both marks</li><li>SVG masters</li><li>confirm ™ vs ® status</li></ul>')
 + '</div>'))

B.append(ch('04','colour','Colour',
 'One ground, one tile, two text colours, one lime. There is no red.',
 T(card('colour'))
 + '<h3 class="t">4.1 palette</h3>'
 + table([['ground','#0F1014','the page'],['tile','#111214','every container; 1px top edge rgb(255 255 255 / .06)'],['white','#FAFAFA','values, headings, body'],['grey','#8E9298','labels, inactive dots, secondary values'],['dim','rgb(250 250 250 / .22)','empty dots'],['<b>lime</b>','<b>#A8FF4A</b>','the accent — one element per tile'],['light','#F2D2AB','the lamp: gradient value only']], ['token','value','use'])
 + '<h3 class="t">4.2 contrast</h3>'
 + table([['white on ground','16.0','pass'],['lime on ground','15.5','pass'],['ground on lime','15.5','pass — buttons'],['grey on ground','6.4','pass — secondary'],['<b>white on lime</b>','<b>1.18</b>','<b>never</b>']], ['pair','ratio','verdict'])
 + T('<div class="label"><b>the green, settled</b></div><p style="margin-top:12px">Volt #E3FC02 (theme) and olive #C8D645 (logo) are both hue 66° — yellow-greens. The trolleys photograph at hue 90° — green. Two colours had been called “the green”. The product cannot be repainted, so the brand green is the product\'s: lime #A8FF4A. The colourway <em>charcoal-lime</em> is now literally the accent.</p>')
 + '<h3 class="t">4.3 off screen</h3>'
 + table([['print, ground','4-colour rich black (60/50/50/100); never 100 K alone'],['print, lime','out of CMYK gamut — specify a fluorescent green spot ink and proof it physically'],['hardware','the photographed green is the reference; never retouch it'],['apparel','black garment, white mark; lime thread for one small detail at most']], ['medium','rule'])))

B.append(ch('05','type','Type',
 'One typeface at every size: DotGothic16, a 16px dot-matrix bitmap face. It is the reference\'s voice, exactly, and the whole brand speaks in it.',
 T(card('type'))
 + '<h3 class="t">5.1 the face</h3>'
 + table([['Family','<b>DotGothic16</b>'],['Designer','Fontworks'],['Licence','SIL Open Font License 1.1 — free for commercial use, self-hosting, PDF embedding, packaging'],['Source','Google Fonts'],['Weights','one'],['Fallback','<code>\'DotGothic16\', \'VT323\', ui-monospace, monospace</code>'],['Smoothing','off — the dots are the point']], ['property','value'])
 + '<h3 class="t">5.2 scale</h3><p class="grey">All sizes are multiples or clean divisions of the 16px bitmap grid.</p>'
 + table([['label','12px','0.14em, uppercase — tile headers, chips, nav'],['body','16px','copy, list rows'],['lead','20px','product names in tiles, FAQ questions'],['h','32px','buy-tile title, statements'],['readout','48px','the value a tile reports'],['display','64px','section openers'],['hero','96px','the hero title, with the cursor']], ['role','size','use'])
 + '<h3 class="t">5.3 rules</h3><div class="board">'
 + T('<div class="label"><b>do</b></div><ul><li>Set values in the readout size; a number in body size is a missed reading</li><li>Keep body copy short — this brand writes in sentences, not paragraphs</li><li>Track labels; never track body</li><li>Let the hero go to 96px</li></ul>')
 + T('<div class="label">never</div><ul class="grey"><li>a second typeface, for any reason, on any brand surface</li><li>font smoothing on</li><li>synthetic bold or italic — there are none</li><li>sizes off the scale (14, 18, 24…)</li><li>justified or centred paragraphs</li></ul>')
 + T('<div class="label">the one exception</div><p style="margin-top:12px">Shopify-controlled checkout and policy pages are not brand surfaces; they fall back to the system mono. Nowhere else.</p>')
 + '</div><h3 class="t">5.4 in the theme</h3>'
 + table([['type_header_font · type_body_font','both → DotGothic16, self-hosted from assets/ (the picker may not carry it)'],['heading_scale · body_scale','100 · 100 — sizes are absolute'],['font smoothing','<code>-webkit-font-smoothing:none</code> in base'],['status','the live theme still runs v1 (Oswald + Figtree)']], ['setting','v3'])))

B.append(ch('06','tile','Tile and board',
 'Every page is a board; everything on it is a tile. There is no other container and no other layout.',
 T(card('tile')) + T(card('grid'))
 + '<h3 class="t">6.1 anatomy</h3>'
 + table([['surface','#111214'],['radius','24px'],['padding','24px'],['edge','inset 0 1px 0 rgb(255 255 255 / .06) — the lamp catching the top'],['label','NN LABEL, 12px tracked caps, top-left; NN in white, label in grey'],['live','a 6px lime dot at the right of the label row'],['span','1, 2 or 3 columns'],['shadow','none']], ['property','value'])
 + '<h3 class="t">6.2 board</h3>'
 + table([['page','1200px'],['columns','3 above 900 · 2 above 600 · 1 below'],['gap','16px — tight, so a cluster reads as one instrument'],['numbering','tiles in reading order; a page\'s numbers are stable addresses'],['pages','home, product, collection, cart, account, contact, 404 — all boards']], ['property','value'])
 + T('<div class="label">no other box</div><p style="margin-top:12px">No cards inside tiles, no bands, no full-bleed hero, no bordered sections, no modals that are not tiles. If it cannot be a tile on the board, it is not on the page.</p>')))

B.append(ch('07','dots','Dots',
 'The only graphic. 6px dots on a 3px pitch — charts, gauges, progress, silhouettes, dividers.',
 T(card('dots'))
 + '<h3 class="t">7.1 spec</h3>'
 + table([['dot','6px'],['gap','3px'],['small tiles','4px / 2px, minimum'],['signal','white; 22 % → 100 % by value'],['empty','rgb(250 250 250 / .22)'],['hot','lime — the one value that matters'],['generators','bars · ring · line · steps · wave']], ['property','value'])
 + '<h3 class="t">7.2 silhouettes</h3><p>Sample the real photograph: luminance → dot size, the green hardware → lime. The EON grid is sampled; ONE, TWO, THREE and NEO use a procedural outline only until they are photographed to §09, then are sampled the same way. Never hand-draw a product; never reuse one model\'s grid for another.</p>'
 + '<div class="board">' + T('<div class="label"><b>use</b></div><ul><li>range, charge, part counts</li><li>the model range as silhouettes</li><li>order and configurator progress</li><li>the hero pulse</li></ul>') + T('<div class="label">never</div><ul class="grey"><li>background texture</li><li>behind text</li><li>logos, marks, people</li><li>a spinner</li><li>two pitches on one board</li></ul>') + '</div>'))

B.append(ch('08','pill','Pill and field',
 'The single rounded element. Buttons, tags, status chips, selectors and inputs are one shape distinguished by kind.',
 table([['button','lime fill, ground text, 14/22px — the purchase; one per tile'],['ghost','outline at 28 % white — every secondary action'],['tag','grey chip, 12px caps — compatibility, categories'],['status','chip with a dot: grey idle, lime live'],['select','radio: white fill when on — models, colourways'],['field','pill input; error = lime border + ▸ instruction. No red.']], ['kind','rule'])
 + T('<div class="label">icons</div><p style="margin-top:12px">There are none. Where a control needs a glyph it is drawn in dots (a 5 × 5 grid) or written as a word. Cart is <code>cart [02]</code>. Never an icon font, never emoji.</p>')))

B.append(ch('09','light','Light and photography',
 'One warm lamp, high and left. It lights the page and it lights every photograph.',
 T(card('light'))
 + '<h3 class="t">9.1 recipe</h3>'
 + table([['key','single warm source, top-left, raking at 30–45°'],['fill','almost none; the shadow side goes to black'],['ground','concrete, asphalt, graphite, dusk — never seamless white, never midday grass'],['grade','warm, slightly desaturated, blacks kept low'],['colour in frame','the hardware green only; no props']], ['element','spec'])
 + '<h3 class="t">9.2 shot list</h3><ol><li>hero three-quarter, low — the silhouette source</li><li>fold, three frames, one camera</li><li>macro: bearing, wheel, magnetic attachment</li><li>folded beside something everyone can measure by eye</li><li>in use — hands and stance, dusk, no faces</li><li>parts, flat, dark ground</li></ol>'))

B.append(ch('10','motion','Motion',
 'Dots draw in. Readouts count. The cursor blinks. Nothing else moves.',
 table([['fast','160ms','hover, focus, colour'],['base','320ms','tiles arriving, accordions'],['slow','640ms','dot grids drawing in, column by column, once'],['ease','cubic-bezier(.2,.8,.2,1)','fast out, soft settle'],['cursor','1.1s steps(1)','hero and footer only']], ['token','value','use'])
 + '<div class="board">' + T('<div class="label"><b>allowed</b></div><ul><li>tiles fading in with a 6px rise, staggered 60ms</li><li>dots drawing in on first view</li><li>readouts counting to their value in ≤ 800ms</li></ul>') + T('<div class="label">forbidden</div><ul class="grey"><li>hover lift, scale, glow</li><li>parallax, carousels, marquees</li><li>bounce easing</li><li>anything looping near the buy pill</li></ul>') + T('<div class="label">reduced motion</div><p style="margin-top:12px">Every motion above is disabled under <code>prefers-reduced-motion</code>; end states show at once and the cursor stops.</p>') + '</div>'))

B.append(ch('11','apps','Applications',
 'Every surface is the same board. Nothing is a one-off.',
 table([['storefront','TopBar · board of tiles · FootBar. Home: hero, range, compat, trust. Product: hero, buy, spec tiles, compare, box, FAQ. Collection: product and part tiles.'],['email','600px, ground background, one tile per message, one lime pill; DotGothic16 will not load — fall back to Courier New and keep the layout'],['social','a single tile, 1:1: label, one readout, the wordmark at 84px. One fact per post.'],['packaging insert','A5 on ground stock, one spec tile in white + spot lime, QR to the parts board'],['spec sheet','A4, the product board, mono laser-safe'],['trade stand','ground walls, one raking warm lamp, products lit as §09, a single lime element in the booth'],['apparel','black, white wordmark 60mm left chest']], ['surface','rule'])))

B.append(ch('12','govern','Governance',
 'Where the system lives, how to change it, and what is open.',
 table([['tokens (source)','design-system/tokens/*.css'],['tokens (portable)','docs/brand/tokens.css · tokens.json'],['components','design-system/components/{primitives,tiles,chrome}'],['specimen cards','design-system/guidelines/'],['marks','design-system/assets/'],['written kit','docs/brand/BRAND_KIT.md (v2 and v1 kept as appendix)'],['this book','tools/build-brandbook.py → regenerate, then publish'],['cloud','Claude Design → Wishbone Golf Design System · skill wishbone-design'],['storefront','theme/ — still v1'],['repo','github.com/mrehb/wishbone_shopify']], ['asset','location'])
 + '<h3 class="t">12.1 to change something</h3><ol><li>change the token in design-system/tokens — never in a component</li><li>mirror to docs/brand</li><li>regenerate this book and the v3 page; re-push the design system</li><li>record the decision in BRAND_KIT.md</li><li>only then the theme — into a draft</li></ol>'
 + '<h3 class="t">12.2 versions</h3>' + table([['v1.0','19 Sep 2026','the store as found: ink, volt + cyan, Oswald caps, radius 0'],['v2.0 “Telemetry”','19 Sep 2026','rebrand — rejected by the owner as not consistent enough'],['<b>v3.0 “Instrument”</b>','19 Sep 2026','from-scratch rebuild from the references: one of everything']], ['version','date','what'])
 + '<h3 class="t">12.3 open</h3>' + table([['01','fold size and weight — unmeasured for every model','Wishbone'],['02','photograph ONE, TWO, THREE, NEO to §09; sample their silhouettes','photographer'],['03','positive + SVG marks; ™ vs ®','designer / Wishbone'],['04','fluorescent spot-ink proof for lime','printer'],['05','theme migration — the storefront runs v1','next build'],['06','“aluminum” → “aluminium”; vendor <em>My Store</em>','theme / admin']], ['#','item','owner'])
 + T('<div class="label"><b>the short version</b></div><p style="font-size:var(--fs-lead);line-height:1.4;margin-top:12px" class="cursor">One typeface. One tile on one board. One dot. One pill. One lamp. One lime. Say the number, and where there is no number, print an em dash and go and measure it</p>')))

toc = "".join(f'<a href="#{s}">{n} {t}</a>' for n, s, t in CH)
HTML = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Wishbone Golf — Brand Book v3.0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DotGothic16&family=VT323&display=swap" rel="stylesheet">
<style>{tokens}
.wrap{{max-width:1080px;margin:0 auto;padding:0 20px 120px}}
.cover{{min-height:86vh;display:flex;flex-direction:column;justify-content:center;gap:22px;border-bottom:1px solid var(--tile-line)}}
.cover img{{width:360px;max-width:70%}}
nav.toc{{position:sticky;top:0;z-index:9;background:rgb(15 16 20 / .94);border-bottom:1px solid var(--tile-line);padding:12px 0;margin-bottom:40px}}
nav.toc .in{{max-width:1080px;margin:0 auto;padding:0 20px;display:flex;gap:6px 18px;flex-wrap:wrap}}
nav.toc a{{color:var(--grey);text-decoration:none;font-size:var(--fs-label);letter-spacing:var(--track-label);text-transform:uppercase;white-space:nowrap}}
nav.toc a:hover{{color:var(--lime)}}
section.ch{{margin:0 0 72px;scroll-margin-top:60px;border-top:1px solid var(--tile-line);padding-top:22px}}
h2.t{{margin-top:10px}}h3.t{{font-size:var(--fs-lead);margin:30px 0 10px}}
.lede{{font-size:var(--fs-lead);max-width:60ch;margin-top:12px}}
.tile{{background:var(--tile);border-radius:var(--r-tile);padding:var(--pad);box-shadow:inset 0 1px 0 var(--tile-edge);margin:16px 0;min-width:0}}
.board{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:var(--grid-gap);margin:16px 0}}
.board .tile{{margin:0}}
table{{width:100%;border-collapse:collapse;margin:12px 0}}th,td{{text-align:left;padding:9px 12px;border-bottom:1px solid var(--tile-line);vertical-align:top}}th{{font-weight:400}}
ul,ol{{padding-left:18px;margin:10px 0}}li{{margin:5px 0}}
code{{font-family:var(--font);background:rgb(255 255 255 / .06);padding:1px 6px;border-radius:4px}}
footer{{border-top:1px solid var(--tile-line);padding-top:18px;margin-top:40px}}
@media print{{nav.toc{{display:none}}}}
</style></head><body><div class="wrap">
<header class="cover"><img src="{WORD}" alt="Wishbone Golf">
  <h1 class="cursor" style="font-size:var(--fs-hero)">Brand book</h1>
  <p class="lede">The complete identity, set in the system it documents. One typeface, one tile, one dot, one pill, one lamp, one lime — and every rule that follows from having one of each.</p>
  <div style="display:flex;gap:32px;flex-wrap:wrap;margin-top:8px">
    <div><div class="label">version</div><div class="readout" style="font-size:var(--fs-h)">3.0</div></div>
    <div><div class="label">codename</div><div class="readout" style="font-size:var(--fs-h)">INSTRUMENT</div></div>
    <div><div class="label">issued</div><div class="readout" style="font-size:var(--fs-h)">19.09.2026</div></div>
    <div><div class="label">supersedes</div><div class="readout" style="font-size:var(--fs-h)">2.0 · 1.0</div></div></div>
</header></div>
<nav class="toc"><div class="in">{toc}</div></nav>
<div class="wrap">{"".join(B)}
<footer class="label">wishbone golf brand book v3.0 instrument · generated from the design system by tools/build-brandbook.py · repo github.com/mrehb/wishbone_shopify</footer></div>
</body></html>"""
dest = pathlib.Path('/tmp/wb/kit/wishbone-brand-book.html'); dest.write_text(HTML)
print('wrote', dest, round(len(HTML)/1024), 'KB ·', len(CH), 'chapters')
