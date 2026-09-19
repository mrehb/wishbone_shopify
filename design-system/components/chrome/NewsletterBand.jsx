import React from 'react';
import { Button } from '../core/Button.jsx';
import { Input } from '../core/Input.jsx';

// A soft panel rather than a full-bleed band — v2 is built from objects on a ground.
export function NewsletterBand({ heading = 'Telemetry, not marketing', style }) {
  return (
    <section style={{
      background: 'var(--surface-card)', border: '1px solid var(--color-border)',
      borderRadius: 'var(--radius-card)', padding: '32px 30px', ...style,
    }}>
      <div style={{ fontFamily: 'var(--font-mono)', fontSize: 11, letterSpacing: '0.18em', textTransform: 'uppercase', color: 'var(--text-muted)' }}>
        <b style={{ color: 'var(--color-volt)', fontWeight: 400 }}>05</b>&nbsp;&nbsp;The list
      </div>
      <h3 style={{ fontFamily: 'var(--font-display)', fontWeight: 500, fontSize: 23, margin: '14px 0 8px', letterSpacing: '-0.01em' }}>{heading}</h3>
      <p style={{ margin: '0 0 20px', maxWidth: '46ch', color: 'var(--text-muted)', fontSize: 14 }}>
        New models, spare-part restocks and firmware notes. Nothing else. Unsubscribe in one click.
      </p>
      <div style={{ display: 'flex', gap: 10, alignItems: 'flex-end', flexWrap: 'wrap' }}>
        <Input label="Email address" placeholder="you@example.com" style={{ flex: '1 1 240px' }} />
        <Button>Sign up</Button>
      </div>
    </section>
  );
}
