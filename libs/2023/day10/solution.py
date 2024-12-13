from typing import NamedTuple

from ...base import BaseSolution, answer
from ...utils.point import Point


class Input(NamedTuple):
    g: list[list[str]]
    start: Point


N = Point(0, -1)
S = Point(0, 1)
E = Point(1, 0)
W = Point(-1, 0)
directions = [E, S, W, N]


allowedMoves = {
    "S": {
        "|": {N, S, E, W},
        "-": {N, S, E, W},
        "L": {N, S, E, W},
        "J": {N, S, E, W},
        "7": {N, S, E, W},
        "F": {N, S, E, W},
        ".": {},
    },
    "|": {
        "S": {N, S, E, W},
        ".": {},
        "|": {N, S},
        "-": {},
        "L": {S},
        "J": {S},
        "7": {N},
        "F": {N},
    },
    "-": {
        "S": {N, S, E, W},
        ".": {},
        "|": {},
        "-": {E, W},
        "L": {W},
        "J": {E},
        "7": {E},
        "F": {W},
    },
    "L": {
        "S": {N, S, E, W},
        ".": {},
        "|": {N},
        "-": {E},
        "L": {},
        "J": {E},
        "7": {N, E},
        "F": {N},
    },
    "J": {
        "S": {N, S, E, W},
        ".": {},
        "|": {N},
        "-": {W},
        "L": {W},
        "J": {},
        "7": {N},
        "F": {N, W},
    },
    "7": {
        "S": {N, S, E, W},
        ".": {},
        "|": {S},
        "-": {W},
        "L": {S, W},
        "J": {S},
        "7": {},
        "F": {W},
    },
    "F": {
        "S": {N, S, E, W},
        ".": {},
        "|": {S},
        "-": {E},
        "L": {S},
        "J": {S, E},
        "7": {E},
        "F": {},
    },
}


class Solution(BaseSolution[Input]):
    def parseInput(self):
        g = []
        start: Point = Point(0, 0)
        for y, line in enumerate(self.lines):
            g.append([])
            for x, c in enumerate(line):
                if c == "S":
                    start = Point(x, y)
                g[-1].append(c)

        return Input(g, start)

    # 6679 too low
    @answer(8, 6754)
    def part1(self):
        [print("".join(line)) for line in self.parsedInput[0]]
        print("start", self.parsedInput[1])
        (g, start) = self.parsedInput

        bound = Point(len(g[0]) - 1, len(g) - 1)
        path: set[Point] = set()
        pathInOrder: list[Point] = []
        curr = start
        done = False

        while not done:
            currSymbol = g[curr.y][curr.x]
            print("")
            print("-- curr", curr, currSymbol, len(path))

            path.add(curr)

            pathInOrder.append(curr)

            for direction in directions:
                neighborPos = curr + direction

                if not neighborPos.isInBound(bound):
                    continue

                if neighborPos in path:
                    if neighborPos == start and len(path) != 2:
                        done = True
                        path.add(curr)
                    continue

                neighbor = g[neighborPos.y][neighborPos.x]
                if direction in allowedMoves[currSymbol][neighbor]:
                    curr = neighborPos
                    break

        print(f"cells in path in order: {len(pathInOrder)}")
        [print(p) for p in pathInOrder]

        # Remove start position
        pathInOrder.pop(0)
        i = 0
        j = len(pathInOrder) - 1

        steps = 0
        while i <= j:
            steps += 1
            print(f"{steps} - i {i} j {j} pi {pathInOrder[i]} pj {pathInOrder[j]}")
            i += 1
            j -= 1

        return len(path) // 2

    # @answer(0, 0)
    # def part2(self):
    # return 1
