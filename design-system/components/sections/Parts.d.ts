export interface Part { title: string; fits: string[]; price?: string | null; src?: string }
export function Parts(props: { n?: string; eyebrow?: string; lines?: string[]; models?: string[]; items: Part[]; initial?: string }): JSX.Element;
