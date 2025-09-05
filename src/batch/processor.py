from batch.file_domain import FileDomain
from core.options import Options
from core.types import T


class Processor[T]:
    options: Options | None

    file_domain: FileDomain

    def __init__(self, file_domain: FileDomain, options: Options | None = None) -> None:
        self.file_domain = file_domain
        self.options = options

    def process(self):
        position = 0

        length = len(self.file_domain)

        for i_a in range(length):
            a = self.file_domain.get_file(position)

            for i_b in range(length):
                if i_a == i_b:
                    continue

                b = self.file_domain.get_file(i_b)
