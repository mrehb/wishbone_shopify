#!/usr/bin/env python3
"""Wishbone CUBE three — one complete product landing page, built on the v4 "Studio" system
and the real Product Bay record (id 9054916). Regenerate after any token or data change."""
import base64, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
PB   = pathlib.Path('/tmp/wb/pb')
tokens = "".join("\n" + re.sub(r"@import[^;]+;", "", (ROOT/'tokens'/f).read_text())
                 for f in ['colors.css','typography.css','geometry.css','layout.css','base.css'])
uri  = lambda p: "data:image/png;base64," + base64.b64encode((ROOT/p).read_bytes()).decode()
WORD = uri('assets/wishbone-wordmark-ink.png')
WORDN= uri('assets/wishbone-wordmark.png')
MONO = uri('assets/wishbone-monogram-ink.png')
DET  = {k: "data:image/jpeg;base64," + v for k, v in json.load(open(PB/'details_b64.json')).items()}

C = 'https://cdn.productbay.ai/insecure/resize:fit:1600:1600/plain/2/'
IMG = {
 'bw':C+'DSCF2323-1775727881706.png', 'bl':C+'DSCF2323-1775727943854.png', 'wr':C+'DSCF2323-1775727971305.png',
 'l1':C+'014A2245-1785769277605.jpg', 'l2':C+'014A2246-1785769277606.jpg', 'l3':C+'014A2249-1785769277606.jpg',
 'l4':C+'014A2302-1785769657546.jpg', 'l5':C+'014A2307-1785769657546.jpg', 'l6':C+'014A2310-1785769657546.jpg',
 'balltee':C.replace('/plain/2/','/plain/min/2/')+'BallTeeHolder-1762519439390.jpg',
 'score':C.replace('/plain/2/','/plain/min/2/')+'Magnetic_Scorecard_Holder_3-1762519607706.jpg',
 'umbrella':C.replace('/plain/2/','/plain/min/2/')+'UmbrellaHolder_2-1762520004846.jpg',
 'drink':C.replace('/plain/2/','/plain/min/2/')+'WISHBONE_Electric_09_11_202101424-1762520226211.jpg',
 'carry':C.replace('/plain/2/','/plain/min/2/')+'Wheelcase-open-1762520413548.png',
 'two':C+'WISHBONE-CUBE-TWO-manual-1764687463834.pdf',
 'one':'https://cdn.productbay.ai/insecure/resize:fit:1200:1200/plain/min/2/WB-ONE---charcaol-red-1736246451452.png',
}

COLOURWAYS = [
 {'id':'black-lime','name':'Black / Lime','img':IMG['bl'],'sku':'WB12218','ean':'9008356027277','a':'#111214','b':'#8cac1c'},
 {'id':'black-white','name':'Black / White','img':IMG['bw'],'sku':'WB12217','ean':'9008356027284','a':'#111214','b':'#e9e9e9'},
 {'id':'white-red','name':'White / Red','img':IMG['wr'],'sku':'WB12219','ean':'9008356027307','a':'#e9e9e9','b':'#e03828'},
]

HOTSPOTS = [
 {'n':'01','x':76,'y':9, 't':'Smart Organizer','d':'A moulded console across the handle: scorecard clip, pencil slot, tee holes and ball recesses, all in reach without stopping.','img':'organizer'},
 {'n':'02','x':86,'y':4, 't':'Height-adjustable handle','d':'The grip sets to your height and stays there. One clamp, no tools.','img':'organizer'},
 {'n':'03','x':38,'y':15,'t':'Adjustable bag bracket','d':'The upper bracket slides and straps to the bag you already own — stand bag or cart bag.','img':'upperbracket'},
 {'n':'04','x':57,'y':21,'t':'Quick Lok base','d':'Four bases on the frame. Umbrella, drink, ball and tee holders click on and off without a spanner.','img':'upperbracket'},
 {'n':'05','x':54,'y':34,'t':'Dual-tube frame','d':'The THREE’s new design language: two aluminium tubes instead of one, which is where the torsional stiffness comes from.','img':'frame'},
 {'n':'06','x':14,'y':60,'t':'Lower bag bracket','d':'A moulded cradle and strap take the weight of the bag low down, so the load sits over the axle.','img':'lowerbracket'},
 {'n':'07','x':44,'y':74,'t':'Front wheel, 24 cm','d':'Folds in with the frame rather than coming off. Tracks straight; it does not swivel.','img':'frontwheel'},
 {'n':'08','x':75,'y':80,'t':'Rear wheels, 29 cm — and the footbrake','d':'Both rear wheels pull off for the boot. The footbrake is a pedal at the axle: press to park.','img':'rearwheel'},
]

SPECS = [
 ('Model','Wishbone CUBE three'),('Type','Manual push trolley, three wheels'),
 ('Frame','Aluminium, dual-tube'),('Folding mechanism','CubeFold'),
 ('Folded dimensions','37.5 × 57 × 46 cm'),('Net weight','7.65 kg'),
 ('Locks when folded and unfolded','Yes'),('Front wheel','24 cm, folds with the frame'),
 ('Rear wheels','29 cm, detachable'),('360° swivel front wheel','No'),
 ('Brake','Footbrake'),('Handle','Height-adjustable'),
 ('Bag bracket','Adjustable, upper and lower'),('Organiser','Smart Organizer console'),
 ('Quick Lok bases','4'),('Scorecard holder','Yes'),('Pencil holder','Yes'),
 ('Tee holder','Yes'),('Integrated bottle holder','Yes'),
 ('Colourways','Black / Lime · Black / White · White / Red'),
 ('RRP','249,00 €'),('Packing size',None),('Gross weight',None),
]

