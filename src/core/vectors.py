from typing import List, Set, TypeVar
from core.range import PartitionVector


T = TypeVar("T", int, str)


def getPartitionVectors[T](
    values: List[T], commonSet: Set[T], position: int = 0
) -> list[PartitionVector]:
    items: List[PartitionVector] = []

    current: PartitionVector | None = None

    for i, value in enumerate(values):
        if value in commonSet:
            if current == None:
                current = PartitionVector(position + i, 0)

                items.append(current)

            current.length += 1

            continue

        current = None

    return items
