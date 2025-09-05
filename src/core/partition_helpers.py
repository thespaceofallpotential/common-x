from typing import List, Set, Tuple, TypeVar
from core.range import PartitionVector, Range
from core.vectors import get_partition_vectors


T = TypeVar("T", int, str)


def partition(r: Range, pv: PartitionVector) -> Range:
    i_start = pv.position - r.position
    i_end = pv.get_end() - r.position

    item = Range(
        r.values[i_start:i_end],
        pv.position,
    )

    return item


def partitions(r: Range, common_set: Set[T]) -> List[Range]:
    vectors = get_partition_vectors(r.values, common_set, r.position)

    ranges = list(map(lambda pv: partition(r, pv), vectors))

    return ranges


def common_partitions(a: Range, b: Range) -> Tuple[List[Range], List[Range]]:
    common_set = a.elements.intersection(b.elements)

    a_ranges = partitions(a, common_set)
    b_ranges = partitions(b, common_set)

    return (a_ranges, b_ranges)


def partition_after(r: Range, i: int) -> Range:
    return Range(r.values[i:], r.position + i)


def partition_at(r: Range, i: int) -> List[Range]:
    # TODO: check inclusive/exclusive
    items = [Range(r.values[0:i], r.position), partition_after(r, i)]

    return [x for x in items if x.length > 0]


def partition_on[T](r: Range[T], delimiter: T) -> List[Range]:
    items: List[Range] = []

    p: int = 0  # position

    i: int = r.get_index(delimiter)  # TODO: check inclusive/exclusive

    while i > -1:
        items.append(Range(r.values[p:i], p))

        p = i

        i = r.get_index(delimiter, i + 1)

        if p < r.length:
            items.append(Range(r.values[p:], p))

    return items
