#!/usr/bin/env python3
"""Generate the Wishbone design-system preview bundle.

Each component is one self-contained HTML preview whose first line is the
@dsCard marker Claude Design reads to build its card index. Regenerate with
`python3 build.py` after changing a token or a component.
"""
import base64, pathlib

ROOT = pathlib.Path(__file__).parent
WORDMARK = base64.b64encode((ROOT/'assets/WISHBONE_GOLF_NEGATIVE.png').read_bytes()).decode()
MONO = base64.b64encode((ROOT/'assets/wb_logo.png').read_bytes()).decode()

SHELL = """<!-- @dsCard group="{group}" name="{name}" subtitle="{subtitle}" -->
<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Wishbone — {name}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600&family=Figtree:ital,wght@0,500;0,700;1,500&display=swap" rel="stylesheet">
<style>
:root{{
  --wb-ink:#1F1F21; --wb-white:#FFFFFF; --wb-volt:#E3FC02; --wb-cyan:#00FCED; --wb-logo-lime:#C8D645;
  --wb-font-heading:'Oswald','Arial Narrow',sans-serif;
  --wb-font-body:'Figtree',-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  --wb-radius:0; --wb-radius-pill:40px; --wb-border-width:1px; --wb-border-opacity:.55;
  --wb-grid-gap:40px; --wb-space-section:52px;
  --line:#34343a; --panel:#26262a; --mut:#9a9da3;
}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--wb-ink);color:var(--wb-white);
  font-family:var(--wb-font-body);font-weight:500;font-size:15px;line-height:1.6;padding:40px}}
h1,h2,h3,h4{{font-family:var(--wb-font-heading);font-weight:500;text-transform:uppercase;margin:0;line-height:1.05}}
h1{{font-size:56px}} h2{{font-size:33.6px}} h3{{font-size:25.2px}} h4{{font-size:15px;letter-spacing:.06em}}
.eyebrow{{font-size:11px;letter-spacing:.16rem;text-transform:uppercase;color:var(--mut);margin-bottom:10px}}
.note{{color:var(--mut);font-size:13px}}
.rule{{border:0;border-top:1px solid var(--line);margin:28px 0}}
.grid{{display:grid;gap:var(--wb-grid-gap)}}
code{{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12.5px;background:var(--panel);padding:1px 6px}}
/* brand components — square, hairline, flat, no shadow */
.wb-btn{{display:inline-block;background:var(--wb-volt);color:var(--wb-ink);font-family:var(--wb-font-heading);
  text-transform:uppercase;font-size:15px;letter-spacing:.04em;padding:13px 26px;border:0;border-radius:var(--wb-radius);cursor:pointer;text-decoration:none}}
.wb-btn--secondary{{background:transparent;color:var(--wb-volt);border:var(--wb-border-width) solid var(--wb-volt)}}
.wb-btn--white{{background:var(--wb-white);color:var(--wb-ink)}}
.wb-btn[disabled]{{opacity:.4;cursor:not-allowed}}
.wb-pill{{display:inline-block;border:var(--wb-border-width) solid rgba(255,255,255,.55);border-radius:var(--wb-radius-pill);padding:9px 20px;font-size:14px;cursor:pointer}}
.wb-pill[aria-checked="true"]{{background:var(--wb-white);color:var(--wb-ink);border-color:var(--wb-white)}}
.wb-input{{display:block;width:100%;border:var(--wb-border-width) solid rgba(255,255,255,.55);border-radius:var(--wb-radius);
  background:transparent;color:var(--wb-white);padding:12px 14px;font-family:var(--wb-font-body);font-size:14px}}
.wb-input::placeholder{{color:var(--mut)}}
{extra}
</style></head><body>
<div class="eyebrow">Wishbone Golf · {group}</div>
<h2>{name}</h2>
<p class="note" style="max-width:640px;margin-top:8px">{blurb}</p>
<hr class="rule">
{body}
</body></html>
"""

