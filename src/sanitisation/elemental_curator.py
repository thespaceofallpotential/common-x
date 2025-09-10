import re
from typing import Callable, Dict, List, cast

from sanitisation.elemental_culture import ElementalCulture
from sanitisation.sanitisation import Director
from sanitisation.regex import BasicRegex, StructuredRegex
from sanitisation.sanitisation_regex import SanitisationTypes
from sanitisation.sanitisation_regex import (
    sanitisation_regex_map,
)
from sanitisation.positive_vectors import (
    PositiveVector,
    get_positive_vectors,
)
from sanitisation.curation_helpers import (
    ElementMap,
    assess_elements,
    fetch_for,
    is_match,
    sanitise,
)
from sanitisation.sanitisation_reporting import REPORT, REPORT_TYPES
from core.strings import ASTERISK, COMMA, EMPTY, EXCLAMATION, NEWLINE, PERIOD, SPACE
from sanitisation.character_analyser import to_character_list2
from core.types import index_withoutexception
from utils.timer import Timer
from utils.custom_exception import CustomException


class ElementalCurator:
    culture: ElementalCulture

    collection: Dict[str, Director | None]

    def __init__(self, culture: ElementalCulture) -> None:
        self.culture = culture

        self.collection = {}

    def curate(self, sanitisation_type: SanitisationTypes):
        culture = self.culture

        regex = culture.regexes[sanitisation_type]

        culture.patterns[sanitisation_type] = regex

        if isinstance(regex, BasicRegex):
            culture.curated_elements[sanitisation_type] = assess_elements(
                culture.elements, regex.pattern, regex.positive
            )

        if isinstance(regex, StructuredRegex):
            structured_regex = cast(StructuredRegex, regex)

            culture.curated_elements[sanitisation_type] = set(
                cast(str, structured_regex.fragments.first)
            )

            culture.structured.add(sanitisation_type)

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

    def quality_assessor(self) -> Callable[..., int]:
        def structured_assessor(content: str, i: int, character: str) -> int:
            director = self.collection.get(character)

            if director is None:
                return 0

            for structured_sanitisation_key in director.structured_sanitisation:
                structured_regex = self.culture.get_structured_regex(
                    structured_sanitisation_key
                )

                if not structured_regex.is_index_ok(i):
                    continue

                fragments = structured_regex.fragments

                first = fragments.first

                if first is not None and character == first:
                    start = fragments.start

                    if start is not None and is_match(content, i, start):
                        # if REPORT and structured_sanitisation_key in REPORT_TYPES:
                        #     print(f"\nstart:{start}")

                        fetched = fetch_for(content, i, fragments)

                        if fetched is not None:
                            if REPORT and structured_sanitisation_key in REPORT_TYPES:
                                print(f"{structured_sanitisation_key}: {fetched}")

                            # if (
                            #     structured_sanitisation_key
                            #     == SanitisationTypes.STRUCTURED_FRONTMATTER
                            #     and i != 0
                            # ):
                            #     print("wtf")

                            return len(fetched.value)

                        # walk to end
            return 1  # if state and not state.isStructured(): return True

        return structured_assessor

    def get_positive_vectors(self, content: str) -> List[PositiveVector]:
        vectors = get_positive_vectors(content, self.quality_assessor())

        return vectors


def curate_and_collect(elements: set[str]) -> ElementalCurator:
    culture = ElementalCulture(elements, sanitisation_regex_map)

    curator = ElementalCurator(culture)

    for key in sanitisation_regex_map:
        curator.curate(key)

    curator.collect()

    return curator


def map_contents(
    curator: ElementalCurator, contents: list[str]
) -> list[list[PositiveVector]]:
    items: list[list[PositiveVector]] = []

    length = len(contents)

    timer = Timer(True)

    assessor = curator.quality_assessor()

    for i, content in enumerate(contents):
        print("progress [%d%%]\r" % ((i + 1) / length * 100), end="")
        # print(f"progress {i} [%d%%]\r" % ((i + 1) / length * 100), end="")

        vectors = get_positive_vectors(content, assessor)

        items.append(vectors)

    print(f"\nt:{timer.end()}")

    return items


