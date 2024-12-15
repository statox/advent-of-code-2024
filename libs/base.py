import functools
import inspect
from pathlib import Path
from typing import Generic, Literal, Optional, TypeVar


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


ParsedInput = TypeVar("ParsedInput")


class BaseSolution(Generic[ParsedInput]):
    lines: list[str]
    lines_alt: list[str] | None
    parsedInput: ParsedInput
    livemode: bool
    day: int
    year: int

    def __init__(
        self, livemode: bool, day: int, year: int, lines: Optional[list[str]] = None
    ):
        self.livemode = livemode
        self.day = day
        self.year = year

        self.lines_alt = None
        if lines is not None:
            self.lines = lines
        elif livemode:
            inputPath = Path(self.getOwnPath(), "input")
            self.lines = read_input_file(inputPath)
        else:
            inputPath = Path(self.getOwnPath(), "input_test")
            self.lines = read_input_file(inputPath)

            if Path(self.getOwnPath(), "input_test_2").exists():
                altInputPath = Path(self.getOwnPath(), "input_test_2")
                self.lines_alt = read_input_file(altInputPath)

        try:
            self.parsedInput = self.parseInput()
        except NotImplementedError:
            self.parsedInput = None

    @classmethod
    def getOwnPath(cls):
        module = inspect.getmodule(cls)
        if module is None or module.__file__ is None:
            raise Exception("Couldnt get class path")

        return Path(module.__file__).parent

    def parseInput(self) -> ParsedInput:
        """Implement to parse input in self.parsedInput"""
        """This function must not modify self.parsedInput but return its value"""
        raise NotImplementedError

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
            if not self.livemode and self.lines_alt is not None:
                print(
                    "WARNING: Using input_test_2 file as input. Remove it if to use input_test instead."
                )
                self.lines = self.lines_alt

            res = self.part2()
            print(
                f"Result for day {self.day}/{self.year} - part 2 - livemode {self.livemode}: {res}"
            )
