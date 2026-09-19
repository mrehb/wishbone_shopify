export interface CompatModel { id: string }
export interface CompatPart { title: string; fits: string[]; price?: string; soldOut?: boolean }
export interface CompatTileProps { n?: string; models?: CompatModel[]; parts?: CompatPart[]; span?: 2 | 3 }
export declare function CompatTile(props: CompatTileProps): JSX.Element;
