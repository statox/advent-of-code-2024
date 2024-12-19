from functools import cache
from typing import NamedTuple

from ...base import BaseSolution, answer


class Input(NamedTuple):
    towels: list[str]
    patterns: list[str]


class Solution(BaseSolution[Input]):
    def parseInput(self):
        towels = [t.strip() for t in self.lines[0].split(",")]
        patterns = self.lines[2:]

        return Input(towels, patterns)

    @answer(6, 236)
    def part1(self):
        (towels, patterns) = self.parsedInput
        ts = [(t, len(t)) for t in towels]

        @cache
        def hasWays(prefix):
            if not prefix:
                return True
            return any(hasWays(prefix[tl:]) is True for t, tl in ts if prefix[:tl] == t)

        return len([pattern for pattern in patterns if hasWays(pattern)])

    @answer(16, 643685981770598)
    def part2(self):
        (towels, patterns) = self.parsedInput
        ts = [(t, len(t)) for t in towels]

        @cache
        def countWays(prefix):
            if not prefix:
                return 1
            return sum([countWays(prefix[tl:]) for t, tl in ts if prefix[:tl] == t])

        return sum([countWays(pattern) for pattern in patterns])
