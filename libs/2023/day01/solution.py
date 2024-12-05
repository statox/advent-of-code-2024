from ...base import BaseSolution, answer


class Solution(BaseSolution):
    @answer(2, 1)
    def part1(self):
        print("2023 day 1")
        return len(self.lines)
