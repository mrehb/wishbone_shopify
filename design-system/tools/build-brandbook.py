#!/usr/bin/env python3
"""Wishbone Golf brand book v4 "Studio" — one self-contained HTML document, set in the system it
documents. Regenerate after any token change."""
import base64, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parent.parent
uri = lambda p: "data:image/png;base64," + base64.b64encode((ROOT/p).read_bytes()).decode()
A = {n: uri(f'assets/{n}.png') for n in ['wishbone-wordmark','wishbone-wordmark-ink','wishbone-monogram-lime','wishbone-monogram-ink']}
tokens = "".join("\n" + re.sub(r"@import[^;]+;", "", (ROOT/'tokens'/f).read_text()) for f in ['colors.css','typography.css','geometry.css','layout.css','base.css'])
def card(name):  # inline a guideline specimen's body so the book shows the real card
    t = (ROOT/'guidelines'/f'{name}.html').read_text()
    body = t.split('<body>')[1].split('</body>')[0]
    for n, u in A.items(): body = body.replace(f'../assets/{n}.png', u)
    return f'<div class="spec">{body}</div>'
CH = []
def ch(n, slug, title, lede, body):
    CH.append((n, slug, title))
    return f'<section class="ch" id="{slug}"><div class="eyebrow"><b>{n}</b>{title}</div><h2 class="display">{title}.</h2><p class="lead grey">{lede}</p>{body}</section>'
def table(rows, head=None):
    h = f"<tr>{''.join(f'<th>{c}</th>' for c in head)}</tr>" if head else ''
    return "<table>" + h + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</table>"
def two(a, b): return f'<div class="two"><div>{a}</div><div>{b}</div></div>'
def box(label, inner, tone=''): return f'<div class="box {tone}"><div class="label grey">{label}</div>{inner}</div>'
B = []
B.append(ch('01','brand','The brand',
 'Wishbone makes golf trolleys that are light, simple and British. The brand shows the product and reports what it is.',
 box('1.1 the statement', '<p class="display display--s" style="margin-top:12px;text-transform:none;letter-spacing:0">Birthed in Britain, Wishbone Golf merges exquisite design with unwavering quality.</p><p class="grey" style="margin-top:12px">The brand\'s own sentence. Nothing in this book replaces it.</p>')
 + '<h3>1.2 pillars</h3>' + table([['engineered light','aircraft-grade aluminium, no bulk. Every claim provable by picking the thing up'],['no nonsense','the brand\'s own phrase, from the EON copy. It governs the product, the site and this book'],['british design','stated once, then demonstrated by the object']])
 + '<h3>1.3 architecture</h3>' + table([['manual','ONE 229 € · TWO 199 € · THREE 249 €'],['electric','NEO (parts only today) · EON 799 €'],['spare parts','22 of 27 products, named <i>Component (MODEL)</i>: ONE 10 · NEO 14 · EON 5 · TWO 2 · THREE 2'],['accessories','umbrella, drink, scorecard, ball &amp; tee holders — fit every model']], ['line','what'])))
B.append(ch('02','direction','The direction',
 'v4 is white because the product is photographed on white. Everything else follows from that.',
 two(box('the reference', '<p style="margin-top:10px">A white, airy page: light geometric sans in upper-case statements, a stats strip under the hero, three-up product tiles on grey, one dark technology band, hairline forms, and a lime button used exactly once. The dot-matrix voice is kept, but only as an accent.</p>'),
     box('the product', '<p style="margin-top:10px">Every one of the store\'s photographs is a white studio shot. On a dark site each one arrives in a white box; on paper and mist they sit where they are put. Fifteen parts have no photograph at all — the dot silhouette stands in for them and for nothing else.</p>'))
 + '<h3>2.1 what v4 keeps from before</h3>' + table([['the green','the idea that the accent is the product\'s own green — but v4.1 corrects <i>which</i> product: the logo is hue 66° and the ONE, TWO and THREE photograph at 72–73°, so the accent is now <b>#CBE832 at hue 70°</b>, not the EON\'s 89°'],['the honesty','unknown prints — with <i>not yet measured</i>; nothing is guessed'],['the catalogue','every component is built on the real products, prices and part names'],['the dot voice','one role: the numbered eyebrow above each headline; silhouettes where a photo is missing']], ['kept','how'])
 + '<h3>2.2 what it drops</h3>' + table([['the dark ground and the lamp','the site is paper and mist; ink appears once per page'],['dot type for everything','Manrope for everything; DotGothic16 for the eyebrow only'],['dot charts, gauges, rings, waves','none — a number is written as a number'],['the tile and the pill','bands and hairlines; radius 0']], ['dropped','replaced by'])))
