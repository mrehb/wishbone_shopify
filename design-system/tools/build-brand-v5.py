#!/usr/bin/env python3
"""Wishbone v5 — brand direction. One self-contained HTML page, stdlib only.
Run tools/render-v5-shots.py first (it needs Pillow); this only reads what it wrote."""
import base64, json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT/'tools')); import dotmatrix as dm
V = ROOT/'assets'/'v5'; SH = V/'shots'
def b64(p, mime): return f"data:{mime};base64," + base64.b64encode(p.read_bytes()).decode()
shot = lambda n: b64(SH/f'{n}-web.jpg', 'image/jpeg')
webp = lambda n: b64(V/f'{n}.webp', 'image/webp')
dots = lambda n: (V/f'{n}-dots.svg').read_text().replace('<svg ', '<svg class="portrait" ', 1)
ANCH = json.loads((SH/'anchors.json').read_text())
WORD = b64(ROOT/'assets'/'wishbone-wordmark.png', 'image/png')
WORD_INK = b64(ROOT/'assets'/'wishbone-wordmark-ink.png', 'image/png')

INK, PAPER, LIME = '#0F1014', '#FFFFFF', '#CBE832'
D = lambda t, on=INK, off=None, cls='dm': dm.svg(t, on=on, off=off, cls=cls)

def callouts(name, labels):
    """labels: {part: (text, side)} — anchors come from the renderer, so they sit on the real part."""
    out = ""
    for part, (text, side) in labels.items():
        x, y = ANCH[name][part]
        out += f'<span class="co co--{side}" style="left:{x}%;top:{y}%"><i></i><b>{text}</b></span>'
    return out

def dimple_ball():
    """A golf ball is a field of dots. Drawn, not photographed."""
    import math
    c, R, out = 120, 108, []
    for ring in range(0, 12):
        r = ring*9.5
        n = max(1, int(2*math.pi*r/10.5))
        for k in range(n):
            a = 2*math.pi*k/n + ring*.35
            x, y = c + r*math.cos(a), c + r*math.sin(a)
            if math.hypot(x-c, y-c) < R-6:
                shade = 1 - (math.hypot(x-c+30, y-c+34)/(R*1.9))
                out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{3.2*max(.35, min(1, shade+.3)):.2f}"/>')
    return (f'<svg viewBox="0 0 240 240" class="ball"><circle cx="{c}" cy="{c}" r="{R}" fill="#F4F4F5"/>'
            f'<g fill="#BFC1C6">{"".join(out)}</g></svg>')

def range_card(img, name, price, line, fact):
    return f'''<article class="rc"><img src="{shot(img)}" alt="Wishbone {name}" loading="lazy">
      <div class="rc-b"><div class="rc-n">{D(name)}</div>
      <div class="rc-f"><span class="ro">{price}</span><span class="ro grey">{fact}</span></div>
      <p>{line}</p></div></article>'''

