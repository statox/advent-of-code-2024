from typing import override

from ...base import BaseSolution, answer


class Solution(BaseSolution[list[list[int]]]):
    @override
    def parseInput(self):
        return [[int(i) for i in line] for line in self.lines]

    def computeSum(self, final_nb_digits: int):
        return sum(
            [self.lineProcessor(line, final_nb_digits) for line in self.parsedInput]
        )

    def lineProcessor(self, vals: list[int], final_nb_digits: int):
        s: list[int] = []
        removed = 0
        max_removed = len(vals) - final_nb_digits
        for d in vals:
            while len(s) > 0 and d > s[-1] and removed < max_removed:
                _ = s.pop()
                removed += 1
            s.append(d)

        return int("".join([str(i) for i in s[:final_nb_digits]]))

    @answer(357, 17311)
    @override
    def part1(self):
        return self.computeSum(2)

    @answer(3121910778619, 171419245422055)
    @override
    def part2(self):
        return self.computeSum(12)