B.append(ch('03','marks','Marks',
 'The wordmark and the monogram, positive on paper, negative on ink. The green in the mark is the brand green.',
 card('marks') + table([['header','ink wordmark, 14px tall, left'],['footer','ink monogram, 96px wide'],['dark band, social avatar','lime monogram on ink'],['clear space','the height of the W on every side'],['minimum','wordmark 96px wide on screen, 30mm in print; monogram 24px / 8mm'],['never','olive, volt, or any green but lime in the mark; the mark over a photograph; the mark rotated or outlined']], ['use','rule'])))
B.append(ch('04','colour','Colour',
 'Paper, mist, ink, grey, a hairline, and one lime. There is no red.',
 card('colour') + '<h3>4.1 the ink band</h3><p>One per page, for the thing with the most technology in it. On ink: text #FAFAFA, secondary #9A9EA6, hairline at 14% white, the eyebrow in lime text, the button lime. The negative wordmark if the header sits on it.</p>'
 + '<h3>4.2 off screen</h3>' + table([['print, paper','uncoated white stock; mist as 4% black'],['print, ink','rich black 60/50/50/100'],['print, lime','out of CMYK gamut — a fluorescent green spot ink, proofed physically'],['hardware','the photographed green is the reference; never retouch it'],['apparel','white or black garment, ink or white wordmark; lime thread for one detail at most']], ['medium','rule'])))
B.append(ch('05','type','Type',
 'Manrope for everything, at four weights. DotGothic16 for the eyebrow, and for nothing else.',
 card('type') + '<h3>5.1 the faces</h3>' + table([['Manrope','Mikhail Sharanda · SIL OFL 1.1 · Google Fonts · weights 300 400 500 600 · <code>\'Manrope\', system-ui, sans-serif</code>'],['DotGothic16','Fontworks · SIL OFL 1.1 · Google Fonts · one weight · <code>\'DotGothic16\', ui-monospace, monospace</code> · smoothing off']], ['face','details'])
 + '<h3>5.2 rules</h3>' + two(box('do', '<ul><li>write headlines as statements, one per line, each with a full stop</li><li>keep the hero to three lines</li><li>set money in 600 and nothing else in 600</li><li>let stats go light and large</li></ul>'),
   box('never', '<ul class="grey"><li>DotGothic16 for a heading, a price, a button, a paragraph</li><li>bold headlines</li><li>a third typeface</li><li>sizes off the scale</li><li>justified or centred paragraphs (stats and trust are the exceptions)</li></ul>'))
 + '<h3>5.3 in the theme</h3>' + table([['type_header_font','Manrope 300 (self-host if the picker lacks it)'],['type_body_font','Manrope 400'],['eyebrow','a section-setting class, DotGothic16 self-hosted from assets/'],['status','the live theme still runs v1 (Oswald + Figtree)']], ['setting','v4'])))
B.append(ch('06','band','Bands and grid',
 'Every page is a stack of full-bleed bands on one 1200px container. Depth is a band change, never a shadow.',
 card('band') + '<h3>6.1 the home page, in order</h3>' + table([['01','Hero','mist','eyebrow, three-line headline, one sentence, lime + outline, slide index; product right'],['','Stats','paper','four facts, hairlines'],['02','Lineup','paper','copy left, three products on mist tiles'],['03','Feature','<b>ink</b>','the battery — the one dark band'],['04','Feature','paper','folding, image left'],['','Trust','mist','five proof points'],['05','Faq','paper','hairline accordion'],['06','Inquiry','paper','newsletter'],['','Footer','paper','']], ['eyebrow','band','tone','content'])
 + '<h3>6.2 the product page</h3>' + table([['01','Buy','paper','gallery 7 columns, buy box 4'],['02','Specs','paper','hairline table + in the box'],['03','Compare','mist','five columns'],['04','Parts','paper','filter tags, four-up grid'],['05','Faq','paper','']], ['eyebrow','band','tone','content'])))
