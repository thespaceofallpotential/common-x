from core.range import PartitionVector, Range
from core.strings import space
from typing import cast

from core.types import CommonRange


def values[T](values: list[T]) -> str:
    return str.join(space, cast(list[str], values))


def rangeValueString[T](r: Range[T]) -> str:
    return values(cast(list[str], r.values))


def partitionString[T](r: Range[T]) -> str:
    return f"p:{r.position} v:{rangeValueString(r)}"


def commonPartitionString[T](r: CommonRange[T]) -> str:
    return f"a:{r.aPosition} b:{r.bPosition} v:{values(r.values)}"


def vectorString[T](pv: PartitionVector) -> str:
    return f"[{pv.position},{pv.length}]"


def vectorsString[T](a: PartitionVector, b: PartitionVector) -> str:
    return f"a:{vectorString(a)} | b:{vectorString(b)}"
