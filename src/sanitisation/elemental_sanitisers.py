from typing import Callable, Dict

from sanitisation.elemental_culture import ElementalCulture
from sanitisation.regex import FragmentTypes
from sanitisation.sanitisation import Fetched, QualityClass
from sanitisation.sanitise_helpers import sanitise
from sanitisation.elemental_curator import ElementalCurator
from utils.timer import Timer

type Curator = Dict[str, QualityClass | None]


def is_match(content: str, i_c: int, pattern: str) -> bool:
    content_length = len(content)

    for i_p, pattern_character in enumerate(pattern):
        i_i = i_c + i_p

        if i_i < content_length:
            if content[i_i] != pattern_character:
                return False

    return True


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


class ElementalSanitiser:
    culture: ElementalCulture

    curator: ElementalCurator

    def __init__(self, curator: ElementalCurator) -> None:
        self.culture = curator.culture

        self.curator = curator

    def is_good(self) -> Callable[..., bool]:
        culture = self.culture
        curator = self.curator

        def is_good(content: str, i: int, character: str) -> bool:
            state = curator.collection.get(character)

            if not state:
                return False

            for structured_sanitisation_key in state.structured_sanitisation:
                fragments = culture.structured_fragments[structured_sanitisation_key]

                first = fragments.get(FragmentTypes.FIRST)

                if first and character == first:
                    start = fragments.get(FragmentTypes.START)

                    if start and is_match(content, i, start):
                        print(f"\nstart:{start}")

                        fetched = Fetched()

                        if is_fetched(content, i, fragments, fetched):
                            print(f"{structured_sanitisation_key}: {fetched}")

                        # walk to end
            return True  # if state and not state.isStructured(): return True

        return is_good

    def sanitise(self, content: str) -> str:
        # vectors: list[PositiveVector] = []

        sanitised2 = sanitise(content, self.is_good())

        return sanitised2

    def get_positive_vectors(self, content: str) -> str:
        # vectors: list[PositiveVector] = []
        sanitised2 = sanitise(content, self.is_good())

        return sanitised2


def sanitise_contents(contents: list[str], curator: ElementalCurator) -> list[str]:
    sanitiser = ElementalSanitiser(curator)

    all_sanitised: list[str] = []

    length = len(contents)

    timer = Timer()

    timer.start()

    for i, content in enumerate(contents):
        print(f"{'progress [%d%%]\r'}" % ((i + 1) / length * 100), end="")

        sanitised = sanitiser.sanitise(content)

        all_sanitised.append(sanitised)

    print(f"\nt:{timer.end()}")

    return all_sanitised
