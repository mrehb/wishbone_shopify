#!/usr/bin/env python3
"""Build the Wishbone Golf brand book — one self-contained HTML document.

Everything is rendered in the v2 system itself: the book is a specimen of the brand
it documents. Logos are inlined as data URIs so the file stands alone.
Regenerate after any token change:  python3 tools/build-brandbook.py
"""
import base64, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
def uri(rel, mime='image/png'):
    return "data:%s;base64,%s" % (mime, base64.b64encode((ROOT/rel).read_bytes()).decode())

WORD = uri('assets/wishbone-wordmark.png')
MONO = uri('assets/wishbone-monogram-volt.png')
MONO_OLD = uri('assets/wishbone-monogram.png')
EON = uri('/tmp/wb/eon.jpg'.replace('/tmp/wb/', ''), 'image/jpeg') if (ROOT/'eon.jpg').exists() else None

CSS = """
:root{
  --carbon:#0f1014; --card:#16171b; --raised:#1e2026; --volt:#e3fc02; --white:#fafafa;
  --muted:#8e9298; --warm:#f2d2ab; --error:#ff6b6b;
  --line:rgb(255 255 255 / .08); --line-strong:rgb(255 255 255 / .24);
  --display:'Space Grotesk',-apple-system,'Segoe UI',sans-serif;
  --body:'Figtree',-apple-system,BlinkMacSystemFont,sans-serif;
  --mono:'Share Tech Mono',ui-monospace,monospace;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--carbon);color:var(--white);font-family:var(--body);font-weight:400;
  font-size:15.5px;line-height:1.65;
  background-image:radial-gradient(120% 70% at 10% 0%, rgb(242 210 171 / .13), transparent 60%);
  background-attachment:fixed}
h1,h2,h3,h4{font-family:var(--display);font-weight:500;letter-spacing:-.02em;margin:0;line-height:1.06}
h1{font-size:64px} h2{font-size:38px} h3{font-size:24px} h4{font-size:17px;letter-spacing:-.01em}
p{margin:0 0 14px} p:last-child{margin-bottom:0}
a{color:var(--volt)}
code{font-family:var(--mono);font-size:13px;background:var(--raised);padding:1px 6px;border-radius:4px}
.label{font-family:var(--mono);font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--muted)}
.label b{color:var(--volt);font-weight:400}
.readout{font-family:var(--mono);letter-spacing:.02em;line-height:1}
.muted{color:var(--muted)}
.wrap{max-width:1080px;margin:0 auto;padding:0 28px 120px}
/* cover */
.cover{min-height:88vh;display:flex;flex-direction:column;justify-content:center;gap:26px;
  border-bottom:1px solid var(--line);margin-bottom:8px}
.cover img{width:380px;max-width:72%}
.cover .meta{display:flex;gap:34px;flex-wrap:wrap;margin-top:12px}
/* contents */
nav.toc{position:sticky;top:0;z-index:20;background:rgb(15 16 20 / .92);backdrop-filter:blur(8px);
  border-bottom:1px solid var(--line);margin-bottom:56px;padding:12px 0}
nav.toc .inner{max-width:1080px;margin:0 auto;padding:0 28px;display:flex;gap:6px 18px;flex-wrap:wrap;
  font-family:var(--mono);font-size:11px;letter-spacing:.14em;text-transform:uppercase}
nav.toc a{color:var(--muted);text-decoration:none;white-space:nowrap}
nav.toc a:hover{color:var(--volt)}
/* chapters */
section.ch{padding-top:30px;margin-bottom:76px;scroll-margin-top:60px}
.ch-head{border-top:1px solid var(--line);padding-top:20px;margin-bottom:26px}
.ch-head .n{font-family:var(--mono);font-size:12px;letter-spacing:.2em;color:var(--volt)}
.ch-head h2{margin-top:10px}
.lede{font-size:18px;line-height:1.55;max-width:70ch;color:var(--white);margin-top:14px}
.block{background:var(--card);border:1px solid var(--line);border-radius:20px;padding:26px 28px;margin:18px 0}
.grid{display:grid;gap:20px}
.g2{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}
.g3{grid-template-columns:repeat(auto-fit,minmax(215px,1fr))}
.g4{grid-template-columns:repeat(auto-fit,minmax(160px,1fr))}
table{width:100%;border-collapse:collapse;font-size:14px;margin:14px 0}
th,td{text-align:left;padding:10px 12px;border-bottom:1px solid var(--line);vertical-align:top}
th{font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted);font-weight:400}
td b{font-weight:700}
ul{padding-left:20px;margin:10px 0}li{margin:6px 0}
.do{border-left:2px solid var(--volt);padding-left:16px}
.dont{border-left:2px solid var(--error);padding-left:16px}
.rule{background:var(--raised);border-radius:14px;padding:18px 20px;margin:16px 0;border:1px solid var(--line)}
.rule .label{margin-bottom:8px;display:block}
.swatch{border:1px solid var(--line);border-radius:14px;overflow:hidden}
.swatch i{display:block;height:110px}
.swatch .m{padding:12px 14px;background:var(--card);font-family:var(--mono);font-size:11.5px;line-height:1.5}
.spec{border-bottom:1px solid var(--line);padding:16px 0}
.spec:last-child{border-bottom:0}
.chip{display:inline-flex;align-items:center;gap:7px;font-family:var(--mono);font-size:11px;letter-spacing:.16em;
  text-transform:uppercase;padding:5px 11px;border-radius:8px;border:1px solid var(--line-strong)}
.btn{display:inline-block;font-family:var(--display);font-weight:500;font-size:14px;padding:12px 22px;
  border-radius:10px;background:var(--volt);color:var(--carbon);border:1px solid transparent}
.btn.ghost{background:transparent;color:var(--white);border-color:var(--line-strong)}
figure{margin:0}
figcaption{font-size:12.5px;color:var(--muted);margin-top:10px}
.mock{border:1px solid var(--line);border-radius:18px;overflow:hidden;background:var(--card)}
.misuse{position:relative;border:1px solid var(--line);border-radius:14px;padding:22px;background:var(--card);
  display:flex;align-items:center;justify-content:center;min-height:110px}
.misuse::after{content:'✕';position:absolute;top:8px;right:12px;color:var(--error);font-size:15px}
.ok::after{content:'✓';color:var(--volt)}
footer{border-top:1px solid var(--line);padding-top:22px;color:var(--muted);font-size:13px}
@media print{nav.toc{display:none}body{background:#fff;color:#111}}
"""

CHAPTERS = []
def ch(num, slug, title, lede, body):
    CHAPTERS.append((num, slug, title))
    return ('<section class="ch" id="%s"><div class="ch-head"><div class="n">%s</div>'
            '<h2>%s</h2><p class="lede">%s</p></div>%s</section>') % (slug, num, title, lede, body)

BODY = []

