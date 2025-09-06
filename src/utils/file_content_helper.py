READ = "r"


class FileContentHelper:
    def get_content(self, path: str) -> str:
        with open(path, READ, encoding="utf-8") as io:
            return io.read()
