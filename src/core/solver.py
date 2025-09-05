import abc

from core.processor import Processor


class Solver[T, C](Processor[T, C], metaclass=abc.ABCMeta):
    def __repr__(self) -> str:
        return f"{self.__class__}"
