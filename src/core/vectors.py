from core.range import PartitionVector


def getPartitionVectors[T](
    values: list[T], commonSet: set[T], position: int = 0
) -> list[PartitionVector]:
    items: list[PartitionVector] = []

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
