import re

from ...base import BaseSolution, answer


def evaluatePart(part: str):
    matches = re.findall("mul\(\d{1,3},\d{1,3}\)", part)
    members = [re.findall("\d{1,3}", m) for m in matches]
    prods = [int(m[0]) * int(m[1]) for m in members]

    return sum(prods)


class Solution(BaseSolution):
    @answer(161, 173731097)
    def part1(self):
        line = self.lines[0]

        return evaluatePart(line)

    @answer(48, 93729253)
    def part2(self):
        line = self.lines[0]

        dodontre = r"do\(\)|don\'t\(\)"
        delims = ["do()"] + re.findall(dodontre, line)
        parts = re.split(dodontre, line)
        zipped = zip(delims, parts)

        return sum([evaluatePart(part) if op == "do()" else 0 for (op, part) in zipped])

        # Dumb one liner version
        #
        # return sum([
        #     sum(
        #     [
        #         int(a)*int(b) for (a, b) in
        #         [re.findall('\d{1,3}', match) for match in re.findall('mul\(\d{1,3},\d{1,3}\)', part)]
        #     ])
        #     if op == 'do()' else 0
        #     for (op, part) in zip(
        #         ['do()'] + re.findall(r"do\(\)|don\'t\(\)", line),
        #         re.split(r"do\(\)|don\'t\(\)", line)
        #     )
        # ])
