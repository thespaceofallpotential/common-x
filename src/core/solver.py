from core.range import Range

import abc


class AbstractSolver[T](metaclass=abc.ABCMeta):
    count: int = 0

    a: Range[T]
    b: Range[T]

    def __init__(self, a: Range[T], b: Range[T]):
        self.a = a
        self.b = b

    def step(self, value: int = 1):
        self.count += value

    @abc.abstractmethod
    def process():
        pass
