import abc

from typing import List

from core.commonality import CommonSequence
from core.sequence import Sequence
from core.partition_helpers import partition_on
from core.types import T


class AbstractResolver[T](metaclass=abc.ABCMeta):
    cost: int = 0

    def __init__(self):
        pass

    def process_sequences(
        self, a_sequences: List[Sequence], b_sequences: List[Sequence], depth: int
    ):
        for a in a_sequences:
            for b in b_sequences:
                self.process(a, b, depth + 1)

    def process_content(self, a: Sequence, b: Sequence, depth: int, new_line: T):
        a_sequences = partition_on(a, new_line)
        b_sequences = partition_on(b, new_line)

        self.process_sequences(a_sequences, b_sequences, depth + 1)

    def step(self, value: int = 1):
        self.cost += value

    @abc.abstractmethod
    def process(self, a: Sequence, b: Sequence, depth: int):
        pass


class AbstractSequenceResolver[T](AbstractResolver):
    common_sequences: List[CommonSequence]

    def __init__(self):
        super().__init__()

        self.common_sequences = []
