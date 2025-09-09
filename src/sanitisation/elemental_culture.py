from typing import Dict


from sanitisation.sanitisation_regex import (
    SanitisationTypes,
    re_match,
    sanitisation_regex_map,
)
from sanitisation.regex import IRegex


def assess(elements: set[str], pattern: str) -> set[str]:
    items: set[str] = set()

    for i, character in enumerate(elements):
        if re_match(pattern, character):
            items.add(character)

    return items


class ElementalCulture:
    elements: set[str]

    map: Dict[SanitisationTypes, IRegex]

    patterns: Dict[SanitisationTypes, IRegex]

    curated_elements: Dict[SanitisationTypes, set[str]]

    def __init__(
        self,
        elements: set,
        map: Dict[SanitisationTypes, IRegex],
    ) -> None:
        self.elements = elements
        self.map = map

        self.patterns = dict()
        self.curated_elements = dict()

    def curate(self, sanitisation_type: SanitisationTypes):
        regex = self.map[sanitisation_type]

        self.patterns[sanitisation_type] = regex

        if regex.type == "basic":
            curated = assess(self.elements, regex.pattern)

            self.curated_elements[sanitisation_type] = curated


def curate_elements(elements: set[str]) -> ElementalCulture:
    culture = ElementalCulture(elements, sanitisation_regex_map)

    for key in sanitisation_regex_map.keys():
        culture.curate(key)

    return culture
