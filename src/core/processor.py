import abc
from typing import List, cast

from batch.batch import Batch
from core.sequence import Sequence
from core.sink import Sink


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

    def step(self, value: int = 1):
        self.count += value

    @abc.abstractmethod
    def process(self, a: Sequence, b: Sequence):
        pass

    def get_batch(self, ai: int, bi: int) -> Batch[C]:
        batch = Batch[C](ai, bi, cast(list[C], self.items))

        self.items = []

        return batch
