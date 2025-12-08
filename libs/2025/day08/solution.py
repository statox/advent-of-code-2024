from typing import NamedTuple, override

from ...base import BaseSolution, answer

Point = tuple[int, int, int]


class ParsedInput(NamedTuple):
    # The distance between each boxes is unique, we store each pair of box
    # indexed by the distance between them
    pairs_by_distance: dict[int, tuple[Point, Point]] = {}
    # This is the list of distances between pairs in increasing order
    sorted_distances: list[int] = []
    # All the circuits, in the initial state their is one circuit by box
    circuits: dict[int, set[Point]] = {}
    # For each box keep track of which circuit it belongs to
    circuits_by_box: dict[Point, int] = {}


class Solution(BaseSolution[ParsedInput]):
    @override
    def parseInput(self):
        boxes = [Point(map(int, line.split(","))) for line in self.lines]

        pairs_by_distance: dict[int, tuple[Point, Point]] = {}
        seen = set()
        for box_1 in boxes:
            for box_2 in boxes:
                if box_1 == box_2:
                    continue
                s = (box_1, box_2) if self.isSmaller(box_1, box_2) else (box_2, box_1)
                if s in seen:
                    continue

                seen.add(s)
                distance_sq = self.dSquared(box_1, box_2)

                if distance_sq in pairs_by_distance:
                    # The problem doesn't explicitely say it should not happen but
                    # it's the case in both the example and my input so it's convenient
                    print("Same distance found for 2 different pairs", distance_sq)
                    assert False

                pairs_by_distance[distance_sq] = (box_1, box_2)

        sorted_distances: list[int] = sorted(pairs_by_distance.keys())

        circuits: dict[int, set[Point]] = {}
        circuits_by_box: dict[Point, int] = {}

        for i, box in enumerate(boxes):
            circuits[i] = {box}
            circuits_by_box[box] = i

        return ParsedInput(pairs_by_distance, sorted_distances, circuits, circuits_by_box)

    def dSquared(self, a: Point, b: Point):
        return (a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1]) + (a[2] - b[2]) * (a[2] - b[2])

    def isSmaller(self, a: Point, b: Point):
        if a[0] != b[0]:
            return a[0] < b[0]

        if a[1] != b[1]:
            return a[1] < b[1]

        return a[2] < b[2]

    def dToOriginSquared(self, a: Point):
        return (a[0]) * (a[0]) + (a[1]) * (a[1]) + (a[2]) * (a[2])

    @answer(40, 47040)
    @override
    def part1(self):
        (pairs_by_distance, sorted_distances, circuits, circuits_by_box) = self.parsedInput
        connections_to_do = 1000 if self.livemode else 10

        for d in sorted_distances[:connections_to_do]:
            (box_1, box_2) = pairs_by_distance[d]
            circuit_1 = circuits_by_box.get(box_1)
            circuit_2 = circuits_by_box.get(box_2)

            assert circuit_1 is not None and circuit_2 is not None

            if circuit_1 == circuit_2:
                continue

            for box in circuits[circuit_2]:
                circuits_by_box[box] = circuit_1
            circuits[circuit_1] = circuits[circuit_1].union(circuits[circuit_2])
            del circuits[circuit_2]

        total = 1
        for circuit in sorted(circuits.keys(), key=lambda k: len(circuits[k]), reverse=True)[:3]:
            total *= len(circuits[circuit])

        return total

    @answer(25272, 4884971896)
    @override
    def part2(self):
        (pairs_by_distance, sorted_distances, circuits, circuits_by_box) = self.parsedInput

        for d in sorted_distances:
            (box_1, box_2) = pairs_by_distance[d]
            circuit_1 = circuits_by_box.get(box_1)
            circuit_2 = circuits_by_box.get(box_2)

            assert circuit_1 is not None and circuit_2 is not None

            if circuit_1 == circuit_2:
                continue

            for box in circuits[circuit_2]:
                circuits_by_box[box] = circuit_1
            circuits[circuit_1] = circuits[circuit_1].union(circuits[circuit_2])
            del circuits[circuit_2]

            if len(circuits) == 1:
                return box_1[0] * box_2[0]

        return -1
