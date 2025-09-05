from typing import List, Set
from core.sequence import PartitionVector


def get_partition_vectors[T](
    values: List[T], common_set: Set[T], position: int = 0
) -> list[PartitionVector]:
    items: List[PartitionVector] = []

    current: PartitionVector | None = None

    for i, value in enumerate(values):
        if value in common_set:
            if current is None:
                current = PartitionVector(position + i, 0)

                items.append(current)

            current.length += 1

            continue

        current = None

    return items
