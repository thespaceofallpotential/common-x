from typing import Dict, List, Set, TypeVar

T = TypeVar("T", int, str)


type SymmetricIndex[T] = Dict[T, List[int]]


# Symmetric Index
# > / Inverted Index (record-level). See "rebranding" notes below
#
# > Map: a map is a lower-dimensional representation of arbitrarily-plural
# higher-dimensional form
#
# A Symmetric-Index maps higher-dimensional form to index-keys, which represent
# indexed-form "literally"
#
# In this way, a Symmetric-Index (or a map generally) represents and exploits
# symmetries-of-form (between arbitrarily-different phenomena/dimensional-spaces)
# to enable interrogation and navigation of higher-dimensions, at the
# (correspondingly lower) cost of lower-dimensional key-space (/representation-space)
#
# > for example: in reality, we can use a map to learn about an area, and
# > how to get somewhere, without needing to physically move; similarly, we can use
# > (smaller) lower-dimensional abstract spaces to avoid the costs of (larger)
# > higher-dimensional ones
#
# Notes: rebranding
#
# The reason for "rebranding" an "inverted index" as "symmetric index", is due to
# symetries between a document-level "intertex index" and the way i was using a
# (set-theoretic) set, as a lower-dimensional space to qualitativly filter complexity.
#
# And as it turns out, symmetry between reference-frames are exploitable both by
# analysis and synthetis, and consequently, symmetry becomes the clear and unavoidable
# thematic unit and interpretive/ representational context; but more will be said
# at a later stage


def to_symmetric_index(values: List[T], common_set: Set[T]) -> SymmetricIndex[T]:
    item: SymmetricIndex[T] = {}

    for i, value in enumerate(values):
        if value not in common_set:
            continue

        if value not in item:
            item[value] = [i]  # 1
        else:
            item[value].append(i)

    return item
