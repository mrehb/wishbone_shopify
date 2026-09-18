import React from 'react';
import { Button } from '../core/Button.jsx';
import { Input } from '../core/Input.jsx';

// Full-width band. Volt variant is the one place the brand shouts — ink type only.
export function NewsletterBand({ heading = 'Join the Wishbone list', tone = 'ink', style }) {
  const onVolt = tone === 'volt';
  return (
    <section style={{
      background: onVolt ? 'var(--color-volt)' : 'var(--color-ink)',
      color: onVolt ? 'var(--color-ink)' : 'var(--color-white)',
      borderTop: onVolt ? 'none' : '1px solid var(--color-border-soft)',
      padding: 'var(--space-section) 24px', ...style,
    }}>
      <h3 style={{ fontFamily: 'var(--font-heading)', fontWeight: 500, textTransform: 'uppercase', fontSize: 25, margin: 0 }}>{heading}</h3>
      <p style={{ margin: '10px 0 18px', maxWidth: '48ch', fontSize: 14 }}>
        New models, spare-part restocks and nothing else. Unsubscribe in one click.
      </p>
      <div style={{ display: 'flex', maxWidth: 480 }}>
        <Input placeholder="Email address" style={{ flex: 1 }} />
        <Button variant={onVolt ? 'invert' : 'primary'} style={{ alignSelf: 'flex-end' }}>Sign up</Button>
      </div>
    </section>
  );
}
