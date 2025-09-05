READ = "r"


class FileContentHelper:
    def get_content(self, path: str) -> str:
        f = open(path, READ)

        return f.read()
