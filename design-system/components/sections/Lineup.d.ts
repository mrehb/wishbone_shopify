export interface LineupItem { id: string; type: string; price?: string | null; src?: string }
export function Lineup(props: { n?: string; eyebrow?: string; lines?: string[]; copy?: string; cta?: string; items: LineupItem[] }): JSX.Element;
