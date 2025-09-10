from typing import Dict, Set, cast


from sanitisation.sanitisation_regex import (
    SanitisationTypes,
)
from sanitisation.regex import IRegex, StructuredRegex


class ElementalCulture:
    elements: set[str]

    regexes: Dict[SanitisationTypes, IRegex]

    patterns: Dict[SanitisationTypes, IRegex]

    curated_elements: Dict[SanitisationTypes, set[str]]

    structured: Set[SanitisationTypes]

    def __init__(
        self,
        elements: set,
        regex_map: Dict[SanitisationTypes, IRegex],
    ) -> None:
        self.elements = elements

        self.regexes = regex_map

        self.patterns = {}

        self.curated_elements = {}

        self.structured = set()

    def get_structured_regex(
        self, sanitisation_type: SanitisationTypes
    ) -> StructuredRegex:
        return cast(StructuredRegex, self.regexes[sanitisation_type])