def map_content_elements(
    curator: ElementalCurator, contents: list[str]
) -> list[ElementMap]:
    items: list[ElementMap] = []

    length = len(contents)

    timer = Timer(True)

    assessor = curator.quality_assessor()

    for i, content in enumerate(contents):
        print("progress [%d%%]\r" % ((i + 1) / length * 100), end="")
        # print(f"progress {i} [%d%%]\r" % ((i + 1) / length * 100), end="")

        element_list = list(set(content))
        element_list.sort()

        elements = str.join("", element_list)

        vectors = get_positive_vectors(elements, assessor)

        items.append(ElementMap(element_list, vectors, content))

    print(f"\nt:{timer.end()}")

    return items


def map_content_elements2(
    curator: ElementalCurator, contents: list[str]
) -> list[ElementMap]:
    items: list[ElementMap] = []

    length = len(contents)

    timer = Timer(True)

    assessor = curator.quality_assessor()

    for i, content in enumerate(contents):
        print("progress [%d%%]\r" % ((i + 1) / length * 100), end="")
        # print(f"progress {i} [%d%%]\r" % ((i + 1) / length * 100), end="")

        temp: dict[str, list[int]] = {}

        character = "["

        pattern = r"\["

        matches = re.finditer(pattern, content)

        for match in matches:
            print(match.start(), match.group())

        i_i = index_withoutexception(content, character)

        while i_i > -1 and i_i < len(content):
            current = temp.get(character)

            if current is None:
                temp[character] = [i_i]
            else:
                temp[character].append(i_i)

            i_i = index_withoutexception(content, character, i_i + 1)

            print(i_i)

        for i_i, character in enumerate(content):
            if character == "[":
                current = temp.get(character)

                if current is None:
                    temp[character] = [i_i]
                    continue

                temp[character].append(i_i)

        translations = str.maketrans(
            {
                COMMA: EMPTY,
                # PERIOD: SPACE,
                # NEWLINE: SPACE,
                ASTERISK: EMPTY,
                EXCLAMATION: EMPTY,
                ":": SPACE,
                ";": SPACE,
                "<": SPACE,
                ">": SPACE,
                '"': EMPTY,
                "'": EMPTY,
                "-": SPACE,
                "–": SPACE,
                "—": SPACE,
                "(": EMPTY,
                ")": EMPTY,
                "?": EMPTY,
                "#": EMPTY,
                "$": EMPTY,
                "&": SPACE,
                "+": SPACE,
                "/": SPACE,
                "=": SPACE,
                "|": SPACE,
                "{": EMPTY,
                "}": EMPTY,
                "[": EMPTY,
                "]": EMPTY,
                "\\": SPACE,
            }
        )

        content = re.sub("({{< rawhtml >}})(.*?)({{< /rawhtml >}})", SPACE, content)

        word_list = content.translate(translations).replace(r"( {2,})", " ").split()

        # word_list = re.sub(r"[^\w\s]", SPACE, content).replace(r"( {2,})", " ").split()

        unique_words = set(word_list)

        unique_word_list = list(unique_words)

        unique_word_list.sort()

        characters = to_character_list2(unique_word_list)

        character_set = set(characters)

        character_set.add(" ")
        character_set.add(NEWLINE)

        filtered = list(filter(lambda x: x in character_set, list(content)))

        filtered_v = str.join("", filtered)

        element_list = list(set(content))

        element_list.sort()

        elements = str.join("", element_list)

        vectors = get_positive_vectors(elements, assessor)

        items.append(ElementMap(element_list, vectors, content))

    print(f"\nt:{timer.end()}")

    return items


def sanitise_contents(curator: ElementalCurator, contents: list[str]) -> list[str]:
    items: list[str] = []

    length = len(contents)

    timer = Timer(True)

    assessor = curator.quality_assessor()

    for i, content in enumerate(contents):
        print(f"{'progress [%d%%]\r'}" % ((i + 1) / length * 100), end="")

        sanitised = sanitise(content, assessor)

        items.append(sanitised)

    print(f"\nt:{timer.end()}")

    return items
