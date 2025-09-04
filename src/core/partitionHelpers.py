from typing import List, Set, Tuple, TypeVar
from core.range import PartitionVector, Range
from core.vectors import getPartitionVectors


T = TypeVar("T", int, str)


def partition[T](r: Range, pv: PartitionVector) -> Range:

    i_start = pv.position - r.position
    i_end = pv.getEnd() - r.position

    range = Range(
        r.values[i_start:i_end],
        pv.position,
    )

    return range


def partitions[T](r: Range, commonSet: Set[T]) -> List[Range]:
    vectors = getPartitionVectors(r.values, commonSet, r.position)

    ranges = list(map(lambda pv: partition(r, pv), vectors))

    return ranges


def commonPartitions[T](a: Range, b: Range) -> Tuple[List[Range], List[Range]]:
    commonSet = a.parts.intersection(b.parts)

    aRanges = partitions(a, commonSet)
    bRanges = partitions(b, commonSet)

    return (aRanges, bRanges)


def partitionAfter[T](r: Range, i: int) -> Range:
    return Range(r.values[i:], r.position + i)


def partitionAt[T](r: Range, i: int) -> List[Range]:
    # TODO: check inclusive/exclusive
    items = [Range(r.values[0:i], r.position), partitionAfter(r, i)]

    return [x for x in items if x.length > 0]


def partitionOn[T](r: Range, delimiter: T) -> List[Range]:
    items: List[Range] = []

    p: int = 0  # position

    i: int = r.getIndex(delimiter)  # TODO: check inclusive/exclusive

    while i > -1:
        items.append(Range(r.values[p:i], p))

        p = i

        i = r.getIndex(delimiter, i + 1)

        if p < r.length:
            items.append(Range(r.values[p:], p))

    return items
