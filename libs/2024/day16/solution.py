import math
from functools import cmp_to_key
from typing import NamedTuple

from ...base import BaseSolution, answer
from ...utils.point import E, N, Point, S, W

directions = [E, N, W, S]

directionsIndices = {E: 0, N: 1, W: 2, S: 3}


class Input(NamedTuple):
    g: list[list[str]]
    start: Point
    end: Point


def pathCost(path: list[Point]):
    cost = 0

    currentDirection = E
    for i in range(len(path) - 1):
        transitionDirection = path[i + 1] - path[i]

        if transitionDirection == currentDirection:
            cost += 1
        else:
            indexCurrentDirection = directionsIndices.get(currentDirection, 0)
            indexTransitionDirection = directionsIndices.get(transitionDirection, 0)
            diff = abs(indexCurrentDirection - indexTransitionDirection)

            if diff in (1, 3):
                cost += 1001
            else:
                cost += 2001

            currentDirection = transitionDirection

        # print(
        #     f"from {path[i]} to {path[i+1]} direction: {transitionDirection}, cost: {cost}"
        # )
    return cost


class Solution(BaseSolution[Input]):
    def parseInput(self):
        g = [list(line) for line in self.lines]
        start = Point(1, len(self.lines) - 2)
        end = Point(len(self.lines[0]) - 2, 1)
        return Input(g, start, end)

    @answer(7036, 98520)
    def part1(self):
        (g, start, end) = self.parsedInput

        s = [(start, E, 0)]
        seen: dict[tuple[Point, Point], int] = {}

        bestScore = math.inf
        iteration = 0
        while s:
            iteration += 1
            if iteration % 1000000 == 0:
                print(f"{iteration}, {len(s)} best {bestScore}")
            (pos, direction, score) = s.pop(0)

            if pos == end:
                if score < bestScore:
                    print(
                        f"  Found new best score. Previous was: {bestScore}, new is {score}"
                    )
                    bestScore = score
                continue

            prevScore = seen.get((pos, direction))
            if prevScore is not None and prevScore < score:
                continue

            seen[(pos, direction)] = score
            directionIndex = directions.index(direction)

            frontPos = pos + direction
            if g[frontPos.y][frontPos.x] in ".E":
                s.append((frontPos, direction, score + 1))

            leftDir = directions[(directionIndex + 1) % 4]
            leftPos = pos + leftDir
            leftBlock = g[leftPos.y][leftPos.x]
            if leftBlock in ".E":
                s.append((leftPos, leftDir, score + 1001))

            rightDir = directions[(directionIndex + 3) % 4]
            rightPos = pos + rightDir
            rightBlock = g[rightPos.y][rightPos.x]
            if rightBlock in ".E":
                s.append((rightPos, rightDir, score + 1001))

            backDir = directions[(directionIndex + 2) % 4]
            backPos = pos + backDir
            backBlock = g[backPos.y][backPos.x]
            if backBlock in ".E":
                s.append((backPos, backDir, score + 2001))

        return int(bestScore)

    @answer(45, 609)
    def part2(self):
        part1BestScore = 98520 if self.livemode else 7036
        (g, start, end) = self.parsedInput

        s = [(start, E, 0, [start])]
        seen: dict[tuple[Point, Point], int] = {}

        allBestTiles: set[Point] = set()
        bestScore = part1BestScore
        iteration = 0
        while s:
            iteration += 1
            if iteration % 1000000 == 0:
                print(f"{iteration}, {len(s)}")
            (pos, direction, score, path) = s.pop(0)

            if score > bestScore:
                continue

            if pos == end:
                print(f"  Found new best score path {score}")
                [allBestTiles.add(p) for p in path]
                continue

            prevScore = seen.get((pos, direction))
            if prevScore is not None and prevScore < score:
                continue

            seen[(pos, direction)] = score
            directionIndex = directions.index(direction)

            frontPos = pos + direction
            if g[frontPos.y][frontPos.x] in ".E":
                s.append((frontPos, direction, score + 1, path + [frontPos]))

            leftDir = directions[(directionIndex + 1) % 4]
            leftPos = pos + leftDir
            leftBlock = g[leftPos.y][leftPos.x]
            if leftBlock in ".E":
                s.append((leftPos, leftDir, score + 1001, path + [leftPos]))

            rightDir = directions[(directionIndex + 3) % 4]
            rightPos = pos + rightDir
            rightBlock = g[rightPos.y][rightPos.x]
            if rightBlock in ".E":
                s.append((rightPos, rightDir, score + 1001, path + [rightPos]))

            backDir = directions[(directionIndex + 2) % 4]
            backPos = pos + backDir
            backBlock = g[backPos.y][backPos.x]
            if backBlock in ".E":
                s.append((backPos, backDir, score + 2001, path + [backPos]))

        return len(allBestTiles)
