from typing import Dict, List, cast

from formulation.sanitisation.elemental_culture import ElementalCulture
from formulation.sanitisation.director import Director
from formulation.sanitisation.regex import BasicRegex, StructuredRegex
from formulation.sanitisation.sanitisation_types import SanitisationTypes
from formulation.sanitisation.sanitisation_regex import (
    structured_regex_map,
)
from formulation.sanitisation.curation_helpers import (
    StructuredPatternMap,
    assess_elements,
)
from utils.custom_exception import CustomException


class ElementalCurator:
    culture: ElementalCulture

    collection: Dict[str, Director | None]

    structured_regex_order: List[SanitisationTypes]

    structured_pattern_maps: Dict[int, StructuredPatternMap]

    def __init__(
        self, culture: ElementalCulture, structured_regex_order: List[SanitisationTypes]
    ) -> None:
        self.culture = culture
        self.structured_regex_order = structured_regex_order

        self.collection = {}
        self.structured_pattern_maps = {}

    def curate(self, sanitisation_type: SanitisationTypes):
        culture = self.culture

        regex = culture.regexes[sanitisation_type]

        culture.patterns[sanitisation_type] = regex

        if isinstance(regex, BasicRegex):
            culture.curated_elements[sanitisation_type] = assess_elements(
                culture.elements, regex.pattern, regex.positive
            )
            # to translations

        if isinstance(regex, StructuredRegex):
            structured_regex = cast(StructuredRegex, regex)

            culture.curated_elements[sanitisation_type] = set(
                cast(str, structured_regex.fragments.first)
            )

            culture.structured.add(sanitisation_type)

            # to finditer

    def collect(self):
        def collect_basic_elements():
            for sanitisation_type in self.culture.curated_elements:
                elements = self.culture.curated_elements[sanitisation_type]

                regex = self.culture.regexes[sanitisation_type]

                for character in elements:
                    current = self.collection.get(character)

                    if current is not None and regex.positive:
                        continue

                    if current is not None and not regex.positive:
                        # might need to add some kind of condiitional negative flag to QualityClass?
                        # need not yet arisen ;)
                        raise CustomException(f"{__name__}")

                    self.collection[character] = Director() if regex.positive else None

        def collect_structured_elements():
            structured_keys = list(self.culture.structured)

            for structured_sanitisation_key in structured_keys:
                structured_regex = self.culture.get_structured_regex(
                    structured_sanitisation_key
                )

                fragments = structured_regex.fragments

                first = fragments.first

                if first is not None:
                    current = self.collection.get(first)

                    if current is None:
                        current = Director()

                        self.collection[first] = current

                    current.structured_sanitisation[structured_sanitisation_key] = (
                        f"{structured_sanitisation_key}"
                    )

        collect_basic_elements()
        collect_structured_elements()


def curate_and_collect(elements: set[str]) -> ElementalCurator:
    culture = ElementalCulture(elements, structured_regex_map)

    structured_regex_order = [
        SanitisationTypes.STRUCTURED_FRONTMATTER,
        SanitisationTypes.STRUCTURED_CALLOUT,
        SanitisationTypes.STRUCTURED_RAWHTML,
        SanitisationTypes.STRUCTURED_MARKDOWN_INTERNAL_LINK,
        SanitisationTypes.STRUCTURED_MARKDOWN_EXTERNAL_LINK,
    ]

    curator = ElementalCurator(culture, structured_regex_order)

    for key in structured_regex_map:
        curator.curate(key)

    curator.collect()

    return curator

    # def structured_assessor(self) -> Callable[..., int]:
    #     def structured_assessor(content: str, i: int, character: str) -> int:
    #         director = self.collection.get(character)

    #         if director is None:
    #             return 0

    #         for structured_sanitisation_key in director.structured_sanitisation:
    #             structured_regex = self.culture.get_structured_regex(
    #                 structured_sanitisation_key
    #             )

    #             if not structured_regex.is_index_ok(i):
    #                 continue

    #             fragments = structured_regex.fragments

    #             first = fragments.first

    #             if first is not None:
    #                 matches = re.finditer(first, content)

    #                 for match in matches:
    #                     print(match.start(), match.group())

    #             if first is not None and character == first:
    #                 start = fragments.start

    #                 if start is not None and is_match(content, i, start):
    #                     # if REPORT and structured_sanitisation_key in REPORT_TYPES:
    #                     #     print(f"\nstart:{start}")

    #                     fetched = fetch_for(content, i, fragments)

    #                     if fetched is not None:
    #                         if REPORT and structured_sanitisation_key in REPORT_TYPES:
    #                             print(f"{structured_sanitisation_key}: {fetched}")

    #                         # if (
    #                         #     structured_sanitisation_key
    #                         #     == SanitisationTypes.STRUCTURED_FRONTMATTER
    #                         #     and i != 0
    #                         # ):
    #                         #     print("wtf")

    #                         return len(fetched.value)

    #                     # walk to end
    #         return 1  # if state and not state.isStructured(): return True

    #     return structured_assessor

    # def get_positive_vectors(self, content: str) -> List[PositiveVector]:
    #     vectors = get_positive_vectors(content, self.structured_assessor())

    #     return vectors
