class PartitionVector:
    position: int
    length: int

    def __init__(self, position: int, length: int):
        self.position = position
        self.length = length

    def get_end(self):
        return self.position + self.length

    def __repr__(self) -> str:
        return f"[p:{self.position},l:{self.length}]"


def vectors_str(a: PartitionVector, b: PartitionVector) -> str:
    return f"a:{a} | b:{b}"