# ── 01 ────────────────────────────────────────────────────────────────────────
BODY.append(ch('01', 'brand', 'The brand',
  'Wishbone makes golf trolleys that are measured objects: light, simple, British. '
  'The brand exists to report what the product is, not to persuade anyone that it is good.',
  """
<div class="block">
  <div class="label"><b>1.1</b>&nbsp;&nbsp;The statement</div>
  <p style="font-family:var(--display);font-size:30px;letter-spacing:-.02em;line-height:1.2;margin:14px 0 0">
  Birthed in Britain, Wishbone Golf merges exquisite design with unwavering quality.</p>
  <p class="muted" style="margin-top:12px">The brand's own words, from the homepage. Everything in this book serves that
  sentence — it is not a tagline to be replaced next season.</p>
</div>

<h3 style="margin-top:34px">1.2 &nbsp;What we sell, in the brand's terms</h3>
<p>A trolley carries the bag so the golfer does not. Wishbone's version of that job is <em>ultra-light aircraft-grade
aluminium, effortless folding, magnetic attachments, sealed bearings</em> — a short list of specific, checkable things.
That specificity is the brand. Where a competitor writes “premium engineering”, Wishbone writes “sealed bearings”.</p>

<h3 style="margin-top:30px">1.3 &nbsp;Three pillars</h3>
<div class="grid g3">
  <div class="block" style="margin:0"><div class="label"><b>01</b>&nbsp;&nbsp;ENGINEERED LIGHT</div>
    <h4 style="margin-top:12px">Weight is the product</h4>
    <p class="muted" style="font-size:14px;margin-top:8px">Aircraft-grade aluminium, no bulk. Every claim we make should
    be provable by picking the thing up.</p></div>
  <div class="block" style="margin:0"><div class="label"><b>02</b>&nbsp;&nbsp;NO NONSENSE</div>
    <h4 style="margin-top:12px">Simple to use, nothing decorative</h4>
    <p class="muted" style="font-size:14px;margin-top:8px">The brand's own phrase, from the EON copy. It governs the
    product, the site and this book.</p></div>
  <div class="block" style="margin:0"><div class="label"><b>03</b>&nbsp;&nbsp;BRITISH DESIGN</div>
    <h4 style="margin-top:12px">Quality assumed, not advertised</h4>
    <p class="muted" style="font-size:14px;margin-top:8px">“Birthed in Britain.” Stated once, then demonstrated by the
    object rather than repeated in adjectives.</p></div>
</div>

<h3 style="margin-top:34px">1.4 &nbsp;Brand architecture</h3>
<p>One brand, one vendor, two product families. There are no sub-brands and none should be created: the range is small
enough that the model name does all the work.</p>
<table>
  <tr><th>Level</th><th>Name</th><th>Written as</th></tr>
  <tr><td>Company</td><td><b>Wishbone Golf</b></td><td>In prose and legal contexts. Never “Wishbone Golf Ltd.” in marketing copy.</td></tr>
  <tr><td>Product family</td><td><b>Wishbone</b></td><td>“the Wishbone range”, “a Wishbone trolley”</td></tr>
  <tr><td>Models — manual</td><td><b>ONE · TWO · THREE</b></td><td>Wishbone ONE, Wishbone THREE. Caps, always.</td></tr>
  <tr><td>Models — electric</td><td><b>NEO · EON</b></td><td>Wishbone EON</td></tr>
  <tr><td>Parts &amp; accessories</td><td><code>Component (MODEL)</code></td><td>Fast Charger (NEO &amp; EON) · Rear Wheel Right (ONE)</td></tr>
</table>
<div class="rule"><span class="label">RULE</span>
The parenthesised model in a part name is <b>never trimmed for layout</b>. It is how a customer finds the right part for
their trolley, and a wrong part is a return.</div>

<h3 style="margin-top:34px">1.5 &nbsp;The range today</h3>
<table>
  <tr><th>Model</th><th>Type</th><th>Price</th><th>Notes</th></tr>
  <tr><td><b>ONE</b></td><td>Manual, 3 wheel</td><td class="muted">—</td><td>The reference frame; most spare parts exist for it</td></tr>
  <tr><td><b>TWO</b></td><td>Manual</td><td>199 €</td><td></td></tr>
  <tr><td><b>THREE</b></td><td>Manual</td><td>249 €</td><td></td></tr>
  <tr><td><b>NEO</b></td><td>Electric</td><td class="muted">—</td><td>Thumb throttle, cruise button, lithium</td></tr>
  <tr><td><b>EON</b></td><td>Electric, flagship</td><td>799 €</td><td>“A full powered, simple ‘no nonsense’ electric cart”</td></tr>
</table>
<p class="muted" style="font-size:13.5px">27 products live on wishbone.golf, all under vendor <b>Wishbone</b> — except one still
published as <em>My Store</em>, which is a data error to fix. Prices are EUR, store locale en-AT.</p>

<h3 style="margin-top:34px">1.6 &nbsp;Who we are talking to</h3>
<div class="grid g2">
  <div class="do"><h4>The buyer</h4><p class="muted" style="font-size:14px">A golfer who walks the course and has decided the
  bag is the problem. They compare specs across brands, read the parts list, and want to know it can be repaired in three
  years. They respond to numbers and to restraint.</p></div>
  <div class="dont"><h4>Not the buyer</h4><p class="muted" style="font-size:14px">Someone looking for a lifestyle brand, a
  logo to be seen with, or the cheapest trolley on a marketplace. Copy that chases them dilutes everything above.</p></div>
</div>
"""))

# ── 02 ────────────────────────────────────────────────────────────────────────
BODY.append(ch('02', 'voice', 'Verbal identity',
  'Report the value, then stop. The voice was the one thing the rebrand did not change — the words were '
  'already right; the design now matches them.',
  """
<h3>2.1 &nbsp;Principles</h3>
<div class="grid g2">
  <div class="block" style="margin:0"><h4>Say the number</h4>
    <p class="muted" style="font-size:14px;margin-top:8px">“27+ holes on one charge.” “799 €.” “Five models.” A number
    is checkable; an adjective is not.</p></div>
  <div class="block" style="margin:0"><h4>Name the material</h4>
    <p class="muted" style="font-size:14px;margin-top:8px">“Aircraft-grade aluminium.” “Sealed bearings.” “Magnetic
    attachments.” Materials are proof; “premium” is a claim.</p></div>
  <div class="block" style="margin:0"><h4>One idea per sentence</h4>
    <p class="muted" style="font-size:14px;margin-top:8px">Short declaratives. If a sentence needs a semicolon to hold
    together, it is two sentences.</p></div>
  <div class="block" style="margin:0"><h4>Report, don't sell</h4>
    <p class="muted" style="font-size:14px;margin-top:8px">“Range · 27+ holes” beats “Incredible battery life”. The
    instrument panel is the tone of voice made visible.</p></div>
</div>

<h3 style="margin-top:34px">2.2 &nbsp;Do and don't</h3>
<table>
  <tr><th>Write</th><th>Not</th></tr>
  <tr><td>Crafted from ultra-light aircraft-grade aluminium.</td><td class="muted">Built with premium, innovative materials.</td></tr>
  <tr><td>27+ holes on one charge.</td><td class="muted">Long-lasting battery life!</td></tr>
  <tr><td>Folds in one movement.</td><td class="muted">Revolutionary folding technology.</td></tr>
  <tr><td>Spare parts kept for ONE, NEO and EON.</td><td class="muted">Industry-leading after-sales support.</td></tr>
  <tr><td>Focus on your game; Wishbone Golf will handle the rest.</td><td class="muted">Let us take your golf to the next level.</td></tr>
</table>

<h3 style="margin-top:30px">2.3 &nbsp;House style</h3>
<table>
  <tr><th>Item</th><th>Standard</th></tr>
  <tr><td>Spelling</td><td><b>British</b> — alumini<b>u</b>m, colour, metres. <span class="muted">The homepage currently says “aluminum”; that is an error to fix.</span></td></tr>
  <tr><td>Model names</td><td>Caps, always: ONE, TWO, THREE, NEO, EON. Never “One”, never “eon”.</td></tr>
  <tr><td>Numbers</td><td>Digits, not words: “3 wheels”, “27+ holes”, “5 models”. Panel numbers are two-digit: <code>01</code>.</td></tr>
  <tr><td>Prices</td><td>Store locale format: <code>799,00 €</code> on the storefront, <code>799 €</code> in prose.</td></tr>
  <tr><td>Unknown values</td><td>Print <b>—</b>. Never estimate, never omit the row.</td></tr>
  <tr><td>Punctuation</td><td>No exclamation marks. No emoji. Em dashes for asides, spaced en dash in ranges.</td></tr>
  <tr><td>Buttons &amp; labels</td><td>Sentence case, verb first: “Add to cart”, “Compare models”, “Find a spare part”.</td></tr>
  <tr><td>Headings</td><td>Sentence case since v2. The uppercase went with Oswald.</td></tr>
</table>

<h3 style="margin-top:30px">2.4 &nbsp;Microcopy library</h3>
<table>
  <tr><th>Context</th><th>Use</th></tr>
  <tr><td>Status line</td><td>All systems operational · Spare parts ship same day · Shipping to AT · DE · UK</td></tr>
  <tr><td>Out of stock</td><td>Sold out — back on <em>date</em>. <span class="muted">Never “currently unavailable” with no date.</span></td></tr>
  <tr><td>Form error</td><td>Add the part after the @ — for example you@example.com.</td></tr>
  <tr><td>Empty cart</td><td>Nothing in the cart. The range is five models and 22 spare parts.</td></tr>
  <tr><td>Newsletter</td><td>New models, spare-part restocks and firmware notes. Nothing else.</td></tr>
  <tr><td>404</td><td>No page at this address. The range, the spare parts, or contact us.</td></tr>
</table>
<div class="rule"><span class="label">RULE</span>
Every message states a fact and, where relevant, the next action. Apologies are one word long at most: the brand is
precise, not sorry.</div>
"""))
print("chapters 1-2 staged")

