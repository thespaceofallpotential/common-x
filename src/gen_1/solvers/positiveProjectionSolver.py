from typing import List, TypeVar
from core import solver
from core.partitionHelpers import partitions
from core.range import Range
from core.types import CommonRange
from gen_1.solvers.bruteForceSolver import BruteForceSolver

T = TypeVar("T", int, str)


# ProjectionSolver: approximation, hallucination, anomalous


class PositiveProjectionSolver[T](solver.AbstractSolver):
    commonRanges: List[CommonRange] = []

    def __init__(self, a: Range, b: Range):
        super().__init__(a, b)

    def process(self) -> solver.AbstractSolver:

        items = self.commonRanges
        a = self.a
        b = self.b

        commonSet = a.elements.intersection(b.elements)

        aRanges = partitions(a, commonSet)
        bRanges = partitions(b, commonSet)

        for aRange in aRanges:

            for bRange in bRanges:

                brute = BruteForceSolver(aRange, bRange)

                brute.process()

                items.extend(brute.commonRanges)

                self.step()

        return self
