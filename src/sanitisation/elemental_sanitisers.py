from typing import Callable, Dict

from core.strings import EMPTY
from sanitisation.elemental_culture import ElementalCulture
from sanitisation.sanitisation_regex import SanitisationTypes
from sanitisation.regex import FragmentTypes


def is_match(content: str, i_c: int, pattern: str) -> bool:
    content_length = len(content)

    for i_p, pattern_character in enumerate(pattern):
        i_i = i_c + i_p

        if i_i < content_length:
            if content[i_i] != pattern_character:
                return False

    return True


class Fetched:
    i_start: int = 0
    i_end: int = 0
    value: str = EMPTY

    def __repr__(self) -> str:
        return f"s:{self.i_start} e:{self.i_end} v:{self.value}"


def is_fetched(
    content: str, i_c: int, fragments: Dict[FragmentTypes, str], fetched: Fetched
):
    start = fragments.get(FragmentTypes.START)

    end = fragments.get(FragmentTypes.END)

    if not start or not end:
        return False

    content_length = len(content)

    i_f = i_c + len(start)

    end_first = end[0:1]

    while i_f < content_length:
        character = content[i_f]

        if character == end_first and is_match(content, i_f, end):
            i_f += len(end)

            fetched.i_start = i_c
            fetched.i_end = i_f
            fetched.value = content[i_c:i_f]

            return True

        i_f += 1

    return False


def sanitise(content: str, fn: Callable[..., bool]) -> str:
    items: list[str] = []

    for i, character in enumerate(content):
        if fn(i, character):
            items.append(character)

    return str.join(EMPTY, items)


class QualityClass:
    structured_sanitisation: Dict[SanitisationTypes, str]

    def __init__(self) -> None:
        self.structured_sanitisation = {}

    def is_structured(self):
        return len(self.structured_sanitisation) > 0


class BasicElementalSanitiser:
    culture: ElementalCulture

    key_space: dict[str, QualityClass | None]

    def __init__(self, culture: ElementalCulture) -> None:
        self.culture = culture

        self.key_space = {}

    def build(self):
        for sanitisation_key in self.culture.curated_elements:
            elements = self.culture.curated_elements[sanitisation_key]

            regex = self.culture.regex_map[sanitisation_key]

            for element in elements:
                current = self.key_space.get(element)

                if current and regex.positive:
                    continue

                if current and not regex.positive:
                    print("uh oh")

                self.key_space[element] = QualityClass() if regex.positive else None

    def sanitise(self, content: str) -> str:
        def is_good(i: int, character: str) -> bool:
            state = self.key_space.get(character)

            if not state:
                return False

            for structured_sanitisation_key in state.structured_sanitisation:
                fragments = self.culture.structured_fragments[
                    structured_sanitisation_key
                ]

                first = fragments.get(FragmentTypes.FIRST)

                if first and character == first:
                    start = fragments.get(FragmentTypes.START)

                    if start and is_match(content, i, start):
                        print(f"\nstart:{start}")

                        fetched = Fetched()

                        if is_fetched(content, i, fragments, fetched):
                            print(f"{structured_sanitisation_key}: {fetched}")

                        # walk to end

            # if not state.isStructured():
            #     return True

            return True

        sanitised = sanitise(content, is_good)

        return sanitised


class StructuredElementalSanitiser(BasicElementalSanitiser):
    def build(self):
        super().build()

        for key in self.culture.structured_fragments:
            elements = self.culture.structured_fragments[key]

            first = elements.get(FragmentTypes.FIRST)

            if first:
                current = self.key_space.get(first)

                if not current:
                    current = QualityClass()
                    self.key_space[first] = current

                current.structured_sanitisation[key] = f"{key}"

    # def sanitise(self, content: str) -> str:
    #     su
    #     def is_good(element: str) -> bool:
    #         return bool(self.key_space.get(element))

    #     sanitised = sanitise(content, is_good)

    #     return sanitised