# ── 03 ────────────────────────────────────────────────────────────────────────
BODY.append(ch('03', 'logo', 'The marks',
  'Two marks, both white on transparent: a horizontal wordmark and a wb monogram. '
  'In v2 the monogram was reissued so its accent matches the brand accent.',
  """
<h3>3.1 &nbsp;Wordmark</h3>
<div class="block">
  <div style="border:1px dashed rgb(227 252 2 / .4);border-radius:16px;padding:30px;display:flex;justify-content:center">
    <img src="__WORD__" alt="Wishbone Golf wordmark" style="width:70%">
  </div>
  <p class="muted" style="margin-top:16px;font-size:13.5px">The dashed frame is the clear-space rule, not part of the mark.</p>
</div>
<table>
  <tr><th>Property</th><th>Specification</th></tr>
  <tr><td>Asset</td><td><code>wishbone-wordmark.png</code> · 800 × 64 px · white on transparent</td></tr>
  <tr><td>Construction</td><td>Wide monoline geometric caps with rounded terminals; <b>GOLF</b> set vertically at the right edge; ™ above it</td></tr>
  <tr><td>Clear space</td><td>The <b>height of the W</b> on all four sides. Nothing enters it — not a nav item, not a photo edge.</td></tr>
  <tr><td>Minimum size</td><td>120 px on screen · 30 mm in print</td></tr>
  <tr><td>Web header</td><td>180 px wide (v2; was 200 px in v1, since the status line above now carries some weight)</td></tr>
  <tr><td>Footer</td><td>150 px wide</td></tr>
  <tr><td>Backgrounds</td><td>Carbon, dark photography (keep the area behind it below ~25 % luminance), or a volt panel</td></tr>
</table>

<h3 style="margin-top:34px">3.2 &nbsp;Monogram</h3>
<div class="grid g2">
  <div class="block" style="margin:0;display:flex;justify-content:center;align-items:center">
    <img src="__MONO__" alt="Wishbone monogram in volt" style="width:58%">
  </div>
  <div>
    <div class="label"><b>REISSUED IN V2</b></div>
    <p style="margin-top:12px">The quarter-circle cut in the <b>b</b> was olive <code>#C8D645</code> while the storefront
    ran on volt <code>#E3FC02</code> — two greens for one brand, visible side by side on every page. The mark now carries
    volt and the conflict is closed.</p>
    <p class="muted" style="font-size:13.5px">Asset <code>wishbone-monogram-volt.png</code> · 600 × 307 px · minimum 24 px ·
    used as favicon, app icon, and anywhere the wordmark will not fit. The v1 original is retained as
    <code>wishbone-monogram.png</code> for archive only.</p>
  </div>
</div>

<h3 style="margin-top:34px">3.3 &nbsp;Misuse</h3>
<div class="grid g3">
  <div><div class="misuse ok" style="background:#0f1014"><img src="__WORD__" style="width:80%"></div>
    <p class="muted" style="font-size:13px;margin-top:8px">Correct — white mark on carbon.</p></div>
  <div><div class="misuse" style="background:#fafafa"><img src="__WORD__" style="width:80%"></div>
    <p class="muted" style="font-size:13px;margin-top:8px">Never on white. The mark is white; it disappears.</p></div>
  <div><div class="misuse" style="background:#e3fc02"><img src="__WORD__" style="width:80%"></div>
    <p class="muted" style="font-size:13px;margin-top:8px">Never white-on-volt — 1.15:1, effectively invisible.</p></div>
  <div><div class="misuse" style="background:#16171b"><img src="__WORD__" style="width:80%;transform:scaleX(1.35)"></div>
    <p class="muted" style="font-size:13px;margin-top:8px">Never stretched or condensed.</p></div>
  <div><div class="misuse" style="background:#16171b"><img src="__WORD__" style="width:70%;filter:drop-shadow(0 4px 10px rgb(0 0 0 / .9))"></div>
    <p class="muted" style="font-size:13px;margin-top:8px">Never shadowed, glowed or embossed.</p></div>
  <div><div class="misuse" style="background:#16171b;gap:14px"><img src="__WORD__" style="width:46%"><img src="__MONO__" style="width:16%"></div>
    <p class="muted" style="font-size:13px;margin-top:8px">Never lock the wordmark and monogram together.</p></div>
</div>
<div class="rule"><span class="label">ALSO NEVER</span>
Recolour either mark (volt included — the marks are white; only the monogram's cut is volt) · rotate · outline ·
box it in a container of its own · rebuild <b>GOLF</b> in Space Grotesk or any other face · place over busy photography ·
use the monogram as a bullet or decorative motif.</div>

<h3 style="margin-top:34px">3.4 &nbsp;Placement</h3>
<table>
  <tr><th>Surface</th><th>Mark</th><th>Size &amp; position</th></tr>
  <tr><td>Site header</td><td>Wordmark</td><td>180 px, left, with the status line above</td></tr>
  <tr><td>Site footer</td><td>Wordmark</td><td>150 px, left column, above “Birthed in Britain.”</td></tr>
  <tr><td>Favicon / app icon</td><td>Monogram (volt)</td><td>Square, carbon field, mark at 62 % of the tile</td></tr>
  <tr><td>Email header</td><td>Wordmark</td><td>160 px, centred on carbon</td></tr>
  <tr><td>Product decal</td><td>Wordmark</td><td>As tooled on the frame today — do not redraw to match the digital mark</td></tr>
  <tr><td>Packaging</td><td>Monogram</td><td>Large, single colour, one per face</td></tr>
  <tr><td>Retailer listings</td><td>Wordmark</td><td>Supply on carbon as a PNG with padding baked in; never let a marketplace place it on white</td></tr>
</table>

<div class="rule" style="border-color:var(--volt)"><span class="label"><b>OUTSTANDING</b>&nbsp;&nbsp;COMMISSION THESE</span>
<ol style="margin:6px 0 0">
  <li><b>A positive (dark-on-light) version</b> of both marks. Today a light background is impossible without someone
  improvising — invoices, spec sheets, a magazine page, any print job on uncoated stock.</li>
  <li><b>SVG masters</b> of both. Everything is currently a raster PNG, which limits large-format print and product tooling.</li>
  <li><b>A one-line clarification of the ™ status</b> — the wordmark carries ™, not ®. Whether a registration exists
  changes what we may print.</li>
</ol>
<p class="muted" style="margin-top:10px;font-size:13.5px">The wordmark's own letterforms are a bespoke logotype, not one of
the three brand typefaces. It stays an image asset; it is never re-typeset.</p></div>
"""))

# ── 04 ────────────────────────────────────────────────────────────────────────
BODY.append(ch('04', 'colour', 'Colour',
  'One ground, one accent. Carbon carries the brand; volt marks the single thing that matters on a screen.',
  """
<h3>4.1 &nbsp;Palette</h3>
<div class="grid g4">
  <div class="swatch"><i style="background:#0f1014;border-bottom:1px solid var(--line)"></i>
    <div class="m"><b>CARBON</b><br>#0F1014<br>rgb(15 16 20)<br><span class="muted">page ground</span></div></div>
  <div class="swatch"><i style="background:#16171b"></i>
    <div class="m"><b>CARD</b><br>#16171B<br>rgb(22 23 27)<br><span class="muted">panels</span></div></div>
  <div class="swatch"><i style="background:#1e2026"></i>
    <div class="m"><b>RAISED</b><br>#1E2026<br>rgb(30 32 38)<br><span class="muted">inputs, wells</span></div></div>
  <div class="swatch"><i style="background:#e3fc02"></i>
    <div class="m"><b>VOLT</b><br>#E3FC02<br>rgb(227 252 2)<br><span class="muted">the only accent</span></div></div>
  <div class="swatch"><i style="background:#fafafa"></i>
    <div class="m"><b>WHITE</b><br>#FAFAFA<br>rgb(250 250 250)<br><span class="muted">type</span></div></div>
  <div class="swatch"><i style="background:#8e9298"></i>
    <div class="m"><b>MUTED</b><br>#8E9298<br>rgb(142 146 152)<br><span class="muted">secondary type</span></div></div>
  <div class="swatch"><i style="background:#f2d2ab"></i>
    <div class="m"><b>WARM LIGHT</b><br>#F2D2AB<br>rgb(242 210 171)<br><span class="muted">lighting only</span></div></div>
  <div class="swatch"><i style="background:#ff6b6b"></i>
    <div class="m"><b>ERROR</b><br>#FF6B6B<br>rgb(255 107 107)<br><span class="muted">errors only</span></div></div>
</div>
<p class="muted" style="font-size:13.5px;margin-top:14px"><b>Warm light</b> is a lighting value — it appears as a gradient wash
and in photography, never as a fill, a button or a text colour. <b>Error</b> is not a second accent: it may not be used
decoratively, and never appears on a page where nothing is wrong.</p>

<h3 style="margin-top:34px">4.2 &nbsp;Proportion</h3>
<div style="display:flex;height:64px;border-radius:12px;overflow:hidden;margin:14px 0 8px">
  <div style="background:#0f1014;flex:78;border:1px solid var(--line);border-right:0;display:flex;align-items:center;padding-left:16px" class="label">78 % CARBON</div>
  <div style="background:#fafafa;flex:18;border:1px solid var(--line);border-left:0;border-right:0"></div>
  <div style="background:#e3fc02;flex:4"></div>
</div>
<p>Roughly <b>78 carbon · 18 white · 4 volt</b>. Volt fell from 10 % in v1 because a dark, soft page lets a single bright
element carry much further. <b>If two volt things are visible at once, one of them is wrong.</b> On a product page the volt
belongs to the price or the primary button — not both.</p>

<h3 style="margin-top:30px">4.3 &nbsp;Contrast — the rule that cannot bend</h3>
<table>
  <tr><th>Pair</th><th>Ratio</th><th>Verdict</th></tr>
  <tr><td>White on carbon</td><td class="readout">16.0</td><td style="color:var(--volt)">Pass · body text</td></tr>
  <tr><td>Volt on carbon</td><td class="readout">15.5</td><td style="color:var(--volt)">Pass · any size</td></tr>
  <tr><td>Carbon on volt</td><td class="readout">15.5</td><td style="color:var(--volt)">Pass · button labels</td></tr>
  <tr><td>Muted on carbon</td><td class="readout">6.4</td><td style="color:var(--volt)">Pass · secondary text only</td></tr>
  <tr><td>White on volt</td><td class="readout">1.15</td><td style="color:var(--error)"><b>Fail — unreadable</b></td></tr>
  <tr><td>Volt on white</td><td class="readout">1.15</td><td style="color:var(--error)"><b>Fail — unreadable</b></td></tr>
</table>
<div class="rule"><span class="label">RULE</span>
<b>Volt always carries carbon type, and never appears as type on white.</b> This is not a preference — it is a measured
accessibility failure in both directions. Every button, chip and selected state in the system is built this way.</div>

<h3 style="margin-top:30px">4.4 &nbsp;States and tints</h3>
<div class="grid g4">
  <div class="swatch"><i style="background:#eeff4a;height:70px"></i><div class="m">VOLT HOVER<br>#EEFF4A</div></div>
  <div class="swatch"><i style="background:#c9df02;height:70px"></i><div class="m">VOLT PRESSED<br>#C9DF02</div></div>
  <div class="swatch"><i style="background:rgb(227 252 2 / .16);height:70px"></i><div class="m">VOLT WASH 16 %<br><span class="muted">selected rows</span></div></div>
  <div class="swatch"><i style="background:rgb(255 255 255 / .08);height:70px"></i><div class="m">HAIRLINE 8 %<br><span class="muted">card borders</span></div></div>
</div>
<p class="muted" style="font-size:13.5px;margin-top:12px">Disabled is opacity, not a colour: 35 % on the whole element.
No new greys may be invented — if a surface needs to sit between card and raised, the layout is wrong, not the palette.</p>

<h3 style="margin-top:30px">4.5 &nbsp;Colour off-screen</h3>
<table>
  <tr><th>Medium</th><th>Guidance</th></tr>
  <tr><td>Print (coated)</td><td>Carbon reproduces as a rich black — ask the printer for a 4-colour black (e.g. 60/50/50/100), never 100 K alone, which goes grey-brown next to the volt.</td></tr>
  <tr><td>Print (volt)</td><td>Volt is out of CMYK gamut. <b>Specify a fluorescent or bright spot ink</b> and proof it; a process-colour approximation reads as a dull lime and undoes the brand.</td></tr>
  <tr><td>Product hardware</td><td>The trolleys' green is a physical finish and photographs around <code>#B4FA6E</code>. Do not retouch it toward volt — the honest photograph is the point. Volt is the digital voice; the hardware is the object.</td></tr>
  <tr><td>Apparel / embroidery</td><td>White mark on black. Volt thread only for a single small detail, if at all.</td></tr>
</table>
<p class="muted" style="font-size:13.5px">Print values above are a starting specification, not a measured proof. Get a physical
proof before any run — particularly for the spot ink.</p>
"""))
print("chapters 3-4 staged")

