import abc

from core.processable import AbstractProcessable


class AbstractSolver[T, C](AbstractProcessable[T, C], metaclass=abc.ABCMeta):
    pass

    def __repr__(self) -> str:
        return f"{self.__class__}"