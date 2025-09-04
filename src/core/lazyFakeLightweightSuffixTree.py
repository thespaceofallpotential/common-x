from typing import Dict, List, TypeVar, cast
from core.range import Range
from core.symmetricIndex import SymmetricIndex, toSymmetricIndex
from core.types import PositionedValues


T = TypeVar("T", int, str)


class LazyFakeLightweightSuffixTree[T]:
    range: Range

    symmetricMap: SymmetricIndex[T]

    cache: Dict[T, list[PositionedValues[T]]] | None

    def __init__(self, range: Range, cache: bool = False) -> None:
        self.range = range

        self.symmetricMap = toSymmetricIndex(range.values, range.elements)

        if cache:
            self.cache = dict()

    def getSuffixes(self, value: T) -> list[PositionedValues[T]] | None:

        cache = self.cache
        symmetricMap = self.symmetricMap
        range = self.range

        if cache:
            return cache.get(value)

        valuePositions = symmetricMap.get(value)

        if valuePositions:
            return list(map(lambda p: PositionedValues[T](p, range.values[p]), valuePositions))

        return None





# export class LazyFakeSuffixTree<T extends Token | Word> extends LazyFakeLightweightSuffixTree<T> {
#     /**
#      * rather than generate and pass all suffixes to caller, check sequence internally
#      * @param ta
#      * @returns
#      */
#     check = (ta: TypeArray<T>): CommonRange<T>[] => {
#         const cra: CommonRange<T>[] = [];

#         const { ra, rssi } = this;

#         for (let i = 0; i < ta.length; i++) {
#             const t = ta[i];

#             const sia = rssi.get(t);

#             if (sia === undefined) continue;

#             const remaining = ta.slice(i);

#             for (let si = 0; si < sia.length - 1; si++) {
#                 const sp = sia[si];

#                 const sa = ra.slice(sp);

#                 const [common, _, __] = strictParser(i, sp, remaining, sa);

#                 if (common) cra.push(common);
#             }
#         }

#         return cra;
#     };
# }
