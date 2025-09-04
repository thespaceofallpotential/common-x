from typing import List, Set, TypeVar, cast

from core.types import values

T = TypeVar("T", int, str)


class PartitionVector:
    position: int
    length: int

    def __init__(self, position: int, length: int):
        self.position = position
        self.length = length

    def getEnd(self):
        return self.position + self.length

    def __repr__(self) -> str:
        return f"[p:{self.position},l:{self.length}]"


def vectorsString[T](a: PartitionVector, b: PartitionVector) -> str:
    return f"a:{a} | b:{b}"


class Range[T](PartitionVector):
    def __init__(
        self,
        values: List[T],
        position: int = 0,
        parts: Set[T] | None = None,
    ):
        super().__init__(position, len(values))

        self.values = values

        self.elements = parts if parts else set[T](values)

    def getIndex(self, value: T, start: int = 0) -> int:
        return self.values.index(value, start)

    def __repr__(self) -> str:
        return f"p:{self.position} l:{self.length} v:{self.values} e:{self.elements}"


def rangeValues[T](r: Range) -> str:
    return values(cast(List[str], r.values))


def range[T](r: Range) -> str:
    return f"p:{r.position} v:{rangeValues(r)}"
