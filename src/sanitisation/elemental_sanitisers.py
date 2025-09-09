from typing import Callable

from core.strings import EMPTY
from sanitisation.elemental_culture import ElementalCulture
from sanitisation.sanitisation_regex import SanitisationTypes


def sanitise(content: str, fn: Callable[..., bool]) -> str:
    items: list[str] = []

    for i in range(len(content)):
        x = content[i]

        if fn(x):
            items.append(x)

    return str.join(EMPTY, items)


class BasicElementalSanitiser:
    culture: ElementalCulture

    key_space: dict[str, str]

    def __init__(self, culture: ElementalCulture) -> None:
        self.culture = culture

        self.key_space = dict()

    def build(self):
        elements = self.culture.curated_elements[SanitisationTypes.WS]

        for element in elements:
            self.key_space[element] = "OK"

    def sanitise(self, content: str) -> str:
        def is_good(element: str) -> bool:
            return bool(self.key_space.get(element))

        sanitised = sanitise(content, is_good)

        return sanitised


class StructuredElementalSanitiser(BasicElementalSanitiser):
    def __init__(self, culture: ElementalCulture) -> None:
        super().__init__(culture)

    def build(self):
        elements = self.culture.curated_elements[SanitisationTypes.WS]

        for element in elements:
            self.key_space[element] = "OK"

    def sanitise(self, content: str) -> str:
        def is_good(element: str) -> bool:
            return bool(self.key_space.get(element))

        sanitised = sanitise(content, is_good)

        return sanitised
