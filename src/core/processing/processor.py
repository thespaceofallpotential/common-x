from typing import TypeVar

from core.processing.fileDomain import FileDomain
from core.options import Options


T = TypeVar("T", int, str)


class Processor[T]:
    options: Options | None

    file_domain: FileDomain

    def __init__(self, file_domain: FileDomain, options: Options | None = None) -> None:
        self.file_domain = file_domain
        self.options = options

    def process(self):
        position = 0

        length = len(self.file_domain)

        while position < length:
            a = self.file_domain.get_file(position)

            for i_b in range(length):
                b = self.file_domain.get_file(i_b)

