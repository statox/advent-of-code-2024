import re

from ...base import BaseSolution, answer

rep = [
    ("twenty", "0"),
    ("nineteen", "9"),
    ("eighteen", "8"),
    ("seventeen", "7"),
    ("sixteen", "6"),
    ("fifteen", "5"),
    ("fourteen", "4"),
    ("thirteen", "3"),
    ("twelve", "2"),
    ("eleven", "1"),
    ("ten", "0"),
    ("nine", "9"),
    ("eight", "8"),
    ("seven", "7"),
    ("six", "6"),
    ("five", "5"),
    ("four", "4"),
    ("three", "3"),
    ("two", "2"),
    ("one", "1"),
]


class Solution(BaseSolution):
    @answer(142, 55386)
    def part1(self):
        total = 0
        for line in self.lines:
            capture = re.findall("[0-9]", line)
            first = capture[0]
            last = capture[-1]
            value = int(first + last)
            total += value

        return total

    @answer(281, 54824)
    def part2(self):
        total = 0
        for line in self.lines:
            chunks = []
            for i, c in enumerate(line):
                if c.isdigit():
                    chunks.append(str(c))
                    continue

                for letters, digits in rep:
                    if line[i:].startswith(letters):
                        chunks.append(digits)
                        break

            first = chunks[0]
            last = chunks[-1]
            value = int(first + last)
            total += value

        return total
