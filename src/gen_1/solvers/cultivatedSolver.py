from typing import List, TypeVar
from core import solver
from core.range import Range
from core.symmetricIndex import toSymmetricIndex
from core.types import CommonRange, CommonRanges
from core.vectors import getPartitionVectors

T = TypeVar("T", int, str)

# CultivtedSolver
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


class CultivatedSolver[T](solver.AbstractSolver):
    commonRanges: List[CommonRange] = []

    def __init__(self, a: Range, b: Range):
        super().__init__(a, b)

    def process(self):
        a = self.a
        b = self.b

        items = self.commonRanges # results

        commonSet = a.parts.intersection(b.parts)
        # unique to each pair

        positivePartionVectors = getPartitionVectors(a.values, commonSet, a.position)
        # sub-partitions of a, composed of common elements

        xValuePositionsMap = toSymmetricIndex(b.values, commonSet)
        # value (word | token) -> position map for all common elements in b

        progress: CommonRanges = dict() # memoise (immediately/ adjacent) prior position

        for vector in positivePartionVectors:
            origin = vector.position

            for i_v in range(vector.length):
                position = origin + i_v

                value = a.values[position] # (word | token)
                
                xPositions = (
                    xValuePositionsMap.get(value) or []
                ) # positions of the value in b: none are redundant
                # TODO: never None - check  python equivalent for TS '!'

                for xp in xPositions:
                    prior = progress.get(xp - 1)

                    if prior:
                        prior.values.append(value)

                        progress[xp] = prior

                    else:
                        common = CommonRange(origin, xp, [value])

                        items.append(common)

                        progress[xp] = common

                    self.step()

            progress.clear()

        return self
