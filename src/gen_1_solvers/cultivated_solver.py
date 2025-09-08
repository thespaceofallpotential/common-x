from batch.solver import Solver
from core.sequence import Sequence
from core.symmetric_index import to_symmetric_index
from core.commonality import CommonSequence, CommonSequences
from core.vector import get_partition_vectors

# CultivatedSolver
# for use, see: src/generation_1_runner.py

# The cultivted solver: organic "knowledge culture" ; middle-out/through
# > search-free "grown" solution; growth from curated parts/ cultivated environment

# The Cultivated Solver will solve the common-substring problem without touching any
# "higher-dimensional negative-space coordinates", and without knowing anything about
# the higher-dimensional structutes (lower or higher dimensions) other than
# "immediate adjacency"

# solutions are grown, piece-by-piece, based upon a pre-curated reduction (and indexing) of
# possiblity-space to "only those parts (of the set of all) which (legally/ validly) go together"

# note: the commnon-x cultivated solver is a toy model of causality -- hear me out!
#
#   what drives causality, is (sufficient) intersection within finite spaces/ reference-frames
#
#   if we think of chemistry/ biology in four-dimensions of space-time
#   then only chemicals which become sufficiently adjacent have the potential to react,
#   only a subset of which react, and a subset again form persisted stable forms
#
#   the same applies to biological organisms: re reward/ avoidance, survival, and reproduction
#
#   whatever volume of phenomena exist within physical spaces, not all is relevant all the time
#   not all is "at play"
#
#   do we learn more by becoming overwhelemed by "the space of all possible", or do we intelligently
#   culture or attention-spaces, to only those phenomena relelevant to an immediate need
#
#   how else might we describe the cultivated solver?


class CultivatedSolver[T](Solver[T, CommonSequence]):
    def process(self, a: Sequence, b: Sequence):
        common_set = a.elements.intersection(b.elements)
        # unique to each pair

        positive_partion_vectors = get_partition_vectors(
            a.values, common_set, a.position
        )
        # sub-partitions of a, composed of common elements

        x_value_positions_map = to_symmetric_index(b.values, common_set)
        # value (word | token) -> position map for all common elements in b

        progress: CommonSequences = {}  # memoise (immediately/ adjacent) prior position

        for vector in positive_partion_vectors:
            origin = vector.position

            for i_v in range(vector.length):
                position = origin + i_v

                value = a.values[position]  # (word | token)

                x_positions = (
                    x_value_positions_map.get(value) or []
                )  # positions of the value in b: none are redundant
                # TODO: never None - check  python equivalent for TS '!'

                for xp in x_positions:
                    prior = progress.get(xp - 1)

                    if prior:
                        prior.values.append(value)

                        progress[xp] = prior

                    else:
                        common = CommonSequence(origin, xp, [value])

                        self.add(common)

                        progress[xp] = common

                    self.step()

            progress.clear()

        return self
