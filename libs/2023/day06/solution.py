import re
from functools import reduce
from operator import mul
from typing import NamedTuple

from ...base import BaseSolution, answer


class Race(NamedTuple):
    time: int
    distance: int


def countWinWays(race: Race):
    # There is probably a smarter way to go here, polynomial function crossing
    # a line and stuff but I'm lazy for now
    return len(
        [1 for hold in range(race.time) if (race.time - hold) * hold > race.distance]
    )


class Solution(BaseSolution):
    @answer(288, 512295)
    def part1(self):
        times = [
            int(v)
            for v in re.sub(r"\s+", ",", self.lines[0].split(":")[1]).split(",")
            if len(v)
        ]
        distances = [
            int(v)
            for v in re.sub(r"\s+", ",", self.lines[1].split(":")[1]).split(",")
            if len(v)
        ]
        races = [Race(v[0], v[1]) for v in zip(times, distances)]
        return reduce(mul, [countWinWays(race) for race in races], 1)

    @answer(71503, 36530883)
    def part2(self):
        time = int(re.sub(r"\s+", "", self.lines[0].split(":")[1]))
        distance = int(re.sub(r"\s+", "", self.lines[1].split(":")[1]))
        race = Race(time, distance)
        return countWinWays(race)
