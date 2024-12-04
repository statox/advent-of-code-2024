from ..base import BaseSolution, answer


class Solution(BaseSolution):
    @answer(18, 2483)
    def part1(self):
        l = self.lines
        H = len(l)
        W = len(l[0])
        total = 0
        for y in range(H):
            for x in range(W):
                if l[y][x] != "X":
                    continue

                if x < W - 3:
                    if y > 2 and "".join([l[y - i][x + i] for i in range(4)]) == "XMAS":
                        total += 1

                    if l[y][x : x + 4] == "XMAS":
                        total += 1

                    if (
                        y < H - 3
                        and "".join([l[y + i][x + i] for i in range(4)]) == "XMAS"
                    ):
                        total += 1

                if y > 2 and "".join([l[y - i][x] for i in range(4)]) == "XMAS":
                    total += 1

                if y < H - 3 and "".join([l[y + i][x] for i in range(4)]) == "XMAS":
                    total += 1

                if x > 2:
                    if y > 2 and "".join([l[y - i][x - i] for i in range(4)]) == "XMAS":
                        total += 1

                    if l[y][x - 3 : x + 1] == "SAMX":
                        total += 1

                    if (
                        y < H - 3
                        and "".join([l[y + i][x - i] for i in range(4)]) == "XMAS"
                    ):
                        total += 1

        return total

    @answer(9, 1925)
    def part2(self):
        l = self.lines
        H = len(l)
        W = len(l[0])
        total = 0
        s = ("MAS", "SAM")

        for y in range(1, H - 1):
            for x in range(1, W - 1):
                if l[y][x] != "A":
                    continue

                d1 = l[y - 1][x - 1] + l[y][x] + l[y + 1][x + 1]
                d2 = l[y + 1][x - 1] + l[y][x] + l[y - 1][x + 1]

                if d1 in s and d2 in s:
                    total += 1

        return total
