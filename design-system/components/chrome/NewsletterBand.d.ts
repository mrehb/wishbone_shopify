import * as React from 'react';
export interface NewsletterBandProps {
  heading?: string;
  /** "ink" on the page, "volt" for the one loud band per journey. */
  tone?: 'ink' | 'volt';
  style?: React.CSSProperties;
}
export declare function NewsletterBand(props: NewsletterBandProps): JSX.Element;
