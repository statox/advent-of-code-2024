import re
from math import gcd
from typing import Literal, NamedTuple

from ...base import BaseSolution, answer


def countStepsForStation(
    start: str, end: str, directions: list[Literal[0, 1]], g: dict[str, tuple[str, str]]
):
    step = 0
    m: set[tuple[str, int]] = set()

    curr = start
    nbDirs = len(directions)
    while curr != end:
        dirIndex = step % nbDirs
        direction = directions[dirIndex]
        if (curr, dirIndex) in m:
            return -1

        m.add((curr, dirIndex))
        curr = g[curr][direction]
        step += 1
    return step


def lcm(numbers):
    lcm = numbers[0]
    for num in numbers[1:]:
        lcm = (lcm * num) // gcd(lcm, num)
    return lcm


class Input(NamedTuple):
    directions: list[Literal[0, 1]]
    g: dict[str, tuple[str, str]]
    startStations: list[str]
    endStations: list[str]


class Solution(BaseSolution[Input]):
    def parseInput(self):
        directions: list[Literal[0, 1]] = [
            0 if v == "L" else 1 for v in list(self.lines[0])
        ]

        startStations: list[str] = []
        endStations: list[str] = []
        g: dict[str, tuple[str, str]] = {}

        for line in self.lines[2:]:
            [key, t] = line.split(" = ")
            [left, right] = re.sub("\(|\)", "", t).split(", ")

            g[key] = (left, right)

            if key[-1] == "A":
                startStations.append(key)
            elif key[-1] == "Z":
                endStations.append(key)

        return Input(directions, g, startStations, endStations)

    @answer(6, 16579)
    def part1(self):
        (directions, g, _, _) = self.parsedInput
        return countStepsForStation("AAA", "ZZZ", directions, g)

    @answer(6, 12927600769609)
    def part2(self):
        (directions, g, startStations, endStations) = self.parsedInput

        periods = [
            period
            for period in [
                countStepsForStation(start, end, directions, g)
                for start in startStations
                for end in endStations
            ]
            if period != -1
        ]

        return lcm(periods)
