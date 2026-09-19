import React from 'react';
import { Button } from '../core/Button.jsx';
import { Badge } from '../core/Badge.jsx';

// The decision block. Price in the telemetry face, one primary action, and the two
// facts that actually close a trolley sale: is it in stock, and can I get parts later.
export function BuyBox({ title, price, was, badge, stock = 'in', delivery, partsNote, children, style }) {
  const soldOut = stock === 'out';
  return (
    <section style={{ display: 'flex', flexDirection: 'column', gap: 16, ...style }}>
      <div>
        {badge && <Badge kind={badge} style={{ marginBottom: 12 }} />}
        <h2 style={{ fontFamily: 'var(--font-display)', fontWeight: 500, fontSize: 32, margin: 0, letterSpacing: '-0.02em' }}>{title}</h2>
      </div>
      <div style={{ display: 'flex', alignItems: 'baseline', gap: 12 }}>
        <span style={{ fontFamily: 'var(--font-mono)', fontSize: 34, lineHeight: 1 }}>{price}</span>
        {was && <span style={{ fontFamily: 'var(--font-mono)', fontSize: 16, color: 'var(--text-muted)', textDecoration: 'line-through' }}>{was}</span>}
      </div>
      {children}
      <div>
        <Button size="lg" disabled={soldOut} style={{ width: '100%', justifyContent: 'center' }}>
          {soldOut ? 'Sold out' : 'Add to cart'}
        </Button>
      </div>
      <dl style={{ margin: 0, display: 'grid', gap: 8, fontSize: 13.5 }}>
        {delivery && (
          <div style={{ display: 'flex', gap: 10 }}>
            <dt style={{ fontFamily: 'var(--font-mono)', fontSize: 11, letterSpacing: '0.16em', textTransform: 'uppercase', color: 'var(--text-muted)', minWidth: 92 }}>Delivery</dt>
            <dd style={{ margin: 0 }}>{delivery}</dd>
          </div>
        )}
        {partsNote && (
          <div style={{ display: 'flex', gap: 10 }}>
            <dt style={{ fontFamily: 'var(--font-mono)', fontSize: 11, letterSpacing: '0.16em', textTransform: 'uppercase', color: 'var(--text-muted)', minWidth: 92 }}>Spare parts</dt>
            <dd style={{ margin: 0 }}>{partsNote}</dd>
          </div>
        )}
      </dl>
    </section>
  );
}
