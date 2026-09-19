import React, { useState } from 'react';
import { Eyebrow } from '../primitives/Eyebrow.jsx';
import { Display } from '../primitives/Display.jsx';
import { Tag } from '../primitives/Tag.jsx';
import { Price } from '../primitives/Price.jsx';
import { Photo } from '../primitives/Silhouette.jsx';

// The parts business, which is most of the store. A model filter as tags, then a four-up grid:
// photo or silhouette, the exact store title, which models it fits, the price.
export function Parts({ n = '04', eyebrow = 'Spare parts', lines = ['Every part.', 'By model.'], models = ['ONE', 'TWO', 'THREE', 'NEO', 'EON'], items = [], initial = 'ALL' }) {
  const [sel, setSel] = useState(initial);
  const shown = items.filter((p) => sel === 'ALL' || p.fits.includes(sel) || p.fits.includes('ALL'));
  return (
    <section className="band"><div className="container" style={{ display: 'grid', gap: 32 }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'end', flexWrap: 'wrap', gap: 24 }}>
        <div style={{ display: 'grid', gap: 20 }}><Eyebrow n={n}>{eyebrow}</Eyebrow><Display lines={lines} /></div>
        <div style={{ display: 'flex', gap: 6, flexWrap: 'wrap' }} role="tablist">{['ALL', ...models].map((m) => <button key={m} role="tab" aria-selected={sel === m} onClick={() => setSel(m)} style={{ padding: 0, border: 0, background: 'none', cursor: 'pointer' }}><Tag on={sel === m}>{m}</Tag></button>)}</div>
      </div>
      <div className="label grey">{shown.length} parts{sel !== 'ALL' ? ` fit the ${sel}` : ' listed'}</div>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '32px 16px' }}>
        {shown.map((p) => (
          <a key={p.title} href="#" style={{ display: 'grid', gap: 10, alignContent: 'start' }}>
            <Photo src={p.src} model={p.fits[0] === 'ALL' ? 'ONE' : p.fits[0]} ratio={1} />
            <div style={{ fontSize: 14, lineHeight: 1.4, minHeight: 40 }}>{p.title}</div>
            <div style={{ display: 'flex', gap: 4, flexWrap: 'wrap' }}>{p.fits.map((f) => <Tag key={f} on={f === sel}>{f}</Tag>)}</div>
            <Price value={p.price} size="14px" />
          </a>
        ))}
      </div>
    </div></section>
  );
}
