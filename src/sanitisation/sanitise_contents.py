import re

from typing import Dict

from sanitisation.curation_helpers import (
    StructuredPatternMap,
)
from sanitisation.elemental_curator import ElementalCurator
from core.types import safe_index
from sanitisation.sanitisation_regex import (
    transform,
    space_translations,
    blank_translations,
)
from utils.timer import Timer


def sanitise_contents(curator: ElementalCurator, contents: list[str]) -> list[str]:
    items: list[str] = []

    length = len(contents)

    timer = Timer(True)

    for i, content in enumerate(contents):
        print(
            f"{'sanitise content progress [%d%%]\r'}" % ((i + 1) / length * 100), end=""
        )

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

            if pattern is None:
                continue

            matches = re.finditer(pattern, content)

            for match in matches:
                i_m = match.start()
                group = match.group()

                is_index_ok = (
                    structured_regex.fixed_index is None
                    or structured_regex.is_index_ok(i_m)
                )

                if not is_index_ok:
                    continue

                structured_pattern_map.add(group, i_m)

                if fragments.transform is None:
                    continue

                replacement = fragments.transform(group)

                content = content.replace(group, replacement)

                # i_r = safe_index(content, group)

                # if i_r > -1:
                #     print("here")

        content = transform(content, space_translations, blank_translations)
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
