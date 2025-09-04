from core import solver
from core.partitionHelpers import partitions
from core.types import CommonRange
from gen_1.solvers.bruteForceSolver import BruteForceSolver


class PositiveProjectionSolver[T](solver.AbstractSolver):
    commonRanges: list[CommonRange[T]] = []

    def __init__(self, a: solver.Range, b: solver.Range):
        super().__init__(a, b)

    def process(self):

        items = self.commonRanges
        a = self.a
        b = self.b

        commonSet = a.parts.intersection(b.parts)

        aRanges = partitions(a, commonSet)
        bRanges = partitions(b, commonSet)

        for i_a, aRange in enumerate(aRanges):

            for i_b, bRange in enumerate(bRanges):

                brute = BruteForceSolver[T](a, b)

                brute.process()

                items.extend(brute.commonRanges)

                self.step()

        return self
