from typing import List, Set, Tuple
from core.sequence import PartitionVector, Sequence
from core.vector import get_partition_vectors
from core.types import T


def partition(sequence: Sequence, pv: PartitionVector) -> Sequence:
    i_start = pv.position - sequence.position
    i_end = pv.get_end() - sequence.position

    item = Sequence(
        sequence.values[i_start:i_end],
        pv.position,
    )

    return item


def partitions(sequence: Sequence, common_set: Set[T]) -> List[Sequence]:
    vectors = get_partition_vectors(sequence.values, common_set, sequence.position)

    sequences = list(map(lambda pv: partition(sequence, pv), vectors))

    return sequences


def common_partitions(
    a: Sequence, b: Sequence
) -> Tuple[List[Sequence], List[Sequence]]:
    common_set = a.elements.intersection(b.elements)

    a_sequences = partitions(a, common_set)
    b_sequences = partitions(b, common_set)

    return (a_sequences, b_sequences)


def partition_after(sequence: Sequence, i: int) -> Sequence:
    return Sequence(sequence.values[i:], sequence.position + i)


def partition_at(sequence: Sequence, i: int) -> List[Sequence]:
    # TODO: check inclusive/exclusive
    items = [
        Sequence(sequence.values[0:i], sequence.position),
        partition_after(sequence, i),
    ]

    return [x for x in items if x.length > 0]


def partition_on(sequence: Sequence, delimiter: T) -> List[Sequence]:
    items: List[Sequence] = []

    p: int = 0  # position

    i: int = sequence.get_index(delimiter)  # TODO: check inclusive/exclusive

    while i > -1:
        items.append(Sequence(sequence.values[p:i], p))

        p = i

        i = sequence.get_index(delimiter, i + 1)

        if p < sequence.length:
            items.append(Sequence(sequence.values[p:], p))

    return items
