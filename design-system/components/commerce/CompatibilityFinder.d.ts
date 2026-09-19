import * as React from 'react';
export interface FinderModel { id: string; label?: string }
export interface FinderPart {
  title: string;
  /** Model ids this part fits, or ['ALL'] for universal accessories. */
  fits: string[];
  price?: string;
  soldOut?: boolean;
}
export interface CompatibilityFinderProps {
  models?: FinderModel[];
  parts?: FinderPart[];
  onSelect?: (modelId: string) => void;
  style?: React.CSSProperties;
}
export declare function CompatibilityFinder(props: CompatibilityFinderProps): JSX.Element;
