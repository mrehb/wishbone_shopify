import React from 'react';
import { Eyebrow } from '../primitives/Eyebrow.jsx';
import { Display } from '../primitives/Display.jsx';
import { Button } from '../primitives/Button.jsx';
import { Photo } from '../primitives/Silhouette.jsx';
import { Price } from '../primitives/Price.jsx';

// "Built to perform": copy left, three products right on mist, name and "from" price beneath.
export function Lineup({ n = '02', eyebrow = 'The lineup', lines = ['Three manual.', 'Two electric.'], copy = 'One frame idea, five expressions. Every one folds flat and rolls on sealed bearings.', cta = 'Explore all models', items = [] }) {
  return (
    <section className="band"><div className="container grid" style={{ alignItems: 'start' }}>
      <div style={{ gridColumn: 'span 4', display: 'grid', gap: 24 }}>
        <Eyebrow n={n}>{eyebrow}</Eyebrow><Display lines={lines} /><p className="grey" style={{ maxWidth: '34ch' }}>{copy}</p><div><Button kind="outline" arrow>{cta}</Button></div>
      </div>
      <div style={{ gridColumn: '5 / span 8', display: 'grid', gridTemplateColumns: `repeat(${Math.min(items.length, 3)}, 1fr)`, gap: 16 }}>
        {items.map((p) => (
          <a key={p.id} href="#" style={{ display: 'grid', gap: 12 }}>
            <Photo src={p.src} model={p.id} alt={`Wishbone ${p.id}`} ratio={0.9} />
            <div><div className="label">Wishbone <span style={{ color: 'var(--grey)' }}>{p.id}</span></div><div className="label grey" style={{ marginTop: 4, textTransform: 'none', letterSpacing: 0, fontWeight: 400 }}>{p.type}</div></div>
            <Price value={p.price} from size="var(--fs-body)" />
          </a>
        ))}
      </div>
    </div></section>
  );
}
