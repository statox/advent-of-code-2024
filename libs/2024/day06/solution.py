from ...base import BaseSolution, answer
from ...utils.point import Point

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
    p = (initialPosition.x, initialPosition.y)
    directionIndex = 0
    bound = (len(g[0]) - 1, len(g) - 1)

    seen = [[[] for _ in line] for line in g]

    nextP = (p[0], p[1])
    nextPInBound = True

    while nextPInBound:
        seen[p[1]][p[0]].append(directionIndex)

        direction = directions[directionIndex]
        nextP = (p[0] + direction.x, p[1] + direction.y)

        nextPInBound = (
            nextP[0] <= bound[0]
            and nextP[1] <= bound[1]
            and nextP[0] >= 0
            and nextP[1] >= 0
        )
        if nextPInBound and directionIndex in seen[nextP[1]][nextP[0]]:
            return True

        if nextPInBound and g[nextP[1]][nextP[0]] != "#":
            g[p[1]][p[0]] = "X"
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
        g = [list(line) for line in self.lines]
        for cell in path:
            g[cell.y][cell.x] = "#"
            if isLoopingGrid(p, g):
                total += 1
            g[cell.y][cell.x] = "."

        return total
