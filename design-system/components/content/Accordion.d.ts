import * as React from 'react';
export interface AccordionItem { q: string; a: React.ReactNode }
export interface AccordionProps { items?: AccordionItem[]; index?: string; title?: string; style?: React.CSSProperties }
export declare function Accordion(props: AccordionProps): JSX.Element;
