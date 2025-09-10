from typing import Dict


from sanitisation.sanitisation_regex import (
    SanitisationTypes,
)
from sanitisation.regex import FragmentTypes, IRegex


class ElementalCulture:
    elements: set[str]

    regex_map: Dict[SanitisationTypes, IRegex]

    patterns: Dict[SanitisationTypes, IRegex]

    curated_elements: Dict[SanitisationTypes, set[str]]

    structured_fragments: Dict[SanitisationTypes, Dict[FragmentTypes, str]]

    def __init__(
        self,
        elements: set,
        regex_map: Dict[SanitisationTypes, IRegex],
    ) -> None:
        self.elements = elements
        self.regex_map = regex_map

        self.patterns = {}
        self.curated_elements = {}
        self.structured_fragments = {}
