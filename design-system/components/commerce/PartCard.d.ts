import * as React from 'react';
export interface PartCardProps {
  /** Full catalogue title including the (MODEL) suffix — never trimmed. */
  title: string;
  price?: string;
  /** Model chips: ["ONE","NEO"] or ["ALL"]. */
  fits?: string[];
  image?: string;
  soldOut?: boolean;
  style?: React.CSSProperties;
}
export declare function PartCard(props: PartCardProps): JSX.Element;
