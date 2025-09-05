from core import solver
from core.sequence import Sequence
from core.symmetric_index import to_symmetric_index
from core.commonality import CommonPoint
from core.types import T

# ConstituientSolver: structureless mass of the solution-relative general-domain


class ConstituientSolver[T](solver.AbstractSolver[T, CommonPoint]):
    def process(self, a: Sequence, b: Sequence):
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

                    self.add(common)

                    self.step()

        return self
