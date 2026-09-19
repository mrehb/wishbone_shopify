export interface BuyTileProps {
  n?: string; title: string; price: string;
  /** Catalogue handles: charcoal-black, charcoal-lime, charcoal-red, white-red */
  colourways?: string[]; delivery?: string;
  /** Number of parts listed for this model — the repairability promise as a number. */
  parts?: number; soldOut?: boolean; span?: 1 | 2;
}
export declare function BuyTile(props: BuyTileProps): JSX.Element;
