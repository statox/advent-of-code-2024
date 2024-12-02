from ..base import BaseSolution


class Solution(BaseSolution):
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

        # livemode false: 11
        # livemode true: 2769675
        return total

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

        # livemode false: 31
        # livemode true: 24643097
        return total
