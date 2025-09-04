type SymmetricIndex[T] = dict[T, list[int]]


def toSymmetricIndex[T](values: list[T], commonSet: set[T]) -> SymmetricIndex[T]:
    item: SymmetricIndex[T] = dict()

    for i, value in enumerate(values):
        if value not in commonSet:
            continue

        if value not in item:
            item[value] = [i] * 1
        else:
            item[value].append(i)

    return item
