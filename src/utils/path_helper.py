class PathHelper:
    root: str

    def __init__(self, root: str):
        self.root = root

    def get_path(self, path: str) -> str:
        return f"{self.root}/{path}"
