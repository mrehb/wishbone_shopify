import React from 'react';
import { Badge } from '../core/Badge.jsx';

// Square image, square card, left-aligned text, hairline border at 10%.
// Mirrors the theme's card scheme: card_style "card", image padding 0, text left.
export function ProductCard({ title, type, price, image, badge, soldOut = false, style }) {
  return (
    <article style={{
      border: '1px solid var(--color-border-soft)', background: 'var(--surface-card)',
      borderRadius: 'var(--radius)', boxShadow: 'none', opacity: soldOut ? 0.55 : 1, ...style,
    }}>
      <div style={{
        aspectRatio: '1', background: image ? `center/cover url(${image})` : 'linear-gradient(135deg,#2b2b30,#141417)',
        display: 'flex', alignItems: 'flex-end', padding: 14,
      }}>{badge && <Badge kind={badge} />}</div>
      <div style={{ padding: 16 }}>
        <h4 style={{ fontFamily: 'var(--font-heading)', fontWeight: 500, textTransform: 'uppercase', fontSize: 16, margin: 0 }}>{title}</h4>
        {type && <div style={{ color: 'var(--text-muted)', fontSize: 13, margin: '4px 0 10px' }}>{type}</div>}
        <div style={{ fontWeight: 700 }}>{soldOut ? 'Sold out' : price}</div>
      </div>
    </article>
  );
}