B.append(ch('07','dots','The dot accent',
 'The part of the old direction worth keeping, kept in two places.',
 card('dots') + '<h3>7.1 silhouettes</h3><p>5px ink dots on a 2px pitch. The EON\'s is sampled from its real photograph; the other models use a procedural outline until they are photographed, then are sampled the same way. Never hand-drawn, never decorative, gone the moment a photograph exists.</p>'))
B.append(ch('08','photo','Photography',
 'White studio, as the store already shoots. The site is built to show it.',
 card('photo') + '<h3>8.1 shot list</h3><ol><li>each model, three-quarter, white studio, every colourway — the ONE has five</li><li>the NEO — it has no photograph at all</li><li>the fifteen unphotographed parts, flat, white</li><li>fold, three frames, one camera</li><li>one lifestyle frame per model: overcast course, grey sky</li></ol>'))
B.append(ch('09','components','Components',
 'Twenty-two components, all built on the real catalogue.',
 table([['Eyebrow','the DotGothic16 label — 01 THE LINEUP'],['Display','light upper-case statement headline, 56 / 40 / 28'],['Button','lime · ink · outline · text, with → when it leads somewhere'],['Stat, StatRow','44px number over 12px label; the strip under the hero'],['Field','underline input; error = lime line + sentence'],['Tag','hairline model chip; lime when selected'],['Price','799,00 € in weight 600'],['Dots, Silhouette, Photo','the image slot: white shot on mist, or the dot silhouette']], ['primitive','what'])
 + table([['Hero','mist; 5 : 7; slide index'],['Stats','four facts, hairlines'],['Lineup','copy + three product tiles'],['Feature','5 : 7 either way; paper / mist / ink'],['Trust','five proof points on mist'],['Inquiry','underline form; contact or newsletter'],['Buy','gallery + buy box with real colourways'],['Specs','hairline table; unknown rows stay'],['Compare','five columns; empty cells print —'],['Parts','model filter; 22 parts, photo or silhouette'],['Faq','hairline accordion'],['Header, Footer','wordmark, five links, CART (n), the lime button · monogram, four columns']], ['section','what'])))
B.append(ch('10','voice','Voice',
 'Short statements. Measured facts. British spelling.', card('voice')))
B.append(ch('11','motion','Motion',
 'Colour changes and content fades. Nothing lifts, nothing loops.', card('motion')))
B.append(ch('12','govern','Governance',
 'Where the system lives, how to change it, and what is open.',
 table([['tokens (source)','design-system/tokens/*.css'],['tokens (portable)','docs/brand/tokens.css · tokens.json'],['components','design-system/components/{primitives,sections,chrome}'],['specimen cards','design-system/guidelines/'],['marks','design-system/assets/ (ink + lime versions)'],['written kit','docs/brand/BRAND_KIT.md (v3, v2, v1 kept as appendix)'],['this book','tools/build-brandbook.py'],['the library page','tools/build-v4.py'],['cloud','Claude Design → Wishbone Golf Design System · skill wishbone-design'],['storefront','theme/ — still v1'],['repo','github.com/mrehb/wishbone_shopify']], ['asset','location'])
 + '<h3>12.1 to change something</h3><ol><li>change the token in design-system/tokens — never in a component</li><li>mirror to docs/brand</li><li>regenerate this book and the v4 page; re-push the design system</li><li>record the decision in BRAND_KIT.md</li><li>only then the theme — into a draft</li></ol>'
 + '<h3>12.2 versions</h3>' + table([['v1.0','19 Sep 2026','the store as found: ink, volt + cyan, Oswald caps'],['v2.0 “Telemetry”','19 Sep 2026','rebrand — rejected as not consistent enough'],['v3.0 “Instrument”','19 Sep 2026','one of everything, dark, dot-matrix — rejected as too dark, too many dots'],['<b>v4.0 “Studio”</b>','19 Sep 2026','white, product-led, Manrope, the dot voice as an accent']], ['version','date','what'])
 + '<h3>12.3 open</h3>' + table([['01','fold size and weight — unmeasured for every model','Wishbone'],['02','photograph the NEO and the fifteen unphotographed parts','photographer'],['03','SVG masters of the marks; ™ vs ®','designer / Wishbone'],['04','fluorescent spot-ink proof for lime','printer'],['05','theme migration — the storefront runs v1','next build'],['06','“aluminum” → “aluminium”; vendor <i>My Store</i>','theme / admin']], ['#','item','owner'])
 + box('the short version', '<p class="lead" style="margin-top:10px">White page, grey frames, one dark band. Manrope, light and upper case. The dot face on the small label and nowhere else. One lime button, and it is the purchase. Say the number; where there is none, print an em dash and go and measure it.</p>')))
