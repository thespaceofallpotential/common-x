from typing import List, Set

from core.sequence import Sequence


def get_union[T](sequences: List[Sequence[T]]) -> Set[T]:
    if len(sequences) == 0:
        return set()

    union = set()

    for sequence in sequences:
        union = union.union(sequence.elements)

    return union
