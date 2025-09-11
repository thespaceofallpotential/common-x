from typing import Dict, Set, cast


from formulation.analysis.structured_regex import (
    SanitisationTypes,
)
from formulation.sanitisation.regex import IRegex, StructuredRegex
from formulation.analysis.analyser import AnalyserType
from formulation.analysis.character_analyser import to_character_list
from formulation.analysis.content_analysis_engine import content_analysis_runner


class ElementalCulture:
    elements: set[str]

    regexes: Dict[SanitisationTypes, IRegex]

    patterns: Dict[SanitisationTypes, IRegex]

    curated_elements: Dict[SanitisationTypes, set[str]]

    structured: Set[SanitisationTypes]

    def __init__(
        self,
        regex_map: Dict[SanitisationTypes, IRegex],
    ) -> None:
        self.regexes = regex_map

        self.elements = set()

        self.patterns = {}

        self.curated_elements = {}

        self.structured = set()

    def initialise_culture(self, contents: list[str]):
        character_analysis = content_analysis_runner(AnalyserType.CHARACTER, contents)

        character_list = to_character_list(character_analysis)

        self.elements.update(set(character_list))

    def get_structured_regex(
        self, sanitisation_type: SanitisationTypes
    ) -> StructuredRegex:
        return cast(StructuredRegex, self.regexes[sanitisation_type])