COMPARE = {
 'models':[
  {'id':'ONE','name':'ONE','price':'229,00 €','img':IMG['one']},
  {'id':'TWO','name':'CUBE two','price':'199,00 €','img':IMG['two']},
  {'id':'THREE','name':'CUBE three','price':'249,00 €','img':IMG['bl']},
 ],
 'rows':[
  ('Frame',{'ONE':'Aluminium','TWO':'Aluminium, single tube','THREE':'Aluminium, dual tube'}),
  ('Net weight',{'TWO':'6.9 kg','THREE':'7.65 kg'}),
  ('Folded size',{'TWO':'35.5 × 53 × 45 cm','THREE':'37.5 × 57 × 46 cm'}),
  ('Folding mechanism',{'TWO':'CubeFold','THREE':'CubeFold'}),
  ('Front / rear wheel',{'TWO':'24 / 29 cm','THREE':'24 / 29 cm'}),
  ('Brake',{'ONE':'Footbrake','TWO':'Footbrake','THREE':'Footbrake'}),
  ('Accessory bases',{'ONE':'1 Quick Fix','TWO':'4 Quick Lok','THREE':'4 Quick Lok'}),
  ('Smart Organizer',{'TWO':'Yes','THREE':'Yes'}),
  ('Scorecard + pencil holder',{'THREE':'Yes'}),
  ('Locks folded and unfolded',{'THREE':'Yes'}),
  ('Colourways',{'ONE':'5','TWO':'3','THREE':'3'}),
 ]}

ACCESSORIES = [
 ('Ball &amp; Tee Holder','13,90 €','WB-07S',IMG['balltee']),
 ('Magnetic Scorecard Holder','29,90 €','WB-08S',IMG['score']),
 ('Umbrella Holder','29,90 €','WB-09S',IMG['umbrella']),
 ('Drink Holder','13,90 €','WB-10S',IMG['drink']),
 ('Carry Bag Set, universal','29,90 €','WB12222',IMG['carry']),
]

FAQ = [
 ('How small does it actually fold?','Into a cube of 37.5 × 57 × 46 cm, and it locks there — it will not spring open when you lift it. Pull the two rear wheels off and it loses another hand’s width each side.'),
 ('Will it take my bag?','Both brackets adjust and strap, so a stand bag and a cart bag both sit properly. The lower cradle carries the weight; the upper bracket only steadies it.'),
 ('Does the front wheel swivel?','No. It is fixed and tracks straight, which is what keeps the trolley going where you point it across a slope. It folds in with the frame rather than coming off.'),
 ('What is the difference between the two and the three?','The three has the dual-tube frame, a scorecard and pencil holder, and locks in both the folded and unfolded position. It is 750 g heavier and 50 € more.'),
 ('Can I get spare parts?','Yes. Wishbone lists parts by model, and the wheels, brackets and holders are all replaceable rather than moulded in.'),
]

NOTES = [
 ('Higgsfield was not reachable in this session','The MCP connector is not attached to this run, so no image was generated. Everything visual on this page is either a real Wishbone photograph or a diagram drawn from the measured numbers. The shot list below is ready to fire the moment the connector is live.'),
 ('The product has a sub-brand the website does not use','The manual and the frame both say <b>CUBE three</b>. Shopify calls it <em>Wishbone THREE</em>. This page uses CUBE three; if that is wrong, it is a one-line change.'),
 ('The specs that were "not yet measured" exist','Weight 7.65 kg and 37.5 × 57 × 46 cm are in Product Bay and have never reached the storefront. The brand book still says these are unknown — that entry can now be closed.'),
 ('The lime is not the brand lime','Sampled from the photograph, the three’s lime is hue 72° (about #8CAC1C) — the same yellow-green family as the logo. The v4 brand accent is #A8FF4A, hue 89°, sampled from the EON. Two different greens are in play across the range and one of them should move.'),
 ('There is red in the brand','The White / Red colourway and the CUBE logo both use #E03828. The v4 system says there is no red. That needs a ruling.'),
 ('Six course photographs are sitting unused','014A2245 through 014A2310 are in Product Bay and on no page of the website. They are the best assets the brand owns.'),
 ('A product tour video exists','<em>Wishbone Three Product Tour.mp4</em>, 211 MB, in Product Bay. It belongs on this page; it needs hosting and a poster frame.'),
 ('Packing size and gross weight are zero','Both are filled in as 0 in Product Bay, which is not a measurement. The spec table prints an em dash instead.'),
]

SHOTLIST = [
 ('The fold, as a sequence','Five frames, same camera, same light: unfolded → front wheel folding in → frame closing → locked cube → cube carried one-handed. Reference the studio PNG for geometry and colour.','5 × 1:1'),
 ('The folded cube, hero','The locked cube on a plain light ground, three-quarter, raking light from the top left, shot to show it is a cube. This is the one image the page most needs and does not have.','1:1'),
 ('Boot shot','The folded cube in the boot of an estate car with a bag beside it, daylight, no people.','16:9'),
 ('Smart Organizer, top-down macro','Directly above the console with a scorecard, pencil, three tees and a ball in place. Fills the frame.','4:5'),
 ('Wheel off','A hand pulling a rear wheel clear of the axle, mid-movement, shallow depth of field.','4:5'),
 ('Footbrake','A shoe pressing the brake pedal, low angle, grass.','16:9'),
 ('Black / Lime and Black / White on the course','The two colourways that have no lifestyle photography at all — only White / Red was shot. Same location and light as 014A2245.','3:2'),
 ('Bag compatibility','The same trolley with a stand bag and with a cart bag, identical framing, so the two can be crossfaded.','2 × 4:5'),
]

