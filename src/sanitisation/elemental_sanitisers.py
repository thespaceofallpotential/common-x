from typing import Callable, Dict

from core.strings import EMPTY
from sanitisation.elemental_culture import ElementalCulture
from sanitisation.sanitisation_regex import SanitisationTypes


def is_match(content: str, i: int, pattern: str) -> bool:
    for i_i in range(len(pattern)):
        if content[i + i_i] != pattern[i_i]:
            return False

    return True


def sanitise(content: str, fn: Callable[..., bool]) -> str:
    items: list[str] = []

    for i, character in enumerate(content):
        if fn(i, character):
            items.append(character)

    return str.join(EMPTY, items)


class QualityClass:
    structures: Dict[SanitisationTypes, str]

    def __init__(self) -> None:
        self.structures = {}

    def isStructured(self):
        return len(self.structures) > 0


class BasicElementalSanitiser:
    culture: ElementalCulture

    key_space: dict[str, QualityClass | None]

    def __init__(self, culture: ElementalCulture) -> None:
        self.culture = culture

        self.key_space = {}

    def build(self):
        for key in self.culture.curated_elements:
            elements = self.culture.curated_elements[key]

            regex = self.culture.regex_map[key]

            for element in elements:
                current = self.key_space.get(element)

                if current and regex.positive:
                    continue

                if current and not regex.positive:
                    print("uh oh")

                self.key_space[element] = QualityClass() if regex.positive else None

    def sanitise(self, content: str) -> str:
        def is_good(i: int, character: str) -> bool:
            if character == "[":
                print("herere")

            state = self.key_space.get(character)

            if not state:
                return False

            for structure in state.structures:
                structured = self.culture.structured_elements[structure]

                first = structured.get("first") # TODO: rethink this dict, etc. lol, looks around...

                if first and character == first:
                    start = structured.get("start")

                    if start and is_match(content, i, start):
                        print(f"\nstart:{start}")

            # if not state.isStructured():
            #     return True

            return True

        sanitised = sanitise(content, is_good)

        return sanitised


class StructuredElementalSanitiser(BasicElementalSanitiser):
    def __init__(self, culture: ElementalCulture) -> None:
        super().__init__(culture)

    def build(self):
        super().build()

        for key in self.culture.structured_elements:
            elements = self.culture.structured_elements[key]

            first = elements.get("first")

            if first:
                current = self.key_space.get(first)

                if not current:
                    current = QualityClass()
                    self.key_space[first] = current

                current.structures[key] = f"{key}"

    # def sanitise(self, content: str) -> str:
    #     su
    #     def is_good(element: str) -> bool:
    #         return bool(self.key_space.get(element))

    #     sanitised = sanitise(content, is_good)

    #     return sanitised
