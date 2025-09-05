from core.sequence import Sequence
from utils.file_content_helper import FileContentHelper


class File[T]:
    path: str

    content: str

    sequence: Sequence

    def __init__(self, path: str, content: str) -> None:
        self.path = path
        self.content = content


class FileHelper:
    content_helper: FileContentHelper

    def __init__(self) -> None:
        self.content_helper = FileContentHelper()

    def get(self, path: str) -> File[str]:
        content = self.content_helper.get_content(path)

        file = File(path, content)

        return file
