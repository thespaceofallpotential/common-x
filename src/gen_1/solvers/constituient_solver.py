from typing import List, TypeVar
from core import solver
from core.sequence import Sequence
from core.symmetric_index import to_symmetric_index
from core.commonality import CommonPoint

T = TypeVar("T", int, str)

# ConstituientSolver: structureless mass of the solution-relative general-domain


class ConstituientSolver[T](solver.AbstractSolver):
    common_points: List[CommonPoint]

    def __init__(self, a: Sequence, b: Sequence):
        super().__init__(a, b)
        self.common_sequences = []

    def process(self) -> solver.AbstractSolver:
        items = self.common_points
        a = self.a
        b = self.b

        common_set = a.elements.intersection(b.elements)

        a_x_value_position_map = to_symmetric_index(a.values, common_set)
        b_x_value_position_map = to_symmetric_index(b.values, common_set)

        common_values = list[T](common_set)

        for value in common_values:
            a_positions = a_x_value_position_map.get(value)
            b_positions = b_x_value_position_map.get(value)

            if not a_positions or not b_positions:
                continue

            for ap in a_positions:
                for bp in b_positions:
                    common = CommonPoint(ap, bp, value)

                    items.append(common)

                    self.step()

        return self
