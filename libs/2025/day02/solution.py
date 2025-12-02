from typing import Callable, override

from ...base import BaseSolution, answer


class Solution(BaseSolution[list[tuple[int, int]]]):
    @override
    def parseInput(self):
        ranges: list[tuple[int, int]] = []
        for rangeStr in self.lines[0].split(","):
            [a, b] = rangeStr.split("-")
            ranges.append((int(a), int(b)))

        return ranges

    def findInvalid(self, checker: Callable[[str], bool]):
        ranges = self.parsedInput
        total = 0

        for a, b in ranges:
            for i in range(a, b + 1):
                s = str(i)
                if checker(s):
                    total += i

        return total

    @answer(1227775554, 40055209690)
    @override
    def part1(self):
        def checker(s: str) -> bool:
            mid = len(s) // 2
            return s[:mid] == s[mid:]

        return self.findInvalid(checker)

    @answer(4174379265, 50857215650)
    @override
    def part2(self):
        def checker(s: str) -> bool:
            n = len(s)

            for pattern_len in range(1, n // 2 + 1):
                # Only check if the pattern length divides the string length evenly
                if n % pattern_len == 0:
                    pattern = s[:pattern_len]
                    # Check if repeating this pattern creates the original string
                    if pattern * (n // pattern_len) == s:
                        return True

            return False

        return self.findInvalid(checker)
