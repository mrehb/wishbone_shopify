export interface CompareModel { id: string; type: string; price?: string | null; src?: string }
export function Compare(props: { n?: string; eyebrow?: string; lines?: string[]; models: CompareModel[]; rows: { label: string; values: Record<string, string | undefined> }[]; highlight?: string }): JSX.Element;
