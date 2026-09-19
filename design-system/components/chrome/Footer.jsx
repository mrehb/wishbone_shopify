import React from 'react';

// Monogram and four link columns on paper, the smallest type in the system, a hairline above
// and the legal line below. Social is written as words.
export function Footer({ columns, legal = '© 2026 Wishbone Golf. All rights reserved.', social = ['Instagram', 'YouTube', 'Facebook'] }) {
  const cols = columns || [
    { h: 'Trolleys', items: ['Wishbone ONE', 'Wishbone TWO', 'Wishbone THREE', 'Wishbone NEO', 'Wishbone EON', 'Compare'] },
    { h: 'Spare parts', items: ['Parts for ONE', 'Parts for TWO', 'Parts for THREE', 'Parts for NEO', 'Parts for EON'] },
    { h: 'Accessories', items: ['Umbrella holder', 'Drink holder', 'Scorecard holder', 'Ball & tee holder'] },
    { h: 'Company', items: ['About', 'Contact', 'Shipping', 'Warranty', 'Privacy'] },
  ];
  return (
    <footer className="band band--tight" style={{ borderTop: 'var(--hair-w) solid var(--hair)' }}>
      <div className="container">
        <div className="grid" style={{ alignItems: 'start' }}>
          <div style={{ gridColumn: 'span 4' }}><img src="../../assets/wishbone-monogram-ink.png" alt="Wishbone" style={{ width: 96 }} /><p className="grey" style={{ fontSize: 13, marginTop: 16, maxWidth: '28ch' }}>Birthed in Britain. Ultra-light aluminium golf trolleys and every part to keep them rolling.</p></div>
          {cols.map((c) => (
            <div key={c.h} style={{ gridColumn: 'span 2' }}>
              <div className="label" style={{ marginBottom: 14 }}>{c.h}</div>
              <ul style={{ listStyle: 'none', padding: 0, display: 'grid', gap: 8, fontSize: 13 }} className="grey">{c.items.map((i) => <li key={i}><a href="#">{i}</a></li>)}</ul>
            </div>
          ))}
        </div>
        <hr className="hair" style={{ margin: '40px 0 20px' }} />
        <div className="label grey" style={{ display: 'flex', justifyContent: 'space-between', flexWrap: 'wrap', gap: 16 }}>
          <span>{legal}</span><span style={{ display: 'flex', gap: 20 }}>{social.map((s) => <a key={s} href="#">{s}</a>)}</span>
        </div>
      </div>
    </footer>
  );
}
