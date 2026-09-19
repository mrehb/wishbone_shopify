import React from 'react';
import { Button } from '../primitives/Button.jsx';

// Wordmark left, nav centre, the one lime button right — as the reference. 72px tall, a hairline
// beneath. Cart is written, not drawn: `CART (2)`.
export function Header({ nav = ['Trolleys', 'Spare parts', 'Accessories', 'About', 'Contact'], cart = 0, cta = 'Shop EON', tone = 'paper' }) {
  const ink = tone === 'ink';
  return (
    <header style={{ background: ink ? 'var(--ink)' : 'var(--paper)', color: ink ? '#fafafa' : 'var(--ink)', borderBottom: `var(--hair-w) solid ${ink ? 'var(--hair-ink)' : 'var(--hair)'}` }}>
      <div className="container" style={{ display: 'flex', alignItems: 'center', height: 72, gap: 32 }}>
        <a href="/" aria-label="Wishbone Golf" style={{ flex: '0 0 auto' }}><img src={ink ? '../../assets/wishbone-wordmark.png' : '../../assets/wishbone-wordmark-ink.png'} alt="Wishbone Golf" style={{ height: 14, width: 'auto' }} /></a>
        <nav className="label" style={{ display: 'flex', gap: 28, margin: '0 auto' }}>{nav.map((n) => <a key={n} href="#">{n}</a>)}</nav>
        <a href="/cart" className="label" style={{ flex: '0 0 auto' }}>Cart ({cart})</a>
        <Button kind="lime" arrow style={{ flex: '0 0 auto', padding: '12px 20px' }}>{cta}</Button>
      </div>
    </header>
  );
}
