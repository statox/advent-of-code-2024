import math

from ...base import BaseSolution, answer
from .part1 import mapAValue, pairwise, parseInput


class Solution(BaseSolution):
    @answer(35, 323142486)
    def part1(self):
        (
            seeds,
            seed2soil,
            soil2fertilizer,
            fertilizer2water,
            water2light,
            light2temperature,
            temperature2humidity,
            humidity2location,
        ) = parseInput(self.lines)

        # print("------")
        # print("seeds", seeds)
        # print("seed2soil", seed2soil)
        # print("soil2fertilizer", soil2fertilizer)
        # print("fertilizer2water", fertilizer2water)
        # print("water2light", water2light)
        # print("light2temperature", light2temperature)
        # print("temperature2humidity", temperature2humidity)
        # print("humidity2location", humidity2location)

        minLocation = math.inf
        for seed in seeds:
            soil = mapAValue(seed, seed2soil)
            fertilizer = mapAValue(soil, soil2fertilizer)
            water = mapAValue(fertilizer, fertilizer2water)
            light = mapAValue(water, water2light)
            temp = mapAValue(light, light2temperature)
            humidity = mapAValue(temp, temperature2humidity)
            location = mapAValue(humidity, humidity2location)

            minLocation = min(minLocation, location)

            # print(
            #     f"Seed {seed}, soil {soil}, fertilizer {fertilizer}, water {water}, light {light}, temperature {temp}, humidity {humidity}, location {location}"
            # )

        return int(minLocation)

    @answer(46, 0)
    def part2(self):
        (
            seeds,
            seed2soil,
            soil2fertilizer,
            fertilizer2water,
            water2light,
            light2temperature,
            temperature2humidity,
            humidity2location,
        ) = parseInput(self.lines)

        minLocation = math.inf
        for i, (seedRangeStart, seedRangeLen) in enumerate(pairwise(seeds)):
            print(f"Range {i}/{int(len(seeds)/2)} - {seedRangeStart}-{seedRangeLen}")
            for seed in [
                seedRangeStart,
                seedRangeStart + math.floor(seedRangeLen / 2) - 2,
                seedRangeStart + math.floor(seedRangeLen / 2) - 1,
                seedRangeStart + math.floor(seedRangeLen / 2),
                seedRangeStart + math.floor(seedRangeLen / 2) + 1,
                seedRangeStart + math.floor(seedRangeLen / 2) + 2,
                seedRangeStart + seedRangeLen - 1,
                seedRangeStart + seedRangeLen,
            ]:
                soil = mapAValue(seed, seed2soil)
                fertilizer = mapAValue(soil, soil2fertilizer)
                water = mapAValue(fertilizer, fertilizer2water)
                light = mapAValue(water, water2light)
                temp = mapAValue(light, light2temperature)
                humidity = mapAValue(temp, temperature2humidity)
                location = mapAValue(humidity, humidity2location)

                minLocation = min(minLocation, location)

        # print(
        #     f"Seed {seed}, soil {soil}, fertilizer {fertilizer}, water {water}, light {light}, temperature {temp}, humidity {humidity}, location {location}"
        # )

        return int(minLocation)
