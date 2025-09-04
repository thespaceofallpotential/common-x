from core.range import Range
from core.partitionHelpers import commonPartitions, partitionAfter
from core.types import CommonRange, CommonalityResult

i_unset = -1


def strictParser[T](
    a: Range[T], b: Range[T], includePartial: bool = False
) -> tuple[CommonRange | None, int, int]:

    item = CommonRange(a.position, b.position)
    
    avl = len(a.values)
    bvl = len(b.values)

    for i, av in enumerate(a.values):
        bv = b.values[i]

        if i >= bvl:
            # a is longer than b; return common partition, with index to split remaining a
            return (item, i, i_unset)

        if av != bv:
            # anomaly found
            if includePartial and len(item.values) > 0:
                return (item, i, i)
            else:
                return (None, i, i)

        item.values.append(av)

    # if b is longer than a, return common partition, with index for remaining b
    i_default = avl if avl < bvl else i_unset

    return (item, i_unset, i_default)


def parseCheck[T](a: Range[T], b: Range[T]) -> CommonalityResult[T]:

    [common, i_a, i_b] = strictParser(a, b)

    if i_a > 0 or i_b > 0:
        # anomlay detected
        return CommonalityResult([a], [b], None)

    # uncontentious
    return CommonalityResult([], [], common)


def parseWithRepartition[T](
    a: Range[T], b: Range[T], haltOnUnhandled: bool = False
) -> CommonalityResult[T]:

    [common, i_a, i_b] = strictParser(a, b)

    if common:
        if i_a > 0:
            # common partition with
            return CommonalityResult([partitionAfter(a, i_a)], [b], common)

        if i_b > 0:
            return CommonalityResult([], [partitionAfter(b, i_b)], common)

        return CommonalityResult([], [], common)

    # if haltOnUnhandled:
    # TODO

    return CommonalityResult([], [], None)


def smartRepartition[T](a: Range[T], b: Range[T]) -> CommonalityResult[T]:

    commonSet = a.parts.intersection(b.parts)

    if len(commonSet) == 0:
        return CommonalityResult([], [], None)

    [aRanges, bRanges] = commonPartitions(a, b)

    arl = len(aRanges)
    brl = len(bRanges)

    if arl > 1 or brl > 1:
        # return partitions for processing
        return CommonalityResult(aRanges, bRanges, None)

    if arl == 0 or brl == 0:
        # no commonality
        return CommonalityResult([], [], None)

    # arl == 1 and brl == 1, then might as well attempt parse
    return parseCheck(aRanges[0], bRanges[0])
