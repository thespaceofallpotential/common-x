import { CommonPoint, CommonPoints } from "../../core/CommonTypes.ts";
import { IRange } from "../../core/Range.ts";
import { ISolver, Solver } from "../../core/Solver.ts";
import { toSymmetricIndex } from "../../core/SymmetricIndex.ts";
import { Token, Word } from "../../core/Types.ts";

export class ConstituientSolver<T extends Token | Word> extends Solver<T> {
    readonly cPa: CommonPoints<T> = [];

    constructor(a: IRange<T>, b: IRange<T>) {
        super(a, b);
    }

    public override process = (): ISolver<T> => {
        const { a, b, step, cPa } = this;

        const crs = a.rs.intersection(b.rs); // +ve common (primitive) set

        const aPpam = toSymmetricIndex(a.ra, crs); // +ve
        const bPpam = toSymmetricIndex(b.ra, crs); // +ve

        const cra = [...crs]; // +ve common (primitive) array

        for (let ci = 0; ci < cra.length; ci++) {
            const value = cra[ci];

            const apa = aPpam.get(value)!;
            const bpa = bPpam.get(value)!;

            for (let ai = 0; ai < apa.length; ai++) {
                for (let bi = 0; bi < bpa.length; bi++) {
                    const ap = apa[ai];
                    const bp = bpa[bi];

                    const cp: CommonPoint<T> = [ap, bp, value];

                    cPa.push(cp);

                    step();
                }
            }
        }

        return this;
    };
}