# ── 05 ────────────────────────────────────────────────────────────────────────
BODY.append(ch('05', 'type', 'Typography',
  'Three typefaces, each with exactly one job. Space Grotesk says what a thing is, Figtree explains it, '
  'Share Tech Mono reports a value. Nothing else is licensed for use.',
  """
<h3>5.1 &nbsp;The three faces</h3>
<div class="grid g3">
  <div class="block" style="margin:0">
    <div class="label"><b>01</b>&nbsp;&nbsp;DISPLAY</div>
    <div style="font-family:var(--display);font-size:46px;letter-spacing:-.02em;margin:14px 0 6px">Space Grotesk</div>
    <p class="muted" style="font-size:14px">Weights 400 · <b>500</b> · 700. Headings, product names, buttons. A technical
    grotesk with squared-off curves — it reads as an instrument label rather than a poster.</p>
  </div>
  <div class="block" style="margin:0">
    <div class="label"><b>02</b>&nbsp;&nbsp;BODY</div>
    <div style="font-family:var(--body);font-weight:500;font-size:40px;margin:14px 0 6px">Figtree</div>
    <p class="muted" style="font-size:14px">Weights <b>400</b> · 500 · 700 + italic. Paragraphs, descriptions, long copy.
    Carried over from v1 — it is quiet, reads long, and stays out of the way.</p>
  </div>
  <div class="block" style="margin:0">
    <div class="label"><b>03</b>&nbsp;&nbsp;TELEMETRY</div>
    <div style="font-family:var(--mono);font-size:38px;margin:14px 0 6px">Share Tech Mono</div>
    <p class="muted" style="font-size:14px">Single weight. Every label, numeral, price, spec value and status line.
    This is the face that makes the brand read as instrumentation.</p>
  </div>
</div>

<div class="rule"><span class="label">THE GOVERNING RULE</span>
<b>A number set in body type is a missed opportunity; prose set in mono is unreadable.</b> If a string is a value the
product reports — range, price, weight, part count, temperature, percentage — it is Share Tech Mono. If it is a sentence,
it is Figtree. If it names a thing, it is Space Grotesk.</div>

<h3 style="margin-top:34px">5.2 &nbsp;Licensing and supply</h3>
<table>
  <tr><th>Face</th><th>Designer</th><th>Licence</th><th>Source</th></tr>
  <tr><td>Space Grotesk</td><td>Florian Karsten</td><td>SIL Open Font License 1.1</td><td>Google Fonts</td></tr>
  <tr><td>Figtree</td><td>Erik Kennedy</td><td>SIL Open Font License 1.1</td><td>Google Fonts</td></tr>
  <tr><td>Share Tech Mono</td><td>Carrois Apostrophe</td><td>SIL Open Font License 1.1</td><td>Google Fonts</td></tr>
</table>
<p>All three are open-licence and free for commercial use, including self-hosting, embedding in PDFs and use on packaging
and signage. There is no per-seat cost, no annual renewal and nothing to buy — deliberately, so that an agency, a printer
and a marketplace listing can all use the real thing.</p>
<div class="rule"><span class="label">BEFORE A PRINT OR PACKAGING RUN</span>
Download the families from Google Fonts and send the actual font files to the supplier along with the licence text.
Re-confirm the licence on the family's page at the time of handoff — open licences are stable, but a supplier's legal
team will ask, and “it's free on Google Fonts” is not an answer.</div>

<h3 style="margin-top:34px">5.3 &nbsp;Specimen</h3>
<div class="block">
  <div class="label">SPACE GROTESK 500</div>
  <p style="font-family:var(--display);font-size:26px;letter-spacing:-.01em;margin:10px 0 4px;line-height:1.35">
  ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>abcdefghijklmnopqrstuvwxyz<br>0123456789 &amp; ™ € £ · — / + %</p>
</div>
<div class="block">
  <div class="label">FIGTREE 400 / 700</div>
  <p style="font-size:19px;margin:10px 0 4px;line-height:1.5">ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz 0123456789<br>
  <b>Crafted from ultra-light aircraft-grade aluminium</b> — effortless folding, magnetic attachments, sealed bearings.</p>
</div>
<div class="block">
  <div class="label">SHARE TECH MONO</div>
  <p style="font-family:var(--mono);font-size:22px;margin:10px 0 4px;line-height:1.5">ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>
  0123456789 · 27+ HOLES · 799,00 € · 36.6 °C · 98 % · 01 02 03</p>
</div>

<h3 style="margin-top:34px">5.4 &nbsp;Scale</h3>
<table>
  <tr><th>Role</th><th>Face</th><th>Size</th><th>Weight</th><th>Tracking</th><th>Leading</th></tr>
  <tr><td>Display</td><td>Space Grotesk</td><td class="readout">68 px</td><td>500</td><td>−0.02em</td><td>1.04</td></tr>
  <tr><td>H1</td><td>Space Grotesk</td><td class="readout">48 / 34 px</td><td>500</td><td>−0.02em</td><td>1.06</td></tr>
  <tr><td>H2</td><td>Space Grotesk</td><td class="readout">32 / 26 px</td><td>500</td><td>−0.02em</td><td>1.1</td></tr>
  <tr><td>H3</td><td>Space Grotesk</td><td class="readout">23 px</td><td>500</td><td>−0.01em</td><td>1.2</td></tr>
  <tr><td>H4</td><td>Space Grotesk</td><td class="readout">18 px</td><td>500</td><td>−0.01em</td><td>1.3</td></tr>
  <tr><td>Body</td><td>Figtree</td><td class="readout">15 px</td><td>400</td><td>0</td><td>1.6</td></tr>
  <tr><td>Body small</td><td>Figtree</td><td class="readout">13 px</td><td>400</td><td>0</td><td>1.55</td></tr>
  <tr><td><b>Readout</b></td><td>Share Tech Mono</td><td class="readout">44 px</td><td>400</td><td>0.02em</td><td>1</td></tr>
  <tr><td><b>Label</b></td><td>Share Tech Mono</td><td class="readout">11 px</td><td>400</td><td><b>0.18em</b></td><td>1.4</td></tr>
</table>
<p class="muted" style="font-size:13.5px">Sizes are absolute px, not rem-scaled — v1's 62.5 % root trick is gone. Two sizes
separated by a slash are desktop / mobile; the breakpoint is 750 px.</p>

<h3 style="margin-top:30px">5.5 &nbsp;Hierarchy in use</h3>
<div class="block">
  <div class="label"><b>02</b>&nbsp;&nbsp;ELECTRIC</div>
  <h3 style="font-size:38px;margin:14px 0 10px">Wishbone EON</h3>
  <p style="max-width:52ch;margin-bottom:16px">A full powered, simple ‘no nonsense’ electric cart. Aircraft-grade aluminium
  frame, sealed bearings, magnetic attachments.</p>
  <div style="display:flex;gap:30px;align-items:baseline">
    <div><div class="label">RANGE</div><div class="readout" style="font-size:36px;margin-top:6px">27+</div></div>
    <div><div class="label">PRICE</div><div class="readout" style="font-size:36px;margin-top:6px">799 €</div></div>
    <div><div class="label">FOLD SIZE</div><div class="readout" style="font-size:36px;margin-top:6px;color:var(--muted)">—</div></div>
  </div>
</div>
<p class="muted" style="font-size:13.5px">Four levels, no more: a mono label says where you are, a display line names the
thing, body type explains it, mono readouts report the values. Anything that does not fit one of those four roles is
probably not needed on the page.</p>

<h3 style="margin-top:30px">5.6 &nbsp;Rules</h3>
<div class="grid g2">
  <div class="do"><h4>Do</h4><ul style="margin-top:8px">
    <li>Set headings in <b>sentence case</b> — the uppercase belonged to Oswald and left with it</li>
    <li>Reserve uppercase for mono labels, tracked 0.18em</li>
    <li>Let display type go large and tight (−0.02em); it is built for it</li>
    <li>Keep body measure at <b>60–75 characters</b></li>
    <li>Align numerals in tables on the decimal; Share Tech Mono is monospaced, so columns line up for free</li>
    <li>Use the real hyphen/en-dash/em-dash, and <code>—</code> for an unknown value</li>
  </ul></div>
  <div class="dont"><h4>Don't</h4><ul style="margin-top:8px">
    <li>Add a fourth typeface, ever — including a “display” face for a campaign</li>
    <li>Set Share Tech Mono below 10 px or in paragraphs</li>
    <li>Use Figtree 700 as a subhead; subheads are Space Grotesk</li>
    <li>Letterspace lowercase body text</li>
    <li>Justify text, hyphenate automatically, or centre a paragraph longer than two lines</li>
    <li>Fake a weight with a text stroke or synthetic bold</li>
  </ul></div>
</div>

<h3 style="margin-top:30px">5.7 &nbsp;Fallbacks and loading</h3>
<table>
  <tr><th>Face</th><th>CSS stack</th></tr>
  <tr><td>Display</td><td><code>'Space Grotesk', -apple-system, 'Segoe UI', sans-serif</code></td></tr>
  <tr><td>Body</td><td><code>'Figtree', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif</code></td></tr>
  <tr><td>Telemetry</td><td><code>'Share Tech Mono', ui-monospace, SFMono-Regular, monospace</code></td></tr>
</table>
<ul>
  <li>Load with <code>font-display: swap</code> and preconnect to <code>fonts.gstatic.com</code>. A flash of fallback text
  is acceptable; invisible text is not.</li>
  <li>Ship only the weights listed in §5.1 — four files total. Every extra weight is bytes the customer pays for.</li>
  <li>Subset to Latin + Latin-Extended (the store sells into AT/DE, so umlauts and the € are required).</li>
  <li>In email, none of the three will load reliably: fall back to <code>Arial, Helvetica, sans-serif</code> for prose and
  <code>Courier New, monospace</code> for readouts, and keep the layout working when they do.</li>
</ul>

<h3 style="margin-top:30px">5.8 &nbsp;In the Shopify theme</h3>
<p>The live theme still runs v1's Oswald + Figtree. The change is a theme-settings edit, not a code rewrite:</p>
<table>
  <tr><th>Setting</th><th>v1 (live today)</th><th>v2 (target)</th></tr>
  <tr><td><code>type_header_font</code></td><td>oswald_n5</td><td>Space Grotesk 500 — in Shopify's font picker, or a custom <code>@font-face</code> if the picker lacks it</td></tr>
  <tr><td><code>type_body_font</code></td><td>figtree_n5</td><td>figtree_n4 (400 — v2 lightens the body weight)</td></tr>
  <tr><td><code>heading_scale</code></td><td>140</td><td>100 — v2 sets absolute sizes rather than scaling</td></tr>
  <tr><td>Telemetry face</td><td>—</td><td>Share Tech Mono, added via <code>@font-face</code> in the theme and a <code>--font-mono</code> variable</td></tr>
</table>
<p class="muted" style="font-size:13.5px">Shopify's font picker carries a fixed library; if Space Grotesk is not in it for this
theme, self-host both it and Share Tech Mono from the theme's <code>assets/</code> — the OFL licence explicitly permits it,
and self-hosting removes a third-party request from the storefront.</p>
"""))

