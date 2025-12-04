from collections import deque
from typing import NamedTuple

from ...base import BaseSolution, answer


class Input(NamedTuple):
    positions: list[complex]
    bound: complex


N = 0 - 1j
S = 0 + 1j
E = 1 + 0j
W = -1 + 0j


def find_path_BFS(g: list[list[str]], start: complex, end: complex, bound: complex):
    s = deque([(start, 0)])
    seen: set[complex] = set()

    while s:
        (pos, steps) = s.popleft()

        if pos in seen:
            continue
        seen.add(pos)

        if pos == end:
            return steps

        for direction in [E, S, W, N]:
            n = pos + direction

            if n.imag < 0 or n.real < 0 or n.imag > bound.imag or n.real > bound.real:
                continue

            if g[int(n.imag)][int(n.real)] != ".":
                continue

            if n in seen:
                continue

            s.append((n, steps + 1))

    return None


class Solution(BaseSolution[Input]):
    def parseInput(self):
        positions = [
            int(x) + int(y) * 1j for x, y in [line.split(",") for line in self.lines]
        ]
        bound = 70 + 70j if self.livemode else 6 + 6j

        return Input(positions, bound)

    @answer(22, 432)
    def part1(self):
        (positions, bound) = self.parsedInput
        nbFalls = 1024 if self.livemode else 12

        g = [
            ["." for _ in range(int(bound.real) + 1)]
            for _ in range(int(bound.imag) + 1)
        ]

        for bytePos in positions[:nbFalls]:
            g[int(bytePos.imag)][int(bytePos.real)] = "#"

        nbSteps = find_path_BFS(g, 0 + 0j, bound, bound)
        return nbSteps if nbSteps else -1

    @answer("6,1", "56,27")
    def part2(self):
        (positions, bound) = self.parsedInput

        g = [
            ["." for _ in range(int(bound.real) + 1)]
            for _ in range(int(bound.imag) + 1)
        ]

        for bytePos in positions:
            g[int(bytePos.imag)][int(bytePos.real)] = "#"

        for bytePos in positions[::-1]:
            g[int(bytePos.imag)][int(bytePos.real)] = "."

            # print(f"Removing {bytePos}")
            # [print("".join(line)) for line in g]

            nbSteps = find_path_BFS(g, 0 + 0j, bound, bound)

            if nbSteps is not None:
                # print(f"First to break is {bytePos}")
                return f"{int(bytePos.real)},{int(bytePos.imag)}"

        raise Exception("Could not complete work")
