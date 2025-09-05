READ = "r"


class FileContentHelper:
    def get_content(self, path: str) -> str:
        io = open(path, READ)

        return io.read()
