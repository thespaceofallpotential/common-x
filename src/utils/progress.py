from utils.timer import Timer


def progress(message: str, i: int, length: int):
    print(f"{message} [%d%%]\r" % ((i + 1) / length * 100), end="")


def progress_complete(message: str, time: float):
    print(f"{message} [100%] t: {time:.4f}s")
    

class TimedProgress:
    timer: Timer

    message: str
    length: int

    def __init__(self, message: str, length: int, start: bool = True) -> None:
        self.message = message
        self.length = length

        self.timer = Timer(True)

    def update(self, i: int):
        progress(f"{self.message}: progress", i, self.length)

    def complete(self):
        ms = self.timer.duration() / 1000000

        s = ms / 1000

        progress_complete(f"{self.message}: ", s)
