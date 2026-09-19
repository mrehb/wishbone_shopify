import React from 'react';
import { Tile } from '../primitives/Tile.jsx';
import { Dots } from '../primitives/Dots.jsx';
import { silhouette } from '../primitives/Silhouettes.jsx';

// Five models in one tile. Manual to electric, left to right.
export function RangeTile({ n = '02', label = 'The range', models = [], span = 3 }) {
  return (
    <Tile n={n} label={label} span={span}>
      <div style={{ display: 'grid', gridTemplateColumns: `repeat(${models.length}, minmax(0,1fr))`, gap: 16 }}>
        {models.map((m) => (
          <a key={m.id} href={m.href || '#'} style={{ textDecoration: 'none', color: 'inherit', display: 'flex', flexDirection: 'column', gap: 12 }}>
            <Dots {...silhouette(m.id)} size={4} gap={2} />
            <div>
              <div style={{ fontSize: 'var(--fs-lead)' }}>{m.id}</div>
              <div className="label" style={{ marginTop: 4 }}>{m.electric ? 'electric' : 'manual'}</div>
              <div style={{ marginTop: 8, color: m.price ? 'var(--white)' : 'var(--grey)' }}>{m.price || '—'}</div>
            </div>
          </a>
        ))}
      </div>
    </Tile>
  );
}
