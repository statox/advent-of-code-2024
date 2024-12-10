import math
from typing import Dict, NamedTuple


class DestinationRange(NamedTuple):
    destStart: int
    length: int
    deltaFromSource: int


AOCMapEntries = Dict[int, DestinationRange]
Memory = Dict[int, int]


class AOCMap(NamedTuple):
    memory: Memory
    map: AOCMapEntries


def parseInput(lines: list[str]):
    seeds = [int(v) for v in lines[0].split(":")[1].strip().split(" ") if len(v)]

    seed2soil: AOCMap = AOCMap(memory={}, map={})
    soil2fertilizer: AOCMap = AOCMap(memory={}, map={})
    fertilizer2water: AOCMap = AOCMap(memory={}, map={})
    water2light: AOCMap = AOCMap(memory={}, map={})
    light2temperature: AOCMap = AOCMap(memory={}, map={})
    temperature2humidity: AOCMap = AOCMap(memory={}, map={})
    humidity2location: AOCMap = AOCMap(memory={}, map={})

    currentMap: AOCMap = seed2soil
    for line in lines[2:]:
        if len(line) == 0:
            continue

        if line == "seed-to-soil map:":
            currentMap = seed2soil
        elif line == "soil-to-fertilizer map:":
            currentMap = soil2fertilizer
        elif line == "fertilizer-to-water map:":
            currentMap = fertilizer2water
        elif line == "water-to-light map:":
            currentMap = water2light
        elif line == "light-to-temperature map:":
            currentMap = light2temperature
        elif line == "temperature-to-humidity map:":
            currentMap = temperature2humidity
        elif line == "humidity-to-location map:":
            currentMap = humidity2location
        else:
            [destStart, sourceStart, length] = [
                int(v) for v in line.split(" ") if len(v)
            ]
            currentMap.map[sourceStart] = DestinationRange(
                destStart, length, deltaFromSource=destStart - sourceStart
            )

    return (
        seeds,
        seed2soil,
        soil2fertilizer,
        fertilizer2water,
        water2light,
        light2temperature,
        temperature2humidity,
        humidity2location,
    )


def mapAValue(v: int, m: AOCMap):
    if m.memory.get(v) is not None:
        m.memory.get(v)

    for sourceStart in m.map:
        (destStart, length, deltaFromSource) = m.map[sourceStart]
        if v >= sourceStart and v <= sourceStart + length:
            res = v + deltaFromSource
            m.memory[v] = res
            return res

    return v


def _part1(lines: list[str]):
    (
        seeds,
        seed2soil,
        soil2fertilizer,
        fertilizer2water,
        water2light,
        light2temperature,
        temperature2humidity,
        humidity2location,
    ) = parseInput(lines)

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
