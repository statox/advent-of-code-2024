import functools


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


class BaseSolution:
    lines: list[str]
    livemode: bool

    def __init__(self, lines: list[str], livemode: bool):
        self.lines = lines
        self.livemode = livemode

    @answer(0, 0)
    def part1(self) -> int:
        raise NotImplementedError

    @answer(0, 0)
    def part2(self) -> int:
        raise NotImplementedError
