from typing import Dict


from sanitisation.sanitisation_regex import (
    SanitisationTypes,
    re_match,
    sanitisation_regex_map,
)
from sanitisation.regex import IRegex


def assess(elements: set[str], pattern: str, positive: bool = True) -> set[str]:
    items: set[str] = set()

    for element in elements:
        if re_match(pattern, element, positive):
            items.add(element)

    return items


class ElementalCulture:
    elements: set[str]

    regex_map: Dict[SanitisationTypes, IRegex]

    patterns: Dict[SanitisationTypes, IRegex]

    curated_elements: Dict[SanitisationTypes, set[str]]

    def __init__(
        self,
        elements: set,
        regex_map: Dict[SanitisationTypes, IRegex],
    ) -> None:
        self.elements = elements
        self.regex_map = regex_map

        self.patterns = {}
        self.curated_elements = {}

    def curate(self, sanitisation_type: SanitisationTypes):
        regex = self.regex_map[sanitisation_type]

        self.patterns[sanitisation_type] = regex

        if regex.type == "basic":
            curated = assess(self.elements, regex.pattern, regex.positive)

            self.curated_elements[sanitisation_type] = curated


def curate_elements(elements: set[str]) -> ElementalCulture:
    culture = ElementalCulture(elements, sanitisation_regex_map)

    for key in sanitisation_regex_map:
        culture.curate(key)

    return culture
