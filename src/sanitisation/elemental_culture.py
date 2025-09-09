from typing import Dict

from sanitisation.sanitisation_regex import (
    SanitisationTypes,
    re_match,
    sanitisation_regex_map,
)


def assess(elements: set[str], pattern: str) -> set[str]:
    items: set[str] = set()

    for i, character in enumerate(elements):
        if re_match(pattern, character):
            items.add(character)

    return items


class ElementalCulture:
    elements: set[str]

    map: Dict[SanitisationTypes, str]

    patterns: Dict[SanitisationTypes, str]

    curated_elements: Dict[SanitisationTypes, set[str]]

    def __init__(
        self,
        elements: set,
        map: Dict[SanitisationTypes, str],
    ) -> None:
        self.elements = elements
        self.map = map

        self.patterns = dict()
        self.curated_elements = dict()

    def curate(self, sanitisation_type: SanitisationTypes):
        pattern = self.map[sanitisation_type]

        curated = assess(self.elements, pattern)

        self.patterns[sanitisation_type] = pattern

        self.curated_elements[sanitisation_type] = curated


def curate_elements(elements: set[str]) -> ElementalCulture:
    culture = ElementalCulture(elements, sanitisation_regex_map)

    culture.curate(SanitisationTypes.WS)
    culture.curate(SanitisationTypes.D)

    return culture