# ---------------------------------------------------------------- page CSS
CSS = """
:root{ --lime-hw:#8cac1c; --red-hw:#e03828; }
html{scroll-behavior:smooth}
body{overflow-x:hidden}
img{display:block;max-width:100%}
.wrap{max-width:var(--page);margin:0 auto;padding:0 var(--pad-x)}
.hairline{border:0;border-top:1px solid var(--hair)}

/* header */
header.site{position:sticky;top:0;z-index:60;background:rgb(255 255 255 / .92);backdrop-filter:blur(14px);
  border-bottom:1px solid var(--hair)}
header.site .bar{display:flex;align-items:center;gap:32px;height:68px}
header.site nav{display:flex;gap:26px;margin:0 auto}
header.site nav a{position:relative;padding:4px 0}
header.site nav a::after{content:'';position:absolute;left:0;right:100%;bottom:0;height:2px;background:var(--lime);
  transition:right var(--t-fast) var(--ease)}
header.site nav a:hover::after{right:0}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:14px;padding:14px 24px;border:1px solid transparent;
  border-radius:0;cursor:pointer;font-family:var(--font);font-size:var(--fs-label);font-weight:var(--w-ui);
  letter-spacing:var(--track-label);text-transform:uppercase;line-height:1;
  transition:background var(--t-fast) var(--ease),color var(--t-fast) var(--ease),border-color var(--t-fast) var(--ease)}
.btn--lime{background:var(--lime);color:var(--on-lime);border-color:var(--lime)}
.btn--lime:hover{background:#97ef33}
.btn--ink{background:var(--ink);color:#fafafa;border-color:var(--ink)}
.btn--out{background:transparent;color:inherit;border-color:currentColor}
.btn--out:hover{background:var(--ink);color:#fafafa;border-color:var(--ink)}
.band--ink .btn--out:hover{background:#fafafa;color:var(--ink);border-color:#fafafa}
.btn--sm{padding:11px 16px}

/* hero */
.hero{background:var(--mist);position:relative;overflow:hidden}
.hero .grid{align-items:center;min-height:660px}
.hero .copy{grid-column:span 5;display:grid;gap:26px;padding:72px 0;position:relative;z-index:2}
.hero .stage{grid-column:7 / span 6;position:relative;align-self:stretch;display:flex;align-items:center;justify-content:center}
.hero .stage img{width:100%;transition:opacity var(--t-slow) var(--ease),transform var(--t-slow) var(--ease)}
.hero .stage .slot{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;opacity:0;transform:scale(.985)}
.hero .stage .slot.on{opacity:1;transform:none;position:relative}
.price{font-weight:var(--w-strong);font-size:28px;font-variant-numeric:tabular-nums}
.sw{display:flex;gap:10px}
.sw button{width:34px;height:34px;padding:0;border:2px solid transparent;outline:1px solid var(--hair);outline-offset:-1px;
  cursor:pointer;border-radius:0;transition:outline-color var(--t-fast) var(--ease),border-color var(--t-fast) var(--ease)}
.sw button[aria-pressed="true"]{border-color:var(--ink);outline-color:var(--ink)}
.idx{display:flex;gap:18px;list-style:none;padding:0;margin:0}
.idx li{padding-bottom:7px;border-bottom:2px solid transparent;color:var(--grey);cursor:pointer}
.idx li.on{border-color:var(--lime);color:var(--ink)}

/* stat strip */
.stats{display:grid;grid-template-columns:repeat(5,1fr)}
.stats>div{padding:34px 20px;text-align:center;border-left:1px solid var(--hair)}
.stats>div:first-child{border-left:0}
.stats .v{font-size:var(--fs-stat);font-weight:var(--w-display);line-height:1;letter-spacing:-.01em;
  font-variant-numeric:tabular-nums}
.stats .v small{font-size:.42em;color:var(--grey);margin-left:5px;font-weight:var(--w-body)}
.stats .k{margin-top:10px}

/* feature map */
.map{display:grid;grid-template-columns:1.25fr .75fr;gap:48px;align-items:start;margin-top:44px}
.map .plate{position:relative;background:var(--mist);aspect-ratio:1}
.map .plate>img{position:absolute;inset:0;width:100%;height:100%;object-fit:contain}
.spot{position:absolute;width:34px;height:34px;transform:translate(-50%,-50%);border-radius:50%;border:1px solid var(--ink);
  background:rgb(255 255 255 / .82);color:var(--ink);font-family:var(--font);font-size:11px;font-weight:var(--w-ui);
  letter-spacing:.06em;cursor:pointer;display:grid;place-items:center;padding:0;
  transition:background var(--t-fast) var(--ease),color var(--t-fast) var(--ease),transform var(--t-fast) var(--ease)}
.spot:hover{transform:translate(-50%,-50%) scale(1.12)}
.spot[aria-pressed="true"]{background:var(--lime);border-color:var(--lime);color:var(--on-lime)}
.det{border-top:1px solid var(--ink);padding-top:22px}
.det img{width:100%;background:var(--mist);margin-bottom:20px}
.det h3{font-size:var(--fs-lead);font-weight:var(--w-ui);margin-bottom:10px}
.featlist{list-style:none;padding:0;margin:26px 0 0;border-top:1px solid var(--hair)}
.featlist li{border-bottom:1px solid var(--hair)}
.featlist button{width:100%;display:flex;gap:16px;align-items:baseline;padding:13px 0;background:none;border:0;
  text-align:left;cursor:pointer;font-size:14px}
.featlist button[aria-pressed="true"]{color:var(--ink)}
.featlist .n{font-family:var(--font-dot);font-size:12px;letter-spacing:.1em;color:var(--grey);-webkit-font-smoothing:none}
.featlist button[aria-pressed="true"] .n{color:var(--ink)}

/* fold diagram */
.fold{display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center}
.fold svg{width:100%;height:auto}
.dimrow{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:30px}
.dimrow .v{font-size:32px;font-weight:var(--w-display);line-height:1;font-variant-numeric:tabular-nums}

/* gallery */
.gal{display:grid;grid-template-columns:repeat(12,1fr);gap:16px}
.gal figure{margin:0;overflow:hidden;background:var(--mist)}
.gal img{width:100%;height:100%;object-fit:cover;transition:transform 900ms var(--ease)}
.gal figure:hover img{transform:scale(1.035)}
.gal .w8{grid-column:span 8}.gal .w4{grid-column:span 4}.gal .w6{grid-column:span 6}.gal .w12{grid-column:span 12}
.gal .h1{aspect-ratio:3/2}.gal .h2{aspect-ratio:1}.gal .h3{aspect-ratio:21/9}

/* colourways */
.cw{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.cw figure{margin:0;background:#fff;border:1px solid var(--hair);padding:22px}
.cw img{width:100%;background:var(--mist)}
.cw .chip{display:inline-block;width:22px;height:22px;vertical-align:middle;margin-right:8px}

/* compare */
table.cmp{width:100%;border-collapse:collapse;font-size:14px}
table.cmp th,table.cmp td{text-align:left;padding:14px 14px 14px 0;border-bottom:1px solid var(--hair);vertical-align:middle}
table.cmp thead th{border-bottom:1px solid var(--ink);vertical-align:bottom;font-weight:400}
table.cmp thead img{width:100%;max-width:150px;background:var(--mist);margin-bottom:12px}
table.cmp .hi{background:rgb(168 255 74 / .10)}
table.cmp td.na{color:var(--grey)}

/* accessories */
.acc{display:grid;grid-template-columns:repeat(5,1fr);gap:16px}
.acc a{display:grid;gap:12px}
.acc img{width:100%;background:var(--mist);aspect-ratio:1;object-fit:cover}

/* spec + faq */
table.spec{width:100%;border-collapse:collapse;font-size:14px}
table.spec th{width:38%;text-align:left;padding:14px 0;border-bottom:1px solid var(--hair);font-weight:var(--w-ui)}
table.spec td{padding:14px 0;border-bottom:1px solid var(--hair);font-variant-numeric:tabular-nums}
details.faq{border-bottom:1px solid var(--hair)}
details.faq summary{list-style:none;cursor:pointer;padding:20px 0;font-size:var(--fs-lead);display:flex;
  justify-content:space-between;gap:24px}
details.faq summary::-webkit-details-marker{display:none}
details.faq summary::after{content:'+';font-weight:300;font-size:24px;line-height:1}
details.faq[open] summary::after{content:'\\2212'}
details.faq p{padding:0 0 22px;max-width:62ch;color:var(--grey)}

/* buy bar */
.buybar{position:sticky;bottom:0;z-index:50;background:rgb(255 255 255 / .94);backdrop-filter:blur(14px);
  border-top:1px solid var(--hair)}
.buybar .in{display:flex;align-items:center;gap:20px;padding:14px 0}

/* notes appendix */
.notes{background:var(--ink);color:#fafafa}
.notes .wrap{padding-top:80px;padding-bottom:96px}
.notes h2{margin:14px 0 8px}
.notes .grid2{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:34px}
.notes .card{border:1px solid var(--hair-ink);padding:24px}
.notes .card h3{font-size:15px;font-weight:var(--w-ui);margin-bottom:10px}
.notes .card p{font-size:14px;color:var(--grey-ink);line-height:1.6}
.notes table{width:100%;border-collapse:collapse;font-size:14px;margin-top:20px}
.notes th,.notes td{text-align:left;padding:12px 14px 12px 0;border-bottom:1px solid var(--hair-ink);vertical-align:top}
.notes th{font-weight:var(--w-ui)}
.notes td.ar{color:var(--lime);white-space:nowrap;font-variant-numeric:tabular-nums}

@media (max-width:980px){
  .hero .copy{grid-column:1 / -1;padding-bottom:0}
  .hero .stage{grid-column:1 / -1;padding:24px 0 56px}
  .map{grid-template-columns:1fr;gap:32px}
  .stats{grid-template-columns:repeat(2,1fr)}
  .stats>div{border-left:0;border-top:1px solid var(--hair);text-align:left}
  .fold,.notes .grid2{grid-template-columns:1fr;gap:32px}
  .acc,.cw{grid-template-columns:repeat(2,1fr)}
  .gal .w8,.gal .w4,.gal .w6{grid-column:span 12}
  header.site nav{display:none}
}
"""

