import abc

from core.processable import AbstractProcessable


class AbstractSolver[T, C](AbstractProcessable[T, C], metaclass=abc.ABCMeta):
    pass
