import React from 'react';
import { Tile } from '../primitives/Tile.jsx';

export function BoxTile({ n, items = [], note }) {
  return (
    <Tile n={n} label="In the box">
      <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
        {items.map((it) => <li key={it.name} style={{ display: 'flex', justifyContent: 'space-between', gap: 12, padding: '9px 0', borderBottom: '1px solid var(--tile-line)' }}>
          <span>{it.name}</span><span className="grey">{it.qty || '1 ×'}</span></li>)}
      </ul>
      {note && <p className="grey" style={{ fontSize: 'var(--fs-label)', letterSpacing: '0.04em' }}>{note}</p>}
    </Tile>
  );
}
