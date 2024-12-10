from ...base import BaseSolution, answer
from .part1 import _part1
from .part2 import _part2


class Solution(BaseSolution):
    @answer(35, 323142486)
    def part1(self):
        return _part1(self.lines)

    # @answer(46, 0)
    def part2(self):
        return _part2(self.lines)
