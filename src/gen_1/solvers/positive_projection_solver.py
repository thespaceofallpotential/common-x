from core import solver
from core.commonality import CommonSequence
from core.partition_helpers import partitions
from core.sequence import Sequence
from core.types import T

from gen_1.solvers.brute_force_solver import BruteForceSolver


# ProjectionSolver: approximation, hallucination, anomalous


class PositiveProjectionSolver[T](solver.AbstractSolver[T, CommonSequence]):
    def process(self, a: Sequence, b: Sequence):
        common_set = a.elements.intersection(b.elements)

        a_sequences = partitions(a, common_set)
        b_sequences = partitions(b, common_set)

        for a_sequence in a_sequences:
            for b_sequence in b_sequences:
                brute = BruteForceSolver()

                brute.process(a_sequence, b_sequence)

                self.add_all(brute.items)

                self.step()

        return self
