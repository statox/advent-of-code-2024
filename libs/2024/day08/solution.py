import itertools

from ...base import BaseSolution, answer
from ...utils.point import Point


def getAntennaGroups(lines: list[str]):
    groups = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == ".":
                continue

            if groups.get(c) is None:
                groups[c] = []

            groups[c].append(Point(x, y))
    return groups


class Solution(BaseSolution):
    @answer(14, 278)
    def part1(self):
        groups = getAntennaGroups(self.lines)
        bound = Point(len(self.lines[0]) - 1, len(self.lines) - 1)

        antinodes: set[Point] = set()
        for group in groups:
            for a, b in itertools.combinations(groups[group], 2):
                atob = b - a
                btoa = a - b

                outerA = a + atob * 2
                outerB = b + btoa * 2

                if outerA.isInBound(bound):
                    antinodes.add(outerA)
                if outerB.isInBound(bound):
                    antinodes.add(outerB)

        return len(antinodes)

    @answer(34, 1067)
    def part2(self):
        groups = getAntennaGroups(self.lines)
        bound = Point(len(self.lines[0]) - 1, len(self.lines) - 1)

        antinodes: set[Point] = set()
        for group in groups:
            for a, b in itertools.combinations(groups[group], 2):
                atob = b - a
                mult = 1
                outerA = a
                while outerA.isInBound(bound):
                    antinodes.add(outerA)
                    mult += 1
                    outerA = a + atob * mult

                btoa = a - b
                mult = 1
                outerB = b
                while outerB.isInBound(bound):
                    antinodes.add(outerB)
                    mult += 1
                    outerB = b + btoa * mult

        return len(antinodes)
