#!/usr/bin/env python3
"""Wishbone v5 — the product-shot recipe, in code.

Every Wishbone product image is the same six layers: a colour FIELD keyed to the colourway, a
LIGHT POOL behind the product, a FLOOR that darkens into the sweep, the brand DOT texture fading
out behind the product, the model name in Wishbone Dot at giant scale tone-on-tone, and the REAL
product cut-out with a contact shadow. Nothing about the product is generated or retouched.

Needs Pillow and PyMuPDF (for the dot numeral):  python3 -m venv .venv && .venv/bin/pip install pillow pymupdf
Writes assets/v5/shots/*.jpg and assets/v5/shots/anchors.json (callout positions, in % of the frame).
"""
import io, json, pathlib, sys
from PIL import Image, ImageDraw, ImageFilter, ImageChops
import pymupdf
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT/'tools')); import dotmatrix as dm
V = ROOT/'assets'/'v5'; OUT = V/'shots'; OUT.mkdir(exist_ok=True)

FIELDS = {  # photography fields — backdrops only, never interface colour
  'lime':     '#CBE832', 'signal':   '#E03828', 'cobalt':  '#3B82F0',
  'concrete': '#D4D5D8', 'graphite': '#2A2C31', 'ink':     '#0F1014', 'paper': '#FFFFFF'}
DARK = {'graphite', 'ink'}

# where the callouts point, measured on each trimmed cut-out (fraction of its width, height)
PARTS = {
  'three-lime': {'rear': (.83,.83), 'front': (.12,.87), 'sleeve': (.60,.40), 'organizer': (.84,.09)},
  'eon-wr':     {'rear': (.86,.72), 'badge': (.49,.43), 'base': (.60,.64)},   # measured on the re-trimmed cut-out
  'one-red':    {'badge': (.50,.42), 'rear': (.80,.72), 'frame': (.63,.46)},
}

def hx(h): h = h.lstrip('#'); return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
def mix(a, b, t): return tuple(round(a[i]+(b[i]-a[i])*t) for i in range(3))
def rgb(c): return '#%02x%02x%02x' % c
def svg_png(svg, w):
    d = pymupdf.open(stream=svg.encode(), filetype='svg'); z = w/d[0].rect.width
    pm = d[0].get_pixmap(matrix=pymupdf.Matrix(z, z), alpha=True)
    return Image.open(io.BytesIO(pm.tobytes('png'))).convert('RGBA')

