from enum import Enum
from typing import List


class FileState(Enum):
    NONE = 0
    OK = 1
    ERROR = 2


class File:
    path: str

    content: str

    state: FileState = FileState.NONE

    frontmatter: str | None = None

    large: list[str] | None = None

    numbers: list[str] | None = None

    def __init__(self, path: str, content: str) -> None:
        self.path = path
        self.content = content

    def ok(self):
        return self.state == FileState.OK


def are_ok(files: List[File]) -> List[File]:
    return list(filter(lambda x: x.ok(), files))
