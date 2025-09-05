from typing import List, Set


class PartitionVector:
    position: int
    length: int

    def __init__(self, position: int, length: int):
        self.position = position
        self.length = length

    def get_end(self):
        return self.position + self.length

    def __repr__(self) -> str:
        return f"[p:{self.position},l:{self.length}]"


def vectors_str(a: PartitionVector, b: PartitionVector) -> str:
    return f"a:{a} | b:{b}"


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