# ── 06 ────────────────────────────────────────────────────────────────────────
BODY.append(ch('06', 'layout', 'Layout, grid & surfaces',
  'Objects on a ground. Panels sit close together so a cluster reads as one instrument; groups sit far apart.',
  """
<h3>6.1 &nbsp;Page</h3>
<table>
  <tr><th>Property</th><th>v2</th><th>v1</th><th>Why it moved</th></tr>
  <tr><td>Page width</td><td class="readout">1440 px</td><td class="muted">1600</td><td>Narrower measure; panels stay legible without stretching</td></tr>
  <tr><td>Gutter</td><td class="readout">24 px</td><td class="muted">24</td><td>Unchanged</td></tr>
  <tr><td>Section spacing</td><td class="readout">72 px</td><td class="muted">52</td><td>More air <em>between</em> ideas</td></tr>
  <tr><td>Grid gap</td><td class="readout">20 px</td><td class="muted">40</td><td>Less air <em>within</em> a cluster</td></tr>
  <tr><td>Breakpoints</td><td class="readout">480 · 750 · 990 · 1400</td><td class="muted">same</td><td>Unchanged</td></tr>
</table>
<p>The tightening is the point: at 40 px gutters every card floated separately; at 20 px, three stat panels read as one
instrument panel with three readings.</p>

<h3 style="margin-top:30px">6.2 &nbsp;Spacing scale</h3>
<div style="display:flex;gap:10px;align-items:flex-end;flex-wrap:wrap;margin:14px 0">
  __SPACING__
</div>
<p class="muted" style="font-size:13.5px">4 · 8 · 12 · 16 · 20 · 28 · 40 · 56 px, then 72 for sections. Nothing in between —
if a gap needs 18 px, the layout is wrong.</p>

<h3 style="margin-top:30px">6.3 &nbsp;Surfaces and radius</h3>
<div class="grid g4">
  <div><div style="height:84px;background:var(--card);border:1px solid var(--line);border-radius:20px"></div>
    <div class="label" style="margin-top:10px">CARD · 20PX</div></div>
  <div><div style="height:84px;background:var(--raised);border:1px solid var(--line-strong);border-radius:10px"></div>
    <div class="label" style="margin-top:10px">CONTROL · 10PX</div></div>
  <div><div style="height:84px;background:var(--card);border:1px solid var(--line);border-radius:16px"></div>
    <div class="label" style="margin-top:10px">MEDIA · 16PX</div></div>
  <div><div style="height:84px;border:1px solid var(--line-strong);border-radius:999px"></div>
    <div class="label" style="margin-top:10px">PILL · FULL</div></div>
</div>
<div class="rule"><span class="label">DEPTH WITHOUT SHADOWS</span>
There are <b>no drop shadows anywhere in this brand</b> — the one rule carried over from v1 unchanged. Depth comes from
three things only: the surface step (carbon → card → raised), a 1 px hairline at 8 %, and the warm wash behind the page.
A gradient may light a scene; it may never fill a component.</div>

<h3 style="margin-top:30px">6.4 &nbsp;Anatomy of a panel</h3>
<div class="block" style="max-width:420px">
  <div class="label"><b>01</b>&nbsp;&nbsp;EON · RANGE</div>
  <div class="readout" style="font-size:44px;margin-top:14px">27+</div>
  <div class="muted" style="font-size:13px;margin-top:6px">One charge, lithium</div>
  <div style="display:flex;gap:22px;margin-top:16px">
    <div><div class="label">PRICE</div><div class="readout" style="font-size:17px;margin-top:4px">799 €</div></div>
    <div><div class="label">FAST CHARGE</div><div class="readout" style="font-size:17px;margin-top:4px">YES</div></div>
  </div>
</div>
<p class="muted" style="font-size:13.5px">Numbered label (18 px from the top edge) → value → one line of context → supporting
pairs. 26–28 px padding, 20 px radius, hairline border. Every panel in the system is this shape.</p>
"""))
print("chapters 5-6 staged")

