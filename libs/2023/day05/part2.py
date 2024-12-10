from typing import NamedTuple


class Mapping(NamedTuple):
    sourceStart: int
    sourceEnd: int
    destStart: int
    destEnd: int
    size: int
    deltaFromSource: int


AOCMap = list[Mapping]


def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)


def parseInput(lines: list[str]):
    seeds = pairwise(
        [int(v) for v in lines[0].split(":")[1].strip().split(" ") if len(v)]
    )

    seed2soil: AOCMap = []
    soil2fertilizer: AOCMap = []
    fertilizer2water: AOCMap = []
    water2light: AOCMap = []
    light2temperature: AOCMap = []
    temperature2humidity: AOCMap = []
    humidity2location: AOCMap = []

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
            [destStart, sourceStart, size] = [int(v) for v in line.split(" ") if len(v)]

            currentMap.append(
                Mapping(
                    sourceStart=sourceStart,
                    sourceEnd=sourceStart + size,
                    destStart=destStart,
                    destEnd=destStart + size,
                    size=size,
                    deltaFromSource=destStart - sourceStart,
                )
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


def isSourceContinuous(m: AOCMap):
    s = sorted(m, key=lambda r: r.destStart)
    for i in range(len(m) - 2):
        a = s[i]
        b = s[i + 1]

        if a.destEnd != b.destStart:
            return False

    return True


def _part2(lines: list[str]):
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

    [print(v) for v in seeds]
    print("seed2soil")
    print(f"source continuous {isSourceContinuous(seed2soil)}")
    [print(r) for r in sorted(seed2soil, key=lambda r: r.destStart)]
    print("soil2fertilizer")
    print(f"source continuous {isSourceContinuous(soil2fertilizer)}")
    [print(r) for r in sorted(soil2fertilizer, key=lambda r: r.destStart)]
    print("fertilizer2water")
    print(f"source continuous {isSourceContinuous(fertilizer2water)}")
    [print(r) for r in sorted(fertilizer2water, key=lambda r: r.destStart)]
    print("water2light")
    print(f"source continuous {isSourceContinuous(water2light)}")
    [print(r) for r in sorted(water2light, key=lambda r: r.destStart)]
    print("light2temperature")
    print(f"source continuous {isSourceContinuous(light2temperature)}")
    [print(r) for r in sorted(light2temperature, key=lambda r: r.destStart)]
    print("temperature2humidity")
    print(f"source continuous {isSourceContinuous(temperature2humidity)}")
    [print(r) for r in sorted(temperature2humidity, key=lambda r: r.destStart)]
    print("humidity2location")
    print(f"source continuous {isSourceContinuous(humidity2location)}")
    [print(r) for r in sorted(humidity2location, key=lambda r: r.destStart)]

    return 0
