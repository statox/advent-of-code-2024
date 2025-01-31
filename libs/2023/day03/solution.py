from ...base import BaseSolution, answer
from ...utils.point import NE, NW, SE, SW, E, N, Point, S, W

directions = [N, S, E, W, NE, NW, SE, SW]


class Solution(BaseSolution):
    def _part1_v2(self):
        H = len(self.lines)
        W = len(self.lines[0])
        bound = Point(W, H)
        total = 0

        for y, line in enumerate(self.lines):
            for x, c in enumerate(line):
                if not c.isdigit() and c != ".":
                    p = Point(x, y)
                    seen: set[Point] = set()
                    for direction in directions:
                        neighbor = p + direction
                        if (
                            not neighbor.isInBound(bound)
                            or not self.lines[neighbor.y][neighbor.x].isdigit()
                        ):
                            continue

                        numberStart = neighbor.x
                        while (
                            numberStart > 0
                            and self.lines[neighbor.y][numberStart - 1].isdigit()
                        ):
                            numberStart -= 1

                        numberEnd = neighbor.x
                        while (
                            numberEnd <= W - 1
                            and self.lines[neighbor.y][numberEnd].isdigit()
                        ):
                            numberEnd += 1

                        partId = self.lines[neighbor.y][numberStart:numberEnd]

                        # print(
                        #     f"Symbol ({p.y:03},{p.x:03}) {self.lines[p.y][p.x]} touches {partId}"
                        # )

                        partCoords = Point(numberStart, neighbor.y)
                        if partCoords in seen:
                            continue

                        seen.add(partCoords)
                        total += int(partId)

        return total

    def _part1_v1(self):
        H = len(self.lines)
        W = len(self.lines[0])
        bound = Point(W - 1, H - 1)

        total = 0
        seen: set[Point] = set()
        for y, line in enumerate(self.lines):
            for x, c in enumerate(line):
                p = Point(x, y)
                if not c.isdigit() or p in seen:
                    continue

                end = x
                points = []
                while end <= W - 1 and line[end].isdigit():
                    dp = Point(end, y)
                    points.append(Point(end, y))
                    seen.add(dp)
                    end += 1
                partId = line[x:end]

                isValidId = False
                for p in points:
                    for direction in directions:
                        dest = p + direction
                        if (
                            not dest.isInBound(bound)
                            or self.lines[dest.y][dest.x].isdigit()
                            or self.lines[dest.y][dest.x] == "."
                        ):
                            continue
                        # print(
                        #     f"Symbol ({dest.y:03},{dest.x:03}) {self.lines[dest.y][dest.x]} touches {partId}"
                        # )
                        isValidId = True
                if isValidId:
                    total += int(partId)

        return total

    @answer(4361, 527446)
    def part1(self):
        # [print(line) for line in self.lines]
        return self._part1_v1()

    @answer(467835, 73201705)
    def part2(self):
        H = len(self.lines)
        W = len(self.lines[0])
        bound = Point(W, H)
        total = 0

        for y, line in enumerate(self.lines):
            for x, c in enumerate(line):
                if c == "*":
                    p = Point(x, y)
                    seen: set[Point] = set()
                    adjacentParts = []
                    for direction in directions:
                        neighbor = p + direction
                        if (
                            not neighbor.isInBound(bound)
                            or not self.lines[neighbor.y][neighbor.x].isdigit()
                        ):
                            continue

                        numberStart = neighbor.x
                        while (
                            numberStart > 0
                            and self.lines[neighbor.y][numberStart - 1].isdigit()
                        ):
                            numberStart -= 1

                        numberEnd = neighbor.x
                        while (
                            numberEnd <= W - 1
                            and self.lines[neighbor.y][numberEnd].isdigit()
                        ):
                            numberEnd += 1

                        partId = self.lines[neighbor.y][numberStart:numberEnd]

                        # print(
                        #     f"Symbol ({p.y:03},{p.x:03}) {self.lines[p.y][p.x]} touches {partId}"
                        # )

                        partCoords = Point(numberStart, neighbor.y)
                        if partCoords in seen:
                            continue

                        seen.add(partCoords)
                        adjacentParts.append(int(partId))

                    if len(adjacentParts) == 2:
                        ratio = adjacentParts[0] * adjacentParts[1]
                        # print(
                        #     f"Gear {p} r: {ratio} {adjacentParts[0]}*{adjacentParts[1]}"
                        # )
                        total += ratio

        return total
