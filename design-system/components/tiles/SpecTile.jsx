import React from 'react';
import { Tile } from '../primitives/Tile.jsx';
import { Readout } from '../primitives/Readout.jsx';
import { Dots, bars, ring } from '../primitives/Dots.jsx';

// One specification, reported. A readout plus the dot graphic that suits it.
export function SpecTile({ n, label, value, unit, note, levels, pct, footer = [] }) {
  return (
    <Tile n={n} label={label}>
      <Readout value={value} unit={unit} note={note} />
      {levels && <Dots {...bars(levels, 7, 0.95)} />}
      {pct != null && <Dots {...ring(pct, 7)} />}
      {footer.length > 0 && (
        <div style={{ display: 'flex', gap: 22, borderTop: '1px solid var(--tile-line)', paddingTop: 12 }}>
          {footer.map((f) => <div key={f.label}><div className="label">{f.label}</div><div style={{ marginTop: 4 }}>{f.value}</div></div>)}
        </div>
      )}
    </Tile>
  );
}
