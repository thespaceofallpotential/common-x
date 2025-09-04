from core.range import Range
from core.partitionHelpers import partitionOn

import abc


class AbstractResolver[T](metaclass=abc.ABCMeta):
    cost: int = 0

    def __init__(self):
        pass

    def processRanges(self, aRanges: list[Range[T]], bRanges: list[Range[T]], depth: int):
        for a in aRanges:
            for b in bRanges:
                self.process(a, b, depth + 1)

    def processContent(self, a: Range[T], b: Range[T], depth: int, newLine: T):
        aRanges = partitionOn(a, newLine)
        bRanges = partitionOn(b, newLine)

        self.processRanges(aRanges, bRanges, depth + 1)

    def step(self, value: int = 1):
        self.cost += value

    @abc.abstractmethod
    def process(self, a: Range[T], b: Range[T], depth: int):
        pass
