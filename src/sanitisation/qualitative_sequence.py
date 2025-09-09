from typing import List, Set
from core.sequence import Sequence


class QualitativeSequence[T](Sequence[T]):
    qualities: set[str]

    def __init__(
        self, values: List[T], position: int = 0, elements: Set[T] | None = None
    ):
        super().__init__(values, position, elements)

        self.qualities = set()
