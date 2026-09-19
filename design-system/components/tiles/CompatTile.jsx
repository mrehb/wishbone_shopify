import React, { useState } from 'react';
import { Tile } from '../primitives/Tile.jsx';
import { Pill } from '../primitives/Pill.jsx';
import { Dots, bars } from '../primitives/Dots.jsx';

// Which trolley do you have? The most important commerce tile in the catalogue:
// 22 of 27 products are parts scoped to a model.
export function CompatTile({ n = '03', models = [], parts = [], span = 2 }) {
  const [sel, setSel] = useState(models[0]?.id);
  const fits = parts.filter((p) => p.fits.includes(sel) || p.fits.includes('ALL'));
  const counts = models.map((m) => parts.filter((p) => p.fits.includes(m.id) || p.fits.includes('ALL')).length);
  const max = Math.max(1, ...counts);
  return (
    <Tile n={n} label="Which trolley do you have?" span={span}>
      <div style={{ display: 'flex', gap: 8, flexWrap: 'wrap' }}>
        {models.map((m) => <Pill key={m.id} kind="select" on={m.id === sel} onClick={() => setSel(m.id)}>{m.id}</Pill>)}
      </div>
      <div style={{ display: 'grid', gridTemplateColumns: '1fr auto', gap: 20, alignItems: 'end' }}>
        <div>
          <div className="readout">{String(fits.length).padStart(2, '0')}</div>
          <div className="label" style={{ marginTop: 6 }}>parts fit the {sel}</div>
        </div>
        <Dots {...bars(counts.map((c) => c / max), 6)} hot={counts.map((c, i) => c / max >= 0.99 ? i : -1).filter((i) => i >= 0)} />
      </div>
      <ul style={{ listStyle: 'none', padding: 0, margin: 0, borderTop: '1px solid var(--tile-line)' }}>
        {fits.map((p) => (
          <li key={p.title} style={{ display: 'flex', justifyContent: 'space-between', gap: 16, padding: '10px 0', borderBottom: '1px solid var(--tile-line)' }}>
            <span>{p.title}</span>
            <span style={{ whiteSpace: 'nowrap', color: p.soldOut ? 'var(--grey)' : 'var(--white)' }}>{p.soldOut ? 'Sold out' : p.price}</span>
          </li>
        ))}
        {fits.length === 0 && <li className="grey" style={{ padding: '10px 0' }}>No parts listed yet. Send us your serial number and we will find it.</li>}
      </ul>
    </Tile>
  );
}
