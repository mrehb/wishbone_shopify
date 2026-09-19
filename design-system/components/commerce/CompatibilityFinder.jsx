import React, { useState } from 'react';
import { VariantPill } from '../core/VariantPill.jsx';

// The most important commerce component in this catalogue: 22 of 27 products are
// spare parts named `Component (MODEL)`. A customer arrives knowing their trolley,
// not the part number. Pick the model, see only what fits.
export function CompatibilityFinder({ models = [], parts = [], onSelect, style }) {
  const [model, setModel] = useState(models[0]?.id || null);
  const fits = parts.filter((p) => p.fits.includes(model) || p.fits.includes('ALL'));
  const active = models.find((m) => m.id === model);
  return (
    <section style={{ background: 'var(--surface-card)', border: '1px solid var(--color-border)', borderRadius: 'var(--radius-card)', padding: '24px 26px', ...style }}>
      <div style={{ fontFamily: 'var(--font-mono)', fontSize: 11, letterSpacing: '0.18em', textTransform: 'uppercase', color: 'var(--text-muted)' }}>
        <b style={{ color: 'var(--color-volt)', fontWeight: 400 }}>01</b>&nbsp;&nbsp;Which trolley do you have?
      </div>
      <div style={{ display: 'flex', gap: 10, flexWrap: 'wrap', margin: '16px 0 20px' }}>
        {models.map((m) => (
          <VariantPill key={m.id} selected={m.id === model} onClick={() => { setModel(m.id); onSelect && onSelect(m.id); }}>
            {m.id}
          </VariantPill>
        ))}
      </div>
      <div style={{ display: 'flex', alignItems: 'baseline', gap: 10, borderTop: '1px solid var(--color-border)', paddingTop: 18 }}>
        <span style={{ fontFamily: 'var(--font-mono)', fontSize: 32, lineHeight: 1 }}>{String(fits.length).padStart(2, '0')}</span>
        <span style={{ color: 'var(--text-muted)', fontSize: 13.5 }}>
          parts fit the {active ? active.label || active.id : '—'}
        </span>
      </div>
      <ul style={{ listStyle: 'none', padding: 0, margin: '16px 0 0', display: 'grid', gap: 1 }}>
        {fits.map((p) => (
          <li key={p.title} style={{ display: 'flex', justifyContent: 'space-between', gap: 16, padding: '11px 0', borderBottom: '1px solid var(--color-border)', fontSize: 14 }}>
            <span>{p.title}{p.fits.includes('ALL') && <span style={{ color: 'var(--text-muted)', fontSize: 12 }}> · fits every model</span>}</span>
            <span style={{ fontFamily: 'var(--font-mono)', whiteSpace: 'nowrap', color: p.soldOut ? 'var(--text-muted)' : 'var(--color-white)' }}>
              {p.soldOut ? 'Sold out' : p.price}
            </span>
          </li>
        ))}
        {fits.length === 0 && (
          <li style={{ color: 'var(--text-muted)', fontSize: 14, padding: '11px 0' }}>
            No parts listed for this model yet. Contact us with your serial number and we will find it.
          </li>
        )}
      </ul>
    </section>
  );
}
