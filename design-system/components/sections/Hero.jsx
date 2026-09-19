import React from 'react';
import { Eyebrow } from '../primitives/Eyebrow.jsx';
import { Display } from '../primitives/Display.jsx';
import { Button } from '../primitives/Button.jsx';
import { Photo } from '../primitives/Silhouette.jsx';

// The opening band, as the reference: eyebrow, a three-line headline, one sentence, two buttons
// and a slide index, with the product large on the right, on mist. `slides` is the model list.
export function Hero({ eyebrow = 'The lightest way round', lines = ['Light.', 'Simple.', 'British.'], copy, cta = 'Shop EON', secondary = 'Compare models', src, model = 'EON', slides = ['ONE', 'TWO', 'THREE', 'NEO', 'EON'], active = 4 }) {
  return (
    <section className="band band--mist" style={{ padding: 0, overflow: 'hidden' }}>
      <div className="container grid" style={{ alignItems: 'center', minHeight: 620 }}>
        <div style={{ gridColumn: 'span 5', padding: '64px 0', display: 'grid', gap: 28 }}>
          <Eyebrow n="01">{eyebrow}</Eyebrow>
          <Display lines={lines} size="hero" as="h1" />
          {copy && <p className="lead grey" style={{ maxWidth: '36ch' }}>{copy}</p>}
          <div style={{ display: 'flex', gap: 12, flexWrap: 'wrap' }}><Button kind="lime" arrow>{cta}</Button><Button kind="outline" arrow>{secondary}</Button></div>
          <ol className="label grey" style={{ display: 'flex', gap: 20, listStyle: 'none', padding: 0, marginTop: 20 }}>
            {slides.map((s, i) => <li key={s} style={{ paddingBottom: 8, borderBottom: `2px solid ${i === active ? 'var(--lime)' : 'transparent'}`, color: i === active ? 'var(--ink)' : undefined }}>{String(i + 1).padStart(2, '0')}</li>)}
          </ol>
        </div>
        <div style={{ gridColumn: '7 / span 6', alignSelf: 'stretch', display: 'flex', alignItems: 'center' }}>
          <Photo src={src} model={model} alt={`Wishbone ${model}`} ratio={1} large style={{ width: '100%', background: 'transparent' }} />
        </div>
      </div>
    </section>
  );
}
