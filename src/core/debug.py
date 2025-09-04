from typing import TypeVar
from core.range import Range, rangeValues, vectorsString

T = TypeVar("T", int, str)

isActive = False


def debugVectors[T](a: Range, b: Range, override: bool = False):
    if override or isActive:
        print(vectorsString(a, b))


def debugValues[T](a: Range, b: Range, override: bool = False):
    if override or isActive:
        print(f"{rangeValues(a)} | {rangeValues(b)}")
