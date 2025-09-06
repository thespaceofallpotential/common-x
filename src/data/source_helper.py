from typing import List
from data.file import File, FileHelper


class SourceHelper:
    file_helper: FileHelper

    names: List[str]

    def __init__(self, path: str) -> None:
        self.file_helper = FileHelper(path)
        self.names = []

    def add(self, name: str):
        self.names.append(name)

    def get_files(self) -> List[File]:
        return list(map(self.file_helper.get_file, self.names))

    def get_file(self, name: str) -> File:
        return self.file_helper.get_file(name)
