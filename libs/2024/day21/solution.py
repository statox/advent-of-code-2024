from collections import deque
from functools import cache
from math import inf
from typing import Literal, TypeAlias

from ...base import BaseSolution, answer

# <vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
# v<<A>>^A<A>AvA<^AA>A<vAAA>^A
# <A^A>^^AvvvA
# 029A


Graph: TypeAlias = dict[str, dict[str, str]]

#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+
transitions_arrows: Graph = {
    "^": {">": "A", "v": "v"},
    "A": {"v": ">", "<": "^"},
    "<": {">": "v"},
    "v": {"^": "^", ">": ">", "<": "<"},
    ">": {"^": "A", "<": "v"},
}

# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+
transitions_digits: Graph = {
    "A": {"^": "3", "<": "0"},
    "0": {"^": "2", ">": "A"},
    "1": {"^": "4", ">": "2"},
    "2": {"^": "5", ">": "3", "v": "0", "<": "1"},
    "3": {"^": "6", "v": "A", "<": "2"},
    "4": {"^": "7", ">": "5", "v": "1"},
    "5": {"^": "8", ">": "6", "v": "2", "<": "4"},
    "6": {"^": "9", "v": "3", "<": "5"},
    "7": {">": "8", "v": "4"},
    "8": {">": "9", "v": "5", "<": "7"},
    "9": {"v": "6", "<": "8"},
}

TransitionType = Literal["digits", "arrows"]


@cache
def get_possible_ways(t: TransitionType, searched: str):
    g = transitions_digits if t == "digits" else transitions_arrows

    searched_len = len(searched)
    shortest_path_len: None | int = None

    s = deque([("A", 0, "", [])])

    possibles = []
    while s:
        (curr_key, searched_index, curr_path, curr_chunk) = s.popleft()

        if shortest_path_len and len(curr_path) > shortest_path_len:
            continue

        if curr_key in curr_chunk:
            continue

        if searched_index == searched_len:
            possibles.append((curr_key, searched_index, curr_path))
            shortest_path_len = len(curr_path)
            continue

        if curr_key == searched[searched_index]:
            s.append((curr_key, searched_index + 1, curr_path + "A", []))
            continue

        for n in g[curr_key]:
            n_key = g[curr_key][n]
            # print("   -> ", n_key)
            s.append(
                (
                    n_key,
                    searched_index,
                    curr_path + n,
                    curr_chunk + [curr_key],
                )
            )

    return [p[2] for p in possibles]


@cache
def get_shortest_way(t: TransitionType, searched: str):
    g = transitions_digits if t == "digits" else transitions_arrows

    searched_len = len(searched)

    s = deque([("A", 0, "", set())])

    while s:
        (curr_key, searched_index, curr_path, curr_chunk) = s.popleft()

        if curr_key in curr_chunk:
            continue

        if curr_key == searched[searched_index]:
            if searched_index + 1 == searched_len:
                return curr_path + "A"

            s.append((curr_key, searched_index + 1, curr_path + "A", set()))
            continue

        for n in g[curr_key]:
            n_key = g[curr_key][n]
            curr_chunk.add(curr_key)
            s.append((n_key, searched_index, curr_path + n, curr_chunk))

    return ""


class Solution(BaseSolution):
    def parseInput(self):
        pass

    @answer(126384, None)
    def part1(self):
        total = 0
        for searched in self.lines:
            code_numerical_value = int(searched[:-1])
            code_ways = get_possible_ways("digits", searched)
            print(f"===== L1 done for {searched} ({code_numerical_value})")
            [print(way) for way in code_ways]

            shortest_l2 = inf
            searched_score = 0
            for j, searched1 in enumerate(code_ways):
                robot1_ways = get_possible_ways("arrows", searched1)
                print(f"  ===== L2 done for ({j}/{len(code_ways)}) {searched1}")
                [print("  ", way) for way in robot1_ways]

                for i, searched2 in enumerate(robot1_ways):
                    robot2_way = get_shortest_way("arrows", searched2)
                    robot2_way_len = len(robot2_way)
                    print(f"    ===== L3 done for ({i}/{len(robot1_ways)}) {searched2}")
                    print("    ", robot2_way)

                    if robot2_way_len < shortest_l2:
                        shortest_l2 = robot2_way_len
                        best = shortest_l2
                        searched_score = code_numerical_value * robot2_way_len
                        print(
                            f"New best {best} for {searched} - score: {searched_score}"
                        )
                    else:
                        print(f"score for {searched} is still: {searched_score}")
            total += searched_score

        return total

    def test(self):
        total = 0
        for searched in self.lines:
            code_numerical_value = int(searched[:-1])
            code_ways = get_possible_ways("digits", searched)
            print(f"===== L1 done for {searched} ({code_numerical_value})")
            [print(way) for way in code_ways]

            shortest_l2 = inf
            searched_score = 0
            for searched1 in code_ways:
                robot1_way = get_shortest_way("arrows", searched1)

                robot2_way = get_shortest_way("arrows", robot1_way)
                robot2_way_len = len(robot2_way)

                if robot2_way_len < shortest_l2:
                    shortest_l2 = robot2_way_len
                    best = shortest_l2
                    searched_score = code_numerical_value * robot2_way_len
                    print(f"New best {best} - score: {searched_score}")
                else:
                    print(f"score is still: {searched_score}")
            total += searched_score

        return total

    # @answer(None, None)
    # def part2(self):
    # return 1
