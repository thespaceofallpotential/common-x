import os


READ = "r"


class DirectoryScanOptions:
    path: str
    extension: str | None
    recursive: bool | None
    relative: bool | None

    def __init__(
        self,
        path: str,
        ext: str | None = None,
        recursive: bool | None = False,
        relative: bool | None = None,
    ) -> None:
        self.path = path
        self.extension = ext
        self.recursive = recursive
        self.relative = relative


class IOHelper:
    def get_content(self, path: str) -> str | None:
        try:
            with open(path, READ, encoding="utf-8") as io:
                return io.read()
        except:  # noqa: E722
            return None

    def get_file_paths(self, options: DirectoryScanOptions) -> list[str]:
        paths: list[str] = []

        ext = options.extension

        def is_valid(x: str) -> bool:
            return (ext and x.endswith(ext)) or not ext

        recursive = options.recursive

        def process(root: str):
            with os.scandir(root) as directory:
                for entry in directory:
                    path = entry.path

                    if entry.is_file() and is_valid(path):
                        paths.append(path)

                    if recursive and entry.is_dir():
                        process(path)

        process(options.path)

        return paths
