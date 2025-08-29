import { CommonRange } from "../core/CommonTypes.ts";
import { IRange, toRanges } from "../core/Range.ts";
import { ISolver, Solver } from "../core/Solver.ts";
import { Token, Word } from "../core/Types.ts";
import { BruteForceSolver } from "./BruteForceSolver.ts";

export class ProjectionSolver<T extends Token | Word> extends Solver<T> {
    readonly cra: CommonRange<T>[] = [];

    constructor(a: IRange<T>, b: IRange<T>) {
        super(a, b);
    }

    public override process = (): ISolver<T> => {
        const { a, b, step, cra } = this;

        const crs = a.rs.intersection(b.rs); // +ve

        const aRa = toRanges(a, crs);

        const bRa = toRanges(b, crs);

        for (let ai = 0; ai < aRa.length; ai++) {
            const ar = aRa[ai];

            for (let bi = 0; bi < bRa.length; bi++) {
                const br = bRa[bi];

                const brute = new BruteForceSolver<T>(ar, br);

                brute.process();

                cra.push(...brute.cra);

                step(brute.cost);
            }
        }

        return this;
    };
}
