from typing import Dict, cast


from sanitisation.sanitisation_regex import (
    SanitisationTypes,
    re_match,
    sanitisation_regex_map,
)
from sanitisation.regex import IRegex, RegexTypes, StructuredRegex


def assess_basic(elements: set[str], pattern: str, positive: bool = True) -> set[str]:
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

    structured_elements: Dict[SanitisationTypes, dict[str, str]]

    def __init__(
        self,
        elements: set,
        regex_map: Dict[SanitisationTypes, IRegex],
    ) -> None:
        self.elements = elements
        self.regex_map = regex_map

        self.patterns = {}
        self.curated_elements = {}
        self.structured_elements = {}

    def curate(self, sanitisation_type: SanitisationTypes):
        regex = self.regex_map[sanitisation_type]

        self.patterns[sanitisation_type] = regex

        if regex.type == RegexTypes.BASIC:
            curated = assess_basic(self.elements, regex.pattern, regex.positive)

            self.curated_elements[sanitisation_type] = curated

        if regex.type == RegexTypes.STRUCTURED:
            structured_regex = cast(StructuredRegex, regex)
            
            first = structured_regex.keys.get("first")
            
            if first:
                self.curated_elements[sanitisation_type] = set(
                    first
                )

            self.structured_elements[sanitisation_type] = structured_regex.keys


def curate_elements(elements: set[str]) -> ElementalCulture:
    culture = ElementalCulture(elements, sanitisation_regex_map)

    for key in sanitisation_regex_map:
        culture.curate(key)

    return culture
