from typing import List


class Batch[C]:
    ai: int
    bi: int

    items: List[C]

    def __init__(self, ai: int, bi: int, items: List[C]):
        self.ai = ai
        self.bi = bi

        self.items = items

    def __repr__(self) -> str:
        return f"ai:{self.ai} bi:{self.bi}, c: --[{str.join(': ', list(map(lambda item: f'{item}', self.items)))}]-- "
