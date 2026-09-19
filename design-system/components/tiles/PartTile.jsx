import React from 'react';
import { Tile } from '../primitives/Tile.jsx';
import { Dots, ring } from '../primitives/Dots.jsx';
import { Pill } from '../primitives/Pill.jsx';

// A spare part. 15 of 22 have no photograph, so the graphic is a ring — a part is a
// component of a whole — and the compatibility chips do the work an image would.
export function PartTile({ n, title, price, fits = [], soldOut = false }) {
  return (
    <Tile n={n} label="Spare part" style={{ opacity: soldOut ? 0.55 : 1 }}>
      <div style={{ display: 'flex', justifyContent: 'center', padding: '4px 0' }}><Dots {...ring(1, 8)} hot={[]} size={4} gap={2} /></div>
      <div style={{ fontSize: 'var(--fs-body)', lineHeight: 1.35 }}>{title}</div>
      <div style={{ display: 'flex', gap: 6, flexWrap: 'wrap' }}>
        {fits.map((f) => <Pill key={f} kind="tag">{f === 'ALL' ? 'every model' : f}</Pill>)}
      </div>
      <div style={{ color: soldOut ? 'var(--grey)' : 'var(--white)', fontSize: 'var(--fs-lead)' }}>{soldOut ? 'Sold out' : price}</div>
    </Tile>
  );
}
