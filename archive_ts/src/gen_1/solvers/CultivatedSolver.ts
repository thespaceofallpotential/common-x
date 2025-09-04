import { CommonRange } from "../../core/CommonTypes.ts";
import { getPositionVectors } from "../../core/helpers.ts";
import { IRange } from "../../core/Range.ts";
import { ISolver, Solver } from "../../core/Solver.ts";
import { toSymmetricIndex } from "../../core/SymmetricIndex.ts";
import { Position, Token, Word } from "../../core/Types.ts";

// solving the common-substring problem while avoiding redundant time and space complexity of "negative-space"

export class CultivatedSolver<T extends Token | Word> extends Solver<T> {
    readonly cra: CommonRange<T>[] = [];

    constructor(a: IRange<T>, b: IRange<T>) {
        super(a, b);
    }

    public override process = (): ISolver<T> => {
        const { a, b, step, cra } = this;

        const crs = a.rs.intersection(b.rs); // +ve: a b symmetry -- document-level

        const aRa = getPositionVectors(a.ra, crs); // +ve: document-level -> numeric record-level index array

        const bXm = toSymmetricIndex(b.ra, crs); // +ve: document-level -> symmetric record-level map

        /**
         * in both numeric and symmetric cases, document-level to record-level indexes/maps, represent 
         * "interdimensional-relationships", which can determined cheaply (in lower-dimensions), 
         * and used to "interrogate and navigate higher-dimensional spaces at lower-dimensional cost"
         */
 
        const progress: Map<Position, CommonRange<T>> = new Map();

        for (let ri = 0; ri < aRa.length; ri++) {
            const range = aRa[ri];

            const origin = range.p;

            for (let pi = 0; pi < range.l; pi++) {
                const p = origin + pi;

                const value = a.ra[p];

                const xpa = bXm.get(value)!;

                for (let xi = 0; xi < xpa.length; xi++) {
                    const xp = xpa[xi];

                    const prior = progress.get(xp - 1);

                    if (prior) {
                        prior.ra.push(value);

                        progress.set(xp, prior);
                    } else {
                        const common: CommonRange<T> = { a: origin, b: xp, ra: [value] };

                        cra.push(common);

                        progress.set(xp, common);
                    }

                    step();
                }
            }

            progress.clear();
        }

        return this;
    };
}
