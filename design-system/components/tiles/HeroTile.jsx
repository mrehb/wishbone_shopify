import React from 'react';
import { Tile } from '../primitives/Tile.jsx';
import { Dots, wave } from '../primitives/Dots.jsx';
import { Pill } from '../primitives/Pill.jsx';
import { silhouette } from '../primitives/Silhouettes.jsx';

// The opening tile. Spans the board. Name, one sentence, one action, the silhouette.
export function HeroTile({ n = '01', label = 'Wishbone', title, copy, cta, secondary, model, stats = [], span = 3 }) {
  const s = model ? silhouette(model, true) : wave(72, 9);
  return (
    <Tile n={n} label={label} span={span} hot>
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 24, alignItems: 'center' }}>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 18 }}>
          <h1 className="cursor" style={{ fontSize: 'var(--fs-hero)' }}>{title}</h1>
          {copy && <p style={{ fontSize: 'var(--fs-lead)', maxWidth: '30ch' }}>{copy}</p>}
          <div style={{ display: 'flex', gap: 10, flexWrap: 'wrap' }}>
            {cta && <Pill kind="button">{cta}</Pill>}{secondary && <Pill kind="ghost">{secondary}</Pill>}
          </div>
          {stats.length > 0 && (
            <div style={{ display: 'flex', gap: 28, flexWrap: 'wrap', marginTop: 6 }}>
              {stats.map((st) => (
                <div key={st.label}>
                  <div className="label">{st.label}</div>
                  <div style={{ fontSize: 'var(--fs-h)', marginTop: 4, color: st.value === '—' ? 'var(--grey)' : 'var(--white)' }}>{st.value}</div>
                </div>
              ))}
            </div>
          )}
        </div>
        <div style={{ display: 'flex', justifyContent: 'center' }}><Dots {...s} /></div>
      </div>
    </Tile>
  );
}
