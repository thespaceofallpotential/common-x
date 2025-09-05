from typing import List, TypeVar
from core import solver
from core.memo import Memo
from core.range import Range
from core.commonality import CommonRange


T = TypeVar("T", int, str)

# BruteForceSolver


class BruteForceSolver[T](solver.AbstractSolver):
    common_ranges: List[CommonRange]

    def __init__(self, a: Range, b: Range) -> None:
        super().__init__(a, b)
        self.common_ranges = []

    def process(self) -> solver.AbstractSolver:
        a = self.a
        b = self.b

        memo = Memo(self.common_ranges)

        for i_a, a_value in enumerate(a.values):
            for i_b, b_value in enumerate(b.values):
                memo.record(a.position + i_a, b.position + i_b, a_value, b_value)

                self.step()

            memo.next()

        return self
