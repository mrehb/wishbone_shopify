import * as React from 'react';
export interface BadgeProps {
  kind?: 'bestseller' | 'new' | 'soldout' | 'spare';
  children?: React.ReactNode;
  style?: React.CSSProperties;
}
export declare function Badge(props: BadgeProps): JSX.Element;
