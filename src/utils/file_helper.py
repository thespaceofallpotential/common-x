from typing import List
from data.file import File
from core.strings import EMPTY
from utils.progress import TimedProgress
from utils.path_helper import PathHelper
from utils.io_helper import IOHelper, ScanOptions


class FileHelper(PathHelper):
    io_helper: IOHelper

    def __init__(self, root: str) -> None:
        super().__init__(root)

        self.io_helper = IOHelper()

    def get_file(self, path: str) -> File:
        full_path = self.get_absolute_path(path)

        content = self.io_helper.get_content(full_path) or EMPTY

        file = File(path, content)

        return file

    def get_files(self, paths: list[str]) -> List[File]:
        items: List[File] = []

        relative_paths = self.get_relative_paths(paths)

        progress = TimedProgress("retrieving files", len(paths))

        for i, relative_path in enumerate(relative_paths):
            progress.update(i)

            file = self.get_file(relative_path)

            items.append(file)

        progress.complete()

        return items

    def get_file_paths(self, options: ScanOptions) -> list[str]:
        if options.path is None:
            options.path = self.root

        options.path = self.get_absolute_path(options.path)

        absolute_paths = self.io_helper.get_file_paths(options)

        relative = options.relative

        return (
            absolute_paths if not relative else self.get_relative_paths(absolute_paths)
        )