# ---------------------------------------------------------------- fold diagram, drawn to scale
def fold_svg():
    s = 3.1                                   # px per cm
    L, D, H = 57.0, 37.5, 46.0                # folded: length, depth, height
    w, h = L*s, H*s
    dx, dy = D*s*0.52, -D*s*0.34              # isometric offset
    ox, oy = 60, 230                          # origin = front-bottom-left
    fx, fy = ox, oy
    P = lambda x, y: f"{x:.1f},{y:.1f}"
    front = f"{P(fx,fy)} {P(fx+w,fy)} {P(fx+w,fy-h)} {P(fx,fy-h)}"
    top   = f"{P(fx,fy-h)} {P(fx+w,fy-h)} {P(fx+w+dx,fy-h+dy)} {P(fx+dx,fy-h+dy)}"
    side  = f"{P(fx+w,fy)} {P(fx+w+dx,fy+dy)} {P(fx+w+dx,fy-h+dy)} {P(fx+w,fy-h)}"
    # cabin bag, 55 x 40 cm, for scale
    bw, bh = 55*s, 40*s
    bx, by = ox+w+dx+64, oy
    return f"""<svg viewBox="0 0 760 300" role="img" aria-label="The folded trolley, 37.5 by 57 by 46 centimetres, drawn to scale beside a 55 by 40 centimetre cabin bag">
  <g fill="none" stroke="#fafafa" stroke-width="1.6" stroke-linejoin="round">
    <polygon points="{front}" fill="rgb(168 255 74 / .10)"/>
    <polygon points="{top}"/><polygon points="{side}"/>
  </g>
  <g stroke="#a8ff4a" stroke-width="1.4">
    <line x1="{ox}" y1="{oy+18}" x2="{ox+w}" y2="{oy+18}"/>
    <line x1="{ox-18}" y1="{oy}" x2="{ox-18}" y2="{oy-h}"/>
    <line x1="{ox+w+6}" y1="{oy+12}" x2="{ox+w+dx+6}" y2="{oy+dy+12}"/>
  </g>
  <g fill="#a8ff4a" font-family="'Manrope',sans-serif" font-size="12" font-weight="500" letter-spacing="1.4">
    <text x="{ox+w/2:.0f}" y="{oy+36:.0f}" text-anchor="middle">57 CM</text>
    <text x="{ox-26:.0f}" y="{oy-h/2:.0f}" text-anchor="end" dominant-baseline="middle">46 CM</text>
    <text x="{ox+w+dx/2+22:.0f}" y="{oy+dy+30:.0f}">37.5 CM</text>
  </g>
  <g fill="none" stroke="rgb(250 250 250 / .30)" stroke-width="1.2" stroke-dasharray="4 4">
    <rect x="{bx:.0f}" y="{by-bh:.0f}" width="{bw:.0f}" height="{bh:.0f}" rx="6"/>
    <path d="M{bx+bw*0.36:.0f} {by-bh:.0f} v-14 h{bw*0.28:.0f} v14"/>
  </g>
  <text x="{bx+bw/2:.0f}" y="{by+24:.0f}" text-anchor="middle" fill="#9a9ea6"
        font-family="'Manrope',sans-serif" font-size="11" letter-spacing="1.4">CABIN BAG 55 × 40, FOR SCALE</text>
</svg>"""

