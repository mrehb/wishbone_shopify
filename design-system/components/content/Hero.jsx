import React from 'react';
import { Button } from '../core/Button.jsx';

// Page opener. A numbered label, the name, one sentence, one action, and a telemetry
// strip — so the first screen already reports values instead of making a claim.
export function Hero({ index = '01', eyebrow, title, copy, cta, secondary, stats = [], media, style }) {
  return (
    <section style={{
      position: 'relative', borderRadius: 'var(--radius-card)', overflow: 'hidden',
      background: 'radial-gradient(110% 90% at 8% -20%, rgb(242 210 171 / .22), transparent 62%), var(--surface-card)',
      border: '1px solid var(--color-border)', padding: '40px 34px', ...style,
    }}>
      <div style={{ display: 'grid', gridTemplateColumns: media ? '1.05fr .95fr' : '1fr', gap: 28, alignItems: 'center' }}>
        <div>
          <div style={{ fontFamily: 'var(--font-mono)', fontSize: 11, letterSpacing: '0.18em', textTransform: 'uppercase', color: 'var(--text-muted)' }}>
            <b style={{ color: 'var(--color-volt)', fontWeight: 400 }}>{index}</b>&nbsp;&nbsp;{eyebrow}
          </div>
          <h1 style={{ fontFamily: 'var(--font-display)', fontWeight: 500, fontSize: 48, letterSpacing: '-0.02em', margin: '16px 0 12px', lineHeight: 1.05 }}>{title}</h1>
          {copy && <p style={{ maxWidth: '46ch', margin: '0 0 22px', color: 'var(--color-white)' }}>{copy}</p>}
          <div style={{ display: 'flex', gap: 12, flexWrap: 'wrap' }}>
            {cta && <Button size="lg">{cta}</Button>}
            {secondary && <Button size="lg" variant="ghost">{secondary}</Button>}
          </div>
          {stats.length > 0 && (
            <div style={{ display: 'flex', gap: 30, marginTop: 28, flexWrap: 'wrap' }}>
              {stats.map((s) => (
                <div key={s.label}>
                  <div style={{ fontFamily: 'var(--font-mono)', fontSize: 10, letterSpacing: '0.16em', textTransform: 'uppercase', color: 'var(--text-muted)' }}>{s.label}</div>
                  <div style={{ fontFamily: 'var(--font-mono)', fontSize: 26, marginTop: 5, color: s.value === '—' ? 'var(--text-muted)' : 'var(--color-white)' }}>{s.value}</div>
                </div>
              ))}
            </div>
          )}
        </div>
        {media && <div style={{ borderRadius: 'var(--radius-media)', overflow: 'hidden', display: 'flex', justifyContent: 'center' }}>{media}</div>}
      </div>
    </section>
  );
}