def card(path, group, name, subtitle, blurb, body, extra=""):
    (ROOT/path).write_text(SHELL.format(group=group, name=name, subtitle=subtitle,
                                        blurb=blurb, body=body, extra=extra))
    print("wrote", path)

# ---------------------------------------------------------------- foundations
card("foundations/colour.html", "Foundations", "Colour", "4 core + 1 conflict",
     "Ink is the ground; Volt is the only action colour. The brights carry ink type only — "
     "white on Volt measures 1.15:1 and is unreadable.",
     """
<div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(170px,1fr))">
  <div><div style="height:130px;background:#1F1F21;border:1px solid var(--line)"></div>
    <h4 style="margin-top:12px">Ink</h4><div class="note">#1F1F21 · the ground</div></div>
  <div><div style="height:130px;background:#FFFFFF"></div>
    <h4 style="margin-top:12px">White</h4><div class="note">#FFFFFF · type &amp; marks</div></div>
  <div><div style="height:130px;background:#E3FC02"></div>
    <h4 style="margin-top:12px">Volt</h4><div class="note">#E3FC02 · action colour</div></div>
  <div><div style="height:130px;background:#00FCED"></div>
    <h4 style="margin-top:12px">Cyan</h4><div class="note">#00FCED · accent panel</div></div>
</div>
<h4 style="margin-top:34px">Proportion</h4>
<div style="display:flex;height:34px;border:1px solid var(--line);margin-top:8px">
  <div style="background:#1F1F21;flex:70"></div><div style="background:#fff;flex:20"></div><div style="background:#E3FC02;flex:10"></div></div>
<div class="note" style="margin-top:6px">70 % ink · 20 % white · 10 % Volt. Cyan is a guest: one element per page.</div>
<h4 style="margin-top:34px">Pairings</h4>
<div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(200px,1fr));margin-top:10px">
  <div style="background:#1F1F21;border:1px solid var(--line);padding:20px"><span style="color:#fff">White on ink · 16.45 ✓</span></div>
  <div style="background:#1F1F21;border:1px solid var(--line);padding:20px"><span style="color:#E3FC02">Volt on ink · 14.25 ✓</span></div>
  <div style="background:#E3FC02;padding:20px"><span style="color:#1F1F21">Ink on Volt · 14.25 ✓</span></div>
  <div style="background:#E3FC02;padding:20px"><span style="color:#fff">White on Volt · 1.15 ✗</span></div>
</div>
<div class="note" style="margin-top:20px"><b style="color:#fff">Unresolved:</b> the monogram ships
<code>#C8D645</code> while the theme uses <code>#E3FC02</code>. Recommendation: standardise on Volt.</div>
""")

card("foundations/typography.html", "Foundations", "Typography", "Oswald 500 · Figtree 500/700",
     "Two families, four weights, nothing else. Headings are Oswald uppercase at a 140 % scale; body is Figtree 500 at 15px.",
     """
<div style="border-bottom:1px solid var(--line);padding:16px 0"><div class="note">Display · 72.8px</div>
  <div style="font-family:var(--wb-font-heading);text-transform:uppercase;font-size:72.8px">EON</div></div>
<div style="border-bottom:1px solid var(--line);padding:16px 0"><div class="note">H1 · 56px / 42px mobile</div>
  <div style="font-family:var(--wb-font-heading);text-transform:uppercase;font-size:56px">We are Wishbone</div></div>
<div style="border-bottom:1px solid var(--line);padding:16px 0"><div class="note">H2 · 33.6px</div>
  <div style="font-family:var(--wb-font-heading);text-transform:uppercase;font-size:33.6px">The Electric Wishbone EON</div></div>
<div style="border-bottom:1px solid var(--line);padding:16px 0"><div class="note">H3 · 25.2px</div>
  <div style="font-family:var(--wb-font-heading);text-transform:uppercase;font-size:25.2px">Engineered light</div></div>
<div style="border-bottom:1px solid var(--line);padding:16px 0"><div class="note">Body · Figtree 500 · 15px</div>
  <div style="max-width:560px">Crafted from ultra-light aircraft-grade aluminium — effortless folding, magnetic attachments, sealed bearings.</div></div>
<div style="border-bottom:1px solid var(--line);padding:16px 0"><div class="note">Bold · Figtree 700</div>
  <div style="font-weight:700">27+ holes on one charge.</div></div>
<div style="padding:16px 0"><div class="note">Caption · 11px · tracked .16rem</div>
  <div class="eyebrow" style="margin:0">Free shipping over 100 €</div></div>
""")

