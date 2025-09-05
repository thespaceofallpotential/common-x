import abc

from typing import List, TypeVar

from core.range import Range
from core.partition_helpers import partition_on


T = TypeVar("T", int, str)


class AbstractResolver[T](metaclass=abc.ABCMeta):
    cost: int = 0

    def __init__(self):
        pass

    def process_ranges(self, a_ranges: List[Range], b_ranges: List[Range], depth: int):
        for a in a_ranges:
            for b in b_ranges:
                self.process(a, b, depth + 1)

    def process_content(self, a: Range, b: Range, depth: int, new_line: T):
        a_ranges = partition_on(a, new_line)
        b_ranges = partition_on(b, new_line)

        self.process_ranges(a_ranges, b_ranges, depth + 1)

    def step(self, value: int = 1):
        self.cost += value

    @abc.abstractmethod
    def process(self, a: Range, b: Range, depth: int):
        pass
