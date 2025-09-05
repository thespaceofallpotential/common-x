from typing import List
from core.sequence import Sequence


class SequenceDomain[T]:
    seqeuences: List[Sequence]

    def __init__(self) -> None:
        self.seqeuences = []

    def get_sequence(self, i: int) -> Sequence:
        return self.seqeuences[i]

    def __len__(self):
        return len(self.seqeuences)
