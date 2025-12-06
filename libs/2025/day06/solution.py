import re
from functools import reduce
from operator import mul
from pathlib import Path
from typing import NamedTuple, override

from ...base import BaseSolution, answer


class ParsedInput(NamedTuple):
    vals: list[list[int]]
    ops: list[str]


class Solution(BaseSolution):
    @override
    def parseInput(self):
        vals = []
        for line in self.lines[:-1]:
            r = [int(s) for s in re.sub(r" +", " ", line).split(" ")]
            vals.append(r)

        ops = re.sub(r" +", " ", self.lines[-1]).split(" ")

        return ParsedInput(vals, ops)

    @answer(4277556, 4648618073226)
    @override
    def part1(self):
        (vals, ops) = self.parsedInput
        total = 0
        for i in range(len(ops)):
            op = ops[i]
            vs = [vals[j][i] for j in range(len(vals))]

            sub = sum(vs) if op == "+" else reduce(mul, vs, 1)
            total += sub
        return total

    @answer(3263827, 7329921182115)
    @override
    def part2(self):
        (_, ops) = self.parsedInput
        total = 0

        # I was too lazy to do the string manipuation in python so I copied the
        # input files,
        # Used the following vim macro to transform the input lines into groups
        #   gg$^VjjjjhdG<leader>opVGJ0
        #
        #   gg$                           Go to the last character of the first line
        #      ^V                         Start visual block mode
        #        jjjj                     Select a colum of 4 characters
        #            h                    Avoid selecting the empty last char of the line
        #             d                   Delete the selection
        #              G                  Go to the last line
        #               <leader>o         (Custom mapping equivalent to o<esc>) create a new line
        #                                 and get back to normal mode
        #                        p        Past the block
        #                         VG      Select the block
        #                           J     Join it
        #                            0    Back to first char of the line, ready to re-run the mapping
        # And then its easy to get get all the lines and create groups on blank
        # lines. Not my proudest AOC but it works

        file = "input1" if self.livemode else "input_test_1"
        with Path.open(Path(self.getOwnPath(), file), "r") as file:
            lines = [line.strip() for line in file]
            groups = [[]]
            for line in lines:
                if line == "":
                    groups.append([])
                else:
                    groups[-1].append(int(line))

            for i in range(len(ops)):
                op = ops[len(ops) - i - 1]
                vs = groups[i]
                sub = sum(vs) if op == "+" else reduce(mul, vs, 1)
                total += sub

        return total
