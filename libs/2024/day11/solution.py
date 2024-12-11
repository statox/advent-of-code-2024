import functools

from ...base import BaseSolution, answer


class Solution(BaseSolution[list[int]]):
    def doWork(self, stones: list[int], steps: int):
        @functools.cache
        def countChildren(stone: int, stepsLeft: int):
            if stepsLeft == 0:
                return 1

            if stone == 0:
                return countChildren(1, stepsLeft - 1)

            stone_str = str(stone)
            stone_str_len = len(str(stone))

            if stone_str_len % 2 == 0:
                left, right = (
                    int(stone_str[: stone_str_len // 2]),
                    int(stone_str[stone_str_len // 2 :]),
                )
                return countChildren(left, stepsLeft - 1) + countChildren(
                    right, stepsLeft - 1
                )

            return countChildren(stone * 2024, stepsLeft - 1)

        return sum([countChildren(stone, steps) for stone in stones])

    def parseInput(self):
        return [int(v) for v in self.lines[0].split(" ")]

    @answer(55312, 175006)
    def part1(self):
        return self.doWork(self.parsedInput, 25)

    @answer(65601038650482, 207961583799296)
    def part2(self):
        return self.doWork(self.parsedInput, 75)
