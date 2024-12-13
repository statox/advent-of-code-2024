import re
from typing import NamedTuple

from ...base import BaseSolution, answer
from ...utils.point import Point


class Machine(NamedTuple):
    a: Point
    b: Point
    prize: Point


def solve_machine_dumb(a: Point, b: Point, prize: Point):
    maxA = min(prize.x // a.x, prize.y // a.y)
    maxB = min(prize.x // b.x, prize.y // b.y)

    # print(a, b, prize)
    # print(f"Will test with maxA {maxA} maxB {maxB}")

    for countA in range(maxA + 1):
        countB = maxB
        dest = a * countA + b * countB
        while dest.x > prize.x or dest.y > prize.y:
            countB -= 1
            dest = a * countA + b * countB

        if dest == prize:
            # print("============ Found", countA, countB, 3 * countA + countB)
            return 3 * countA + countB

    return None


def get_solution(a: Point, b: Point, prize: Point):
    (x1, y1) = (a.x, a.y)
    (x2, y2) = (b.x, b.y)
    (x, y) = (prize.x, prize.y)

    det = x1 * y2 - x2 * y1
    if det == 0:
        return (None, None)

    m = (y2 * x - x2 * y) / det
    if m != int(m):
        return (None, None)
    n = (-y1 * x + x1 * y) / det
    if n != int(n):
        return (None, None)

    return (int(m), int(n))


def solve_machine(a: Point, b: Point, prize: Point):
    countA, countB = get_solution(a, b, prize)
    if countA is None or countB is None:
        return 0

    return 3 * countA + countB


class Solution(BaseSolution[list[Machine]]):
    def parseInput(self):
        machines = []
        r = "([0-9]+)"
        for i in range(0, len(self.lines), 4):
            [ax, ay] = [int(v) for v in re.findall(r, self.lines[i])]
            [bx, by] = [int(v) for v in re.findall(r, self.lines[i + 1])]
            [px, py] = [int(v) for v in re.findall(r, self.lines[i + 2])]

            a = Point(ax, ay)
            b = Point(bx, by)
            prize = Point(px, py)
            machines.append(Machine(a, b, prize))

        return machines

    @answer(480, 29023)
    def part1(self):
        total = 0
        for machine in self.parsedInput:
            # print("Try", machine.a, machine.b, machine.prize)
            res = solve_machine(machine.a, machine.b, machine.prize)
            if res is not None:
                total += res

        return total

    @answer(875318608908, 96787395375634)
    def part2(self):
        total = 0
        for machine in self.parsedInput:
            # print("Try", machine.a, machine.b, machine.prize)
            s = solve_machine(
                machine.a,
                machine.b,
                machine.prize + Point(10000000000000, 10000000000000),
            )
            total += s

        return total
