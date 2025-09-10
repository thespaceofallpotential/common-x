import re

from typing import Dict

from sanitisation.curation_helpers import (
    StructuredPatternMap,
)
from sanitisation.elemental_curator import ElementalCurator
from utils.timer import Timer


def map_contents(
    curator: ElementalCurator, contents: list[str]
) -> Dict[int, StructuredPatternMap]:
    items: Dict[int, StructuredPatternMap] = {}

    length = len(contents)

    timer = Timer(True)

    for i, content in enumerate(contents):
        print(f"{'progress [%d%%]\r'}" % ((i + 1) / length * 100), end="")

        ordered_keys = list(curator.structured_regex_order)

        structured_pattern_map = StructuredPatternMap()

        curator.structured_pattern_maps[i] = structured_pattern_map

        for structured_sanitisation_key in ordered_keys:
            structured_regex = curator.culture.get_structured_regex(
                structured_sanitisation_key
            )

            pattern = structured_regex.get_fragment_pattern()

            if pattern is not None:
                matches = re.finditer(pattern, content)

                for match in matches:
                    i_m = match.start()
                    group = match.group()

                    if structured_regex.fixed_index is not None:
                        if structured_regex.is_index_ok(i_m):
                            structured_pattern_map.add(group, i_m)
                    else:
                        structured_pattern_map.add(group, i_m)

        items[i] = structured_pattern_map

    print(f"\nt:{timer.end()}")

    return items
