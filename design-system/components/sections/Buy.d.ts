export interface BuyImage { src: string; alt?: string }
export function Buy(props: { model?: string; type?: string; price?: string | null; colourways?: string[]; images?: (string | BuyImage)[]; copy?: string; delivery?: string; parts?: number; soldOut?: boolean; facts?: { label: string; value: string }[] }): JSX.Element;
