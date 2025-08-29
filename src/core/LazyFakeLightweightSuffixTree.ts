import { CommonRange } from "./CommonTypes.ts";
import { IRange } from "./Range.ts";
import { SymmetricIndex, toSymmetricIndex } from "./SymmetricIndex.ts";
import { PositionArray, Token, TypeArray, Word } from "./Types.ts";
import { strictParser } from "./helpers.ts";

export class LazyFakeLightweightSuffixTree<T extends Token | Word> {
    readonly ra: TypeArray<T>;

    readonly rssi: SymmetricIndex<T>;

    readonly cache: Map<T, PositionArray<T>[]> | undefined;

    constructor(r: IRange<T>, cache: boolean = false) {
        this.ra = r.ra;

        this.rssi = toSymmetricIndex(r.ra, r.rs);

        if (cache) this.cache = new Map();
    }

    getSuffixes = (t: T): PositionArray<T>[] => {
        const { ra, rssi: rsii, cache } = this;

        if (cache?.has(t)) return cache.get(t)!;

        const sia = rsii.get(t);

        const pa = sia ? sia.map((p) => ({ p, ta: ra.slice(p) } as PositionArray<T>)) : [];

        cache?.set(t, pa);

        return pa;
    };
}

export class LazyFakeSuffixTree<T extends Token | Word> extends LazyFakeLightweightSuffixTree<T> {
    /**
     * rather than generate and pass all suffixes to caller,
     * check sequence internally
     * @param ta
     * @returns
     */
    check = (ta: TypeArray<T>): CommonRange<T>[] => {
        const cra: CommonRange<T>[] = [];

        const { ra, rssi: rsii } = this;

        for (let i = 0; i < ta.length; i++) {
            const t = ta[i];

            const sia = rsii.get(t);

            if (sia === undefined) continue;

            const remaining = ta.slice(i);

            for (let si = 0; si < sia.length - 1; si++) {
                const sp = sia[si];

                const sa = ra.slice(sp);

                const [common, _, __] = strictParser(i, sp, remaining, sa);

                if (common) cra.push(common);
            }
        }

        return cra;
    };
}
