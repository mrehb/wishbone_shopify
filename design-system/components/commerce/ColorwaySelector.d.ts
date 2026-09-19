import * as React from 'react';
export interface ColorwaySelectorProps {
  /** Catalogue colourway handles: charcoal-black, charcoal-lime, charcoal-red, white-red. */
  options?: string[];
  value?: string;
  onChange?: (value: string) => void;
  style?: React.CSSProperties;
}
export declare function ColorwaySelector(props: ColorwaySelectorProps): JSX.Element;
