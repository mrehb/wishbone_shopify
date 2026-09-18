import React from 'react';

// Transparent header on ink. Wordmark at 200px (the theme's logo_width), sparse nav.
export function SiteHeader({ links = ['Trolleys', 'Accessories', 'Spare parts', 'Contact'], cartCount = 0, style }) {
  return (
    <header style={{
      display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: 32,
      padding: '18px 24px', background: 'var(--color-ink)',
      borderBottom: '1px solid var(--color-border-soft)', ...style,
    }}>
      <img src="../../assets/wishbone-wordmark.png" alt="Wishbone Golf" style={{ width: 200, maxWidth: '40%' }} />
      <nav style={{ display: 'flex', gap: 24, fontSize: 13, letterSpacing: '0.06em', textTransform: 'uppercase' }}>
        {links.map((l) => <a key={l} href="#" style={{ color: 'var(--color-white)', textDecoration: 'none' }}>{l}</a>)}
      </nav>
      <span style={{ fontSize: 13, letterSpacing: '0.06em', textTransform: 'uppercase' }}>Cart ({cartCount})</span>
    </header>
  );
}
