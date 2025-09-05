from typing import List, TypeVar
from core import resolver
from core.debug import debugValues, debugVectors
from core.parsers import parseCheck, smartRepartition
from core.range import Range
from core.commonality import CommonRange

T = TypeVar("T", int, str)


def isCandidate(a: Range, b: Range) -> bool:
    # customisable: dependent upon kind of problem

    isSameSize = a.length == b.length

    isCommon = len(a.elements.symmetric_difference(b.elements)) == 0

    return isSameSize & isCommon


def areValid(aRanges: List[Range], bRanges: List[Range]):
    # customisable: dependent upon kind of problem

    return len(aRanges) > 0 and len(bRanges) > 0


# DeductiveSolver: idiomatic divide & dismiss, organic: unknown special-domain creativity/ insight


# DeductiveResolver (generation 1: general case)
#
# The DeductiveResolver recursivly eliminates (solution)-negative-space
# to reveal common-substrings without "searching"
# -- (searching: knowing about higher-dimensional structures/ unconditional enumeration of possibility-space) --
#
# very much like:
#   whittling down a piece of wood to reveal the final artefactual-form,
#   or expert archeological excavation & discovery
#
class DeductiveResolver[T](resolver.AbstractResolver):
    commonRanges: List[CommonRange]

    def __init__(self) -> None:
        super().__init__()
        self.commonRanges = []

    def process(self, a: Range, b: Range, depth: int = 1) -> resolver.AbstractResolver:
        # debugVectors(a, b)

        # isCandidate: if range constituients and lengths are the same size
        # parseCheck: check the values by parsing (linear brute-force)
        # smartRepartitioning: if not, repartition based upon relative common elements (between
        # each partition's cached valueSet)
        #
        # recursion continues for all qualifying pairs of subpartitions
        #
        # > note: later generations will natively handle problematic edge-cases
        result = parseCheck(a, b) if isCandidate(a, b) else smartRepartition(a, b)

        if result.common:
            # debugValues(a, b)

            # either:
            #   candidate & result of parseCheck, or
            #   non-candidate, but smartRepartitioning led to one-to-one partitions (a == 1 and b == 1), then parsed
            self.add(result.common)

        aRanges = result.aRanges  # add filtering here: minimum length, etc
        bRanges = result.bRanges

        if areValid(aRanges, bRanges):  # non-zero
            # fractal recursion:
            #   this process function: 1) attempts parse; 2) repartitions ranges; 3) if partitions are valid, calls processRanges
            #   the processRanges function iteratively cross-checks partitions, by calling this function
            #
            # explanation:
            # on each iteration (for each pair of partitions), the set of elements which drives
            # repartitioning changes, (the intersect between valueSets is relative to the pair)
            #
            # insight:
            # this approach might seem inefficient due to the way the same ranges are checked and reduced over and over
            # but at all times, negative-space is being elimintated by nothing other than elementary logic
            # with no knowledge of the special-domain structure (word-strings in this case), this method will
            # eliminate all negative-space, leaving only solution positive-space
            #
            # > "exclude the impossible and what is left, however improbable, must be the truth"
            #
            # the deductiveResolver is therefore, a model elementary logical deduction
            #
            # which is more intelligent:
            #   - a process which unconditionally processes all form/space only once, (positive and negative form/space)
            #   - a process which conditionally reprocesses form/space, to "circle and reevaluate" circumstances under different conditions
            #
            # when all is said and done, i feel that "hold-up! wtf was that? i'mma take another look!"
            # is about as clear a sign of "real/organic/natural" intelligence as is possible to discern
            # from such a simple practical demonstration
            self.processRanges(aRanges, bRanges, depth + 1)

            # self.step(len(result.aRanges) + len(result.bRanges))
            # // TODO: need to update this value... ballpark for now; custom data-structures will significanly reduce & custom hardware will eliminate

        return self

    def add(self, common: CommonRange):
        self.commonRanges.append(common)
