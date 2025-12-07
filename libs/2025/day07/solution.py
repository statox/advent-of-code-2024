from collections import defaultdict
from typing import override

from ...base import BaseSolution, answer


class Solution(BaseSolution[list[list[str]]]):
    @override
    def parseInput(self):
        return [list(line) for line in self.lines]

    @answer(21, 1717)
    @override
    def part1(self):
        g = self.parsedInput
        x_start = g[0].index("S")
        beams = {x_start}
        hit = set()

        for y in range(len(g) - 2):
            next_beams = set()
            for x in beams:
                if g[y + 1][x] == "^":
                    hit.add((x, y))
                    next_beams.add(x - 1)
                    next_beams.add(x + 1)
                else:
                    next_beams.add(x)
            beams = next_beams

        return len(hit)

    @answer(40, 231507396180012)
    @override
    def part2(self):
        g = self.parsedInput
        x_start = g[0].index("S")
        beams = {x_start: 1}

        for y in range(len(g) - 2):
            next_beams = defaultdict(int)

            for x, hits in beams.items():
                if g[y + 1][x] == "^":
                    next_beams[x - 1] += hits
                    next_beams[x + 1] += hits
                else:
                    next_beams[x] += hits

            beams = next_beams

        return sum([beams[x] for x in beams])
