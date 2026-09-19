import React from 'react';
import { Eyebrow } from '../primitives/Eyebrow.jsx';
import { Display } from '../primitives/Display.jsx';
import { Button } from '../primitives/Button.jsx';
import { Field } from '../primitives/Field.jsx';

// The reference's inquiry band: copy left, an underlined form right, one ink button with an arrow.
// kind 'contact' has five fields; 'newsletter' has one.
export function Inquiry({ n = '06', eyebrow = 'Contact', lines = ['Ask us anything.'], copy = 'Parts, compatibility, delivery to your club. A person answers, usually the same day.', kind = 'contact', cta = 'Send' }) {
  return (
    <section className="band"><div className="container grid" style={{ alignItems: 'start' }}>
      <div style={{ gridColumn: 'span 4', display: 'grid', gap: 20 }}><Eyebrow n={n}>{eyebrow}</Eyebrow><Display lines={lines} size="s" /><p className="grey" style={{ maxWidth: '30ch' }}>{copy}</p></div>
      <form onSubmit={(e) => e.preventDefault()} style={{ gridColumn: '6 / span 7', display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '28px 32px' }}>
        {kind === 'contact' ? (<>
          <Field label="First name" /><Field label="Last name" />
          <Field label="Email" type="email" /><Field label="Phone" type="tel" />
          <Field label="Your trolley and question" multiline style={{ gridColumn: 'span 2' }} />
        </>) : <Field label="Email" type="email" placeholder="you@example.com" style={{ gridColumn: 'span 2' }} />}
        <div style={{ gridColumn: 'span 2', display: 'flex', justifyContent: 'flex-end' }}><Button kind="ink" arrow>{cta}</Button></div>
      </form>
    </div></section>
  );
}