card("foundations/logo.html", "Foundations", "Logo", "Wordmark + monogram, clear space",
     "Both marks are white on transparent, so they live on ink, dark photography or a Volt panel — never on white. "
     "Clear space is the height of the W on all four sides.",
     """
<div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(300px,1fr))">
  <div>
    <div style="background:var(--panel);padding:36px;border:1px solid var(--line)">
      <div style="border:1px dashed rgba(227,252,2,.5);padding:26px;display:flex;justify-content:center">
        <img src="data:image/png;base64,{wordmark}" alt="Wishbone Golf" style="width:78%"></div></div>
    <h4 style="margin-top:14px">Wordmark</h4>
    <div class="note">800 × 64 PNG · header use at 200px wide · dashed line = clear space</div>
  </div>
  <div>
    <div style="background:var(--panel);padding:36px;border:1px solid var(--line)">
      <div style="border:1px dashed rgba(227,252,2,.5);padding:26px;display:flex;justify-content:center">
        <img src="data:image/png;base64,{mono}" alt="Wishbone monogram" style="width:52%"></div></div>
    <h4 style="margin-top:14px">Monogram</h4>
    <div class="note">600 × 307 PNG · favicon · the lime cut is #C8D645, pending the green decision</div>
  </div>
</div>
<h4 style="margin-top:30px">Never</h4>
<div class="note">On white or mid-grey · recoloured, outlined, stretched, rotated or boxed · shadowed ·
wordmark and monogram side by side · GOLF rebuilt in another typeface.</div>
<div class="note" style="margin-top:14px"><b style="color:#fff">Missing:</b> a positive (ink-on-light) version and an SVG of each mark.</div>
""".replace("{wordmark}", WORDMARK).replace("{mono}", MONO))

card("foundations/geometry.html", "Foundations", "Geometry", "Square · hairline · flat",
     "The most consistent part of the existing system. Radius is 0 on every surface; variant pills at 40 are the one exception; nothing casts a shadow.",
     """
<div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr))">
  <div><h4>Radius 0</h4><div style="height:90px;background:var(--panel);border:1px solid var(--line);border-radius:0"></div>
    <div class="note" style="margin-top:8px">Buttons, cards, inputs, media</div></div>
  <div><h4>Pill 40 — the exception</h4><div style="height:90px;background:var(--panel);border:1px solid var(--line);border-radius:40px"></div>
    <div class="note" style="margin-top:8px">Variant selectors only</div></div>
  <div><h4>Hairline 1px · 55 %</h4><div style="height:90px;border:1px solid rgba(255,255,255,.55)"></div>
    <div class="note" style="margin-top:8px">Never heavy rules</div></div>
</div>
<table style="width:100%;border-collapse:collapse;margin-top:26px;font-size:14px">
  <tr><td style="padding:8px 0;border-bottom:1px solid var(--line)">Shadows</td><td style="border-bottom:1px solid var(--line)"><b>none — opacity 0 everywhere</b></td></tr>
  <tr><td style="padding:8px 0;border-bottom:1px solid var(--line)">Page width</td><td style="border-bottom:1px solid var(--line)">1600px</td></tr>
  <tr><td style="padding:8px 0;border-bottom:1px solid var(--line)">Section spacing</td><td style="border-bottom:1px solid var(--line)">52px</td></tr>
  <tr><td style="padding:8px 0;border-bottom:1px solid var(--line)">Grid gutters</td><td style="border-bottom:1px solid var(--line)">40 × 40px</td></tr>
  <tr><td style="padding:8px 0">Hover / motion</td><td>no hover effects · reveal on scroll on</td></tr>
</table>
""")