def render(prod, field, word=None, W=1600, H=2000, scale=.80, numeral=True, texture=True, plain=False):
    f = hx(FIELDS[field]); dark = field in DARK
    im = Image.new('RGB', (W, H), f)
    if not plain:
        pool = mix(f, (255,255,255), .14 if dark else .30); floor = mix(f, (0,0,0), .16)
        m = Image.new('L', (W, H), 0); ImageDraw.Draw(m).ellipse([W*.08, H*.02, W*.92, H*.82], fill=255)
        im = Image.composite(Image.new('RGB', (W, H), pool), im, m.filter(ImageFilter.GaussianBlur(W*.14)))
        g = Image.new('L', (1, H))
        for y in range(H): g.putpixel((0, y), int(255*max(0, min(1, (y/H-.70)/.30))**1.2))
        im = Image.composite(Image.new('RGB', (W, H), floor), im, g.resize((W, H)))
        if texture:
            tex = Image.new('L', (W, H), 0); d = ImageDraw.Draw(tex); p = max(12, W//57); r = p*.115
            for y in range(p//2, H, p):
                for x in range(p//2, W, p): d.ellipse([x-r, y-r, x+r, y+r], fill=255)
            fm = Image.new('L', (W, H), 255); ImageDraw.Draw(fm).ellipse([W*.12, H*.06, W*.88, H*.80], fill=0)
            dotc = mix(f, (255,255,255), .10) if dark else mix(f, (0,0,0), .13)
            im = Image.composite(Image.new('RGB', (W, H), dotc), im, ImageChops.multiply(tex, fm.filter(ImageFilter.GaussianBlur(W*.10))))
        if numeral and word:
            numc = mix(f, (255,255,255), .07) if dark else mix(f, (0,0,0), .09)
            n = svg_png(dm.svg(word, on=rgb(numc), pitch=10, r=4.2), int(W*.86))
            if n.height > H*.30: n = n.resize((int(n.width*H*.30/n.height), int(H*.30)), Image.LANCZOS)
            im.paste(n, ((W-n.width)//2, int(H*.06)), n)
    pr = Image.open(V/f'{prod}.webp').convert('RGBA'); ph = int(H*scale)
    pr = pr.resize((int(pr.width*ph/pr.height), ph), Image.LANCZOS)
    if pr.width > W*.88: pw = int(W*.88); pr = pr.resize((pw, int(pr.height*pw/pr.width)), Image.LANCZOS)
    px, py = (W-pr.width)//2, int(H*.93)-pr.height
    if not plain:
        sh = Image.new('L', (W, H), 0); ImageDraw.Draw(sh).ellipse([W*.5-pr.width*.40, H*.895, W*.5+pr.width*.40, H*.955], fill=200 if dark else 150)
        im = Image.composite(Image.new('RGB', (W, H), mix(mix(f,(0,0,0),.16), (0,0,0), .5)), im, sh.filter(ImageFilter.GaussianBlur(W*.018)))
    im.paste(pr, (px, py), pr)
    anchors = {k: [round((px+x*pr.width)/W*100, 2), round((py+y*pr.height)/H*100, 2)] for k, (x, y) in PARTS.get(prod, {}).items()}
    return im, anchors

LINEUP_H = {'neo-wb': .88, 'eon-red': .92}   # visual balance only; the line-up makes no claim about relative size

def lineup(prods, field, W=3200, H=1500, word='WISHBONE'):
    """The range, side by side, at one height — the family shot."""
    f = hx(FIELDS[field])
    bg = Image.new('RGB', (W, H), f)
    pool = mix(f, (255,255,255), .30); floor = mix(f, (0,0,0), .16)
    m = Image.new('L', (W, H), 0); ImageDraw.Draw(m).ellipse([W*.05, -H*.1, W*.95, H*.85], fill=255)
    bg = Image.composite(Image.new('RGB', (W, H), pool), bg, m.filter(ImageFilter.GaussianBlur(W*.10)))
    g = Image.new('L', (1, H))
    for y in range(H): g.putpixel((0, y), int(255*max(0, min(1, (y/H-.66)/.34))**1.2))
    bg = Image.composite(Image.new('RGB', (W, H), floor), bg, g.resize((W, H)))
    numc = mix(f, (0,0,0), .05); n = svg_png(dm.svg(word, on=rgb(numc), pitch=10, r=4.2), int(W*.84))
    bg.paste(n, ((W-n.width)//2, int(H*.08)), n)
    slot = W/len(prods); ph = int(H*.66)
    for i, p in enumerate(prods):
        h = int(ph*LINEUP_H.get(p, 1)); pr = Image.open(V/f'{p}.webp').convert('RGBA'); pr = pr.resize((int(pr.width*h/pr.height), h), Image.LANCZOS)
        if pr.width > slot*.96: pw = int(slot*.96); pr = pr.resize((pw, int(pr.height*pw/pr.width)), Image.LANCZOS)
        cx = int(slot*(i+.5)); px, py = cx-pr.width//2, int(H*.92)-pr.height
        sh = Image.new('L', (W, H), 0); ImageDraw.Draw(sh).ellipse([cx-pr.width*.42, H*.885, cx+pr.width*.42, H*.945], fill=150)
        bg = Image.composite(Image.new('RGB', (W, H), mix(floor, (0,0,0), .5)), bg, sh.filter(ImageFilter.GaussianBlur(22)))
        bg.paste(pr, (px, py), pr)
    return bg

SHOTS = [  # name, product, field, word, format
  ('three-lime',   'three-lime',   'lime',     'THREE', '4:5'), ('three-folded', 'three-folded', 'lime', 'THREE', '4:5'),
  ('three-wr',     'three-wr',     'ink',      'THREE', '4:5'), ('three-bw',     'three-bw',     'concrete','THREE','4:5'),
  ('two-lime',     'two-lime',     'concrete', 'TWO',   '4:5'), ('two-wr',       'two-wr',       'graphite','TWO', '4:5'),
  ('one-lime',     'one-lime',     'lime',     'ONE',   '4:5'), ('one-red',      'one-red',      'signal', 'ONE',  '4:5'),
  ('one-blue',     'one-blue',     'cobalt',   'ONE',   '4:5'), ('one-black',    'one-black',    'concrete','ONE', '4:5'),
  ('eon-red',      'eon-red',      'signal',   'EON',   '4:5'), ('eon-wr',       'eon-wr',       'ink',    'EON',  '4:5'),
  ('neo-wb',       'neo-wb',       'graphite', 'NEO',   '4:5'),
  ('sq-three-lime','three-lime',   'lime',     'THREE', '1:1'), ('sq-one-red',   'one-red',      'signal', 'ONE',  '1:1'),
  ('sq-two-lime',  'two-lime',     'concrete', 'TWO',   '1:1'),
  # the don'ts, for the guideline
  ('dont-paper',   'three-lime',   'paper',    None,    'plain'), ('dont-dark', 'one-black', 'ink', 'ONE', '4:5'),
]
def halftone(prod, cols=72):
    """Dot portrait: each dot's size is the real cut-out's coverage in that cell — the product, in dots."""
    im = Image.open(V/f'{prod}.webp').convert('RGBA'); w, h = im.size; rows = int(h/(w/cols))
    a = im.getchannel('A').resize((cols, rows), Image.BOX); dots = []
    for y in range(rows):
        for x in range(cols):
            c = a.getpixel((x, y))/255
            if c >= .06: dots.append(f'<circle cx="{x+.5:.1f}" cy="{y+.5:.1f}" r="{.46*min(1, c**.7):.3f}"/>')
    (V/f'{prod}-dots.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {cols} {rows}">{"".join(dots)}</svg>')

FMT = {'4:5': (1600, 2000, .80), '1:1': (1600, 1600, .78), 'plain': (1600, 2000, .80)}
if __name__ == '__main__':
    anchors = {}
    for name, prod, field, word, fmt in SHOTS:
        W, H, sc = FMT[fmt]
        im, a = render(prod, field, word, W, H, sc, plain=(fmt == 'plain'))
        im.save(OUT/f'{name}.jpg', 'JPEG', quality=86, optimize=True, progressive=True)
        web = im.copy(); web.thumbnail((900, 900), Image.LANCZOS); web.save(OUT/f'{name}-web.jpg', 'JPEG', quality=82, optimize=True, progressive=True)
        if a: anchors[name] = a
        print(f'{name:16s} {field:9s} {fmt:5s} {(OUT/(name+".jpg")).stat().st_size//1024} KB')
    lu = lineup(['one-lime', 'two-lime', 'three-lime', 'eon-red', 'neo-wb'], 'concrete')
    lu.save(OUT/'lineup.jpg', 'JPEG', quality=86, optimize=True, progressive=True); print('lineup', (OUT/'lineup.jpg').stat().st_size//1024, 'KB')
    web = lu.copy(); web.thumbnail((1800, 1800), Image.LANCZOS); web.save(OUT/'lineup-web.jpg', 'JPEG', quality=82, optimize=True, progressive=True)
    for p in ('one-lime', 'two-lime', 'three-lime', 'three-folded', 'eon-red', 'neo-wb'): halftone(p)
    (OUT/'anchors.json').write_text(json.dumps(anchors, indent=1)+'\n')
