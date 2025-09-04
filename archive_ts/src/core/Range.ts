import { getPositionVectors } from "./helpers.ts";
import { IRangeVector, RangeVector } from "./RangeVector.ts";
import { PositionVector, Token, TypeArray, TypeSet, Word } from "./Types.ts";

export interface IRange<T extends Token | Word> extends IRangeVector {
    /**
     * Range Array
     */
    readonly ra: TypeArray<T>;

    /**
     * Range Set
     */
    readonly rs: TypeSet<T>;
}

export type IRanges<T extends Token | Word> = IRange<T>[];

export class Range<T extends Token | Word> extends RangeVector implements IRange<T> {
    readonly ra: Readonly<TypeArray<T>> = [];

    readonly rs: Readonly<TypeSet<T>> = new Set();

    constructor(ra: Readonly<TypeArray<T>>, position: number = 0, rs?: TypeSet<T>) {
        super(position, ra.length);

        this.ra = ra;

        this.rs = rs ? rs : new Set(ra);
    }
}

export const toRange = <T extends Token | Word>(r: IRange<T>, v: PositionVector): IRange<T> => new Range(r.ra.slice(v.p, v.p + v.l), v.p);

export const toRanges = <T extends Token | Word>(r: IRange<T>, crs: TypeSet<T>): IRange<T>[] => {
    const rva = getPositionVectors(r.ra, crs); // +ve

    return rva.map((x) => toRange(r, x));
};