# ----------------------------------------------------------------- components
card("components/buttons.html", "Components", "Buttons", "Primary / secondary / white, 3 states",
     "Oswald uppercase, square, no shadow. Primary is Volt with ink type — the brights never carry white type.",
     """
<div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(240px,1fr))">
  <div><h4>Primary</h4><p><a class="wb-btn" href="#">Add to cart</a></p>
    <div class="note">Volt · ink label · one per view</div></div>
  <div><h4>Secondary</h4><p><a class="wb-btn wb-btn--secondary" href="#">Learn more</a></p>
    <div class="note">Volt hairline, transparent fill</div></div>
  <div><h4>On a Volt panel</h4>
    <div style="background:var(--wb-volt);padding:22px"><a class="wb-btn" style="background:var(--wb-ink);color:var(--wb-volt)" href="#">Buy the EON</a></div>
    <div class="note" style="margin-top:8px">Invert: ink fill, Volt label</div></div>
</div>
<h4 style="margin-top:30px">States</h4>
<p style="display:flex;gap:14px;flex-wrap:wrap;align-items:center">
  <span class="wb-btn">Default</span>
  <span class="wb-btn" style="background:#c9df02">Pressed</span>
  <button class="wb-btn" disabled>Sold out</button>
</p>
<div class="note">No hover transform, no shadow, no radius. Pressed is a 10 % darker Volt.</div>
""")

card("components/variant-pills.html", "Components", "Variant pills", "The one rounded element",
     "Model and option selectors. Radius 40 is the single deliberate exception to the square rule; selected is a white fill with ink type.",
     """
<div role="radiogroup" aria-label="Model" style="display:flex;gap:10px;flex-wrap:wrap">
  <span class="wb-pill" role="radio" aria-checked="false">ONE</span>
  <span class="wb-pill" role="radio" aria-checked="false">TWO</span>
  <span class="wb-pill" role="radio" aria-checked="false">THREE</span>
  <span class="wb-pill" role="radio" aria-checked="true">NEO</span>
  <span class="wb-pill" role="radio" aria-checked="false">EON</span>
</div>
<div class="note" style="margin-top:16px">Model names are always caps. Unavailable options get 40 % opacity and a strikethrough, never removal.</div>
""")

card("components/product-card.html", "Components", "Product card", "Image · title · price",
     "Square image, square card, left-aligned text, hairline border at 10 % — the theme's card scheme on ink.",
     """
<div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(230px,1fr))">
  <article style="border:1px solid rgba(255,255,255,.1);background:var(--wb-ink)">
    <div style="aspect-ratio:1;background:linear-gradient(135deg,#2b2b30,#141417);display:flex;align-items:flex-end;padding:16px">
      <span class="eyebrow" style="margin:0;color:var(--wb-volt)">Best seller</span></div>
    <div style="padding:16px">
      <h4 style="font-size:16px">Wishbone EON</h4>
      <div class="note" style="margin:4px 0 10px">Electric trolley</div>
      <div style="font-weight:700">799,00 €</div></div>
  </article>
  <article style="border:1px solid rgba(255,255,255,.1);background:var(--wb-ink)">
    <div style="aspect-ratio:1;background:linear-gradient(135deg,#2b2b30,#141417)"></div>
    <div style="padding:16px">
      <h4 style="font-size:16px">Wishbone THREE</h4>
      <div class="note" style="margin:4px 0 10px">Manual trolley</div>
      <div style="font-weight:700">249,00 €</div></div>
  </article>
  <article style="border:1px solid rgba(255,255,255,.1);background:var(--wb-ink);opacity:.55">
    <div style="aspect-ratio:1;background:linear-gradient(135deg,#2b2b30,#141417)"></div>
    <div style="padding:16px">
      <h4 style="font-size:16px">Fast Charger (NEO &amp; EON)</h4>
      <div class="note" style="margin:4px 0 10px">Sold out</div>
      <div style="font-weight:700">99,90 €</div></div>
  </article>
</div>
<div class="note" style="margin-top:16px">Parts keep their <code>Component (MODEL)</code> name in full — it is how customers find the right one.</div>
""")

