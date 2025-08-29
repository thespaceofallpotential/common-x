import { CommonRange } from "../core/CommonTypes.ts";
import { strictParser } from "../core/helpers.ts";
import { LazyFakeLightweightSuffixTree } from "../core/LazyFakeLightweightSuffixTree.ts";
import { IRange } from "../core/Range.ts";
import { ISolver, Solver } from "../core/Solver.ts";
import { aWr, bWr } from "../core/Source.ts";
import { Token, Word } from "../core/Types.ts";

/**
 * My intention was to implement and compare a generalised suffix-tree, but 
 * after reading the technical implementation, i came to my senses
 * 
 * In present form, the below implementation is a "lazily-evaluated uncompressed suffix-array"
 * 
 * A future revision will address compression seperately
 */

export class LazyFakeSuffixTreeSolver<T extends Token | Word> extends Solver<T> {
    readonly cra: CommonRange<T>[] = [];

    readonly lazyFake: LazyFakeLightweightSuffixTree<T>;

    constructor(a: IRange<T>, b: IRange<T>) {
        super(a, b);

        this.lazyFake = new LazyFakeLightweightSuffixTree(a);
    }

    public override process = (): ISolver<T> => {
        const { b, lazyFake, step, cra } = this;

        const bra = b.ra;

        // const ca = lazyFake.check(b.ra);

        for (let i = 0; i < bra.length; i++) {
            const t = bra[i];

            const remaining = bra.slice(i);

            // const ca = lazyFake.check(i, remaining);

            const spa = lazyFake.getSuffixes(t);

            for (let si = 0; si < spa.length; si++) {
                const pa = spa[si];

                const [common, axi, _bxi] = strictParser(i, pa.p, remaining, pa.ta);

                step(common ? common.ra.length : axi);

                if (common) cra.push(common);
            }
        }

        return this;
    };
}

const solver = new LazyFakeSuffixTreeSolver(aWr, bWr);

solver.process();

console.log(`${solver.lazyFake}`);
