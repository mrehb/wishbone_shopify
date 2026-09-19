export interface ProductTileProps {
  n?: string; model: string; title: string; type?: string; price?: string;
  status?: string; hot?: boolean; soldOut?: boolean;
}
export declare function ProductTile(props: ProductTileProps): JSX.Element;