# ── 07 ────────────────────────────────────────────────────────────────────────
BODY.append(ch('07', 'dots', 'The dot matrix',
  'The signature device. Every quantity, chart, progress state and product silhouette is drawn as a grid of '
  'dots — the visual form of "report the value, then stop".',
  """
<div class="block" style="text-align:center;padding:30px">
  <canvas id="bookdots" style="max-width:100%"></canvas>
  <p class="muted" style="font-size:13px;margin-top:14px">A waveform at 64 × 22, dot 5 px, gap 3 px — volt where the value peaks.</p>
</div>

<h3 style="margin-top:30px">7.1 &nbsp;Specification</h3>
<table>
  <tr><th>Property</th><th>Value</th></tr>
  <tr><td>Dot diameter</td><td class="readout">5 px</td></tr>
  <tr><td>Gap</td><td class="readout">3 px</td></tr>
  <tr><td>Dot opacity</td><td>0.18 (empty) → 0.92 (full), scaled by the value</td></tr>
  <tr><td>Accent dots</td><td>Solid volt — reserved for the part of the data that matters</td></tr>
  <tr><td>Small panels</td><td>4 px dot / 2 px gap, minimum. Below that the grid reads as texture and stops working</td></tr>
  <tr><td>Implementation</td><td><code>DotMatrix</code> and <code>DotBars</code> in <code>components/core/</code></td></tr>
</table>

<h3 style="margin-top:30px">7.2 &nbsp;How a silhouette is made</h3>
<ol>
  <li>Take the real product photograph — lit as specified in §09, matte black on a dark ground.</li>
  <li>Resize to the grid (typically 120–140 columns) and read each cell's luminance.</li>
  <li>Dot radius = luminance; cells below ~6 % are left empty so the object emerges from nothing.</li>
  <li>Cells where the source is green become volt dots, so the hardware accents light up on their own.</li>
</ol>
<div class="rule"><span class="label">WHY IT MATTERS</span>
The dotted EON is the <b>actual EON</b>, sampled from its own photograph — not an illustration of a trolley. A brand that
insists on real numbers cannot draw fake products.</div>

<h3 style="margin-top:30px">7.3 &nbsp;Where to use it</h3>
<div class="grid g2">
  <div class="do"><h4>Use</h4><ul style="margin-top:8px">
    <li>Battery, range and charge readouts</li>
    <li>The model range as five silhouettes</li>
    <li>Spare-part availability</li>
    <li>Progress: order status, configurator steps</li>
    <li>A hero silhouette where a photo would be too literal</li>
  </ul></div>
  <div class="dont"><h4>Never</h4><ul style="margin-top:8px">
    <li>As background texture or a pattern fill</li>
    <li>Behind text</li>
    <li>To render a logo, a mark or a person</li>
    <li>As a loading spinner or decorative animation</li>
    <li>In two different densities on one screen</li>
  </ul></div>
</div>
<p class="muted" style="font-size:13.5px">A dot grid always means <b>this is data</b>. The moment it decorates, the device
stops working and the page becomes a different brand.</p>
"""))

# ── 08 ────────────────────────────────────────────────────────────────────────
BODY.append(ch('08', 'icons', 'Iconography',
  'The brand has no icon set. Until one is commissioned, this is the specification anything drawn must meet.',
  """
<p>Nothing in the current theme ships a Wishbone icon set — the storefront uses its theme's defaults. That is a gap, and
it is worth filling deliberately rather than by accumulation.</p>

<h3 style="margin-top:26px">8.1 &nbsp;Specification</h3>
<table>
  <tr><th>Property</th><th>Value</th></tr>
  <tr><td>Style</td><td>Stroke only. No filled icons, no duotone, no rounded cartoon forms.</td></tr>
  <tr><td>Stroke weight</td><td><b>1.5 px</b> at 24 px — matching the hairline language of the UI</td></tr>
  <tr><td>Terminals</td><td>Butt caps, mitre joins. The wordmark is rounded; the icons are not — they belong to the instrument layer.</td></tr>
  <tr><td>Grid</td><td>24 × 24 with a 2 px safe margin</td></tr>
  <tr><td>Colour</td><td>White at 92 %. Volt only for an icon that <em>is</em> the accent element on the screen.</td></tr>
  <tr><td>Corner radius</td><td>2 px, to sit with 10 px controls without looking soft</td></tr>
</table>

<h3 style="margin-top:26px">8.2 &nbsp;Minimum set to commission</h3>
<p class="muted" style="font-size:14px">Cart · search · account · menu · close · chevron (4 directions) · plus/minus ·
check · alert · battery · charge · weight · fold · wheel · bag · shipping · returns · warranty · spanner (spare parts) ·
play · sound.</p>
<div class="rule"><span class="label">INTERIM</span>
Until the set exists, use a 1.5 px stroke open-source set (Lucide or similar) at <code>stroke-width:1.5</code>, and keep
the choice consistent across the whole storefront. <b>Do not mix two icon sources</b> — that reads faster to a customer
than any typeface error. Replace wholesale when the commissioned set arrives.</div>
<p class="muted" style="font-size:13.5px">Never substitute emoji or unicode glyphs for icons, in any surface including
email and packaging.</p>
"""))

# ── 09 ────────────────────────────────────────────────────────────────────────
BODY.append(ch('09', 'photography', 'Photography & light',
  'One warm source raking across a matte black object on a dark ground. The green hardware is the only '
  'colour in the frame.',
  """
<div class="block" style="padding:0;overflow:hidden">
  <div style="height:190px;background:
    radial-gradient(120% 95% at 8% -15%, rgba(242,210,171,.4), transparent 58%), #0f1014;
    display:flex;align-items:flex-end;padding:20px">
    <span class="label"><b>#F2D2AB</b>&nbsp;&nbsp;KEY LIGHT · TOP-LEFT · FALLS TO BLACK</span>
  </div>
</div>

<h3 style="margin-top:30px">9.1 &nbsp;The lighting recipe</h3>
<table>
  <tr><th>Element</th><th>Specification</th></tr>
  <tr><td>Key</td><td>Single warm source, high and to the <b>left</b>, raking across the frame at roughly 30–45°</td></tr>
  <tr><td>Fill</td><td>Almost none. Let the shadow side go to near-black; the object should emerge rather than sit.</td></tr>
  <tr><td>Rim</td><td>Optional cool rim at low power to separate the frame from the background</td></tr>
  <tr><td>Ground</td><td>Concrete, asphalt, brushed graphite, workshop floor. Never seamless white, never grass at midday.</td></tr>
  <tr><td>Grade</td><td>Warm, slightly desaturated. Blacks lifted no more than a touch — the brand lives at the bottom of the histogram.</td></tr>
  <tr><td>Colour in frame</td><td>The green hardware, and nothing else. No props, no coloured tees, no branded towels.</td></tr>
</table>

<h3 style="margin-top:26px">9.2 &nbsp;Shot list for any model</h3>
<ol>
  <li><b>Hero three-quarter, low angle</b> — the shot the homepage and the dot matrix are built from.</li>
  <li><b>Fold sequence</b>, 3 frames, identical camera — the single most persuasive thing this product does.</li>
  <li><b>Macro: bearing, wheel profile, magnetic attachment</b> — the proof behind the copy.</li>
  <li><b>Scale shot</b> — folded, beside something everyone can measure by eye (a car boot, a doorway).</li>
  <li><b>In use</b> — hands and stance only, on the course at dusk. No faces, no lifestyle.</li>
  <li><b>Flat parts layout</b> for the spare-parts range, dark ground, evenly lit.</li>
</ol>

<h3 style="margin-top:26px">9.3 &nbsp;Do and don't</h3>
<div class="grid g2">
  <div class="do"><h4>Do</h4><ul style="margin-top:8px">
    <li>Shoot close enough to read the engineering</li>
    <li>Keep the horizon out or very low</li>
    <li>Leave generous negative space for type</li>
    <li>Photograph the product as it is — including its green</li>
  </ul></div>
  <div class="dont"><h4>Don't</h4><ul style="margin-top:8px">
    <li>White studio sweeps or e-commerce cut-outs as hero images</li>
    <li>Cool blue-grey grading — v2 is warm</li>
    <li>Lens flare, heavy vignettes, motion blur</li>
    <li>Stock golfers laughing, clubhouse scenes, sunsets with people</li>
    <li>Retouch the hardware green toward volt</li>
  </ul></div>
</div>
<p class="muted" style="font-size:13.5px">Catalogue and marketplace listings are the exception that proves the rule: where a
channel demands a white background, supply a clean cut-out and keep it out of brand-owned surfaces.</p>
"""))

