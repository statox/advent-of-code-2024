from collections import deque
from itertools import combinations
from typing import NamedTuple, Optional

from ...base import BaseSolution, answer


class Input(NamedTuple):
    g: list[list[str]]
    start: complex
    end: complex


N = 0 - 1j
S = 0 + 1j
E = 1 + 0j
W = -1 + 0j
directions = [N, E, S, W]


def getCell(g: list[list[str]], p: complex, bound: Optional[complex] = None):
    if bound is None:
        bound = len(g[0]) + len(g) * 1j

    if p.imag < 0 or p.real < 0 or p.imag >= bound.imag or p.real >= bound.real:
        return "!"
    return g[int(p.imag)][int(p.real)]


class Solution(BaseSolution[Input]):
    def parseInput(self):
        start: complex = -1
        end: complex = -1

        g = []
        for y, line in enumerate(self.lines):
            g.append([])
            for x, c in enumerate(line):
                if c == "S":
                    start = x + y * 1j
                    g[-1].append(".")
                elif c == "E":
                    end = x + y * 1j
                    g[-1].append(".")
                else:
                    g[-1].append(c)

        return Input(g, start, end)

    def get_distances_from_end_dict(self):
        (g, start, end) = self.parsedInput
        path: dict[complex, int] = {end: 0}
        current = end

        step = 0
        while current != start:
            step += 1
            for direction in [N, S, E, W]:
                n = current + direction
                if n not in path and getCell(g, n) != "#":
                    current = n
                    path[current] = step
                    break

        return path

    def get_distances_from_start_dict(self):
        (g, start, end) = self.parsedInput
        path: dict[complex, int] = {start: 0}
        current = start

        step = 0
        while current != end:
            step += 1
            for direction in [N, S, E, W]:
                n = current + direction
                if n not in path and getCell(g, n) != "#":
                    current = n
                    path[current] = step
                    break

        return path

    def get_distances_from_start(self):
        (g, start, end) = self.parsedInput
        path: list[tuple[complex, int]] = [(start, 0)]
        seen: set[complex] = {start}

        current = start

        step = 0
        while current != end:
            step += 1
            for direction in [N, S, E, W]:
                n = current + direction
                if n not in seen and getCell(g, n) != "#":
                    current = n
                    path.append((current, step))
                    seen.add(current)
                    break

        return path

    @answer(5, 1448)
    def part1(self):
        (g, _, _) = self.parsedInput

        distances_from_end = self.get_distances_from_end_dict()

        min_gain_target = 100 if self.livemode else 20
        max_steps = 2

        total = 0
        for a in distances_from_end:
            s = [(a, 0)]

            while s:
                (dest, steps) = s.pop()

                if steps == max_steps:
                    distance_diff = distances_from_end[a] - distances_from_end[dest]
                    cheat_length = steps
                    score = distance_diff - cheat_length

                    if score >= min_gain_target:
                        total += 1

                    continue

                looking_for = "#" if steps < max_steps - 1 else "."
                s.extend(
                    [
                        (n, steps + 1)
                        for n in [dest + direction for direction in directions]
                        if getCell(g, n) == looking_for
                    ]
                )

        return total

    @answer(285, 1017615)
    def test(self):
        distances_from_start = self.get_distances_from_start()
        search_radius = 20
        min_gain_target = 100 if self.livemode else 50
        total = 0

        for (a, a_from_start), (b, b_from_start) in combinations(
            distances_from_start, 2
        ):
            diff = b - a
            distance_ab = abs(diff.real) + abs(diff.imag)

            if distance_ab > search_radius:
                continue

            gain = b_from_start - a_from_start - distance_ab
            if gain >= min_gain_target:
                total += 1

        return total

    @answer(285, 1017615)
    def part2(self):
        (g, _, _) = self.parsedInput

        bound = len(g[0]) + len(g) * 1j
        distances_from_start = self.get_distances_from_start_dict()

        search_radius = 20
        min_gain_target = 100 if self.livemode else 50

        total = 0

        for a in distances_from_start:
            a_from_start = distances_from_start[a]

            for y in range(
                int(a.imag) - search_radius, 1 + int(a.imag) + search_radius
            ):
                for x in range(
                    int(a.real) - search_radius, 1 + int(a.real) + search_radius
                ):
                    if y < 0 or x < 0 or y >= bound.imag or x >= bound.real:
                        continue

                    if g[y][x] == "#":
                        continue

                    b = x + y * 1j
                    diff = b - a
                    # Minor performence gain by doing abs() "manually"
                    # distance_ab = abs(diff.real) + abs(diff.imag)
                    distance_ab = (diff.real if diff.real > 0 else -diff.real) + (
                        diff.imag if diff.imag > 0 else -diff.imag
                    )

                    if distance_ab > search_radius:
                        continue

                    b_from_start = distances_from_start[b]

                    gain = b_from_start - a_from_start - distance_ab
                    if gain >= min_gain_target:
                        total += 1

        return total
