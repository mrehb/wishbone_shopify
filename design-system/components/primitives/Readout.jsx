import React from 'react';

// A value the product reports. Big, mono, dot-matrix. Unknown prints "—".
export function Readout({ value, unit, note, size = 'var(--fs-readout)', style }) {
  const unknown = value === undefined || value === null || value === '' || value === '—';
  return (
    <div style={style}>
      <div style={{ display: 'flex', alignItems: 'baseline', gap: 8 }}>
        <span className="readout" style={{ fontSize: size, color: unknown ? 'var(--grey)' : 'var(--white)' }}>{unknown ? '—' : value}</span>
        {unit && !unknown && <span className="grey" style={{ fontSize: 'var(--fs-label)', letterSpacing: 'var(--track-label)', textTransform: 'uppercase' }}>{unit}</span>}
      </div>
      {note && <div className="grey" style={{ fontSize: 'var(--fs-label)', letterSpacing: '0.06em', marginTop: 6 }}>{unknown ? 'not yet measured' : note}</div>}
    </div>
  );
}
