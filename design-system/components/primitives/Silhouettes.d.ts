import { DotGrid } from './Dots';
export declare const EON_S: DotGrid;
export declare const EON_L: DotGrid;
export declare function outline(electric?: boolean, cols?: number, rows?: number): DotGrid;
/** Sampled grid for EON; procedural outline for the others until they are photographed. */
export declare function silhouette(id: string, large?: boolean): DotGrid;
