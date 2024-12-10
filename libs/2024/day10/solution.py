from typing import NamedTuple

from ...base import BaseSolution, answer
from ...utils.point import Point


class Input(NamedTuple):
    heads: list[Point]
    g: list[list[int]]


directions = [Point(0, -1), Point(1, 0), Point(0, 1), Point(-1, 0)]


def findTrailsForHead(head: Point, g: list[list[int]]):
    total = 0
    stack = [head]
    bound = Point(len(g[0]) - 1, len(g) - 1)
    seen: set[Point] = set()

    while stack:
        current = stack.pop()
        if current in seen:
            continue

        seen.add(current)
        currentValue = g[current.y][current.x]

        if currentValue == 9:
            total += 1
            continue

        [
            stack.append(neighbor)
            for neighbor in (current + d for d in directions)
            if neighbor.isInBound(bound)
            and g[neighbor.y][neighbor.x] == currentValue + 1
        ]

    return total


def countTrailsForHead(head: Point, g: list[list[int]]):
    total = 0
    stack: list[list[Point]] = [[head]]
    bound = Point(len(g[0]) - 1, len(g) - 1)

    while stack:
        currentTrail = stack.pop()
        current = currentTrail[-1]

        currentValue = g[current.y][current.x]

        if currentValue == 9:
            total += 1
            continue

        [
            stack.append(currentTrail + [neighbor])
            for neighbor in (current + d for d in directions)
            if neighbor.isInBound(bound)
            and g[neighbor.y][neighbor.x] == currentValue + 1
        ]

    return total


class Solution(BaseSolution[Input]):
    def parseInput(self):
        heads: list[Point] = []
        g: list[list[int]] = []

        for y, line in enumerate(self.lines):
            g.append([])
            for x, c in enumerate(line):
                if c == "0":
                    heads.append(Point(x, y))
                g[-1].append(int(c))
        return Input(heads, g)

    @answer(36, 538)
    def part1(self):
        (heads, g) = self.parsedInput
        return sum(findTrailsForHead(h, g) for h in heads)

    @answer(81, 1110)
    def part2(self):
        (heads, g) = self.parsedInput
        return sum(countTrailsForHead(h, g) for h in heads)
