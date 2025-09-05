from typing import Tuple, TypeVar
from core.commonality import CommonRange, CommonalityResult
from core.range import Range
from core.partition_helpers import common_partitions, partition_after

T = TypeVar("T", int, str)

I_UNSET = -1


def strict_parser(
    a: Range, b: Range, include_partial: bool = False
) -> Tuple[CommonRange | None, int, int]:
    item = CommonRange(a.position, b.position)

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


def parse_check(a: Range, b: Range) -> CommonalityResult:
    [common, i_a, i_b] = strict_parser(a, b)

    if i_a > 0 or i_b > 0:
        # anomlay detected
        return CommonalityResult([a], [b], None)

    # uncontentious
    return CommonalityResult([], [], common)


def parse_with_repartition(a: Range, b: Range) -> CommonalityResult:
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


def smart_repartition(a: Range, b: Range) -> CommonalityResult:
    common_set = a.elements.intersection(b.elements)

    if len(common_set) == 0:
        return CommonalityResult([], [], None)

    [a_ranges, b_ranges] = common_partitions(a, b)

    arl = len(a_ranges)
    brl = len(b_ranges)

    if arl > 1 or brl > 1:
        # return partitions for processing
        return CommonalityResult(a_ranges, b_ranges, None)

    if arl == 0 or brl == 0:
        # no commonality
        return CommonalityResult([], [], None)

    # arl == 1 and brl == 1, then might as well attempt parse
    return parse_check(a_ranges[0], b_ranges[0])
