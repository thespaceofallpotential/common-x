import abc
from typing import List


from core.commonality import CommonPoint, CommonSequence
from core.sequence import Sequence


class AbstractSolver(metaclass=abc.ABCMeta):
    count: int = 0

    a: Sequence
    b: Sequence

    def __init__(self, a: Sequence, b: Sequence):
        self.a = a
        self.b = b

    def step(self, value: int = 1):
        self.count += value

    @abc.abstractmethod
    def process(self):
        pass


class AbstractSequenceSolver(AbstractSolver):
    common_sequences: List[CommonSequence]

    def __init__(self, a: Sequence, b: Sequence):
        super().__init__(a, b)

        self.common_sequences = []


class AbstractPointSolver(AbstractSolver):
    common_points: List[CommonPoint]

    def __init__(self, a: Sequence, b: Sequence):
        super().__init__(a, b)

        self.common_points = []
