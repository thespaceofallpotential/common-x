from core.range import PartitionVector, Range
from core.vectors import getPartitionVectors


def partition[T](r: Range[T], pv: PartitionVector) -> Range[T]:

    i_start = pv.position - r.position
    i_end = pv.getEnd() - r.position

    range = Range(
        r.values[i_start:i_end],
        pv.position,
    )

    return range


def partitions[T](r: Range[T], commonSet: set[T]) -> list[Range[T]]:
    vectors = getPartitionVectors(r.values, commonSet, r.position)

    ranges = list(map(lambda pv: partition(r, pv), vectors))

    return ranges


def commonPartitions[T](a: Range[T], b: Range[T]) -> tuple[list[Range[T]], list[Range[T]]]:
    commonSet = a.parts.intersection(b.parts)

    aRanges = partitions(a, commonSet)
    bRanges = partitions(b, commonSet)

    return (aRanges, bRanges)


def partitionAfter[T](r: Range[T], i: int) -> Range[T]:
    return Range[T](r.values[i:], r.position + i)


def partitionAt[T](r: Range[T], i: int) -> list[Range[T]]:
    # TODO: check inclusive/exclusive
    items = [Range[T](r.values[0:i], r.position), partitionAfter(r, i)]

    return [x for x in items if x.length > 0]


def partitionOn[T](r: Range[T], delimiter: T) -> list[Range[T]]:
    items: list[Range[T]] = []

    p: int = 0  # position

    i: int = r.getIndex(delimiter)  # TODO: check inclusive/exclusive

    while i > -1:
        items.append(Range[T](r.values[p:i], p))

        p = i

        i = r.getIndex(delimiter, i + 1)

        if p < r.length:
            items.append(Range[T](r.values[p:], p))

    return items
