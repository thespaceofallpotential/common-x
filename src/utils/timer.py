import math
import time


class Timer:
    __start: float = 0

    def __init__(self, start: bool = False) -> None:
        self.__start = 0.0

        if start:
            self.start()

    def start(self):
        self.__start = time.time_ns()

    def duration(self) -> int:
        difference = time.time_ns() - self.__start

        value = math.floor(difference)

        return value

    def duration_stop(self) -> int:
        value = self.duration()

        self.__start = 0

        return value
