from core.range import Range
from core.reporting import rangeValueString, vectorString, vectorsString

isActive = False


def debugVectors[T](a: Range[T], b: Range[T], override: bool = False):
    if override or isActive:
        print(vectorsString(a, b))


def debugValues[T](a: Range[T], b: Range[T], override: bool = False):
    if override or isActive:
        print(f"{rangeValueString(a)} | {rangeValueString(b)}")
