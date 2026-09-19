import React from 'react';

// The system line and the wordmark. Reads as a device header, because it is one.
export function TopBar({ status = 'All systems operational', links = ['Trolleys', 'Electric', 'Spare parts', 'Contact'], cart = 0 }) {
  const mono = { fontSize: 'var(--fs-label)', letterSpacing: 'var(--track-label)', textTransform: 'uppercase' };
  return (
    <header style={{ display: 'flex', flexDirection: 'column', gap: 14, padding: '18px 0 26px' }}>
      <div style={{ ...mono, display: 'flex', alignItems: 'center', gap: 10, color: 'var(--grey)' }}>
        <i style={{ width: 6, height: 6, borderRadius: '50%', background: 'var(--lime)' }} />{status}
      </div>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: 24, flexWrap: 'wrap' }}>
        <img src="../../assets/wishbone-wordmark.png" alt="Wishbone Golf" style={{ width: 200, maxWidth: '44%' }} />
        <nav style={{ ...mono, display: 'flex', gap: 22 }}>{links.map((l) => <a key={l} href="#" style={{ color: 'var(--white)', textDecoration: 'none' }}>{l}</a>)}</nav>
        <span style={{ ...mono, color: 'var(--lime)' }}>cart [{String(cart).padStart(2, '0')}]</span>
      </div>
    </header>
  );
}
