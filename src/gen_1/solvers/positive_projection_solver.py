from typing import List, TypeVar
from core import solver
from core.partition_helpers import partitions
from core.sequence import Sequence
from core.commonality import CommonSequence
from gen_1.solvers.brute_force_solver import BruteForceSolver

T = TypeVar("T", int, str)


# ProjectionSolver: approximation, hallucination, anomalous


class PositiveProjectionSolver[T](solver.AbstractSolver):
    common_sequences: List[CommonSequence]

    def __init__(self, a: Sequence, b: Sequence):
        super().__init__(a, b)
        self.common_sequences = []

    def process(self) -> solver.AbstractSolver:
        items = self.common_sequences
        a = self.a
        b = self.b

        common_set = a.elements.intersection(b.elements)

        a_sequences = partitions(a, common_set)
        b_sequences = partitions(b, common_set)

        for a_sequence in a_sequences:
            for b_sequence in b_sequences:
                brute = BruteForceSolver(a_sequence, b_sequence)

                brute.process()

                items.extend(brute.common_sequences)

                self.step()

        return self
