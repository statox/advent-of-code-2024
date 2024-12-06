from ...base import BaseSolution, answer
from ...utils import Point

directions = [Point(0, -1), Point(1, 0), Point(0, 1), Point(-1, 0)]


def getInitialPosition(lines: list[str]):
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "^":
                return Point(x, y)

    raise Exception("Start position not found")


def getOriginalPath(lines: list[str]):
    g = [list(line) for line in lines]
    p = getInitialPosition(lines)
    directionIndex = 0
    bound = Point(len(g[0]) - 1, len(g) - 1)

    seen: set[Point] = set()

    nextP = p
    while nextP.isInBound(bound):
        seen.add(p)
        direction = directions[directionIndex]
        nextP = p + direction
        if nextP.isInBound(bound) and g[nextP.y][nextP.x] != "#":
            g[p.y][p.x] = "X"
            p = nextP
        else:
            directionIndex = (directionIndex + 1) % len(directions)

    return seen


def isLoopingGrid(initialPosition: Point, g: list[list[str]]):
    p = initialPosition
    directionIndex = 0
    bound = Point(len(g[0]) - 1, len(g) - 1)

    seen: set[Point] = set()

    nextP = p
    while nextP.isInBound(bound):
        seen.add((p, directionIndex))
        direction = directions[directionIndex]
        nextP = p + direction
        if (nextP, directionIndex) in seen:
            return True

        if nextP.isInBound(bound) and g[nextP.y][nextP.x] != "#":
            g[p.y][p.x] = "X"
            p = nextP
        else:
            directionIndex = (directionIndex + 1) % len(directions)

    return False


class Solution(BaseSolution):
    @answer(41, 5239)
    def part1(self):
        return len(getOriginalPath(self.lines))

    @answer(6, 1753)
    def part2(self):
        total = 0
        p = getInitialPosition(self.lines)
        path = getOriginalPath(self.lines)
        for cell in path:
            g = [list(line) for line in self.lines]
            g[cell.y][cell.x] = "#"
            if isLoopingGrid(p, g):
                # print(cell, "is possible obstacle")
                total += 1

        return total
