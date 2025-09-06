from typing import List, Set, cast

from core.vector import PartitionVector
from core.value_helpers import as_str, to_str, values_str


class BasicSequence[T](PartitionVector):
    values: List[T]

    def __init__(self, position: int, values: List[T]):
        super().__init__(position, len(values))

        self.values = values

    def __repr__(self) -> str:
        return f"p:{self.position} l:{self.length} v:{values_str(cast(List[str], self.values))}"


class Sequence[T](BasicSequence):
    elements: Set[T]

    def __init__(
        self,
        values: List[T],
        position: int = 0,
        elements: Set[T] | None = None,
    ):
        super().__init__(position, values)

        self.elements = elements if elements else set[T](values)

    def get_index(self, value: T, start: int = 0) -> int:
        return self.values.index(value, start)

    def __repr__(self) -> str:
        values = self.values if isinstance(T, str) else to_str(self.values)

        elements = list(self.elements) if isinstance(T, str) else as_str(self.elements)

        return f"p:{self.position} l:{self.length} v:{values_str(values)} e:{elements}"


def sequence_values_str(sequence: Sequence) -> str:
    return values_str(cast(List[str], sequence.values))
