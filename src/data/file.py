from utils.path_helper import PathHelper
from utils.file_content_helper import FileContentHelper


class File[T]:
    path: str

    content: str

    def __init__(self, path: str, content: str) -> None:
        self.path = path
        self.content = content


class FileHelper(PathHelper):
    content_helper: FileContentHelper

    def __init__(self, root: str) -> None:
        super().__init__(root)

        self.content_helper = FileContentHelper()

    def get_file(self, path: str) -> File[str]:
        full_path = self.get_path(path)

        content = self.content_helper.get_content(full_path)

        file = File(path, content)

        return file
