import React from 'react';
import { Tile } from '../primitives/Tile.jsx';
import { Dots } from '../primitives/Dots.jsx';
import { Pill } from '../primitives/Pill.jsx';
import { silhouette } from '../primitives/Silhouettes.jsx';

// A trolley in the grid. Silhouette, name, type, price. One optional status chip.
export function ProductTile({ n, model, title, type, price, status, hot = false, soldOut = false }) {
  return (
    <Tile n={n} label={type} hot={hot} style={{ opacity: soldOut ? 0.55 : 1 }}>
      <div style={{ display: 'flex', justifyContent: 'center', padding: '6px 0' }}><Dots {...silhouette(model)} size={4} gap={2} /></div>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-end', gap: 12 }}>
        <div>
          <div style={{ fontSize: 'var(--fs-lead)' }}>{title}</div>
          <div style={{ marginTop: 4, color: soldOut ? 'var(--grey)' : 'var(--white)' }}>{soldOut ? 'Sold out' : price}</div>
        </div>
        {status && <Pill kind="status" hot={hot}>{status}</Pill>}
      </div>
    </Tile>
  );
}
