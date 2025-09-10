from typing import List
from sanitisation.sanitisation_regex import (
    re_match,
)
from sanitisation.regex import StructuredRegexFragments
from sanitisation.sanitisation import Fetched
from sanitisation.positive_vectors import (
    PositiveVector,
    TStepAssessor,
    get_positive_vectors,
    print_vectors,
)


def assess_elements(
    elements: set[str], pattern: str, positive: bool = True
) -> set[str]:
    items: set[str] = set()

    for element in elements:
        if re_match(pattern, element, positive):
            items.add(element)

    return items


def is_match(content: str, i_c: int, pattern: str) -> bool:
    content_length = len(content)

    for i_p, pattern_character in enumerate(pattern):
        i_i = i_c + i_p

        if i_i < content_length:
            if content[i_i] != pattern_character:
                return False

    return True


def fetch_for(
    content: str, i_c: int, fragments: StructuredRegexFragments
) -> Fetched | None:
    start = fragments.start

    end = fragments.end

    if not start or not end:
        return None

    content_length = len(content)

    i_f = i_c + len(start)

    end_first = end[0:1]

    fetched = Fetched()

    while i_f < content_length:
        character = content[i_f]

        if character == end_first and is_match(content, i_f, end):
            i_f += len(end)

            fetched.i_start = i_c
            fetched.i_end = i_f
            fetched.value = content[i_c:i_f]

            return fetched

        i_f += 1

    return None


def sanitise(content: str, assessor: TStepAssessor) -> str:
    vectors = get_positive_vectors(content, assessor)

    return print_vectors(content, vectors)


class ElementMap:
    elements: list[str]

    positive_vectors: List[PositiveVector]

    content: str | None

    def __init__(
        self, elements: list[str], vectors: List[PositiveVector], content: str | None = None
    ) -> None:
        self.elements = elements
        self.positive_vectors = vectors
        self.content = content

    def __repr__(self) -> str:
        return f"e:{self.elements} v:{self.positive_vectors} c:{self.content}"

# class WordElementMap:
#     elements: list[str]

#     positive_vectors: List[PositiveVector]

#     content: str | None

#     def __init__(
#         self, elements: list[str], vectors: List[PositiveVector], content: str | None = None
#     ) -> None:
#         self.elements = elements
#         self.positive_vectors = vectors
#         self.content = content

#     def __repr__(self) -> str:
#         return f"e:{self.elements} v:{self.positive_vectors} c:{self.content}"
