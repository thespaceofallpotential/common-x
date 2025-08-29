import { CommonRange } from "../core/CommonTypes.ts";
import { IRange } from "../core/Range.ts";
import { ISolver, Solver } from "../core/Solver.ts";
import { Position, Token, Word } from "../core/Types.ts";

class Memo<T extends Token | Word> {
    readonly cra: CommonRange<T>[] = [];

    prior: Map<Position, CommonRange<T>> = new Map();

    current: Map<Position, CommonRange<T>> = new Map();

    constructor(cra: CommonRange<T>[]) {
        this.cra = cra;
    }

    record = (ai: Position, bi: Position, av: T, bv: T): void => {
        if (av !== bv) return;

        const { prior, current, cra } = this;

        const update = (bi: number, av: T): boolean => {
            const existing = prior.get(bi - 1);

            if (!existing) return false;

            existing.ra.push(av);

            current.set(bi, existing);

            return true;
        };

        const create = (ai: Position, bi: Position, av: T): void => {
            const x: CommonRange<T> = { a: ai, b: bi, ra: [av] };

            cra.push(x);

            current.set(bi, x);
        };

        if (!update(bi, av)) create(ai, bi, av);
    };

    next = () => {
        this.prior = this.current;

        this.current = new Map();
    };
}

export class BruteForceSolver<T extends Token | Word> extends Solver<T> {
    readonly cra: CommonRange<T>[] = [];

    constructor(a: IRange<T>, b: IRange<T>) {
        super(a, b);
    }

    public override process = (): ISolver<T> => {
        const { a, b, step, cra } = this;

        const memo = new Memo(cra);

        for (let ai = 0; ai < a.ra.length; ai++) {
            const av = a.ra[ai];

            for (let bi = 0; bi < b.ra.length; bi++) {
                const bv = b.ra[bi];

                memo.record(a.position + ai, b.position + bi, av, bv);

                step();
            }

            memo.next();
        }

        return this;
    };
}
