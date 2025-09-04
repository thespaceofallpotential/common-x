import { IOptions } from "./Options.ts";
import { IRange, IRanges, Range, toRanges } from "./Range.ts";
import { Position, Token, Word } from "./Types.ts";

export const splitCommon = <T extends Token | Word>(a: IRange<T>, b: IRange<T>, options?: IOptions): [aRa: IRange<T>[], bRa: IRange<T>[]] => {
    const crs = a.rs.intersection(b.rs);

    const aRa = toRanges(a, crs);
    const bRa = toRanges(b, crs);

    // deno-lint-ignore no-empty
    if (options) {
    }

    return [aRa, bRa];
};

export const splitAt = <T extends Token | Word>(r: IRange<T>, i: Position): IRange<T>[] => {
    const parts: IRange<T>[] = [new Range<T>(r.ra.slice(0, i), r.position), new Range<T>(r.ra.slice(i), r.position + i)];

    return parts.filter((x) => x.length > 0);
};

export const splitFrom = <T extends Token | Word>(r: IRange<T>, i: Position): IRange<T> => {
    const remainder: IRange<T> = new Range<T>(r.ra.slice(i), r.position + i);

    return remainder;
};

export const splitOnNewLine = <T extends Token | Word>(r: IRange<T>, newLine: T): IRanges<T> => {
    const items: IRanges<T> = [];

    const { ra } = r;

    let p: Position = 0;

    let i: Position = ra.indexOf(newLine);

    while (i > -1) {
        items.push(new Range<T>(ra.slice(p, i), p));

        p = i;

        i = ra.indexOf(newLine, i + 1);
    }

    if (p < ra.length) {
        items.push(new Range<T>(ra.slice(p), p));
    }

    return items;
};

// export const splitOnCommonTokenVectors = <T extends Token | Word>(a: IRange<T>, b: IRange<T>, options: IOptions): [aRa: IRange<T>[], bRa: IRange<T>[]] => {
//     const aTvm = createTokenVectorMap(a.ta as (number | undefined)[], a.position);

//     const bTvm = createTokenVectorMap(b.ta as (number | undefined)[], b.position);

//     const x2Tvm = aTvm.xIntersection(bTvm);

//     if (x2Tvm.size === 0) return [[], []];

//     const aSide = 0;
//     const bSide = 1;

//     const aPTvs = new PositiveTokenVectorSpace(x2Tvm, aSide).configure();
//     const aCTvs = new ContigousTokenVectorSpace(aPTvs, options).configure();

//     const aRa = sortTokenRange(aCTvs.toTRanges());

//     const bPTvs = new PositiveTokenVectorSpace(x2Tvm, bSide).configure();
//     const bCTvs = new ContigousTokenVectorSpace(bPTvs, options).configure();

//     const bRa = sortTokenRange(bCTvs.toTRanges());

//     return [aRa, bRa];
// };