# ---------------------------------------------------------------- markup helpers
eyebrow = lambda n, t: f'<div class="eyebrow"><b>{n}</b>{t}</div>'
def display(lines, cls='display'):
    return f'<h2 class="{cls}">' + "".join(f'<span style="display:block">{l}</span>' for l in lines) + '</h2>'

def build():
    cw_buttons = "".join(
        f'<button data-cw="{c["id"]}" aria-label="{c["name"]}" aria-pressed="{"true" if i==0 else "false"}" '
        f'style="background:linear-gradient(135deg,{c["a"]} 0 50%,{c["b"]} 50% 100%)"></button>' for i, c in enumerate(COLOURWAYS))
    cw_slots = "".join(f'<div class="slot{" on" if i==0 else ""}" data-cw="{c["id"]}">'
                       f'<img src="{c["img"]}" alt="Wishbone CUBE three in {c["name"]}" '
                       f'{"" if i==0 else "loading=lazy"}></div>' for i, c in enumerate(COLOURWAYS))
    idx = "".join(f'<li data-cw="{c["id"]}" class="{"on" if i==0 else ""}">{str(i+1).zfill(2)}</li>'
                  for i, c in enumerate(COLOURWAYS))

    spots = "".join(f'<button class="spot" data-i="{i}" style="left:{s["x"]}%;top:{s["y"]}%" '
                    f'aria-pressed="{"true" if i==0 else "false"}" aria-label="{s["t"]}">{s["n"]}</button>'
                    for i, s in enumerate(HOTSPOTS))
    featlist = "".join(f'<li><button data-i="{i}" aria-pressed="{"true" if i==0 else "false"}">'
                       f'<span class="n">{s["n"]}</span><span>{s["t"]}</span></button></li>'
                       for i, s in enumerate(HOTSPOTS))

    stats = "".join(f'<div><div class="v">{v}{f"<small>{u}</small>" if u else ""}</div><div class="k label grey">{k}</div></div>'
                    for v, u, k in [('7.65','kg','net weight'),('57','cm','folded, longest side'),
                                    ('4','','Quick Lok bases'),('3','','colourways'),('249','€','RRP')])

    cws = "".join(f'''<figure>
      <img src="{c['img']}" alt="Wishbone CUBE three in {c['name']}" loading="lazy">
      <figcaption style="margin-top:18px">
        <div class="label"><span class="chip" style="background:linear-gradient(135deg,{c['a']} 0 50%,{c['b']} 50% 100%)"></span>{c['name']}</div>
        <div class="grey" style="font-size:13px;margin-top:10px;font-variant-numeric:tabular-nums">SKU {c['sku']}<br>EAN {c['ean']}</div>
      </figcaption></figure>''' for c in COLOURWAYS)

    head = "".join(f'<th class="{"hi" if m["id"]=="THREE" else ""}"><img src="{m["img"]}" alt="Wishbone {m["name"]}" loading="lazy">'
                   f'<div class="label">{m["name"]}</div>'
                   f'<div class="grey" style="font-weight:600;margin-top:6px">{m["price"]}</div></th>' for m in COMPARE['models'])
    rows = ""
    for label, vals in COMPARE['rows']:
        cells = "".join(
            f'<td class="{"hi " if m["id"]=="THREE" else ""}{"na" if not vals.get(m["id"]) else ""}">{vals.get(m["id"]) or "—"}</td>'
            for m in COMPARE['models'])
        rows += f'<tr><th style="font-weight:500">{label}</th>{cells}</tr>'

    accs = "".join(f'<a href="#"><img src="{img}" alt="{n}" loading="lazy">'
                   f'<div class="label" style="font-size:11px">{n}</div>'
                   f'<div class="grey" style="font-size:13px">{p} · {sku}</div></a>' for n, p, sku, img in ACCESSORIES)

    specs = "".join(f'<tr><th>{k}</th><td>{v if v else "<span class=grey>— not recorded</span>"}</td></tr>' for k, v in SPECS)
    faqs  = "".join(f'<details class="faq"{" open" if i==0 else ""}><summary>{q}</summary><p>{a}</p></details>'
                    for i, (q, a) in enumerate(FAQ))
    notes = "".join(f'<div class="card"><h3>{t}</h3><p>{d}</p></div>' for t, d in NOTES)
    shots = "".join(f'<tr><th>{t}</th><td style="color:var(--grey-ink)">{d}</td><td class="ar">{r}</td></tr>'
                    for t, d, r in SHOTLIST)
    return dict(cw_buttons=cw_buttons, cw_slots=cw_slots, idx=idx, spots=spots, featlist=featlist,
                stats=stats, cws=cws, head=head, rows=rows, accs=accs, specs=specs, faqs=faqs,
                notes=notes, shots=shots, fold=fold_svg())

