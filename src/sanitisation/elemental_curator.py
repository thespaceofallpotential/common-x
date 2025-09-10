from typing import Dict, cast

from sanitisation.elemental_culture import ElementalCulture
from sanitisation.sanitisation import QualityClass
from sanitisation.regex import FragmentTypes, RegexTypes, StructuredRegex
from sanitisation.sanitisation_regex import SanitisationTypes
from utils.custom_exception import CustomException

from sanitisation.sanitisation_regex import (
    re_match,
    sanitisation_regex_map,
)


def assess_basic(elements: set[str], pattern: str, positive: bool = True) -> set[str]:
    items: set[str] = set()

    for element in elements:
        if re_match(pattern, element, positive):
            items.add(element)

    return items


class ElementalCurator:
    culture: ElementalCulture

    collection: Dict[str, QualityClass | None]

    def __init__(self, culture: ElementalCulture) -> None:
        self.culture = culture

        self.collection = {}

    def curate(self, sanitisation_type: SanitisationTypes):
        regex_map = self.culture.regex_map
        patterns = self.culture.patterns
        elements = self.culture.elements
        curated_elements = self.culture.curated_elements
        structured_fragments = self.culture.structured_fragments

        regex = regex_map[sanitisation_type]

        patterns[sanitisation_type] = regex

        if regex.type == RegexTypes.BASIC:
            curated = assess_basic(elements, regex.pattern, regex.positive)

            curated_elements[sanitisation_type] = curated

        if regex.type == RegexTypes.STRUCTURED:
            structured_regex = cast(StructuredRegex, regex)

            first = structured_regex.keys.get(FragmentTypes.FIRST)

            if first:
                curated_elements[sanitisation_type] = set(first)

            structured_fragments[sanitisation_type] = structured_regex.keys

    def collect(self):
        def collect_basic_elements():
            for sanitisation_type in self.culture.curated_elements:
                elements = self.culture.curated_elements[sanitisation_type]

                regex = self.culture.regex_map[sanitisation_type]

                for character in elements:
                    current = self.collection.get(character)

                    if current and regex.positive:
                        continue

                    if current and not regex.positive:
                        # might need to add some kind of condiitional negative flag to QualityClass?
                        # need not yet arisen ;)
                        raise CustomException(f"{__name__}")

                    self.collection[character] = (
                        QualityClass() if regex.positive else None
                    )

        def collect_structured_elements():
            for sanitisation_type in self.culture.structured_fragments:
                fragments = self.culture.structured_fragments[sanitisation_type]

                first = fragments.get(FragmentTypes.FIRST)

                if first:
                    current = self.collection.get(first)

                    if not current:
                        current = QualityClass()
                        self.collection[first] = current

                    current.structured_sanitisation[sanitisation_type] = (
                        f"{sanitisation_type}"
                    )

        collect_basic_elements()
        collect_structured_elements()


def curate_elements(elements: set[str]) -> ElementalCurator:
    culture = ElementalCulture(elements, sanitisation_regex_map)

    curator = ElementalCurator(culture)

    for key in sanitisation_regex_map:
        curator.curate(key)

    curator.collect()

    return curator
