export interface CompareRow { label: string; values: Record<string, string> }
export interface CompareTileProps { n?: string; models?: { id: string }[]; rows?: CompareRow[]; highlight?: string; span?: 2 | 3 }
export declare function CompareTile(props: CompareTileProps): JSX.Element;
