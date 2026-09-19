import React from 'react';
import { Stat } from '../core/Stat.jsx';
import { DotBars } from '../core/DotMatrix.jsx';

// The product-page block the rebrand exists for: specs reported as telemetry.
export function SpecPanel({ specs = [], style }) {
  return (
    <section style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit,minmax(220px,1fr))', gap: 'var(--grid-gap)', ...style }}>
      {specs.map((s, i) => (
        <Stat key={s.label} index={String(i + 1).padStart(2, '0')} label={s.label}
          value={s.value} unit={s.unit} note={s.note} footer={s.footer || []}>
          {s.levels && <DotBars levels={s.levels} />}
        </Stat>
      ))}
    </section>
  );
}
