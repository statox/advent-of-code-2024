from typing import Literal

from ...base import BaseSolution, answer


def generateReportSteps(s: list[int]):
    def getNextS(s: list[int]):
        return [s[i + 1] - s[i] for i in range(len(s) - 1)]

    def isFinal(s: list[int]):
        return not any(v for v in s if v != 0)

    steps = [s]
    while not isFinal(steps[-1]):
        steps.append(getNextS(steps[-1]))

    return steps


class Solution(BaseSolution[list[list[list[int]]]]):
    def parseInput(self):
        return [
            generateReportSteps(report)
            for report in [[int(v) for v in line.split(" ")] for line in self.lines]
        ]

    @answer(114, 2101499000)
    def part1(self):
        return self.doAll("back")

    @answer(2, 1089)
    def part2(self):
        return self.doAll("front")

    def doAll(self, op: Literal["front", "back"]):
        return sum([self.doOne(op, reportSteps) for reportSteps in self.parsedInput])

    def doOne(self, operation: Literal["front", "back"], steps: list[list[int]]):
        res = 0
        for step in steps[::-1]:
            if operation == "back":
                res = step[-1] + res
                step.append(res)
            else:
                res = step[0] - res
                step.insert(0, res)

        return res
