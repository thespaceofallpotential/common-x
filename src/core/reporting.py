from core.range import PartitionVector, Range
from core.strings import space
from core.types import CommonRange
from typing import List, TypeVar, cast

T = TypeVar("T", int, str)


def values[T](values: List[T]) -> str:
    return str.join(space, cast(List[str], values))


def rangeValueString[T](r: Range) -> str:
    return values(cast(List[str], r.values))


def partitionString[T](r: Range) -> str:
    return f"p:{r.position} v:{rangeValueString(r)}"


def commonPartitionString[T](r: CommonRange) -> str:
    return f"a:{r.aPosition} b:{r.bPosition} v:{values(r.values)}"


def vectorString[T](pv: PartitionVector) -> str:
    return f"[{pv.position},{pv.length}]"


def vectorsString[T](a: PartitionVector, b: PartitionVector) -> str:
    return f"a:{vectorString(a)} | b:{vectorString(b)}"


# import { CommonRange } from "./CommonTypes.ts";
# import { COMMA, COMMA_SEPARATOR, NEW_LINE, Position, PositionPair, Report, SPACE, Word } from "./Types.ts";

# const toReport = (ranges: CommonRange<Word>[]): Report => {
#     const report: Report = new Map();

#     ranges.forEach((x) => {
#         const value = x.ra.join(SPACE);

#         const positions: PositionPair = { a: new Set([x.a]), b: new Set([x.b]) };

#         const current = report.get(value);

#         if (current) {
#             current.a.add(x.a);
#             current.b.add(x.b);
#         } else {
#             report.set(value, positions);
#         }
#     });

#     return report;
# };

# const toList = (x: Set<Position>): string => [...x].sort((a, b) => a - b).join(COMMA);

# const describe = (x: [string, PositionPair]) => `${x[0]} -- (a:${toList(x[1].a)} ; b:${toList(x[1].b)}) (${x[1].a.size} | ${x[1].b.size})`;

# const describeReport = (report: Report) => [...report.entries()].map((x) => describe(x)).join(NEW_LINE);

# export const describeWordRanges = (ranges: CommonRange<Word>[], cost: number, summary: boolean = false) => {
#     ranges.sort((a, b) => b.ra.length - a.ra.length);

#     const report = toReport(ranges);

#     const rangeDescription = ranges.map((x) => `a:${x.a} b:${x.b} s:${x.ra.join(SPACE)}`).join(NEW_LINE);

#     const reportDescription = describeReport(report);

#     console.log(`count:${report.size} -- (unique ranges:${ranges.length}) -- cost:${cost}`);

#     if (summary) return;

#     console.log(NEW_LINE);

#     console.log(rangeDescription);

#     console.log(reportDescription);
# };

# export const topics = (x: object): string[] => Object.keys(x);

# export const topicListInline = (x: object): string => topics(x).join(COMMA_SEPARATOR);
