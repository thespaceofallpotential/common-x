from typing import cast

from core.strings import SPACE


def to_str(values: list[int]) -> list[str]:
    return list(map(lambda x: f"{x}", values))


def as_str[T](elements: set[T]) -> list[str]:
    return to_str(cast(list[int], list(elements)))


def values_str(values: list[str]) -> str:
    return str.join(SPACE, values)


def elements_str(elements: set[str]) -> str:
    return str.join(SPACE, list(elements))
