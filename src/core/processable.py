import abc

from core.sequence import Sequence
from core.sink import Sink


class AbstractProcessable[T, C](Sink[C], metaclass=abc.ABCMeta):
    count: int = 0

    def step(self, value: int = 1):
        self.count += value

    @abc.abstractmethod
    def process(self, a: Sequence, b: Sequence):
        pass
