import * as React from 'react';
export interface ProductCardProps {
  title: string;
  type?: string;
  price?: string;
  image?: string;
  badge?: 'live' | 'best' | 'soldout' | 'spare';
  soldOut?: boolean;
  /** Optional media-well content — usually a DotMatrix silhouette. */
  children?: React.ReactNode;
  style?: React.CSSProperties;
}
export declare function ProductCard(props: ProductCardProps): JSX.Element;
