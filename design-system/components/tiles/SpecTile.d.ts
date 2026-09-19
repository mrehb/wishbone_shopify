export interface SpecTileProps {
  n?: string; label: string; value?: string; unit?: string; note?: string;
  /** dot bars */ levels?: number[];
  /** ring gauge 0..1 */ pct?: number;
  footer?: { label: string; value: string }[];
}
export declare function SpecTile(props: SpecTileProps): JSX.Element;
