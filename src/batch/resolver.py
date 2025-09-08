import abc

from typing import List

from batch.processor import Processor
from core.sequence import Sequence
from core.partition_helpers import partition_on


class Resolver[T, C](Processor[T, C]):
    def process_content(self, a: Sequence, b: Sequence, depth: int, new_line: T):
        a_sequences = partition_on(a, new_line)
        b_sequences = partition_on(b, new_line)

        self.process_sequences(a_sequences, b_sequences, depth + 1)

    def process_sequences(
        self, a_sequences: List[Sequence], b_sequences: List[Sequence], depth: int
    ):
        for a in a_sequences:
            for b in b_sequences:
                self.process(a, b, depth + 1)

    @abc.abstractmethod
    def process(self, a: Sequence, b: Sequence, depth: int = 1):
        pass
