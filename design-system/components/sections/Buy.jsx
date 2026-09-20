import React, { useState } from 'react';
import { Eyebrow } from '../primitives/Eyebrow.jsx';
import { Display } from '../primitives/Display.jsx';
import { Button } from '../primitives/Button.jsx';
import { Price } from '../primitives/Price.jsx';
import { Photo } from '../primitives/Silhouette.jsx';

// The product page opener: gallery on mist left, the buy column right. Colourways are the
// store's real option values, drawn as split squares; the lime button is the purchase.
const SW = { 'charcoal-black': ['#2b2b2e', '#0f1014'], 'charcoal-lime': ['#2b2b2e', '#8cac1c'], 'charcoal-red': ['#2b2b2e', '#b3342a'], 'charcoal-blue': ['#2b2b2e', '#2f5aa8'], 'white-red': ['#e9e9e9', '#b3342a'] };
export function Buy({ model = 'EON', type = 'electric', price, colourways = [], images = [], copy, delivery = '2–4 days · AT DE UK', parts, soldOut = false, facts = [] }) {
  const [cw, setCw] = useState(colourways[0]);
  const [img, setImg] = useState(0);
  const src = images[img] && (images[img].src || images[img]);
  return (
    <section className="band" style={{ paddingTop: 48 }}><div className="container grid" style={{ alignItems: 'start' }}>
      <div style={{ gridColumn: 'span 7', display: 'grid', gap: 12 }}>
        <Photo src={src} model={model} alt={`Wishbone ${model}`} ratio={1} large />
        {images.length > 1 && <div style={{ display: 'flex', gap: 8 }}>{images.map((im, i) => <button key={i} onClick={() => setImg(i)} aria-label={`image ${i + 1}`} style={{ width: 64, padding: 0, border: `1px solid ${i === img ? 'var(--ink)' : 'var(--hair)'}`, background: 'var(--mist)', cursor: 'pointer' }}><Photo src={im.src || im} model={model} ratio={1} style={{ width: '100%' }} /></button>)}</div>}
      </div>
      <div style={{ gridColumn: '9 / span 4', display: 'grid', gap: 24, position: 'sticky', top: 24 }}>
        <Eyebrow n="01">{type}</Eyebrow>
        <Display lines={[`Wishbone ${model}.`]} size="s" as="h1" />
        <Price value={price} size="var(--fs-h)" />
        {copy && <p className="grey">{copy}</p>}
        {colourways.length > 0 && (
          <div style={{ display: 'grid', gap: 10 }}>
            <div className="label grey">Colourway <span style={{ color: 'var(--ink)' }}>{cw}</span></div>
            <div style={{ display: 'flex', gap: 8 }}>{colourways.map((c) => { const [a, b] = SW[c] || ['#2b2b2e', '#2b2b2e']; const on = c === cw; return (
              <button key={c} aria-label={c} aria-pressed={on} onClick={() => setCw(c)} style={{ width: 'var(--swatch)', height: 'var(--swatch)', padding: 0, cursor: 'pointer', background: `linear-gradient(135deg, ${a} 0 50%, ${b} 50% 100%)`, border: `2px solid ${on ? 'var(--ink)' : 'var(--paper)'}`, outline: `1px solid ${on ? 'var(--ink)' : 'var(--hair)'}` }} />); })}</div>
          </div>
        )}
        <Button kind="lime" arrow block disabled={soldOut}>{soldOut ? 'Sold out' : 'Add to cart'}</Button>
        <dl style={{ margin: 0, borderTop: 'var(--hair-w) solid var(--hair)' }}>
          {[['Delivery', delivery], parts != null && ['Spare parts', `${parts} listed for this model`], ...facts.map((f) => [f.label, f.value])].filter(Boolean).map(([k, v]) => (
            <div key={k} style={{ display: 'flex', justifyContent: 'space-between', gap: 16, padding: '12px 0', borderBottom: 'var(--hair-w) solid var(--hair)', fontSize: 14 }}><dt className="label grey">{k}</dt><dd style={{ margin: 0, textAlign: 'right' }}>{v}</dd></div>
          ))}
        </dl>
      </div>
    </div></section>
  );
}
