export interface RangeModel { id: string; electric?: boolean; price?: string; href?: string }
export interface RangeTileProps { n?: string; label?: string; models?: RangeModel[]; span?: 2 | 3 }
export declare function RangeTile(props: RangeTileProps): JSX.Element;
