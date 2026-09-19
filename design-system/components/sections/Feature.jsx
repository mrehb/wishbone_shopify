import React from 'react';
import { Eyebrow } from '../primitives/Eyebrow.jsx';
import { Display } from '../primitives/Display.jsx';
import { Button } from '../primitives/Button.jsx';
import { Photo } from '../primitives/Silhouette.jsx';

// One feature, two halves. tone 'ink' is the page's single dark band (the reference's battery
// section); 'paper' and 'mist' alternate. flip puts the image on the left. facts are three
// short label/value pairs under the copy.
export function Feature({ n, eyebrow, lines = [], copy, cta, facts = [], src, model, tone = 'paper', flip = false, ratio = 1.2 }) {
  const cls = 'band' + (tone === 'ink' ? ' band--ink' : tone === 'mist' ? ' band--mist' : '');
  const text = (
    <div style={{ gridColumn: 'span 5', display: 'grid', gap: 24, alignContent: 'center' }}>
      <Eyebrow n={n}>{eyebrow}</Eyebrow><Display lines={lines} />
      {copy && <p className="grey" style={{ maxWidth: '38ch' }}>{copy}</p>}
      {facts.length > 0 && (
        <dl style={{ display: 'grid', gridTemplateColumns: `repeat(${facts.length}, auto)`, gap: 32, justifyContent: 'start', margin: '8px 0 0' }}>
          {facts.map((f) => <div key={f.label}><dt className="num" style={{ fontSize: 'var(--fs-lead)', fontWeight: 'var(--w-ui)' }}>{f.value}</dt><dd className="label grey" style={{ margin: '6px 0 0' }}>{f.label}</dd></div>)}
        </dl>
      )}
      {cta && <div><Button kind={tone === 'ink' ? 'lime' : 'outline'} arrow>{cta}</Button></div>}
    </div>
  );
  const img = <div style={{ gridColumn: 'span 7' }}><Photo src={src} model={model} alt="" ratio={ratio} tone={tone === 'ink' ? 'paper' : 'ink'} large style={tone === 'mist' ? { background: 'transparent' } : undefined} /></div>;
  return <section className={cls}><div className="container grid" style={{ alignItems: 'center' }}>{flip ? <>{img}{text}</> : <>{text}{img}</>}</div></section>;
}
