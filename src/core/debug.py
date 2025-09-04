from typing import TypeVar
from core.range import Range
from core.reporting import rangeValueString, vectorsString

T = TypeVar("T", int, str)

isActive = False


def debugVectors[T](a: Range, b: Range, override: bool = False):
    if override or isActive:
        print(vectorsString(a, b))


def debugValues[T](a: Range, b: Range, override: bool = False):
    if override or isActive:
        print(f"{rangeValueString(a)} | {rangeValueString(b)}")
