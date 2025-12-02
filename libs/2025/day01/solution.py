from ...base import BaseSolution, answer


class Solution(BaseSolution):
    @answer(3, 1147)
    def part1(self):
        total = 0
        pos = 50

        for line in self.lines:
            direction = line[0]
            rot = int(line[1:])

            if direction == "R":
                pos = (pos + rot) % 100
            else:
                pos -= rot
                while pos < 0:
                    pos += 100

            if pos == 0:
                total += 1

        return total

    @answer(6, 6789)
    def part2(self):
        total = 0
        pos = 50

        for line in self.lines:
            direction = line[0]
            rot = int(line[1:])

            if direction == "R":
                while rot > 0:
                    pos += 1
                    rot -= 1
                    if pos == 100:
                        pos = 0
                        total += 1
            else:
                while rot > 0:
                    pos -= 1
                    rot -= 1
                    if pos == 0:
                        total += 1
                    if pos == -1:
                        pos = 99

        return total
