import abc


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
