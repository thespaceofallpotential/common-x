from typing import List
from data.file import File
from utils.io_helper import DirectoryScanOptions
from utils.file_helper import FileHelper


class SourceHelper:
    file_helper: FileHelper

    relative_paths: List[str]

    def __init__(self, root: str) -> None:
        self.file_helper = FileHelper(root)
        self.relative_paths = []

    def add(self, relative_path: str):
        self.relative_paths.append(relative_path)

    def add_all_for(self, options: DirectoryScanOptions):
        options.relative = True

        paths = self.file_helper.get_file_paths(options)

        self.relative_paths.extend(paths)

    def get_content(self, path: str) -> str:
        file = self.get_file(path)

        return file.content

    def get_file(self, path: str) -> File:
        return self.file_helper.get_file(path)

    def get_files(self):
        return self.file_helper.get_files(self.relative_paths)