# ---------------------------------------------------------------- the page
HTML = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Wishbone CUBE three — push trolley</title>
<meta name="description" content="The Wishbone CUBE three folds to 37.5 × 57 × 46 cm and locks there. Dual-tube aluminium frame, 7.65 kg, four Quick Lok bases, Smart Organizer. 249 €.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600&family=DotGothic16&display=swap" rel="stylesheet">
<style>__TOKENS__ __CSS__</style></head><body>

<header class="site"><div class="wrap bar">
  <a href="/" aria-label="Wishbone Golf"><img src="__WORD__" alt="Wishbone Golf" style="height:13px;width:auto"></a>
  <nav class="label"><a href="#features">Trolleys</a><a href="#parts">Spare parts</a><a href="#accessories">Accessories</a><a href="#compare">Compare</a><a href="#faq">Support</a></nav>
  <a href="/cart" class="label">Cart (0)</a>
  <a class="btn btn--lime btn--sm" href="#buy">Buy the three <span aria-hidden="true">→</span></a>
</div></header>

<!-- 01 hero -->
<section class="hero"><div class="wrap grid">
  <div class="copy">
    __EYE_HERO__
    <h1 class="display display--hero"><span style="display:block">Three wheels.</span><span style="display:block">One cube.</span><span style="display:block">7.65 kg.</span></h1>
    <p class="lead grey" style="max-width:38ch">The CUBE three folds into 37.5 × 57 × 46 cm and locks there. A dual-tube aluminium frame, four Quick Lok bases and a Smart Organizer where your hands already are.</p>
    <div style="display:flex;align-items:baseline;gap:16px"><span class="price">249,00 €</span><span class="label grey">incl. VAT · 2–4 days</span></div>
    <div><div class="label grey" style="margin-bottom:10px">Colourway <span id="cwname" style="color:var(--ink)">Black / Lime</span></div>
      <div class="sw" id="sw">__CW_BUTTONS__</div></div>
    <div style="display:flex;gap:12px;flex-wrap:wrap">
      <a class="btn btn--lime" href="#buy">Add to cart <span aria-hidden="true">→</span></a>
      <a class="btn btn--out" href="#compare">Compare models <span aria-hidden="true">→</span></a></div>
    <ol class="idx label" id="idx">__IDX__</ol>
  </div>
  <div class="stage" id="stage">__CW_SLOTS__</div>
</div></section>

<!-- stat strip -->
<section style="border-bottom:1px solid var(--hair)"><div class="wrap"><div class="stats">__STATS__</div></div></section>

<!-- 02 feature map -->
<section class="band" id="features"><div class="wrap">
  __EYE_FEAT__
  __D_FEAT__
  <p class="grey" style="max-width:46ch;margin-top:16px">Eight things worth knowing, in the order you meet them. Pick a number.</p>
  <div class="map">
    <div class="plate"><img src="__HERO_BL__" alt="Wishbone CUBE three, feature map">__SPOTS__</div>
    <div>
      <div class="det" id="det">
        <img id="detimg" src="" alt="">
        <div class="label grey" id="detn">01</div>
        <h3 id="dett"></h3>
        <p class="grey" id="detd"></p>
      </div>
      <ul class="featlist" id="featlist">__FEATLIST__</ul>
    </div>
  </div>
</div></section>

<!-- 03 the fold — the one dark band -->
<section class="band band--ink"><div class="wrap">
  <div class="fold">
    <div>
      __EYE_FOLD__
      <h2 class="display" style="margin-top:18px"><span style="display:block">It folds to a cube.</span><span style="display:block">Then it locks.</span></h2>
      <p class="grey" style="max-width:40ch;margin-top:18px">CubeFold closes the frame in one movement and holds it shut, so the trolley does not spring open when you lift it into the boot. It locks open as well — the reason the dual-tube frame does not flex under a loaded bag.</p>
      <div class="dimrow">
        <div><div class="v">37.5</div><div class="label grey" style="margin-top:8px">cm deep</div></div>
        <div><div class="v">57</div><div class="label grey" style="margin-top:8px">cm long</div></div>
        <div><div class="v">46</div><div class="label grey" style="margin-top:8px">cm high</div></div>
      </div>
      <p class="grey" style="margin-top:22px;font-size:13px">Both rear wheels pull off without tools if you need it smaller still.</p>
      <div style="margin-top:28px"><a class="btn btn--lime" href="#buy">Add to cart · 249,00 € <span aria-hidden="true">→</span></a></div>
    </div>
    <div>__FOLD_SVG__</div>
  </div>
</div></section>

<!-- 04 organiser -->
<section class="band band--mist"><div class="wrap grid" style="align-items:center">
  <div style="grid-column:span 5;display:grid;gap:22px">
    __EYE_ORG__
    <h2 class="display"><span style="display:block">Everything you</span><span style="display:block">reach for, on top.</span></h2>
    <p class="grey" style="max-width:36ch">The Smart Organizer sits across the handle, so a scorecard, a pencil, three tees and a ball are where your hands already are. You do not stop walking to use it.</p>
    <ul class="label grey" style="list-style:none;padding:0;display:grid;gap:12px;margin-top:6px">
      <li style="border-top:1px solid var(--hair);padding-top:12px">Scorecard holder</li>
      <li style="border-top:1px solid var(--hair);padding-top:12px">Pencil holder</li>
      <li style="border-top:1px solid var(--hair);padding-top:12px">Tee holder</li>
      <li style="border-top:1px solid var(--hair);padding-top:12px">Ball recesses</li>
      <li style="border-top:1px solid var(--hair);padding-top:12px">Integrated bottle holder</li>
    </ul>
  </div>
  <div style="grid-column:7 / span 6"><img src="__DET_ORG__" alt="The Smart Organizer console"></div>
</div></section>

