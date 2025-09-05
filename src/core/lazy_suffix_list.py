from typing import Dict, TypeVar
from core.sequence import BasicSequence, Sequence
from core.symmetric_index import SymmetricIndex, to_symmetric_index


T = TypeVar("T", int, str)


class LazyFakeLightweightSuffixList[T]:
    sequence: Sequence

    symmetric_map: SymmetricIndex[T]

    cache: Dict[T, list[BasicSequence]] | None  # noqa: F821

    def __init__(self, sequence: Sequence, cache: bool = False) -> None:
        self.sequence = sequence

        self.symmetric_map = to_symmetric_index(sequence.values, sequence.elements)

        if cache:
            self.cache = {}

    def get_suffixes(self, value: T) -> list[BasicSequence] | None:
        cache = self.cache
        symmetric_map = self.symmetric_map
        r = self.sequence

        if cache:
            return cache.get(value)

        value_positions = symmetric_map.get(value)

        if value_positions:
            return list(map(lambda p: BasicSequence(p, r.values[p]), value_positions))

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
