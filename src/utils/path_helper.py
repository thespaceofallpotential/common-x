import os

SRC = "src"


class PathHelper:
    root: str

    absolute_root: str

    def __init__(self, root: str):
        self.root = root

        cwd_parts = os.getcwd().split(SRC)

        self.absolute_root = f"{cwd_parts[0]}{root}"

        print(self.absolute_root)

    def get_path(self, path: str) -> str:
        return f"{self.absolute_root}/{path}"
