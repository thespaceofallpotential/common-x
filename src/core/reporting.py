from core.range import PartitionVector, Range
from core.strings import space
from core.types import CommonRange
from typing import List, TypeVar, cast

T = TypeVar("T", int, str)

def values[T](values: List[T]) -> str:
    return str.join(space, cast(List[str], values))


def rangeValueString[T](r: Range) -> str:
    return values(cast(List[str], r.values))


def partitionString[T](r: Range) -> str:
    return f"p:{r.position} v:{rangeValueString(r)}"


def commonPartitionString[T](r: CommonRange) -> str:
    return f"a:{r.aPosition} b:{r.bPosition} v:{values(r.values)}"


def vectorString[T](pv: PartitionVector) -> str:
    return f"[{pv.position},{pv.length}]"


def vectorsString[T](a: PartitionVector, b: PartitionVector) -> str:
    return f"a:{vectorString(a)} | b:{vectorString(b)}"