# ── 10 ────────────────────────────────────────────────────────────────────────
BODY.append(ch('10', 'motion', 'Motion',
  'Restrained. Things arrive; they do not perform.',
  """
<table>
  <tr><th>Token</th><th>Duration</th><th>Used for</th></tr>
  <tr><td><code>--motion-fast</code></td><td class="readout">180 ms</td><td>Hover, focus, colour changes</td></tr>
  <tr><td><code>--motion</code></td><td class="readout">320 ms</td><td>Panels, drawers, accordions</td></tr>
  <tr><td><code>--motion-slow</code></td><td class="readout">600 ms</td><td>Reveal on scroll, hero entrances</td></tr>
  <tr><td><code>--ease</code></td><td colspan="2"><code>cubic-bezier(.16,.84,.44,1)</code> — fast out, soft settle</td></tr>
</table>
<div class="grid g2" style="margin-top:12px">
  <div class="do"><h4>Allowed</h4><ul style="margin-top:8px">
    <li>Fade + 8 px rise on scroll, staggered 60 ms across a cluster</li>
    <li>Dot matrices drawing in column by column, once, on first view</li>
    <li>Readouts counting up to their value in ≤ 800 ms</li>
    <li>Colour and border transitions on interactive elements</li>
  </ul></div>
  <div class="dont"><h4>Forbidden</h4><ul style="margin-top:8px">
    <li>Hover lift, scale or shadow growth — there are no shadows to grow</li>
    <li>Parallax, auto-playing carousels, marquees</li>
    <li>Bounce or elastic easing</li>
    <li>Looping animation anywhere near the buy button</li>
  </ul></div>
</div>
<div class="rule"><span class="label">ACCESSIBILITY</span>
Every motion above must be disabled under <code>prefers-reduced-motion: reduce</code>, with the end state shown
immediately. Counting readouts jump straight to the value.</div>
"""))
print("chapters 7-10 staged")

# ── 11 ────────────────────────────────────────────────────────────────────────
BODY.append(ch('11', 'applications', 'Applications',
  'The system on real surfaces. Each of these is built from the same tokens and components — '
  'nothing here is a one-off.',
  """
<h3>11.1 &nbsp;Storefront — header and hero</h3>
<div class="mock">
  <div class="label" style="display:flex;align-items:center;gap:8px;padding:9px 20px;border-bottom:1px solid var(--line)">
    <i style="width:6px;height:6px;border-radius:50%;background:var(--volt);display:inline-block"></i>ALL SYSTEMS OPERATIONAL</div>
  <div style="display:flex;align-items:center;justify-content:space-between;gap:24px;padding:16px 20px;border-bottom:1px solid var(--line)">
    <img src="__WORD__" style="width:150px">
    <span class="label" style="display:flex;gap:16px">TROLLEYS &nbsp;ELECTRIC &nbsp;SPARE PARTS &nbsp;CONTACT</span>
    <span class="label" style="color:var(--volt)">CART [02]</span>
  </div>
  <div style="padding:40px 26px;background:radial-gradient(110% 90% at 10% -20%, rgba(242,210,171,.2), transparent 60%)">
    <div class="label"><b>01</b>&nbsp;&nbsp;ELECTRIC</div>
    <h3 style="font-size:44px;margin:14px 0 12px">Wishbone EON</h3>
    <p style="max-width:44ch;margin-bottom:20px">A full powered, simple ‘no nonsense’ electric cart.</p>
    <div style="display:flex;gap:12px;flex-wrap:wrap"><span class="btn">Add to cart · 799 €</span><span class="btn ghost">Compare models</span></div>
  </div>
</div>

<h3 style="margin-top:34px">11.2 &nbsp;Product page — the spec block</h3>
<div class="grid g3">
  <div class="block" style="margin:0"><div class="label"><b>01</b>&nbsp;&nbsp;RANGE</div>
    <div class="readout" style="font-size:40px;margin-top:12px">27+</div>
    <div class="muted" style="font-size:13px;margin-top:6px">holes · one charge</div></div>
  <div class="block" style="margin:0"><div class="label"><b>02</b>&nbsp;&nbsp;FRAME</div>
    <div class="readout" style="font-size:40px;margin-top:12px">AL</div>
    <div class="muted" style="font-size:13px;margin-top:6px">aircraft-grade aluminium</div></div>
  <div class="block" style="margin:0"><div class="label"><b>03</b>&nbsp;&nbsp;FOLD SIZE</div>
    <div class="readout" style="font-size:40px;margin-top:12px;color:var(--muted)">—</div>
    <div class="muted" style="font-size:13px;margin-top:6px">not yet measured</div></div>
</div>
<p class="muted" style="font-size:13.5px;margin-top:10px">The third panel is deliberate. A missing value is shown, not hidden —
it is also the standing reminder to go and measure it.</p>

<h3 style="margin-top:34px">11.3 &nbsp;Email</h3>
<div class="grid g2">
  <div class="mock" style="padding:24px">
    <img src="__WORD__" style="width:130px;display:block;margin:0 auto 20px">
    <div class="label" style="text-align:center"><b>03</b>&nbsp;&nbsp;BACK IN STOCK</div>
    <h4 style="text-align:center;font-size:22px;margin:12px 0 8px">Fast Charger (NEO &amp; EON)</h4>
    <p style="text-align:center;font-size:14px;color:var(--muted);margin-bottom:18px">99,90 € · ships same day</p>
    <div style="text-align:center"><span class="btn">Add to cart</span></div>
  </div>
  <div>
    <h4>Rules</h4>
    <ul style="font-size:14px;margin-top:8px">
      <li>Carbon background, white type — email clients honour it, and it keeps the brand consistent in the inbox</li>
      <li>Single column, 600 px, one action per email</li>
      <li>Subject lines report: <em>“Fast Charger back in stock — 99,90 €”</em>, never <em>“You won't believe…”</em></li>
      <li>Fallback faces from §5.7; never an image of text</li>
      <li>Always include the plain-text alternative — a values-and-facts brand reads perfectly well in plain text</li>
    </ul>
  </div>
</div>

<h3 style="margin-top:34px">11.4 &nbsp;Social</h3>
<div class="grid g3">
  <div class="mock" style="aspect-ratio:1;padding:22px;display:flex;flex-direction:column;justify-content:space-between">
    <div class="label"><b>01</b>&nbsp;&nbsp;EON</div>
    <div><div class="readout" style="font-size:52px">27+</div>
      <div class="muted" style="font-size:13px;margin-top:6px">holes on one charge</div></div>
    <img src="__WORD__" style="width:84px;opacity:.9">
  </div>
  <div class="mock" style="aspect-ratio:1;padding:22px;display:flex;flex-direction:column;justify-content:space-between;
    background:radial-gradient(100% 80% at 15% 0%, rgba(242,210,171,.22), transparent 62%), var(--card)">
    <div class="label"><b>02</b>&nbsp;&nbsp;THE RANGE</div>
    <h4 style="font-size:26px">Five models.<br>Three manual, two electric.</h4>
    <img src="__WORD__" style="width:84px;opacity:.9">
  </div>
  <div class="mock" style="aspect-ratio:1;display:flex;align-items:center;justify-content:center;background:var(--volt)">
    <img src="__MONO__" style="width:44%;filter:brightness(0)">
  </div>
</div>
<p class="muted" style="font-size:13.5px;margin-top:10px">One fact per post. The volt tile is the exception that proves §4.2 —
on a volt field the monogram goes solid carbon, never white. No captions baked into the image; no more than one post in
five may be a pure brand tile.</p>

<h3 style="margin-top:34px">11.5 &nbsp;Print &amp; physical</h3>
<div class="grid g2">
  <div class="mock" style="padding:22px;aspect-ratio:1.75;display:flex;flex-direction:column;justify-content:space-between">
    <img src="__WORD__" style="width:120px">
    <div><div style="font-family:var(--display);font-size:17px">Name Surname</div>
      <div class="label" style="margin-top:6px">ROLE · WISHBONE.GOLF</div></div>
  </div>
  <div>
    <h4>Specifications</h4>
    <table style="margin-top:6px">
      <tr><td>Business card</td><td>85 × 55 mm, carbon uncoated, white + spot volt, soft-touch optional</td></tr>
      <tr><td>Packaging insert</td><td>A5, carbon, one panel of specs in mono, QR to the spare-parts page</td></tr>
      <tr><td>Spec sheet</td><td>A4 PDF, the §6.4 panel grid, one model per sheet, printable on mono laser</td></tr>
      <tr><td>Trade stand</td><td>Carbon walls, one raking warm key, products lit as §09; a single volt element in the whole booth</td></tr>
      <tr><td>Apparel</td><td>Black garment, white wordmark left chest 60 mm; no volt on garments larger than a detail</td></tr>
    </table>
  </div>
</div>
"""))

