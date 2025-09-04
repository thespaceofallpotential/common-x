import { CommonRange } from "./CommonTypes.ts";
import { IRange } from "./Range.ts";
import { Position, PositionVector, Token, TypeArray, TypeSet, Word } from "./Types.ts";

export const getPositionVectors = <T extends Token | Word>(ra: TypeArray<T>, crs: TypeSet<T>): PositionVector[] => {
    const pva: PositionVector[] = [];

    let pv: PositionVector | undefined;

    for (let i = 0; i < ra.length; i++) {
        const f = ra[i];

        if (crs.has(f)) {
            if (pv === undefined) {
                pv = { p: i, l: 0 };

                pva.push(pv);
            }

            pv.l++;

            continue;
        }

        pv = undefined;
    }

    return pva;
};

export const toCommonRange = <T extends Token | Word>(a: IRange<T>, b: IRange<T>): [cr: CommonRange<T> | undefined, ai: number, bi: number] => {
    const cr: CommonRange<T> = { a: a.position, b: b.position, ra: [] };

    const unset = -1;

    for (let i = 0; i < a.ra.length; i++) {
        const at = a.ra[i];
        const bt = b.ra[i];

        if (i >= b.ra.length) return [cr, i, unset];

        if (at !== bt) return [undefined, i, i];

        cr.ra.push(at);
    }

    const ei = a.ra.length < b.ra.length ? a.ra.length : unset;

    return [cr, unset, ei];
};

export const strictParser = <T extends Token | Word>(ap: Position, bp: Position, ara: TypeArray<T>, bra: TypeArray<T>): [cr: CommonRange<T> | undefined, ai: number, bi: number] => {
    const cr: CommonRange<T> = { a: ap, b: bp, ra: [] };

    const unset = -1;

    for (let i = 0; i < ara.length; i++) {
        const at = ara[i];
        const bt = bra[i];

        if (i >= bra.length) return [cr, i, unset];

        if (at !== bt) return cr.ra.length > 0 ? [cr, i, i] : [undefined, i, i];

        cr.ra.push(at);
    }

    const ei = ara.length < bra.length ? ara.length : unset;

    return [undefined, unset, ei];
};