toc = "".join(f'<a href="#{s}">{n}&nbsp;&nbsp;{t}</a>' for n, s, t in CH)
HTML = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Wishbone Golf — Brand Book v4.0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600&family=DotGothic16&display=swap" rel="stylesheet">
<style>{tokens}
.wrap{{max-width:1080px;margin:0 auto;padding:0 24px 120px}}
.cover{{min-height:86vh;display:flex;flex-direction:column;justify-content:center;gap:24px;border-bottom:1px solid var(--hair)}}
.cover img{{height:18px;width:auto}}
.toc{{display:grid;grid-template-columns:repeat(3,1fr);gap:8px 24px;padding:40px 0;border-bottom:1px solid var(--hair);font-size:14px}}
.ch{{padding:72px 0 0}}.ch>.eyebrow{{margin-bottom:18px}}.ch>.lead{{max-width:60ch;margin:16px 0 28px}}
h3{{font-size:12px;font-weight:500;letter-spacing:.16em;text-transform:uppercase;margin:40px 0 12px;color:var(--grey)}}
table{{width:100%;border-collapse:collapse;font-size:14px;margin-top:8px}}th,td{{text-align:left;padding:10px 12px 10px 0;border-bottom:1px solid var(--hair);vertical-align:top}}th{{font-weight:500}}
.two{{display:grid;grid-template-columns:1fr 1fr;gap:16px}}.box{{border:1px solid var(--hair);padding:24px;font-size:14px}}.box ul,.box ol{{padding-left:18px;margin-top:10px}}
.spec{{border:1px solid var(--hair);padding:32px;margin:8px 0 8px}}.spec .k{{display:grid;gap:24px}}.spec table{{margin:0}}
.spec .sw{{display:grid;grid-template-columns:repeat(6,1fr);gap:12px}}.spec .sw div{{height:96px;padding:12px;display:flex;flex-direction:column;justify-content:flex-end;gap:2px;font-size:12px;border:1px solid var(--hair)}}.spec .sw .v{{font-family:var(--font-dot);letter-spacing:.1em}}
ol{{padding-left:18px}}code{{font-family:ui-monospace,monospace;font-size:13px}}
@media(max-width:700px){{.two,.toc{{grid-template-columns:1fr}}}}
</style></head><body><div class="wrap">
<div class="cover"><img src="{A['wishbone-wordmark-ink']}" alt="Wishbone Golf">
<div class="eyebrow"><b>v4.0</b>Brand book · Studio · 19 September 2026</div>
<h1 class="display display--hero">Light.<br>Simple.<br>British.</h1>
<p class="lead grey" style="max-width:52ch">The identity of Wishbone Golf: a white, product-led system with one typeface, one line, one dark band and one lime, and the dot-matrix voice kept as a small accent. Twelve chapters, each with its rule and its reason.</p></div>
<nav class="toc">{toc}</nav>
{''.join(B)}
<p class="label grey" style="margin-top:80px;border-top:1px solid var(--hair);padding-top:20px">Wishbone Golf · brand book v4.0 · generated from design-system/ by tools/build-brandbook.py · the live theme still runs v1</p>
</div></body></html>"""
dest = pathlib.Path('/tmp/wb/kit/wishbone-brand-book.html'); dest.parent.mkdir(parents=True, exist_ok=True); dest.write_text(HTML)
print('wrote', dest, round(len(HTML)/1024), 'KB ·', len(CH), 'chapters')
