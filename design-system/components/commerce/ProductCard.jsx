import React from 'react';
import { Badge } from '../core/Badge.jsx';

// v2: soft card, warm surface, mono price. The image well can hold a photo or a DotMatrix.
export function ProductCard({ title, type, price, image, badge, soldOut = false, children, style }) {
  return (
    <article style={{
      background: 'var(--surface-card)', border: '1px solid var(--color-border)',
      borderRadius: 'var(--radius-card)', overflow: 'hidden', boxShadow: 'none',
      opacity: soldOut ? 0.6 : 1, ...style,
    }}>
      <div style={{
        aspectRatio: '4 / 3', margin: 10, borderRadius: 'var(--radius-media)',
        background: image ? `center/cover url(${image})` : 'radial-gradient(90% 70% at 20% 0%, #23252c, #121318)',
        display: 'flex', alignItems: children ? 'center' : 'flex-end', justifyContent: children ? 'center' : 'flex-start',
        padding: 14, overflow: 'hidden',
      }}>{children || (badge && <Badge kind={badge} />)}</div>
      <div style={{ padding: '6px 20px 20px' }}>
        <h4 style={{ fontFamily: 'var(--font-display)', fontWeight: 500, fontSize: 18, margin: 0, letterSpacing: '-0.01em' }}>{title}</h4>
        {type && <div style={{ fontFamily: 'var(--font-mono)', fontSize: 11, letterSpacing: '0.16em', textTransform: 'uppercase', color: 'var(--text-muted)', margin: '7px 0 12px' }}>{type}</div>}
        <div style={{ fontFamily: 'var(--font-mono)', fontSize: 18 }}>{soldOut ? 'Sold out' : price}</div>
      </div>
    </article>
  );
}
