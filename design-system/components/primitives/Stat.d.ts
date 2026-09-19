export interface StatProps { value?: string | number | null; unit?: string; label: string; note?: string }
export function Stat(props: StatProps): JSX.Element;
export function StatRow(props: { items: StatProps[] }): JSX.Element;