# ── 12 ────────────────────────────────────────────────────────────────────────
BODY.append(ch('12', 'governance', 'Governance',
  'Where the system lives, how to change it, and what is still open. A brand book that cannot be updated '
  'becomes a PDF nobody opens.',
  """
<h3>12.1 &nbsp;Where everything lives</h3>
<table>
  <tr><th>Asset</th><th>Location</th></tr>
  <tr><td>This book</td><td><code>design-system/tools/build-brandbook.py</code> → regenerate, then publish</td></tr>
  <tr><td>Tokens (source of truth)</td><td><code>design-system/tokens/*.css</code></td></tr>
  <tr><td>Tokens (portable)</td><td><code>docs/brand/tokens.css</code> · <code>tokens.json</code></td></tr>
  <tr><td>Components</td><td><code>design-system/components/{core,commerce,chrome}</code></td></tr>
  <tr><td>Specimen cards</td><td><code>design-system/guidelines/*.html</code></td></tr>
  <tr><td>Marks</td><td><code>design-system/assets/</code> · <code>docs/brand/assets/</code></td></tr>
  <tr><td>Written kit</td><td><code>docs/brand/BRAND_KIT.md</code> — the decisions and their evidence</td></tr>
  <tr><td>Design system (cloud)</td><td>Claude Design → <em>Wishbone Golf Design System</em>, skill <code>wishbone-design</code></td></tr>
  <tr><td>Storefront</td><td><code>theme/</code> — the live Shopify theme, version-controlled</td></tr>
  <tr><td>Repository</td><td><code>github.com/mrehb/wishbone_shopify</code></td></tr>
</table>

<h3 style="margin-top:30px">12.2 &nbsp;How to change something</h3>
<ol>
  <li>Change the value in <code>design-system/tokens/</code> — never in a component.</li>
  <li>Mirror it into <code>docs/brand/tokens.css</code> and <code>tokens.json</code>.</li>
  <li>Regenerate this book and the system overview; re-push the design system.</li>
  <li>Record the decision and its reason in <code>BRAND_KIT.md</code>.</li>
  <li>Only then touch the theme — and only into a draft.</li>
</ol>
<div class="rule"><span class="label">THE LIVE-STORE RULE</span>
wishbone.golf sells. Nothing reaches a customer except by building a draft theme, reviewing its preview, and publishing by
hand in Shopify admin. Tooling enforces it: <code>bin/wb</code> has no publish command and refuses the live theme, and a
guard hook blocks live writes even in bypass mode.</div>

<h3 style="margin-top:30px">12.3 &nbsp;Versions</h3>
<table>
  <tr><th>Version</th><th>Date</th><th>What it was</th></tr>
  <tr><td><b>v1.0</b></td><td>19 Sep 2026</td><td>The store as found: ink ground, volt + cyan, Oswald caps, radius 0 everywhere</td></tr>
  <tr><td><b>v2.0 “Telemetry”</b></td><td>19 Sep 2026</td><td>Rebrand. Carbon ground, volt only, soft geometry, Space Grotesk + Figtree + Share Tech Mono, dot matrix. Voice, naming, architecture and the no-shadow rule carried over unchanged.</td></tr>
</table>

<h3 style="margin-top:30px">12.4 &nbsp;Open — and who has to close it</h3>
<table>
  <tr><th>#</th><th>Item</th><th>Owner</th></tr>
  <tr><td>01</td><td><b>Fold size and weight</b> are missing from the catalogue. A brand that reports values needs them; panels print <code>—</code> until they exist.</td><td>Wishbone</td></tr>
  <tr><td>02</td><td><b>Positive and SVG versions of both marks</b> — no light-background or large-format use is possible today.</td><td>Designer, to commission</td></tr>
  <tr><td>03</td><td><b>Icon set</b> to §8.1, or a documented decision to stay on an open-source set.</td><td>Designer</td></tr>
  <tr><td>04</td><td><b>Spot-ink proof for volt</b> before any print run.</td><td>Printer</td></tr>
  <tr><td>05</td><td>“aluminum” → “aluminium” on the homepage.</td><td>One-line theme fix</td></tr>
  <tr><td>06</td><td>One product still published under vendor <em>My Store</em>.</td><td>Shopify admin</td></tr>
  <tr><td>07</td><td>Trademark status of the wordmark — ™ is shown; is it registered?</td><td>Wishbone</td></tr>
  <tr><td>08</td><td><b>Theme migration to v2</b> — the storefront still runs v1 in full.</td><td>Next build</td></tr>
</table>

<h3 style="margin-top:30px">12.5 &nbsp;The short version</h3>
<div class="block">
  <p style="font-family:var(--display);font-size:22px;letter-spacing:-.01em;line-height:1.45;margin:0">
  Carbon ground. One volt accent, four per cent of the page, always carrying carbon type. Soft corners, hairline borders,
  no shadows. Space Grotesk names it, Figtree explains it, Share Tech Mono reports it. Data is drawn in dots. Say the
  number — and where there is no number, print an em dash and go and measure it.</p>
</div>
"""))
print("chapters 11-12 staged")

# ── assembly ─────────────────────────────────────────────────────────────────
spacing = "".join(
    '<div style="text-align:center"><div style="width:%dpx;height:%dpx;background:var(--volt);border-radius:3px"></div>'
    '<div class="label" style="margin-top:8px">%d</div></div>' % (v, max(v, 8), v)
    for v in [4, 8, 12, 16, 20, 28, 40, 56])

toc = "".join('<a href="#%s">%s &nbsp;%s</a>' % (slug, num, title) for num, slug, title in CHAPTERS)

DOTSCRIPT = """
<script>
(function(){
  var c=document.getElementById('bookdots'); if(!c) return;
  var COLS=64,ROWS=22,S=5,G=3,step=S+G,dpr=window.devicePixelRatio||1;
  c.width=COLS*step*dpr; c.height=ROWS*step*dpr;
  c.style.width=(COLS*step)+'px'; c.style.height=(ROWS*step)+'px';
  var x=c.getContext('2d'); x.scale(dpr,dpr);
  for(var r=0;r<ROWS;r++) for(var col=0;col<COLS;col++){
    var wave=Math.sin(col/7)*0.5+0.5, band=1-Math.abs((r/ROWS)-wave)*2.6;
    var v=Math.max(0,Math.min(1,band)); if(v<0.06) continue;
    x.beginPath(); x.arc(col*step+S/2, r*step+S/2, Math.max(v*(S/2),0.4), 0, 6.2832);
    x.fillStyle = (col>46 && v>0.55) ? '#e3fc02' : 'rgba(250,250,250,'+(0.18+v*0.74).toFixed(3)+')';
    x.fill();
  }
})();
</script>
"""

HTML = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Wishbone Golf — Brand Book v2.0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=Figtree:ital,wght@0,400;0,500;0,700;1,400&family=Share+Tech+Mono&display=swap" rel="stylesheet">
<style>__CSS__</style></head><body>

<div class="wrap">
  <header class="cover">
    <img src="__WORD__" alt="Wishbone Golf">
    <h1 style="max-width:16ch">Brand book</h1>
    <p class="lede" style="max-width:56ch">The complete identity: who Wishbone is, how it speaks, and every rule that
    governs how it looks — marks, colour, typography, layout, the dot matrix, photography, motion and the surfaces they
    land on.</p>
    <div class="meta">
      <div><div class="label">VERSION</div><div class="readout" style="font-size:22px;margin-top:6px">2.0</div></div>
      <div><div class="label">CODENAME</div><div class="readout" style="font-size:22px;margin-top:6px">TELEMETRY</div></div>
      <div><div class="label">ISSUED</div><div class="readout" style="font-size:22px;margin-top:6px">19.09.2026</div></div>
      <div><div class="label">SUPERSEDES</div><div class="readout" style="font-size:22px;margin-top:6px">1.0</div></div>
    </div>
  </header>
</div>

<nav class="toc"><div class="inner">__TOC__</div></nav>

<div class="wrap">
__BODY__

<footer>
  Wishbone Golf brand book v2.0 “Telemetry” · issued 19 September 2026 · generated from the live design system, so the book
  and the components cannot drift apart · source <code>design-system/tools/build-brandbook.py</code> ·
  repository <code>github.com/mrehb/wishbone_shopify</code>
</footer>
</div>
__DOTSCRIPT__
</body></html>
"""

out = (HTML.replace('__CSS__', CSS).replace('__TOC__', toc)
           .replace('__BODY__', "\n".join(BODY))
           .replace('__SPACING__', spacing)
           .replace('__DOTSCRIPT__', DOTSCRIPT)
           .replace('__WORD__', WORD).replace('__MONO__', MONO).replace('__MONO_OLD__', MONO_OLD))

dest = pathlib.Path('/tmp/wb/kit/wishbone-brand-book.html')
dest.parent.mkdir(parents=True, exist_ok=True)
dest.write_text(out)
print('wrote', dest, round(len(out)/1024), 'KB ·', len(CHAPTERS), 'chapters')