card("components/forms.html", "Components", "Forms", "Input · select · newsletter",
     "Square fields, 1px hairline at 55 %, label above, no placeholder-as-label. Errors are stated in words, not colour alone.",
     """
<div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr))">
  <div>
    <h4>Text field</h4>
    <label class="note" for="e">Email address</label>
    <input class="wb-input" id="e" placeholder="you@example.com" style="margin-top:6px">
  </div>
  <div>
    <h4>With error</h4>
    <label class="note" for="e2">Email address</label>
    <input class="wb-input" id="e2" value="you@" style="margin-top:6px;border-color:#ff6b6b">
    <div style="color:#ff6b6b;font-size:13px;margin-top:6px">Add the part after the @ — for example you@example.com.</div>
  </div>
</div>
<h4 style="margin-top:30px">Newsletter row</h4>
<div style="display:flex;gap:0;max-width:520px;margin-top:8px">
  <input class="wb-input" placeholder="Email address" style="border-right:0">
  <button class="wb-btn" style="white-space:nowrap">Sign up</button>
</div>
""")

card("components/sections.html", "Components", "Page sections", "Hero · statement · split",
     "The three layouts the homepage already uses. 52px between sections, 1600px page width, text left, one action per section.",
     """
<section style="border:1px solid var(--line);padding:46px;background:linear-gradient(135deg,#232329,#141417);margin-bottom:52px">
  <div class="eyebrow">Electric</div>
  <h2 style="font-size:44px;max-width:16ch">The Electric Wishbone EON</h2>
  <p style="max-width:44ch;margin:14px 0 22px">A full powered, simple ‘no nonsense’ electric cart.</p>
  <a class="wb-btn" href="#">Learn more</a>
</section>
<section style="text-align:center;padding:10px 0 52px;border-bottom:1px solid var(--line);margin-bottom:52px">
  <h2 style="font-size:40px">We are Wishbone</h2>
  <p style="max-width:62ch;margin:16px auto 0">Birthed in Britain, Wishbone Golf merges exquisite design with unwavering quality.</p>
</section>
<section style="display:grid;grid-template-columns:1fr 1fr;gap:var(--wb-grid-gap);align-items:center">
  <div style="aspect-ratio:4/3;background:linear-gradient(135deg,#2b2b30,#141417);border:1px solid var(--line)"></div>
  <div><h3>The Manual Wishbone ONE</h3>
    <p style="margin:12px 0 20px">Wishbone One 3 Wheel Golf Trolley.</p>
    <a class="wb-btn wb-btn--secondary" href="#">Learn more</a></div>
</section>
""")

card("components/voice.html", "Guidelines", "Voice", "Do / don't, with examples",
     "Short declaratives, concrete nouns, one idea per sentence. Name the material and say the number.",
     """
<div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(280px,1fr))">
  <div style="border-left:3px solid var(--wb-volt);padding-left:16px">
    <h4>Do</h4>
    <ul style="padding-left:18px">
      <li>“Crafted from ultra-light aircraft-grade aluminium.”</li>
      <li>“27+ holes on one charge.”</li>
      <li>“Focus on your game; Wishbone Golf will handle the rest.”</li>
      <li>British spelling throughout.</li>
    </ul>
  </div>
  <div style="border-left:3px solid #ff6b6b;padding-left:16px">
    <h4>Don't</h4>
    <ul style="padding-left:18px">
      <li>“Innovative, premium, game-changing.”</li>
      <li>“Long-lasting battery life.”</li>
      <li>Three clauses and a semicolon.</li>
      <li>“aluminum” inside British copy — as the homepage does today.</li>
    </ul>
  </div>
</div>
<h4 style="margin-top:30px">Naming</h4>
<div class="note">Wishbone ONE · Wishbone EON — brand first, model in caps. The company is <b style="color:#fff">Wishbone Golf</b>;
the family is <b style="color:#fff">Wishbone</b>. Parts are <code>Component (MODEL)</code>.</div>
""")
