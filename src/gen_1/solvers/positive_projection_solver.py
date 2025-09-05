from typing import List, TypeVar
from core import solver
from core.partition_helpers import partitions
from core.range import Range
from core.commonality import CommonRange
from gen_1.solvers.brute_force_solver import BruteForceSolver

T = TypeVar("T", int, str)


# ProjectionSolver: approximation, hallucination, anomalous


class PositiveProjectionSolver[T](solver.AbstractSolver):
    common_ranges: List[CommonRange]

    def __init__(self, a: Range, b: Range):
        super().__init__(a, b)
        self.common_ranges = []

    def process(self) -> solver.AbstractSolver:
        items = self.common_ranges
        a = self.a
        b = self.b

        common_set = a.elements.intersection(b.elements)

        a_ranges = partitions(a, common_set)
        b_ranges = partitions(b, common_set)

        for a_range in a_ranges:
            for b_range in b_ranges:
                brute = BruteForceSolver(a_range, b_range)

                brute.process()

                items.extend(brute.common_ranges)

                self.step()

        return self
