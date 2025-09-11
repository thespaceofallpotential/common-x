import re

from formulation.analysis.curation_helpers import StructuredPatternMap


def get_word_pattern(x: str) -> re.Pattern[str]:
    return re.compile(r"(^| )" + x + r"( |$)")


def get_pattern(items: list[str]) -> re.Pattern[str]:
    captured = map(lambda x: f"({x})", items)

    return re.compile(r"(^| )" + str.join("|", captured) + r"( |$)")

    # def prepare(x: str) -> str:
    #     x = f"(^| ){x}( |$)"

    #     return x

    # items = list(map(lambda x: prepare(x), items))

    # return str.join("|", items)


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
