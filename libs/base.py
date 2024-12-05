import functools
import inspect
from pathlib import Path
from typing import Literal, Optional


class InvalidSolutionError(Exception):
    def __init__(self, expected: int, actual: int):
        self.expected = expected
        self.actual = actual
        message = f"Invalid solution: Expected {expected}, but got {actual}"
        super().__init__(message)


def answer(expectedAnswerTest: int, expectedAnswerLivemode: int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            expectedAnswer = (
                expectedAnswerLivemode if self.livemode else expectedAnswerTest
            )
            res = func(self, *args, **kwargs)

            if res != expectedAnswer:
                raise InvalidSolutionError(expected=expectedAnswer, actual=res)

            # setattr(self, "failedWith", expectedAnswer)
            return res

        return wrapper

    return decorator


def read_input_file(path: Path):
    try:
        with Path.open(path, "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"The file {path} was not found.")
        raise
    except IOError:
        print("An error occurred while reading the file.")
        raise


class BaseSolution:
    lines: list[str]
    livemode: bool
    day: int
    year: int

    def __init__(
        self, livemode: bool, day: int, year: int, lines: Optional[list[str]] = None
    ):
        if lines is None:
            inputFile = "input" if livemode else "input_test"
            inputPath = Path(self.getOwnPath(), inputFile)

            self.lines = read_input_file(inputPath)
        else:
            self.lines = lines

        self.livemode = livemode
        self.day = day
        self.year = year

    @classmethod
    def getOwnPath(cls):
        module = inspect.getmodule(cls)
        if module is None or module.__file__ is None:
            raise Exception("Couldnt get class path")

        return Path(module.__file__).parent

    @answer(0, 0)
    def part1(self) -> int:
        raise NotImplementedError

    @answer(0, 0)
    def part2(self) -> int:
        raise NotImplementedError

    def runPart(self, which: Literal["one", "two", "both"]):
        if which in ["one", "both"]:
            res = self.part1()
            print(
                f"Result for day {self.day}/{self.year} - part 1 - livemode {self.livemode}: {res}"
            )

        if which in ["two", "both"]:
            res = self.part2()
            print(
                f"Result for day {self.day}/{self.year} - part 2 - livemode {self.livemode}: {res}"
            )
