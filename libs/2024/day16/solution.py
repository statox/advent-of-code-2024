import math
from typing import NamedTuple

from ...base import BaseSolution, answer
from ...utils.point import E, N, Point, S, W

# front, left, right, back
neighborsDirections = {
    N: [(N, 1), (W, 1001), (E, 1001), (S, 2001)],
    S: [(S, 1), (E, 1001), (W, 1001), (N, 2001)],
    E: [(E, 1), (N, 1001), (S, 1001), (W, 2001)],
    W: [(W, 1), (S, 1001), (N, 1001), (E, 2001)],
}


class Input(NamedTuple):
    g: list[list[str]]
    start: Point
    end: Point


def doWork(parsedInput: Input):
    (g, start, end) = parsedInput

    s = [(start, E, 0, [start])]
    seen: dict[tuple[Point, Point], int] = {}

    bestTiles: set[Point] = set()
    bestScore = math.inf
    while s:
        (pos, direction, score, path) = s.pop(0)

        if score > bestScore:
            continue

        prevScore = seen.get((pos, direction))
        if prevScore is not None and prevScore < score:
            continue
        seen[(pos, direction)] = score

        if pos == end:
            if score < bestScore:
                # print(
                #     f"  Found new best score. Previous was: {bestScore}, new is {score}"
                # )
                bestScore = score
                bestTiles = set()
            bestTiles = bestTiles.union(path)
            continue

        # Using the default value can not happen but I want to avoid checking that we do get a value
        for newDirection, scoreInc in neighborsDirections.get(direction, []):
            n = pos + newDirection
            if g[n.y][n.x] in ".E":
                s.append((n, newDirection, score + scoreInc, path + [n]))

    return (int(bestScore), len(bestTiles))


class Solution(BaseSolution[Input]):
    def parseInput(self):
        g = [list(line) for line in self.lines]
        start = Point(1, len(self.lines) - 2)
        end = Point(len(self.lines[0]) - 2, 1)
        return Input(g, start, end)

    @answer(7036, 98520)
    def part1(self):
        res = doWork(self.parsedInput)
        return res[0]

    @answer(45, 609)
    def part2(self):
        res = doWork(self.parsedInput)
        return res[1]