<!-- 05 wheels -->
<section class="band"><div class="wrap grid" style="align-items:center">
  <div style="grid-column:span 6"><img src="__DET_REAR__" alt="The rear wheel and footbrake" style="background:var(--mist)"></div>
  <div style="grid-column:8 / span 5;display:grid;gap:22px">
    __EYE_WHEEL__
    <h2 class="display"><span style="display:block">29 at the back.</span><span style="display:block">24 at the front.</span></h2>
    <p class="grey" style="max-width:36ch">Large rear wheels carry the load and roll over wet ground rather than cutting into it. The front wheel is fixed, not swivelled — it tracks straight across a slope instead of wandering. Press the footbrake at the axle to park.</p>
    <div style="display:flex;gap:12px"><img src="__DET_FRONT__" alt="The front wheel" style="width:48%;background:var(--mist)"><img src="__DET_FRAME__" alt="The dual-tube frame" style="width:48%;background:var(--mist)"></div>
  </div>
</div></section>

<!-- 06 on the course -->
<section class="band band--tight" style="padding-top:72px"><div class="wrap">
  __EYE_COURSE__
  <h2 class="display" style="margin:18px 0 32px"><span style="display:block">On the course,</span><span style="display:block">where it is judged.</span></h2>
  <div class="gal">
    <figure class="w8 h1"><img src="__L2__" alt="The CUBE three on the fairway"></figure>
    <figure class="w4 h1"><img src="__L1__" alt="The CUBE three, three-quarter view on grass"></figure>
    <figure class="w6 h2"><img src="__L3__" alt="The CUBE three loaded with a cart bag"></figure>
    <figure class="w6 h2"><img src="__L6__" alt="A golfer taking a club from the bag"></figure>
    <figure class="w12 h3"><img src="__L4__" alt="A golfer pushing the CUBE three along the fairway"></figure>
  </div>
</div></section>

<!-- 07 colourways -->
<section class="band band--mist" id="buy"><div class="wrap">
  __EYE_CW__
  <h2 class="display" style="margin:18px 0 32px"><span style="display:block">Three colourways.</span></h2>
  <div class="cw">__CWS__</div>
</div></section>

<!-- 08 compare -->
<section class="band" id="compare"><div class="wrap">
  __EYE_CMP__
  <h2 class="display" style="margin:18px 0 8px"><span style="display:block">One, two or three.</span></h2>
  <p class="grey" style="max-width:48ch;margin-bottom:32px">An em dash means the figure is not recorded yet, not that the trolley does not do it.</p>
  <table class="cmp"><thead><tr><th style="width:24%"></th>__HEAD__</tr></thead><tbody>__ROWS__</tbody></table>
</div></section>

<!-- 09 accessories -->
<section class="band band--mist" id="accessories"><div class="wrap">
  __EYE_ACC__
  <h2 class="display" style="margin:18px 0 8px"><span style="display:block">Four bases.</span><span style="display:block">Click on what you want.</span></h2>
  <p class="grey" style="max-width:44ch;margin-bottom:32px">Every holder fits the Quick Lok bases on the frame, and every one of them fits the other models too.</p>
  <div class="acc">__ACCS__</div>
</div></section>

<!-- 10 spec -->
<section class="band" id="parts"><div class="wrap grid" style="align-items:start">
  <div style="grid-column:span 4;display:grid;gap:18px">
    __EYE_SPEC__
    <h2 class="display display--s"><span style="display:block">The whole</span><span style="display:block">specification.</span></h2>
    <p class="grey" style="font-size:14px">Taken from the Wishbone product record. Where a figure has not been measured, it says so.</p>
  </div>
  <div style="grid-column:6 / span 7"><table class="spec">__SPECS__</table></div>
</div></section>

<!-- 11 faq -->
<section class="band band--mist" id="faq"><div class="wrap grid" style="align-items:start">
  <div style="grid-column:span 4;display:grid;gap:18px">__EYE_FAQ__<h2 class="display display--s"><span style="display:block">Asked often.</span></h2></div>
  <div style="grid-column:6 / span 7;border-top:1px solid var(--hair)">__FAQS__</div>
</div></section>

<footer class="band band--tight" style="border-top:1px solid var(--hair)"><div class="wrap">
  <div class="grid" style="align-items:start">
    <div style="grid-column:span 4"><img src="__MONO__" alt="Wishbone" style="width:92px">
      <p class="grey" style="font-size:13px;margin-top:16px;max-width:28ch">Birthed in Britain. Ultra-light aluminium golf trolleys and every part to keep them rolling.</p></div>
    <div style="grid-column:span 2"><div class="label" style="margin-bottom:14px">Trolleys</div>
      <ul class="grey" style="list-style:none;padding:0;display:grid;gap:8px;font-size:13px"><li>Wishbone ONE</li><li>CUBE two</li><li>CUBE three</li><li>NEO</li><li>EON</li></ul></div>
    <div style="grid-column:span 2"><div class="label" style="margin-bottom:14px">Spare parts</div>
      <ul class="grey" style="list-style:none;padding:0;display:grid;gap:8px;font-size:13px"><li>Parts for the three</li><li>Wheels</li><li>Brackets</li><li>Brake kit</li></ul></div>
    <div style="grid-column:span 2"><div class="label" style="margin-bottom:14px">Accessories</div>
      <ul class="grey" style="list-style:none;padding:0;display:grid;gap:8px;font-size:13px"><li>Umbrella holder</li><li>Drink holder</li><li>Scorecard holder</li><li>Carry bag set</li></ul></div>
    <div style="grid-column:span 2"><div class="label" style="margin-bottom:14px">Company</div>
      <ul class="grey" style="list-style:none;padding:0;display:grid;gap:8px;font-size:13px"><li>About</li><li>Contact</li><li>Shipping</li><li>Warranty</li></ul></div>
  </div>
  <hr class="hairline" style="margin:40px 0 20px">
  <div class="label grey" style="display:flex;justify-content:space-between;flex-wrap:wrap;gap:16px">
    <span>© 2026 Wishbone Golf. All rights reserved.</span><span>Instagram · YouTube · Facebook</span></div>
</div></footer>

