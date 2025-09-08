import abc
from enum import Enum
from typing import List, cast

from batch.batch import Batch
from core.sequence import Sequence
from core.sink import Sink


class ProcessorTypes(Enum):
    BRUTE_FORCE = 1
    CONSTITUENT = 2
    CULTIVATED = 3
    DEDUCTIVE = 4
    POSITIVE_PROJECTION = 5


class IProcessor[T, C](metaclass=abc.ABCMeta):
    count: int

    items: List[C]

    @abc.abstractmethod
    def process(self, a: Sequence[T], b: Sequence[T]):
        pass

    @abc.abstractmethod
    def get_batch(self, ai: int, bi: int) -> Batch[C]:
        pass


class Processor[T, C](IProcessor[T, C], Sink[C], metaclass=abc.ABCMeta):
    count: int = 0

    items: List[C]

    def __init__(self) -> None:
        super(Sink).__init__()
        self.items = []

    def step(self, value: int = 1):
        self.count += value

    @abc.abstractmethod
    def process(self, a: Sequence, b: Sequence):
        pass

    def get_batch(self, ai: int, bi: int) -> Batch[C]:
        batch = Batch[C](ai, bi, cast(list[C], self.items))

        self.items = []

        return batch
