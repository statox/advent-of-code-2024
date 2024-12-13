from math import inf
from typing import NamedTuple

from ...base import BaseSolution, answer
from ...utils.point import E, N, Point, S, W

directions = [E, S, W, N]


class Group(NamedTuple):
    points: list[Point]
    area: int
    perimeter: int


def getGroups(g: list[list[str]]):
    seen: set[Point] = set()
    bound = Point(len(g[0]) - 1, len(g) - 1)

    groups: list[Group] = []
    for y, line in enumerate(g):
        for x in range(len(line)):
            p = Point(x, y)
            if p in seen:
                continue

            group: list[Point] = []

            stack = [p]
            perimeter = 0
            area = 0
            while stack:
                curr = stack.pop()
                if curr in seen:
                    continue
                group.append(curr)
                seen.add(curr)

                area += 1
                for direction in directions:
                    neighborPos = curr + direction

                    if not neighborPos.isInBound(bound):
                        perimeter += 1
                        continue

                    neighbor = g[neighborPos.y][neighborPos.x]

                    if neighbor != g[curr.y][curr.x]:
                        perimeter += 1
                        continue

                    stack.append(neighborPos)

            groups.append(Group(group, area, perimeter))
    return groups


# For a row count the needed fences on north and south
# For a col count the needed fences of left and right
def countFencesInDirections(
    group: list[Point], line: list[Point], directions: tuple[Point, Point]
):
    total = 0
    fenceA = False
    fenceB = False

    for p in line:
        neighborA = p + directions[0]
        neighborB = p + directions[1]

        isInGroup = p in group
        neighborAInGroup = neighborA in group
        neighborBInGroup = neighborB in group

        needsFenceA = isInGroup and not neighborAInGroup
        needsFenceB = isInGroup and not neighborBInGroup

        if fenceA and not needsFenceA:
            fenceA = False
        elif not fenceA and needsFenceA:
            fenceA = True
            total += 1

        if fenceB and not needsFenceB:
            fenceB = False
        elif not fenceB and needsFenceB:
            fenceB = True
            total += 1

    return total


class Solution(BaseSolution[list[list[str]]]):
    def parseInput(self):
        return [list(line) for line in self.lines]

    @answer(1930, 1424006)
    def part1(self):
        return sum(
            [area * perimeter for (_, area, perimeter) in getGroups(self.parsedInput)]
        )

    @answer(1206, 858684)
    def part2(self):
        groups = getGroups(self.parsedInput)

        total = 0
        for group, area, _ in groups:
            # groupChar = g[group[0].y][group[0].x]

            minP = Point(inf, inf)
            maxP = Point(0, 0)

            for p in group:
                minP.x = min(minP.x, p.x)
                minP.y = min(minP.y, p.y)
                maxP.x = max(maxP.x, p.x)
                maxP.y = max(maxP.y, p.y)

            rows = [
                [Point(x, y) for x in range(minP.x, maxP.x + 1)]
                for y in range(minP.y, maxP.y + 1)
            ]

            cols = [
                [Point(x, y) for y in range(minP.y, maxP.y + 1)]
                for x in range(minP.x, maxP.x + 1)
            ]

            fences = 0
            for col in cols:
                fences += countFencesInDirections(group, col, (E, W))

            for row in rows:
                fences += countFencesInDirections(group, row, (N, S))

            price = area * fences
            total += price
            # print(
            #     f"Group {groupChar} area {area} x fences {fences} = {price}    (total {total})"
            # )

        return total
