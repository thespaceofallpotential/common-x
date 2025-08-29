import { Position, Token, TypeArray, TypeSet, Word } from "./Types.ts";

/**
 * Symmetric Index
 * 
 * > Map: a map is a lower-dimensional representation of arbitrarily-plural 
 * higher-dimensional form
 * 
 * A Symmetric-Index maps higher-dimensional form to index-keys which represent 
 * (that) indexed-form literally
 * 
 * In this way, a Symmetric-Index (or a map generally) represents and exploits 
 * symmetries-of-form (between arbitrarily-different phenomena/dimensional-spaces) 
 * to enable interrogation and navigation of higher-dimensions, at the 
 * (correspondingly lower) cost of lower-dimensional key-space (/representation-space)
 */
export type SymmetricIndex<T extends Token | Word> = Map<T, Array<Position>>;

export const toSymmetricIndex = <T extends Token | Word>(ra: TypeArray<T>, crs: TypeSet<T>): SymmetricIndex<T> => {
    const si: SymmetricIndex<T> = new Map();

    for (let i = 0; i < ra.length; i++) {
        const f = ra[i];

        if (!crs.has(f)) continue;

        if (!si.has(f)) {
            si.set(f, [i]);
        } else {
            si.get(f)!.push(i);
        }
    }

    return si;
};
