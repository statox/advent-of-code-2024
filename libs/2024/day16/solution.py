import math
from collections import deque
from typing import NamedTuple

from ...base import BaseSolution, answer
from ...utils.point import E, N, Point, S, W

# doWorkWithComplex implements the same function as doWork but uses the `complex` built-in type
# instead of my own `Point` class to represent points and directions, it makes for a nearly 40%
# run time improvement.
#
# doWorkWithComplexWrapper does the same but with a custom class used to wrap the `complex` type
# the performence is not as good as with the raw complex
#
# With complex:
# time ./main.py -d16 -l
# Result for day 16/2024 - part 1 - livemode True: 98520
# Result for day 16/2024 - part 2 - livemode True: 609
# ./main.py -d16 -l  13,94s user 0,07s system 99% cpu 14,020 total
#
# With complex wrapper:
# Result for day 16/2024 - part 1 - livemode True: 98520
# Result for day 16/2024 - part 2 - livemode True: 609
# ./main.py -d16 -l  20,86s user 0,06s system 99% cpu 20,926 total
#
# With Point:
# time ./main.py -d16 -l
# Result for day 16/2024 - part 1 - livemode True: 98520
# Result for day 16/2024 - part 2 - livemode True: 609
# ./main.py -d16 -l  23,47s user 0,07s system 99% cpu 23,545 total


class Input(NamedTuple):
    g: list[list[str]]
    start: Point
    end: Point


class CPoint:
    def __init__(self, x, y):
        self._complex = complex(x, y)

    @property
    def x(self):
        return self._complex.real

    @property
    def y(self):
        return self._complex.imag

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        return CPoint(self.x + other.x, self.y + other.y)

    def __hash__(self):
        return self._complex.__hash__()

    def __eq__(self, other):
        return isinstance(other, CPoint) and self._complex == other._complex


CCN = CPoint(0, -1)
CCS = CPoint(0, 1)
CCE = CPoint(1, 0)
CCW = CPoint(-1, 0)

# front, left, right, back
neighborsDirectionsCC = {
    CCN: [(CCN, 1), (CCW, 1001), (CCE, 1001), (CCS, 2001)],
    CCS: [(CCS, 1), (CCE, 1001), (CCW, 1001), (CCN, 2001)],
    CCE: [(CCE, 1), (CCN, 1001), (CCS, 1001), (CCW, 2001)],
    CCW: [(CCW, 1), (CCS, 1001), (CCN, 1001), (CCE, 2001)],
}


def doWorkWithComplexWrapper(parsedInput: Input):
    (g, start, end) = parsedInput

    startC = CPoint(start.x, start.y)
    endC = CPoint(end.x, end.y)

    s = deque([(startC, CCE, 0, [startC])])
    seen: dict[tuple[CPoint, CPoint], int] = {}

    bestTiles: set[CPoint] = set()
    bestScore = math.inf
    while s:
        (pos, direction, score, path) = s.popleft()
        # print(f"{pos} {direction} {score} {len(path)}")

        if score > bestScore:
            continue

        prevScore = seen.get((pos, direction))
        if prevScore is not None and prevScore < score:
            continue
        seen[(pos, direction)] = score

        if pos == endC:
            if score < bestScore:
                # print(
                #     f"  Found new best score. Previous was: {bestScore}, new is {score}"
                # )
                bestScore = score
                bestTiles = set()
            bestTiles = bestTiles.union(path)
            continue

        # Using the default value can not happen but I want to avoid checking that we do get a value
        for newDirection, scoreInc in neighborsDirectionsCC.get(direction, []):
            n = pos + newDirection
            if g[int(n.y)][int(n.x)] in ".E":
                s.append((n, newDirection, score + scoreInc, path + [n]))

    return (int(bestScore), len(bestTiles))


CN = 0 - 1j
CS = 0 + 1j
CE = 1 + 0j
CW = -1 + 0j

# front, left, right, back
neighborsDirectionsC = {
    CN: [(CN, 1), (CW, 1001), (CE, 1001), (CS, 2001)],
    CS: [(CS, 1), (CE, 1001), (CW, 1001), (CN, 2001)],
    CE: [(CE, 1), (CN, 1001), (CS, 1001), (CW, 2001)],
    CW: [(CW, 1), (CS, 1001), (CN, 1001), (CE, 2001)],
}


def doWorkWithComplex(parsedInput: Input):
    (g, start, end) = parsedInput

    startC = start.x + start.y * 1j
    endC = end.x + end.y * 1j

    s = deque([(startC, CE, 0, [startC])])
    seen: dict[tuple[complex, complex], int] = {}

    bestTiles: set[complex] = set()
    bestScore = math.inf
    while s:
        (pos, direction, score, path) = s.popleft()
        # print(f"{pos} {direction} {score} {len(path)}")

        if score > bestScore:
            continue

        prevScore = seen.get((pos, direction))
        if prevScore is not None and prevScore < score:
            continue
        seen[(pos, direction)] = score

        if pos == endC:
            if score < bestScore:
                # print(
                #     f"  Found new best score. Previous was: {bestScore}, new is {score}"
                # )
                bestScore = score
                bestTiles = set()
            bestTiles = bestTiles.union(path)
            continue

        # Using the default value can not happen but I want to avoid checking that we do get a value
        for newDirection, scoreInc in neighborsDirectionsC.get(direction, []):
            n = pos + newDirection
            if g[int(n.imag)][int(n.real)] in ".E":
                s.append((n, newDirection, score + scoreInc, path + [n]))

    return (int(bestScore), len(bestTiles))


# front, left, right, back
neighborsDirections = {
    N: [(N, 1), (W, 1001), (E, 1001), (S, 2001)],
    S: [(S, 1), (E, 1001), (W, 1001), (N, 2001)],
    E: [(E, 1), (N, 1001), (S, 1001), (W, 2001)],
    W: [(W, 1), (S, 1001), (N, 1001), (E, 2001)],
}


def doWork(parsedInput: Input):
    (g, start, end) = parsedInput

    s = deque([(start, E, 0, [start])])
    seen: dict[tuple[Point, Point], int] = {}

    bestTiles: set[Point] = set()
    bestScore = math.inf
    while s:
        (pos, direction, score, path) = s.popleft()
        # print(f"{pos} {direction} {score} {len(path)}")

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
        # res = doWork(self.parsedInput)
        res = doWorkWithComplex(self.parsedInput)
        return res[0]

    @answer(45, 609)
    def part2(self):
        # res = doWork(self.parsedInput)
        res = doWorkWithComplex(self.parsedInput)
        # res = doWorkWithComplexWrapper(self.parsedInput)
        return res[1]
