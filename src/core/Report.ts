import { CommonRange } from "./CommonTypes.ts";
import { COMMA, NEW_LINE, Position, PositionPair, Report, SPACE, Word } from "./Types.ts";

const toReport = (ranges: CommonRange<Word>[]): Report => {
    const report: Report = new Map();

    ranges.forEach((x) => {
        const value = x.ra.join(SPACE);

        const positions: PositionPair = { a: new Set([x.a]), b: new Set([x.b]) };

        const current = report.get(value);

        if (current) {
            current.a.add(x.a);
            current.b.add(x.b);
        } else {
            report.set(value, positions);
        }
    });

    return report;
};

const toList = (x: Set<Position>): string => [...x].sort((a, b) => a - b).join(COMMA);

const describe = (x: [string, PositionPair]) => `${x[0]} -- (a:${toList(x[1].a)} ; b:${toList(x[1].b)}) (${x[1].a.size} | ${x[1].b.size})`;

const describeReport = (report: Report) => [...report.entries()].map((x) => describe(x)).join(NEW_LINE);

export const describeWordRanges = (ranges: CommonRange<Word>[], cost: number, summary: boolean = false) => {
    ranges.sort((a, b) => b.ra.length - a.ra.length);

    const report = toReport(ranges);

    const rangeDescription = ranges.map((x) => `a:${x.a} b:${x.b} s:${x.ra.join(SPACE)}`).join(NEW_LINE);

    const reportDescription = describeReport(report);

    console.log(`count:${report.size} -- (unique ranges:${ranges.length}) -- cost:${cost}`);

    if (summary) return;

    console.log(NEW_LINE);

    console.log(rangeDescription);

    console.log(reportDescription);
};
