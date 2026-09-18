import * as React from 'react';
export interface SiteHeaderProps {
  links?: string[];
  cartCount?: number;
  style?: React.CSSProperties;
}
export declare function SiteHeader(props: SiteHeaderProps): JSX.Element;
