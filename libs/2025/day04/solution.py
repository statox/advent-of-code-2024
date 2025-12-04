from typing import NamedTuple, override

from ...base import BaseSolution, answer


class ParsedInput(NamedTuple):
    g: list[list[str]]
    W: int
    H: int


class Solution(BaseSolution[ParsedInput]):
    @override
    def parseInput(self):
        g = [list(line) for line in self.lines]
        H = len(g)
        W = len(g[0])

        return ParsedInput(g, W, H)

    def getAccessibleRolls(self, g: list[list[str]], W: int, H: int):
        accessible: list[tuple[int, int]] = []

        # Only keep the coordinates of the roll cells (marked with '@')
        rolls_coords = ((x, y) for y in range(H) for x in range(W) if g[y][x] == "@")

        # Only keep the coordinates of the neighbors which are in the grid
        for x, y in rolls_coords:
            n_coords = (
                (xn, yn)
                for (xn, yn) in [
                    (x - 1, y - 1),
                    (x, y - 1),
                    (x + 1, y - 1),
                    (x - 1, y),
                    (x + 1, y),
                    (x - 1, y + 1),
                    (x, y + 1),
                    (x + 1, y + 1),
                ]
                if xn >= 0 and xn <= W - 1 and yn >= 0 and yn <= H - 1
            )

            # Count the neighbors with a roll in it
            neighborsRolls = sum([g[y][x] == "@" for (x, y) in n_coords])

            # We can access the rolls which have less than 4 rolls around them
            if neighborsRolls < 4:
                accessible.append((x, y))

        return accessible

    @answer(13, 1445)
    @override
    def part1(self):
        (g, W, H) = self.parsedInput
        return len(self.getAccessibleRolls(g, W, H))

    @answer(43, 8317)
    @override
    def part2(self):
        (g, W, H) = self.parsedInput

        removables: list[tuple[int, int]] = []
        total = 0

        while total == 0 or len(removables) > 0:
            removables = self.getAccessibleRolls(g, W, H)
            total += len(removables)

            for x, y in removables:
                g[y][x] = "."

        return total
