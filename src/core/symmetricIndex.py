from typing import Dict, List, Set, TypeVar

T = TypeVar("T", int, str)


type SymmetricIndex[T] = Dict[T, List[int]]


def toSymmetricIndex[T](values: List[T], commonSet: Set[T]) -> SymmetricIndex[T]:
    item: SymmetricIndex[T] = dict()

    for i, value in enumerate(values):
        if value not in commonSet:
            continue

        if value not in item:
            item[value] = [i] * 1
        else:
            item[value].append(i)

    return item
