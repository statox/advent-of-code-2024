import math
from typing import NamedTuple

from ...base import BaseSolution, answer
from ...utils.point import Point


class Robot:
    p: Point
    v: Point

    def __init__(self, p: Point, v: Point):
        self.p = p
        self.v = v

    def move(self, dimensions: Point):
        self.p += self.v

        if self.p.x > dimensions.x - 1:
            self.p.x = self.p.x % dimensions.x
        elif self.p.x < 0:
            self.p.x = dimensions.x + self.p.x

        if self.p.y > dimensions.y - 1:
            self.p.y = self.p.y % dimensions.y
        elif self.p.y < 0:
            self.p.y = dimensions.y + self.p.y

    def makeXMove(self, x: int, dimensions: Point):
        for _ in range(x):
            self.move(dimensions)


class Input(NamedTuple):
    robots: list[Robot]
    dimensions: Point


class Solution(BaseSolution[Input]):
    def parseInput(self):
        robots = []
        for line in self.lines:
            [left, right] = line.split(" ")
            pstr = left.split("=")[1]
            vstr = right.split("=")[1]

            [px, py] = [int(c) for c in pstr.split(",")]
            [vx, vy] = [int(c) for c in vstr.split(",")]
            robot = Robot(p=Point(px, py), v=Point(vx, vy))
            robots.append(robot)

        dimensions = Point(101, 103) if self.livemode else Point(11, 7)
        return Input(robots, dimensions)

    @answer(12, 217132650)
    def part1(self):
        (robots, dimensions) = self.parsedInput

        [r.makeXMove(100, dimensions) for r in robots]
        # [print(robot.p) for robot in robots]

        g = []
        for _ in range(dimensions.y):
            g.append([])
            for _ in range(dimensions.x):
                g[-1].append(0)

        for r in robots:
            g[r.p.y][r.p.x] += 1
        # [print("".join([v.__str__() if v != 0 else "." for v in line])) for line in g]

        NW = 0
        NE = 0
        SW = 0
        SE = 0

        for r in robots:
            if r.p.y < dimensions.y // 2:
                if r.p.x < dimensions.x // 2:
                    NW += 1
                elif r.p.x > dimensions.x // 2:
                    NE += 1
            elif r.p.y > dimensions.y // 2:
                if r.p.x < dimensions.x // 2:
                    SW += 1
                elif r.p.x > dimensions.x // 2:
                    SE += 1

        # print(f"NW {NW} NE {NE} SW {SW} SE {SE}")
        return NW * NE * SW * SE

    @answer(78, 6516)
    def part2(self):
        (robots, dimensions) = self.parsedInput

        seen: set[str] = set()
        step = 0
        done = False
        while not done:
            step += 1
            [r.makeXMove(1, dimensions) for r in robots]
            # print(f"step {step}")

            g = []
            for _ in range(dimensions.y):
                g.append([])
                for _ in range(dimensions.x):
                    g[-1].append(0)

            # done = True
            for r in robots:
                g[r.p.y][r.p.x] += 1
                # Another heuristic: The tree is found when no spot has 2 bots
                # if g[r.p.y][r.p.x] > 1:
                #     done = False

                # Dumb heuristic: The tree is found when at least 6 robots are aligned
                if (
                    r.p.x < dimensions.x - 6
                    and g[r.p.y][r.p.x] > 0
                    and g[r.p.y][r.p.x + 1] > 0
                    and g[r.p.y][r.p.x + 2] > 0
                    and g[r.p.y][r.p.x + 3] > 0
                    and g[r.p.y][r.p.x + 4] > 0
                    and g[r.p.y][r.p.x + 5] > 0
                ):
                    done = True

            boardStr = "\n".join(
                ["".join([v.__str__() if v != 0 else " " for v in line]) for line in g]
            )
            # print(boardStr)

            if boardStr in seen:
                done = True
            seen.add(boardStr)

        # print(
        #     "\n".join(
        #         ["".join([v.__str__() if v != 0 else " " for v in line]) for line in g]
        #     )
        # )
        return step
