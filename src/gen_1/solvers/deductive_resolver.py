from typing import List
from core import resolver
from utils.debug import debug_values, debug_vectors
from core.parsers import parse_check, smart_repartition
from core.sequence import Sequence
from core.commonality import CommonSequence
from core.types import T


def is_candidate(a: Sequence, b: Sequence) -> bool:
    # customisable: dependent upon kind of problem

    is_same_size = a.length == b.length

    is_common = len(a.elements.symmetric_difference(b.elements)) == 0

    return is_same_size & is_common


def are_valid(a_sequences: List[Sequence], b_sequences: List[Sequence]):
    # customisable: dependent upon kind of problem

    return len(a_sequences) > 0 and len(b_sequences) > 0


# DeductiveSolver: idiomatic divide & dismiss
# > organic: unknown-special-domain creativity/ insight


# DeductiveResolver (generation 1: general case)
#
# The DeductiveResolver recursivly eliminates (solution)-negative-space
# to reveal common-substrings without "searching"
#
# > searching:-
# >  - knowing about higher-dimensional structures
# >  - unconditional (positive & negative) enumeration of possibility-space
#
# very much like:
#   whittling down a piece of wood to reveal the final artefactual-form,
#   or expert archeological excavation & discovery
#
class DeductiveResolver[T](resolver.AbstractSequenceResolver):
    def __init__(self) -> None:
        super().__init__()

    def process(
        self, a: Sequence, b: Sequence, depth: int = 1
    ) -> resolver.AbstractSequenceResolver:
        # debugVectors(a, b)

        # isCandidate: if sequence constituients and lengths are the same size
        # parseCheck: check the values by parsing (linear brute-force)
        # smartRepartitioning: if not, repartition based upon relative common elements (between
        # each partition's cached valueSet)
        #
        # recursion continues for all qualifying pairs of subpartitions
        #
        # > note: later generations will natively handle problematic edge-cases
        result = parse_check(a, b) if is_candidate(a, b) else smart_repartition(a, b)

        if result.common:
            # debugValues(a, b)

            # either:
            #   candidate & result of parseCheck, or
            #   non-candidate, but smartRepartitioning led to one-to-one partitions (a == 1 and b == 1), then parsed
            self.add(result.common)

        a_sequences = result.a_sequences  # add filtering here: minimum length, etc
        b_sequences = result.b_sequences

        if are_valid(a_sequences, b_sequences):  # non-zero
            # fractal recursion:
            #   this process function: 1) attempts parse; 2) repartitions sequences; 3) if partitions are valid, calls process_sequences
            #   the process_sequences function iteratively cross-checks partitions, by calling this function
            #
            # explanation:
            # on each iteration (for each pair of partitions), the set of elements which drives
            # repartitioning changes, (the intersect between valueSets is relative to the pair)
            #
            # insight:
            # this approach might seem inefficient due to the way the same sequences are checked and reduced over and over
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
            self.process_sequences(a_sequences, b_sequences, depth + 1)

            # self.step(len(result.a_sequences) + len(result.b_sequences))
            # // TODO: need to update this value... ballpark for now; custom data-structures will significanly reduce & custom hardware will eliminate

        return self

    def add(self, common: CommonSequence):
        self.common_sequences.append(common)
