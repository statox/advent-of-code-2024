import re
from ..base import BaseSolution


def evaluatePart(part: str):
    matches = re.findall('mul\(\d{1,3},\d{1,3}\)', part)
    members = [re.findall('\d{1,3}', m) for m in matches]
    prods = [int(m[0])*int(m[1]) for m in members]

    return sum(prods)


class Solution(BaseSolution):
    def part1(self):
        line = self.lines[0]

        # livemode false: 161
        # livemode true: 173731097
        return evaluatePart(line)

    def part2(self):
        line = self.lines[0]

        dodontre = r"do\(\)|don\'t\(\)"
        delims = ['do()'] + re.findall(dodontre, line)
        parts = re.split(dodontre, line)
        zipped = zip(delims, parts)

        r = sum([evaluatePart(part) if op == 'do()' else 0 for (op, part) in zipped])

        # livemode false: 48
        # livemode true: 93729253
        return r
