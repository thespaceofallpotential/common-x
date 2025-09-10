import math
import time


class Timer:
    __start: float = 0

    def __init__(self, start: bool = False) -> None:
        self.__start = 0.0

        if start:
            self.start()

    def start(self):
        self.__start = time.time()

    def end(self) -> int:
        value = math.floor(time.time() - self.__start)

        self.__start = 0

        return value
