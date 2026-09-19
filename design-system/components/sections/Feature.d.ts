export interface Fact { label: string; value: string }
export function Feature(props: { n?: string; eyebrow?: string; lines?: string[]; copy?: string; cta?: string; facts?: Fact[]; src?: string; model?: string; tone?: 'paper' | 'mist' | 'ink'; flip?: boolean; ratio?: number }): JSX.Element;
