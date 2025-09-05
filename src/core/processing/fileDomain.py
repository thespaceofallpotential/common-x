from typing import List
from core.processing.file import File


class FileDomain:
    files: List[File]

    def __init__(self, files: List[File]) -> None:
        self.files = files

    def get_file(self, i: int) -> File:
        return self.files[i]

    def __len__(self):
        return self.files.__len__()
