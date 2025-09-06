import os

from core.strings import EMPTY

SRC = "src"


class PathHelper:
    root: str

    absolute_root: str

    def __init__(self, root: str):
        self.root = root

        cwd_parts = os.getcwd().split(SRC)

        self.absolute_root = f"{cwd_parts[0]}{root}"

        print(self.absolute_root)

    def get_absolute_path(self, path: str) -> str:
        if path is EMPTY or self.absolute_root.endswith(path):
            return self.absolute_root

        return f"{self.absolute_root}/{path}"

    def get_relative_path(self, path: str) -> str:
        root = self.absolute_root

        def to_relative(path: str) -> str:
            return path[len(root) + 1 :]

        return to_relative(path) if path.startswith(root) else path

    def get_relative_paths(self, paths: list[str]) -> list[str]:
        return list(map(self.get_relative_path, paths))
