from ..base import BaseSolution, answer


class Solution(BaseSolution):
    @answer(11, 2769675)
    def part1(self):
        left = []
        right = []

        for line in self.lines:
            a, b = [int(n) for n in line.split()]
            left.append(a)
            right.append(b)

        left = sorted(left)
        right = sorted(right)

        total = 0
        for i in range(len(left)):
            diff = abs(left[i] - right[i])
            # print(left[i], right[i], diff)
            total += diff

        return total

    @answer(31, 24643097)
    def part2(self):
        left = []
        rightCount = {}

        for line in self.lines:
            a, b = [int(n) for n in line.split()]
            left.append(a)
            rightCount[b] = rightCount.get(b, 0) + 1

        total = 0
        for a in left:
            score = a * rightCount.get(a, 0)
            # print(a, score)
            total += score

        return total
