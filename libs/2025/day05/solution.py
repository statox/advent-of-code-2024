from typing import NamedTuple, override

from ...base import BaseSolution, answer


class ParsedInput(NamedTuple):
    ranges: list[tuple[int, int]]
    ids: list[int]


class Solution(BaseSolution[ParsedInput]):
    @override
    def parseInput(self):
        splitIndex = self.lines.index("")
        rangesInput = self.lines[:splitIndex]
        idsInput = self.lines[splitIndex + 1 :]

        # Parse ids as integers
        ids = [int(i) for i in idsInput]

        # Parse ranges as tuple of integers
        ranges: list[tuple[int, int]] = []
        for rInput in rangesInput:
            [a, b] = [int(c) for c in rInput.split("-")]
            ranges.append((a, b))

        #
        # Merge overlapping ranges
        #
        # First sort ranges by their lower bound
        ranges = sorted(ranges, key=lambda x: x[0])
        # Keep merging adjacent ranges until no more merge is possible
        prev_len = 0
        while len(ranges) != prev_len:
            prev_len = len(ranges)
            i = 0
            while i < len(ranges) - 1:
                (a, b) = ranges[i]
                (c, d) = ranges[i + 1]

                if (c >= a and c <= b) or (d >= a and d <= b):
                    ranges[i] = (min(a, c), max(b, d))
                    _ = ranges.pop(i + 1)
                else:
                    i += 1

        return ParsedInput(ranges, ids)

    @answer(3, 828)
    @override
    def part1(self):
        (ranges, ids) = self.parsedInput
        return sum(i >= a and i <= b for a, b in ranges for i in ids)

    @answer(14, 352681648086146)
    @override
    def part2(self):
        (ranges, _) = self.parsedInput
        return sum(b - a + 1 for a, b in ranges)
