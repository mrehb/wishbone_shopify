import React, { useState } from 'react';

// Real colourways from the catalogue: charcoal-black, charcoal-lime, charcoal-red, white-red.
// Two-tone products need two-tone swatches — a single dot lies about the object.
const SWATCHES = {
  'charcoal-black': ['#2b2b2e', '#0f1014'],
  'charcoal-lime':  ['#2b2b2e', '#b4fa6e'],
  'charcoal-red':   ['#2b2b2e', '#c0392b'],
  'white-red':      ['#f2f2f2', '#c0392b'],
};

export function ColorwaySelector({ options = [], value, onChange, style }) {
  const [sel, setSel] = useState(value || options[0]);
  const pick = (o) => { setSel(o); onChange && onChange(o); };
  return (
    <div style={style}>
      <div style={{ fontFamily: 'var(--font-mono)', fontSize: 11, letterSpacing: '0.18em', textTransform: 'uppercase', color: 'var(--text-muted)' }}>
        Colourway · <span style={{ color: 'var(--color-white)' }}>{sel}</span>
      </div>
      <div style={{ display: 'flex', gap: 10, marginTop: 12 }}>
        {options.map((o) => {
          const [a, b] = SWATCHES[o] || ['#2b2b2e', '#2b2b2e'];
          const on = o === sel;
          return (
            <button key={o} onClick={() => pick(o)} aria-label={o} aria-pressed={on}
              style={{
                width: 38, height: 38, padding: 0, cursor: 'pointer', borderRadius: '50%',
                background: `linear-gradient(135deg, ${a} 0 50%, ${b} 50% 100%)`,
                border: `2px solid ${on ? 'var(--color-volt)' : 'transparent'}`,
                outline: on ? 'none' : '1px solid var(--color-border-strong)', outlineOffset: -1,
              }} />
          );
        })}
      </div>
    </div>
  );
}
