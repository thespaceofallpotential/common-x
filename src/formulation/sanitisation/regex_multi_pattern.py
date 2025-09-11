import re

from formulation.sanitisation.curation_helpers import StructuredPatternMap


def get_pattern(items: list[str]) -> str:
    items = list(map(lambda x: re.escape(x), items))

    return str.join("|", items)


def get_structured_pattern_map(
    content: str, patterns: str, fixed_index: int | None = None
):
    items = StructuredPatternMap()

    matches = re.finditer(patterns, content)

    for match in matches:
        i_m = match.start()
        group = match.group()

        if fixed_index is not None:
            if fixed_index == i_m:
                items.add(group, i_m)
        else:
            items.add(group, i_m)

    return items


def get_structured_pattern_list(
    content: str, patterns: str, fixed_index: int | None = None
) -> list[str]:
    items: set[str] = set()

    matches = re.finditer(patterns, content)

    for match in matches:
        group = match.group()

        items.add(group)

    return list(items)
