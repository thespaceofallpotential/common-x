import { CommonRange } from "../core/CommonTypes.ts";
import { getPositionVectors } from "../core/helpers.ts";
import { IRange } from "../core/Range.ts";
import { ISolver, Solver } from "../core/Solver.ts";
import { toSymmetricIndex } from "../core/SymmetricIndex.ts";
import { Position, Token, Word } from "../core/Types.ts";

// solving the common-substring problem while avoiding redundant time and space complexity of "negative-space"

export class CultivatedSolver<T extends Token | Word> extends Solver<T> {
    readonly cra: CommonRange<T>[] = [];

    constructor(a: IRange<T>, b: IRange<T>) {
        super(a, b);
    }

    public override process = (): ISolver<T> => {
        const { a, b, step, cra } = this;

        const crs = a.rs.intersection(b.rs); // +ve

        const aRa = getPositionVectors(a.ra, crs); // +ve

        const bXm = toSymmetricIndex(b.ra, crs); // +ve

        const pxpm: Map<Position, Map<Position, CommonRange<T>>> = new Map();

        for (let ri = 0; ri < aRa.length; ri++) {
            const range = aRa[ri];

            const origin = range.p;

            const xpm = pxpm.get(origin) ?? pxpm.set(origin, new Map()).get(origin);

            for (let pi = 0; pi < range.l; pi++) {
                const p = origin + pi;

                const value = a.ra[p];

                const xpa = bXm.get(value)!;

                for (let xi = 0; xi < xpa.length; xi++) {
                    const xp = xpa[xi];

                    const prior = xpm?.get(xp - 1);

                    if (prior) {
                        prior.ra.push(value);

                        xpm!.set(xp, prior);
                    } else {
                        const common: CommonRange<T> = { a: origin, b: xp, ra: [value] };

                        cra.push(common);

                        xpm!.set(xp, common);
                    }

                    step();
                }
            }
        }

        return this;
    };
}
