import functools
import inspect
from dataclasses import dataclass
from pathlib import Path
from typing import Generic, Literal, TypeVar

PossibleAnswer = int | str


class InvalidSolutionError(Exception):
    def __init__(self, expected: PossibleAnswer, actual: PossibleAnswer):
        self.expected = expected
        self.actual = actual
        message = f"Invalid solution: Expected {expected}, but got {actual}"
        super().__init__(message)


class InvalidSolutionOptions(Exception):
    def __init__(self, message):
        super().__init__(f"Invalid solution options: {message}")


def answer(
    expectedAnswerTest: PossibleAnswer | None,
    expectedAnswerLivemode: PossibleAnswer | None,
):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            expectedAnswer = (
                expectedAnswerLivemode if self.livemode else expectedAnswerTest
            )
            res = func(self, *args, **kwargs)

            if expectedAnswer is not None and res != expectedAnswer:
                raise InvalidSolutionError(expected=expectedAnswer, actual=res)

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


@dataclass
class SolutionOptions:
    livemode: bool
    day: int = 1
    year: int = 2024
    lines: list[str] | None = None
    alternativeInputFile: int | None = None


class BaseSolution(Generic[ParsedInput]):
    lines: list[str]
    lines_alt: list[str] | None
    parsedInput: ParsedInput
    livemode: bool
    day: int
    year: int

    def __init__(self, options: SolutionOptions):
        self.livemode = options.livemode
        self.day = options.day
        self.year = options.year

        self.lines_alt = None

        if options.lines is not None and options.livemode:
            raise InvalidSolutionOptions(
                "Can't specify both lines when livemode is true"
            )

        if options.alternativeInputFile is not None and options.livemode:
            raise InvalidSolutionOptions(
                "Can't specify alternative input when livemode is true"
            )

        if options.lines is not None and options.alternativeInputFile is not None:
            raise InvalidSolutionOptions(
                "Can't specify both lines and alternativeInputFile"
            )

        if self.livemode:
            # In livemode always read the main input file
            inputPath = Path(self.getOwnPath(), "input")
            self.lines = read_input_file(inputPath)
        elif options.lines is not None:
            # If some lines are directly specified use that as the input
            self.lines = options.lines
        elif options.alternativeInputFile is None:
            # If not in livemode and no alternativeInputFile is specified use the input_test file
            inputPath = Path(self.getOwnPath(), "input_test")
            self.lines = read_input_file(inputPath)
        else:
            # If not in livemode and alternativeInputFile is specified try to use the corresponding file
            alternativeInputFile = Path(
                self.getOwnPath(), f"input_test_{options.alternativeInputFile}"
            )
            if not alternativeInputFile.exists():
                raise InvalidSolutionOptions(
                    f"Specified alternative file not found: {alternativeInputFile}"
                )

            self.lines = read_input_file(alternativeInputFile)

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
    def part1(self) -> PossibleAnswer:
        raise NotImplementedError

    @answer(0, 0)
    def part2(self) -> PossibleAnswer:
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
