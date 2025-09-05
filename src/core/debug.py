from typing import TypeVar
from core.range import Range, range_values_str, vectors_str

T = TypeVar("T", int, str)

IS_ACTIVE = False


def debug_vectors(a: Range, b: Range, override: bool = False):
    if override or IS_ACTIVE:
        print(vectors_str(a, b))


def debug_values(a: Range, b: Range, override: bool = False):
    if override or IS_ACTIVE:
        print(f"{range_values_str(a)} | {range_values_str(b)}")