HTML = r"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Wishbone — brand direction v5</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700&family=DotGothic16&display=swap" rel="stylesheet">
<style>
:root{--ink:#0F1014;--graphite:#2A2C31;--concrete:#D4D5D8;--mist:#EDEDEF;--paper:#FFFFFF;--lime:#CBE832;
--signal:#E03828;--cobalt:#3B82F0;--grey:#6B7075;--hair:#E4E4E7;--font:'Manrope',system-ui,sans-serif;--ro:'DotGothic16',ui-monospace,monospace}
*{box-sizing:border-box;margin:0}html{scroll-behavior:smooth}
body{font:400 16px/1.6 var(--font);color:var(--ink);background:var(--paper);-webkit-font-smoothing:antialiased}
img{display:block;max-width:100%}
.w{max-width:1320px;margin:0 auto;padding:0 40px}
section{padding:120px 0;position:relative}
.ink{background:var(--ink);color:var(--paper)}.lime{background:var(--lime)}.concrete{background:var(--concrete)}.mist{background:var(--mist)}
.ro{font-family:var(--ro);font-size:13px;letter-spacing:.08em;text-transform:uppercase;-webkit-font-smoothing:none}
.grey{color:var(--grey)}.ink .grey{color:#8A8E96}
.kick{display:flex;gap:14px;align-items:center;margin-bottom:28px}.kick .dot{width:10px;height:10px;border-radius:50%;background:var(--lime)}
.lime .kick .dot{background:var(--ink)}
h1,h2{font-weight:300;letter-spacing:-.01em;line-height:1.02}
h2{font-size:clamp(40px,5.4vw,76px)}h3{font-size:22px;font-weight:600;letter-spacing:-.005em}
.lead{font-size:21px;line-height:1.5;max-width:40ch;font-weight:400}
.g{display:grid;grid-template-columns:repeat(12,1fr);gap:24px}
.dm{display:block;width:100%;height:auto}
.hair{border-top:1px solid var(--hair)}.ink .hair{border-color:#2A2C31}
/* cover */
.cover{min-height:100vh;display:flex;flex-direction:column;justify-content:space-between;padding:32px 0 48px;overflow:hidden}
.bar{display:flex;justify-content:space-between;align-items:center}
.bar img{height:22px;width:auto}
.cover .big{margin:9vh 0 4vh}
.cover .claim{font-size:clamp(28px,3.4vw,48px);font-weight:300;line-height:1.1}
.cover .claim b{font-weight:600}
/* numbers */
.vs{display:grid;grid-template-columns:1fr 1fr;gap:0;margin-top:64px;border:1px solid var(--hair)}
.vs>div{padding:40px}.vs>div+div{border-left:1px solid var(--hair);background:var(--ink);color:var(--paper)}
.row-dots{display:flex;gap:10px;flex-wrap:wrap;margin:22px 0 26px}.row-dots i{width:22px;height:22px;border-radius:50%;background:#C9CBD0}
.vs>div+div .row-dots i{background:var(--lime)}
.facts{list-style:none;padding:0;display:grid;gap:10px}.facts li{display:flex;justify-content:space-between;gap:20px;border-top:1px solid var(--hair);padding-top:10px}
.vs>div+div .facts li{border-color:#2A2C31}
.facts span:last-child{font-weight:600;text-align:right}
.ledger{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:64px}
.ledger>div{padding:28px;border:1px solid var(--hair)}.ledger ul{padding-left:18px;margin-top:12px;display:grid;gap:8px;font-size:15px}
.ledger .ok{border-top:4px solid var(--lime)}.ledger .chk{border-top:4px solid #F3B33D}.ledger .no{border-top:4px solid var(--ink)}
/* idea */
.manifesto{font-size:clamp(48px,8.4vw,132px);font-weight:600;line-height:.95;letter-spacing:-.03em}
.pr{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:80px}.pr>div{border-top:2px solid var(--ink);padding-top:20px}
.pr p{margin-top:10px;font-size:15px}
.voice{display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-top:64px}
.voice>div{background:rgba(15,16,20,.06);padding:28px}.voice p{font-size:19px;margin-top:10px;line-height:1.4}
.voice .x p{text-decoration:line-through;text-decoration-thickness:1px;color:rgba(15,16,20,.55)}
/* dot */
.src{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:64px}
.src figure{background:#16181D;padding:0;overflow:hidden}.src figure .im{aspect-ratio:1;display:flex;align-items:center;justify-content:center;background:#E7E8EA}
.src figure .im img{width:100%;height:100%;object-fit:cover}.src .ball{width:78%}
.src figcaption{padding:20px 22px}.src figcaption p{font-size:15px;color:#B9BCC2;margin-top:6px}
.rule{margin-top:88px;display:grid;grid-template-columns:5fr 7fr;gap:48px;align-items:center}
.rule .big{font-size:clamp(34px,3.8vw,54px);font-weight:300;line-height:1.08}
.facts-dm{display:grid;gap:28px}
.spec{margin-top:88px;background:#16181D;padding:40px}
.tiers{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:40px}
.tiers>div{border-top:1px solid #2A2C31;padding-top:16px}.tiers .s{font-size:15px;color:#B9BCC2;margin-top:6px}
.portraits{display:grid;grid-template-columns:repeat(6,1fr);gap:16px;margin-top:40px}
.portrait{width:100%;height:auto;fill:var(--lime)}
/* colour */
.sw{display:grid;grid-template-columns:repeat(7,1fr);gap:12px;margin-top:48px}
.sw div{aspect-ratio:3/4;padding:14px;display:flex;flex-direction:column;justify-content:flex-end;font-size:13px}
.sw b{font-weight:600;display:block}
.pairs{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:48px}
.pairs figure img{width:100%}.pairs figcaption{margin-top:12px;font-size:14px}
.law{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:56px}.law>div{border-top:2px solid var(--ink);padding-top:16px}
.law p{font-size:15px;margin-top:8px}
/* shot */
.anat{display:grid;grid-template-columns:6fr 6fr;gap:56px;align-items:center;margin-top:64px}
.layers{list-style:none;padding:0;counter-reset:l}.layers li{display:grid;grid-template-columns:48px 1fr;gap:14px;border-top:1px solid rgba(15,16,20,.18);padding:16px 0}
.layers li::before{counter-increment:l;content:counter(l,decimal-leading-zero);font-family:var(--ro);font-size:14px}
.layers b{display:block;font-weight:600}.layers span{font-size:15px}
.stagebox{position:relative}.stagebox img{width:100%}
.co{position:absolute;width:0;height:0}
.co i{position:absolute;left:-6px;top:-6px;width:12px;height:12px;border-radius:50%;background:var(--ink);box-shadow:0 0 0 3px rgba(255,255,255,.75)}
.co::before{content:"";position:absolute;top:0;height:1px;width:64px;background:var(--ink)}
.co b{position:absolute;top:-10px;white-space:nowrap;font-family:var(--ro);font-weight:400;font-size:13px;letter-spacing:.08em;background:var(--ink);color:var(--paper);padding:3px 7px;-webkit-font-smoothing:none}
.co--r::before{left:6px}.co--r b{left:70px}.co--l::before{right:6px}.co--l b{right:70px}
.co--w i{background:var(--paper);box-shadow:0 0 0 3px rgba(15,16,20,.6)}.co--w::before{background:var(--paper)}.co--w b{background:var(--paper);color:var(--ink)}
.gallery{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:48px}
.dd{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:48px}
.dd figure{position:relative}.dd figcaption{margin-top:12px;font-size:14px}
.dd .tag{position:absolute;top:12px;left:12px;font-family:var(--ro);font-size:12px;padding:3px 8px;background:var(--lime);color:var(--ink)}
.dd .tag.x{background:var(--ink);color:var(--paper)}
.brief{display:grid;grid-template-columns:repeat(2,1fr);gap:24px;margin-top:64px}
.brief>div{background:var(--paper);padding:28px}.brief ol,.brief ul{padding-left:20px;margin-top:12px;display:grid;gap:8px;font-size:15px}
/* applications */
.browser{background:#1A1C21;padding:10px;margin-top:56px}
.browser .top{display:flex;gap:7px;padding:4px 6px 12px}.browser .top i{width:10px;height:10px;border-radius:50%;background:#3A3D44}
.site{background:var(--paper);overflow:hidden}
.nav{display:flex;justify-content:space-between;align-items:center;padding:20px 32px;font-size:14px;font-weight:500}
.nav img{height:18px}.nav .l{display:flex;gap:28px}
.hero{display:grid;grid-template-columns:5fr 7fr;background:var(--lime);min-height:620px}
.hero .t{padding:64px 48px;display:flex;flex-direction:column;justify-content:space-between}
.hero h1{font-size:clamp(40px,4.4vw,68px);font-weight:600;letter-spacing:-.03em;line-height:.98}
.btn{display:inline-flex;gap:10px;align-items:center;background:var(--ink);color:var(--paper);padding:15px 22px;font-weight:600;font-size:15px;text-decoration:none}
.strip{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid rgba(15,16,20,.2)}
.strip>div{padding:18px 20px;border-right:1px solid rgba(15,16,20,.2)}
.rangegrid{display:grid;grid-template-columns:repeat(5,1fr);gap:0;background:var(--paper)}
.rc img{width:100%;aspect-ratio:4/5;object-fit:cover}
.rc-b{padding:20px 18px 26px;border-right:1px solid var(--hair)}.rc-n{width:62%}
.rc-f{display:flex;justify-content:space-between;margin:14px 0 10px}.rc p{font-size:14px;color:var(--grey)}
.pdp{display:grid;grid-template-columns:7fr 5fr;background:var(--ink);color:var(--paper)}
.pdp .t{padding:56px 44px;display:flex;flex-direction:column;gap:22px;justify-content:center}
.pdp h3{font-size:40px;font-weight:300}
.social{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:40px}
.post{position:relative}.post img{width:100%}
.post .ov{position:absolute;left:6%;right:6%;bottom:6%;display:flex;justify-content:space-between;align-items:flex-end}
.post .ov .dm{width:46%}.post .ov small{font-size:12px;font-weight:600;max-width:20ch;text-align:right}
.teaser{background:#000;padding:120px 40px;text-align:center;overflow:hidden}
.teaser .dm{max-width:1000px;margin:0 auto}
.teaser .dm circle:not([fill]){opacity:0;animation:on .01s forwards}
@keyframes on{to{opacity:1}}
@media (prefers-reduced-motion:reduce){.teaser .dm circle:not([fill]){opacity:1;animation:none}}
.tbl{width:100%;border-collapse:collapse;margin-top:48px;font-size:15px}
.tbl th,.tbl td{text-align:left;padding:16px 12px;border-top:1px solid var(--hair);vertical-align:top}
.tbl th{font-weight:600;width:22%}.tbl td:nth-child(2){color:var(--grey)}
.next{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;margin-top:56px}
.next>div{border-top:1px solid #2A2C31;padding-top:18px}.next p{font-size:15px;color:#B9BCC2;margin-top:8px}
.src-list{font-size:13px;margin-top:48px}.src-list a{color:inherit}
@media (max-width:900px){.w{padding:0 20px}section{padding:72px 0}.vs,.voice,.anat,.rule,.hero,.pdp,.brief{grid-template-columns:1fr}
.vs>div+div{border-left:0}.ledger,.pr,.src,.law,.tiers,.social,.next{grid-template-columns:1fr}.sw{grid-template-columns:repeat(4,1fr)}
.pairs,.gallery,.dd{grid-template-columns:repeat(2,1fr)}.rangegrid{grid-template-columns:repeat(2,1fr)}.portraits{grid-template-columns:repeat(3,1fr)}}
</style></head><body>

<!-- COVER -->
<section class="cover ink"><div class="w" style="width:100%">
  <div class="bar"><img src="__WORD__" alt="Wishbone"><span class="ro grey">Brand direction v5 · 22.09.2026 · not approved</span></div>
  <div class="big">__COVER_DM__</div>
  <div class="g" style="align-items:end">
    <p class="claim" style="grid-column:span 8">Everything you need.<br><b>Nothing you don't.</b></p>
    <p class="grey" style="grid-column:10/span 3;font-size:15px">A direction for the whole Wishbone range — five trolleys today, an electric cart in 2027 — and the case for taking on PowaKaddy with it.</p>
  </div>
</div></section>

<!-- 01 THE MOVE -->
<section><div class="w">
  <div class="kick"><span class="dot"></span><span class="ro">The move</span></div>
  <h2>They sell screens.<br>We sell the trolley.</h2>
  <p class="lead" style="margin-top:28px">PowaKaddy is the more attackable of the two. Motocaddy owns scale — “the world’s #1 electric trolley brand”. PowaKaddy owns a feature race: GPS, touchscreens, “world’s first” claims, and a range too long to explain. A brand that does five trolleys well is the clearest possible answer to that.</p>
  <div class="vs">
    <div><div class="ro grey">PowaKaddy · on its homepage, Sept 2026</div>
      <div class="row-dots">__PK_DOTS__</div>
      <ul class="facts">
        <li><span>Trolleys in the range</span><span>13</span></li>
        <li><span>Electric models</span><span>10</span></li>
        <li><span>Flagship claim</span><span>“World’s first 5″ folding touchscreen GPS trolley”</span></li>
        <li><span>Push trolleys</span><span>£179.99 – £229.99 · 6.8 – 7.5 kg</span></li>
        <li><span>Electric trolleys</span><span>from £599 · 9.6 – 9.9 kg</span></li></ul></div>
    <div><div class="ro grey">Wishbone · Product Bay</div>
      <div class="row-dots">__WB_DOTS__</div>
      <ul class="facts">
        <li><span>Trolleys in the range</span><span>5</span></li>
        <li><span>Electric models</span><span>2 · EON, NEO</span></li>
        <li><span>What we lead with</span><span>The trolley itself</span></li>
        <li><span>Push trolleys</span><span>199 – 249 € · ONE under 4 kg*</span></li>
        <li><span>Electric trolleys</span><span>799 € · 999 €</span></li></ul></div>
  </div>
  <div class="ledger">
    <div class="ok"><h3>Say it now</h3><ul><li>Five trolleys. That’s the range.</li><li>TWO 6.9 kg · 199 €. THREE 7.65 kg · 249 €.</li><li>THREE folds to 37.5 × 57 × 46 cm and locks there.</li><li>EON comes with battery, charger, umbrella and scorecard holder.</li></ul></div>
    <div class="chk"><h3>Confirm first</h3><ul><li><b>ONE “under 4 kg”</b> — Product Bay’s own copy says so (frame 2,350 g), but there is no net-weight field. If it holds, it is the sharpest line we have: PowaKaddy’s lightest push trolley is 6.8 kg.</li><li>Any price comparison — ours are € RRPs, theirs are £ press prices.</li><li>NEO: 999 € in Product Bay, not sold on the storefront.</li></ul></div>
    <div class="no"><h3>Never say</h3><ul><li>“Lighter than PowaKaddy” for the TWO or THREE — it isn’t (6.8 kg vs 6.9 / 7.65).</li><li>“Cheaper” for the electrics — 799 € is not below their £599 entry model.</li><li>Anything about screens, apps or GPS we haven’t checked on the EON and NEO.</li></ul></div>
  </div>
</div></section>

<!-- 02 THE IDEA -->
<section class="lime"><div class="w">
  <div class="kick"><span class="dot"></span><span class="ro">The idea</span></div>
  <p class="manifesto">Everything you need.<br>Nothing you don’t.</p>
  <div class="pr">
    <div><h3>Essential</h3><p>Every part earns its place. If a feature needs explaining, it had better be worth it. That is the whole product brief and the whole brand.</p></div>
    <div><h3>Honest</h3><p>Facts, not adjectives. Every number we print is measured and on record. “Lightweight” is a claim; “6.9 kg” is a fact.</p></div>
    <div><h3>Considered</h3><p>Entry price is not an excuse. The colour, the fold, the dot on the e — the details are where a fair price proves it is not a cheap one.</p></div>
  </div>
  <div class="voice">
    <div><span class="ro">Sounds like Wishbone</span><p>Five trolleys. That’s the range.</p><p>Folds. Locks. Goes in the boot.</p><p>249 €. Everything included that you’ll use.</p></div>
    <div class="x"><span class="ro">Doesn’t</span><p>Revolutionary next-generation trolley technology.</p><p>The ultimate premium golfing experience.</p><p>Innovative smart features for every golfer!</p></div>
  </div>
</div></section>

<!-- 03 THE DOT -->
<section class="ink"><div class="w">
  <div class="kick"><span class="dot"></span><span class="ro">The dot</span></div>
  <h2>The dot is already<br>on everything we make.</h2>
  <p class="lead grey" style="margin-top:28px">The dot-matrix type was a good instinct without a reason behind it. It has three.</p>
  <div class="src">
    <figure><div class="im">__BALL__</div><figcaption><h3>The ball</h3><p>A golf ball is a field of dimples. The game’s most essential object is already a dot matrix.</p></figcaption></figure>
    <figure><div class="im"><img src="__GRIP__" alt="The perforated handle grip of the Wishbone EON"></div><figcaption><h3>The grip</h3><p>The EON’s handle is perforated with dots. Real, on the product, in the render in Product Bay.</p></figcaption></figure>
    <figure><div class="im"><img src="__BADGE__" alt="The one badge on the Wishbone ONE, with the dot on its e"></div><figcaption><h3>The name</h3><p>Every model wordmark — one, three, eon — carries a dot on its e. The brand has been signing its products with a dot all along.</p></figcaption></figure>
  </div>
  <div class="rule">
    <p class="big">So the dot gets one job: <b style="font-weight:600;color:var(--lime)">it only ever states a fact.</b> Names, weights, sizes, prices. If it is set in dots, it is true and it is on record.</p>
    <div class="facts-dm">__FACTS_DM__</div>
  </div>
  <div class="spec">
    <div class="ro grey">Wishbone Dot — a 5 × 7 matrix of round dots, drawn, not a font file</div>
    <div style="margin-top:28px">__SPECIMEN__</div>
    <div class="tiers">
      <div><span class="ro" style="color:var(--lime)">Wishbone Dot</span><div class="s">Round dots, drawn as SVG. Model names, prices, weights, sizes — at 32 px and up. Round because the ball, the grip and the e are round.</div></div>
      <div><span class="ro" style="color:var(--lime)">DotGothic16</span><div class="s">Kept for small readouts under 16 px — labels, callouts, spec lines — where drawn dots would not resolve.</div></div>
      <div><span class="ro" style="color:var(--lime)">Manrope</span><div class="s">Everything that is said rather than measured: headlines, copy, buttons.</div></div>
    </div>
  </div>
  <div style="margin-top:88px"><div class="ro grey">Dot portraits — each dot sized by the real product photograph beneath it. A secondary graphic for packaging, social and the 2027 launch; never a replacement for the photo.</div>
  <div class="portraits">__PORTRAITS__</div></div>
</div></section>

<!-- 04 COLOUR -->
<section><div class="w">
  <div class="kick"><span class="dot"></span><span class="ro">Colour and fields</span></div>
  <h2>Never on white again.</h2>
  <p class="lead" style="margin-top:28px">White made every trolley look like a catalogue entry. The products are charcoal with one accent colour — so the field behind them does the work. Five core colours run the interface; the fields exist only behind products.</p>
  <div class="sw">
    <div style="background:var(--ink);color:#fff"><b>Ink</b>#0F1014</div><div style="background:var(--graphite);color:#fff"><b>Graphite</b>#2A2C31</div>
    <div style="background:var(--concrete)"><b>Concrete</b>#D4D5D8</div><div style="background:var(--mist)"><b>Mist</b>#EDEDEF</div>
    <div style="background:var(--lime)"><b>Lime</b>#CBE832</div><div style="background:var(--signal);color:#fff"><b>Signal</b>#E03828 · field only</div>
    <div style="background:var(--cobalt);color:#fff"><b>Cobalt</b>#3B82F0 · field only</div>
  </div>
  <div class="law">
    <div><h3>Tonal first</h3><p>A colourway goes on its own colour: lime on lime, red on signal, blue on cobalt. The trolley reads as its colourway before you see the badge.</p></div>
    <div><h3>Dark on light, light on dark</h3><p>Charcoal trolleys go on lime, concrete or a colour field. White trolleys go on ink or graphite. A charcoal trolley on ink disappears — see the don’ts.</p></div>
    <div><h3>Lime is a field, not a button</h3><p>v4 allowed lime once per view. v5 lets it fill the screen. The brand should be recognisable from a thumbnail by its colour alone.</p></div>
  </div>
  <div class="pairs">__PAIRS__</div>
</div></section>

<!-- 05 THE SHOT -->
<section class="concrete"><div class="w">
  <div class="kick"><span class="dot"></span><span class="ro">The product shot</span></div>
  <h2>We only make one kind of picture.<br>So it has to be the best one.</h2>
  <div class="anat">
    <div class="stagebox"><img src="__HERO_SHOT__" alt="The Wishbone THREE on a lime field">__HERO_CO__</div>
    <ol class="layers">
      <li><div><b>Field</b><span>Keyed to the colourway. Flat colour, never white.</span></div></li>
      <li><div><b>Light pool</b><span>A soft lift behind the product, so it sits in space rather than on paper.</span></div></li>
      <li><div><b>Floor</b><span>The bottom third darkens into a sweep. The product stands on something.</span></div></li>
      <li><div><b>Dot texture</b><span>The brand dot on a fine grid, fading out behind the product.</span></div></li>
      <li><div><b>Name</b><span>The model in Wishbone Dot, giant, tone on tone. Behind, never over.</span></div></li>
      <li><div><b>The product</b><span>The real photograph or render, cut out, with a contact shadow. Never generated, never retouched into something it is not.</span></div></li>
      <li><div><b>Callouts</b><span>Optional. Only facts, in DotGothic, pointing at the part that makes them true.</span></div></li>
    </ol>
  </div>
  <p style="margin-top:28px;font-size:15px;max-width:70ch">All of this is <code>tools/render-v5-shots.py</code>: one recipe, run over the real Product Bay cut-outs, writing finished 4:5, 1:1 and 16:9 images — plus the callout positions, so a label always lands on the right part.</p>
  <div class="gallery">__GALLERY__</div>
  <div class="dd">
    <figure><span class="tag">Do</span><img src="__DO1__" alt=""><figcaption>Tonal field, name behind, product owns the frame.</figcaption></figure>
    <figure><span class="tag">Do</span><img src="__DO2__" alt=""><figcaption>White trolley on ink. The colourway does the talking.</figcaption></figure>
    <figure><span class="tag x">Don’t</span><img src="__DONT1__" alt=""><figcaption>On white. This is the catalogue we are leaving.</figcaption></figure>
    <figure><span class="tag x">Don’t</span><img src="__DONT2__" alt=""><figcaption>Charcoal on ink. The trolley disappears.</figcaption></figure>
  </div>
  <div class="brief">
    <div><h3>Brief for the next shoot — and the 2027 cart</h3><ol>
      <li>Deliver cut-outs: transparent PNG, 4000 px, <b>no baked floor shadow</b> (the EON renders carry one; it had to be stripped).</li>
      <li>One camera for every model: three-quarter front-left, lens at a third of the trolley’s height, 85–100 mm. The range lines up only if the angle never changes.</li>
      <li>Every colourway, every model. Today the ONE and EON exist only as renders; the TWO and THREE as studio photos.</li>
      <li>Rim light on every charcoal frame, so it holds its edge on any field.</li></ol></div>
    <div><h3>The set, per model</h3><ul>
      <li>Hero — three-quarter, unfolded</li><li>Profile — straight side-on</li><li>Folded — standing, and in hand</li>
      <li>Details — wheel hub, badge with its dot, fold lock, brake, organiser or grip</li>
      <li>Film — 10 s of the fold, locked-off camera, for a loop</li></ul></div>
  </div>
</div></section>

<!-- 06 APPLICATIONS -->
<section><div class="w">
  <div class="kick"><span class="dot"></span><span class="ro">Applied</span></div>
  <h2>wishbone.golf, in v5.</h2>
  <div class="browser"><div class="top"><i></i><i></i><i></i></div><div class="site">
    <div class="nav"><img src="__WORD_INK__" alt="Wishbone"><div class="l"><span>Trolleys</span><span>Electric</span><span>Parts</span><span>Why Wishbone</span></div><span>Cart (0)</span></div>
    <div class="hero"><div class="t"><div><span class="ro">Wishbone THREE · 249 €</span><h1 style="margin-top:20px">Everything you need.<br>Nothing you don’t.</h1></div>
      <div><p style="max-width:34ch;margin-bottom:24px">Folds to 37.5 × 57 × 46 cm and locks there. 7.65 kg. Four accessory mounts, a Smart Organizer, a footbrake. That’s it.</p><a class="btn" href="#">Shop the THREE →</a></div></div>
      <div style="background:url(__HERO_WIDE__) center/cover"></div></div>
    <div class="strip">__STRIP__</div>
    <img src="__LINEUP__" alt="The Wishbone range: ONE, TWO, THREE, EON and NEO">
    <div class="rangegrid">__RANGE__</div>
    <p class="ro grey" style="padding:14px 18px;font-size:11px">* ONE weight from Wishbone’s own Product Bay copy — weigh one before it goes live.</p>
    <div class="pdp"><div class="stagebox"><img src="__PDP__" alt="Wishbone EON in white and red on ink">__PDP_CO__</div>
      <div class="t"><span class="ro" style="color:var(--lime)">Electric</span><div style="width:44%">__EON_DM__</div>
      <p style="color:#B9BCC2;max-width:34ch">Battery, charger, umbrella and scorecard holder in the box. Wheels come off. Electronic brake. One price.</p>
      <div style="width:40%">__EON_PRICE__</div><a class="btn" href="#" style="background:var(--lime);color:var(--ink);align-self:flex-start">Shop the EON →</a></div></div>
  </div></div>
  <div style="margin-top:96px"><div class="kick"><span class="dot"></span><span class="ro">Social · 1:1</span></div>
  <div class="social">__SOCIAL__</div></div>
</div></section>

<!-- 2027 -->
<section class="teaser"><div class="ro grey" style="margin-bottom:40px">The 2027 electric cart — a launch that starts as a display switching on</div>
  __TEASER__
  <p class="grey" style="margin-top:40px;font-size:15px">No render of the new cart exists yet, so nothing here pretends to show it. When it does, it gets the full recipe: field, pool, floor, dot, name, product.</p>
</section>

<!-- 07 WHAT CHANGES -->
<section><div class="w">
  <div class="kick"><span class="dot"></span><span class="ro">What changes from v4.1</span></div>
  <h2>Your calls.</h2>
  <table class="tbl">
    <tr><th>Lime</th><td>Once per view, as a button</td><td>A full field — behind products, whole bands, the homepage hero</td></tr>
    <tr><th>Red and blue</th><td>Red is a product colour only; no interface red</td><td>Still true for the interface. But signal red and cobalt become <b>photography fields</b> behind red and blue colourways — inside the product image, never as buttons or errors. Confirm this reading of the ruling.</td></tr>
    <tr><th>The dot</th><td>DotGothic16 for numbered eyebrows only</td><td>Wishbone Dot (round, drawn) for facts at display size; DotGothic16 for small readouts; eyebrows lose their numbers</td></tr>
    <tr><th>Product images</th><td>Studio white, multiplied onto mist</td><td>The six-layer recipe, never on white</td></tr>
    <tr><th>Page structure</th><td>Numbered sections, one per feature</td><td>A few big moments: the idea, the product, the facts, the colour</td></tr>
    <tr><th>Motion</th><td>Colour and opacity only, nothing loops</td><td>Adds one thing: dots switching on, like a display, once</td></tr>
  </table>
</div></section>

<section class="ink"><div class="w">
  <div class="kick"><span class="dot"></span><span class="ro">Next</span></div>
  <h2>If this is the direction.</h2>
  <div class="next">
    <div><span class="ro" style="color:var(--lime)">1 · Rulings</span><p>Lime as a field, red and cobalt as photography fields, the dot’s one job. Then v5 replaces v4.1 in the brand kit.</p></div>
    <div><span class="ro" style="color:var(--lime)">2 · The ONE’s weight</span><p>Weigh one. If “under 4 kg” holds, it leads the attack.</p></div>
    <div><span class="ro" style="color:var(--lime)">3 · One shoot</span><p>Every model, every colourway, one camera, cut-outs without shadows. It pays for itself in every image after.</p></div>
    <div><span class="ro" style="color:var(--lime)">4 · The storefront</span><p>Homepage and one product page in the live theme, as a draft — nothing published without your sign-off.</p></div>
  </div>
  <div class="src-list grey">Competitor figures: <a href="https://www.powakaddy.com">powakaddy.com</a> homepage (range, taglines, Sept 2026); <a href="https://www.todays-golfer.com/equipment/best/powakaddy-golf-trolleys/">Today’s Golfer, Best PowaKaddy golf trolleys</a> (prices, weights — press figures, some models may have moved); <a href="https://www.motocaddy.com">motocaddy.com</a> homepage. Wishbone figures: Product Bay, product ids 7821489, 9054912, 9054916, 8010088, 7821500. Every product image here is a real Product Bay photograph or render; none is generated.</div>
</div></section>
<script>
document.querySelectorAll('.teaser .dm circle:not([fill])').forEach(function(c,i){ c.style.animationDelay = (Math.random()*1.6 + 0.2).toFixed(2)+'s' });
</script>
</body></html>"""

def build():
    cover = D('WISHBONE', on='#FFFFFF', off='#1C1E23')
    facts = "".join(f'<div>{D(t, on=LIME)}<div class="ro grey" style="margin-top:8px">{c}</div></div>' for t, c in
                    [('7.65 KG', 'Wishbone THREE, net'), ('249 €', 'Wishbone THREE, RRP'), ('29 CM', 'THREE rear wheel')])
    specimen = D('ABCDEFGHIJKLMNOPQRSTUVWXYZ', on='#FFFFFF', off='#23252B') + '<div style="height:16px"></div>' + D('0123456789 €×.-/', on='#FFFFFF', off='#23252B')
    portraits = "".join(f'<div>{dots(n)}<div class="ro grey" style="margin-top:10px">{l}</div></div>' for n, l in
                        [('one-lime','ONE'),('two-lime','TWO'),('three-lime','THREE'),('three-folded','THREE · folded'),('eon-red','EON'),('neo-wb','NEO')])
    pairs = "".join(f'<figure><img src="{shot(n)}" alt="" loading="lazy"><figcaption><b>{a}</b> <span class="grey">on {b}</span></figcaption></figure>' for n, a, b in
                    [('three-lime','THREE Black / Lime','lime'),('one-red','ONE Charcoal / Red','signal'),('one-blue','ONE Charcoal / Blue','cobalt'),('two-lime','TWO Black / Lime','concrete'),
                     ('three-wr','THREE White / Red','ink'),('two-wr','TWO White / Red','graphite'),('eon-red','EON Charcoal / Red','signal'),('neo-wb','NEO White / Blue','graphite')])
    gallery = "".join(f'<img src="{shot(n)}" alt="" loading="lazy">' for n in ['three-folded','three-bw','one-lime','one-black','eon-wr','two-lime','one-blue','neo-wb'])
    strip = "".join(f'<div>{D(v)}<div class="ro" style="margin-top:8px;font-size:11px">{k}</div></div>' for v, k in
                    [('7.65 KG','net weight'),('57 CM','folded, longest side'),('4','accessory mounts'),('249 €','RRP')])
    rng = "".join(range_card(*a) for a in [
        ('one-lime','ONE','229 €','Five colourways. Wheels come off.','UNDER 4 KG*'),
        ('two-lime','TWO','199 €','Folds to 35.5 × 53 × 45 cm.','6.9 KG'),
        ('three-lime','THREE','249 €','Folds, and locks folded.','7.65 KG'),
        ('eon-red','EON','799 €','Electric. Battery included.','ELECTRIC'),
        ('neo-wb','NEO','999 €','Electric.','ELECTRIC')])
    social = "".join(f'<div class="post"><img src="{shot(n)}" alt=""><div class="ov">{D(t, on=c)}<small>{s}</small></div></div>' for n, t, c, s in
                     [('sq-three-lime','249 €',INK,'Wishbone THREE. Everything you need.'),
                      ('sq-one-red','< 4 KG*',PAPER,'Wishbone ONE. *Confirm before posting.'),
                      ('sq-two-lime','199 €',INK,'Wishbone TWO. Nothing you don’t.')])
    teaser = D('NEW · 2027', on=LIME, off='#141518')
    hero_co = callouts('three-lime', {'organizer': ('SMART ORGANIZER', 'l'), 'sleeve': ('DUAL-TUBE FRAME', 'r'), 'front': ('24 CM', 'r'), 'rear': ('29 CM', 'l')})
    pdp_co = callouts('eon-wr', {'badge': ('ALUMINIUM FRAME', 'l'), 'base': ('BATTERY INCLUDED', 'r'), 'rear': ('WHEELS DETACH', 'r')}).replace('co co--', 'co co--w co--')
    rep = {
      '__WORD__': WORD, '__WORD_INK__': WORD_INK, '__COVER_DM__': cover,
      '__PK_DOTS__': '<i></i>'*13, '__WB_DOTS__': '<i></i>'*5,
      '__BALL__': dimple_ball(), '__GRIP__': webp('detail-eon-grip'), '__BADGE__': webp('detail-one-badge'),
      '__FACTS_DM__': facts, '__SPECIMEN__': specimen, '__PORTRAITS__': portraits, '__PAIRS__': pairs,
      '__HERO_SHOT__': shot('three-lime'), '__HERO_CO__': hero_co, '__GALLERY__': gallery,
      '__DO1__': shot('one-red'), '__DO2__': shot('three-wr'), '__DONT1__': shot('dont-paper'), '__DONT2__': shot('dont-dark'),
      '__HERO_WIDE__': shot('three-lime'), '__STRIP__': strip, '__LINEUP__': b64(SH/'lineup-web.jpg', 'image/jpeg'),
      '__RANGE__': rng, '__PDP__': shot('eon-wr'), '__PDP_CO__': pdp_co, '__EON_DM__': D('EON', on=PAPER),
      '__EON_PRICE__': D('799 €', on=LIME), '__SOCIAL__': social, '__TEASER__': teaser}
    out = HTML
    for k, v in rep.items(): out = out.replace(k, v)
    return out

if __name__ == '__main__':
    out = build()
    left = sorted(set(__import__('re').findall(r'__[A-Z0-9_]+__', out)))
    dest = pathlib.Path('/tmp/wb/kit/wishbone-brand-v5.html'); dest.parent.mkdir(parents=True, exist_ok=True); dest.write_text(out)
    print('wrote', dest, round(len(out)/1024), 'KB', '· unreplaced:', left or 'none')
