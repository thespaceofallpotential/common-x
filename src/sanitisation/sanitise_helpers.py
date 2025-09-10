from typing import Callable

from core.strings import EMPTY
from sanitisation.sanitisation import PositiveVector


def print_vectors(content: str, vectors: list[PositiveVector]) -> str:
    positive_content = list(map(lambda x: content[x.i : x.i + x.length], vectors))

    return str.join(EMPTY, positive_content)


def sanitise(content: str, is_good: Callable[..., bool]) -> str:
    vectors: list[PositiveVector] = []

    current: PositiveVector | None = None

    for i, character in enumerate(content):
        if is_good(content, i, character):
            if current:
                current.length += 1
                continue

            current = PositiveVector(i, 1)

            vectors.append(current)
            continue

        current = None

    return print_vectors(content, vectors)
