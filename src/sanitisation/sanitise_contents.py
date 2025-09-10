import re

from typing import Dict

from sanitisation.curation_helpers import (
    StructuredPatternMap,
)
from sanitisation.elemental_curator import ElementalCurator
from core.types import safe_index
from utils.timer import Timer


def sanitise_contents(curator: ElementalCurator, contents: list[str]) -> list[str]:
    items: list[str] = []

    length = len(contents)

    timer = Timer(True)

    for i, content in enumerate(contents):
        print(f"{'progress [%d%%]\r'}" % ((i + 1) / length * 100), end="")

        ordered_keys = list(curator.structured_regex_order)

        structured_pattern_map = StructuredPatternMap()

        curator.structured_pattern_maps[i] = structured_pattern_map

        original = content

        for structured_sanitisation_key in ordered_keys:
            structured_regex = curator.culture.get_structured_regex(
                structured_sanitisation_key
            )

            pattern = structured_regex.pattern
            fragments = structured_regex.fragments

            if pattern is not None:
                matches = re.finditer(pattern, content)

                if i == 3:
                    print("sfds")

                for match in matches:
                    i_m = match.start()
                    group = match.group()

                    if structured_regex.fixed_index is not None:
                        if not structured_regex.is_index_ok(i_m):
                            continue

                    structured_pattern_map.add(group, i_m)

                    if fragments.transform is not None:
                        replacement = fragments.transform(group)

                        content = content.replace(group, replacement)

                        i_r = safe_index(content, group)

                        if i_r > -1:
                            print("here")

        # sanitised = sanitise(content, assessor)

        if content == original:
            c_e = set(list(content))
            o_e = set(list(original))
            diff = c_e.symmetric_difference(o_e)
            if len(diff) > 0:
                print("here")

        items.append(content)

    print(f"\nt:{timer.end()}")

    return items
