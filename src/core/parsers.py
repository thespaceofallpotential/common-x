from typing import Tuple, TypeVar
from core.commonality import CommonSequence, CommonalityResult
from core.sequence import Sequence
from core.partition_helpers import common_partitions, partition_after

T = TypeVar("T", int, str)

I_UNSET = -1


def strict_parser(
    a: Sequence, b: Sequence, include_partial: bool = False
) -> Tuple[CommonSequence | None, int, int]:
    item = CommonSequence(a.position, b.position)

    avl = len(a.values)
    bvl = len(b.values)

    for i, av in enumerate(a.values):
        bv = b.values[i]

        if i >= bvl:
            # a is longer than b; return common partition, with index to split remaining a
            return (item, i, I_UNSET)

        if av != bv:
            # anomaly found
            if include_partial and len(item.values) > 0:
                return (item, i, i)

            return (None, i, i)

        item.values.append(av)

    # if b is longer than a, return common partition, with index for remaining b
    i_default = avl if avl < bvl else I_UNSET

    return (item, I_UNSET, i_default)


def parse_check(a: Sequence, b: Sequence) -> CommonalityResult:
    [common, i_a, i_b] = strict_parser(a, b)

    if i_a > 0 or i_b > 0:
        # anomlay detected
        return CommonalityResult([a], [b], None)

    # uncontentious
    return CommonalityResult([], [], common)


def parse_with_repartition(a: Sequence, b: Sequence) -> CommonalityResult:
    [common, i_a, i_b] = strict_parser(a, b)

    if common:
        if i_a > 0:
            # common partition with
            return CommonalityResult([partition_after(a, i_a)], [b], common)

        if i_b > 0:
            return CommonalityResult([], [partition_after(b, i_b)], common)

        return CommonalityResult([], [], common)

    # if haltOnUnhandled:
    # TODO

    return CommonalityResult([], [], None)


def smart_repartition(a: Sequence, b: Sequence) -> CommonalityResult:
    common_set = a.elements.intersection(b.elements)

    if len(common_set) == 0:
        return CommonalityResult([], [], None)

    [a_sequences, b_sequences] = common_partitions(a, b)

    arl = len(a_sequences)
    brl = len(b_sequences)

    if arl > 1 or brl > 1:
        # return partitions for processing
        return CommonalityResult(a_sequences, b_sequences, None)

    if arl == 0 or brl == 0:
        # no commonality
        return CommonalityResult([], [], None)

    # arl == 1 and brl == 1, then might as well attempt parse
    return parse_check(a_sequences[0], b_sequences[0])
