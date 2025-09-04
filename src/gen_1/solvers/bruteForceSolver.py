from core import solver
from core.memo import Memo
from core.range import Range
from core.types import CommonRange


class BruteForceSolver[T](solver.AbstractSolver):
    commonRanges: list[CommonRange[T]] = []

    def __init__(self, a: Range[T], b: Range[T]) -> None:
        super().__init__(a, b)

    def process(self) -> solver.AbstractSolver:

        a = self.a
        b = self.b

        memo = Memo(self.commonRanges)

        for i_a, aValue in enumerate(a.values):

            for i_b, bValue in enumerate(b.values):

                memo.record(a.position + i_a, b.position + i_b, aValue, bValue)

                self.step()

            memo.next()

        return self
