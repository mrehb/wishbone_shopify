import * as React from 'react';
export interface ProductCardProps {
  /** Full product name. Spare parts keep their `Component (MODEL)` form. */
  title: string;
  /** Short descriptor: "Electric trolley", "Manual trolley", "Spare part". */
  type?: string;
  /** Formatted with the store's locale: "799,00 €". */
  price?: string;
  image?: string;
  badge?: 'bestseller' | 'new' | 'soldout' | 'spare';
  soldOut?: boolean;
  style?: React.CSSProperties;
}
export declare function ProductCard(props: ProductCardProps): JSX.Element;