<div class="buybar"><div class="wrap in">
  <img src="__HERO_BL__" alt="" style="width:44px;height:44px;object-fit:contain">
  <div><div class="label">Wishbone CUBE three</div><div class="grey" style="font-size:13px" id="barcw">Black / Lime · 7.65 kg</div></div>
  <div style="margin-left:auto;display:flex;align-items:center;gap:18px">
    <span class="price" style="font-size:20px">249,00 €</span>
    <a class="btn btn--lime" href="#">Add to cart <span aria-hidden="true">→</span></a></div>
</div></div>

<!-- appendix, not part of the page -->
<section class="notes"><div class="wrap">
  <div class="eyebrow" style="color:var(--lime)"><b>★</b>Not part of the page — notes for the owner</div>
  <h2 class="display" style="margin-top:16px"><span style="display:block">What building this</span><span style="display:block">turned up.</span></h2>
  <div class="grid2">__NOTES__</div>
  <h3 class="label" style="margin:56px 0 0">Higgsfield shot list — ready to run</h3>
  <p class="grey" style="font-size:14px;margin-top:10px;max-width:70ch">Eight generations that would finish this page, in priority order. Each one references the studio PNG (2048 px, transparent) so the geometry and the colourway stay true.</p>
  <table>__SHOTS__</table>
</div></section>

<script>
var CW = __CW_JSON__, SP = __SP_JSON__, DET = __DET_JSON__;
function setCw(id){
  document.querySelectorAll('#stage .slot').forEach(function(s){ s.classList.toggle('on', s.dataset.cw===id) });
  document.querySelectorAll('#sw button').forEach(function(b){ b.setAttribute('aria-pressed', String(b.dataset.cw===id)) });
  document.querySelectorAll('#idx li').forEach(function(l){ l.classList.toggle('on', l.dataset.cw===id) });
  var c = CW.filter(function(x){return x.id===id})[0];
  if(c){ document.getElementById('cwname').textContent = c.name;
         document.getElementById('barcw').textContent = c.name + ' · 7.65 kg'; }
}
document.querySelectorAll('#sw button, #idx li').forEach(function(el){
  el.addEventListener('click', function(){ setCw(el.dataset.cw) }) });

function setSpot(i){
  var s = SP[i];
  document.getElementById('detimg').src = DET[s.img];
  document.getElementById('detimg').alt = s.t;
  document.getElementById('detn').textContent = s.n;
  document.getElementById('dett').textContent = s.t;
  document.getElementById('detd').textContent = s.d;
  document.querySelectorAll('.spot').forEach(function(b){ b.setAttribute('aria-pressed', String(+b.dataset.i===i)) });
  document.querySelectorAll('#featlist button').forEach(function(b){ b.setAttribute('aria-pressed', String(+b.dataset.i===i)) });
}
document.querySelectorAll('.spot, #featlist button').forEach(function(b){
  b.addEventListener('click', function(){ setSpot(+b.dataset.i) });
  b.addEventListener('mouseenter', function(){ if(b.classList.contains('spot')) setSpot(+b.dataset.i) });
});
setSpot(0);
</script>
</body></html>"""

def main():
    B = build()
    out = (HTML
      .replace('__TOKENS__', tokens).replace('__CSS__', CSS)
      .replace('__WORD__', WORD).replace('__MONO__', MONO)
      .replace('__EYE_HERO__', eyebrow('01','Wishbone CUBE three'))
      .replace('__EYE_FEAT__', eyebrow('02','Every feature'))
      .replace('__D_FEAT__', display(['Eight reasons it is','fifty euros more.']))
      .replace('__EYE_FOLD__', eyebrow('03','CubeFold'))
      .replace('__EYE_ORG__', eyebrow('04','Smart Organizer'))
      .replace('__EYE_WHEEL__', eyebrow('05','Wheels and brake'))
      .replace('__EYE_COURSE__', eyebrow('06','On the course'))
      .replace('__EYE_CW__', eyebrow('07','Colourways'))
      .replace('__EYE_CMP__', eyebrow('08','Compare'))
      .replace('__EYE_ACC__', eyebrow('09','Accessories'))
      .replace('__EYE_SPEC__', eyebrow('10','Specification'))
      .replace('__EYE_FAQ__', eyebrow('11','Questions'))
      .replace('__CW_BUTTONS__', B['cw_buttons']).replace('__CW_SLOTS__', B['cw_slots']).replace('__IDX__', B['idx'])
      .replace('__STATS__', B['stats']).replace('__SPOTS__', B['spots']).replace('__FEATLIST__', B['featlist'])
      .replace('__FOLD_SVG__', B['fold']).replace('__CWS__', B['cws'])
      .replace('__HEAD__', B['head']).replace('__ROWS__', B['rows']).replace('__ACCS__', B['accs'])
      .replace('__SPECS__', B['specs']).replace('__FAQS__', B['faqs'])
      .replace('__NOTES__', B['notes']).replace('__SHOTS__', B['shots'])
      .replace('__HERO_BL__', IMG['bl'])
      .replace('__L1__', IMG['l1']).replace('__L2__', IMG['l2']).replace('__L3__', IMG['l3'])
      .replace('__L4__', IMG['l4']).replace('__L6__', IMG['l6'])
      .replace('__DET_ORG__', DET['organizer']).replace('__DET_REAR__', DET['rearwheel'])
      .replace('__DET_FRONT__', DET['frontwheel']).replace('__DET_FRAME__', DET['frame'])
      .replace('__CW_JSON__', json.dumps([{'id':c['id'],'name':c['name']} for c in COLOURWAYS]))
      .replace('__SP_JSON__', json.dumps(HOTSPOTS))
      .replace('__DET_JSON__', json.dumps(DET)))
    dest = pathlib.Path('/tmp/wb/kit/wishbone-cube-three.html'); dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(out)
    print('wrote', dest, round(len(out)/1024), 'KB ·', len(HOTSPOTS), 'hotspots ·', len(SHOTLIST), 'shots queued')

if __name__ == '__main__':
    main()
