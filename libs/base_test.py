import unittest

from .base import BaseSolution, InvalidSolutionError, answer


class DecoratedSolution(BaseSolution):
    @answer(1, 2)
    def part1(self):
        # part1 returns expected values in both livemode
        if self.livemode:
            return 2

        return 1

    @answer(1, 2)
    def part2(self):
        # part2 never returns expected value
        if self.livemode:
            return 4

        return 3


class UnknownSolution(BaseSolution):
    def part1(self):
        return 1


# tests


class Solution_Tests(unittest.TestCase):
    def test_decorated_valid(self):
        """Decorated solution returning the expected value should not throw"""
        DecoratedSolution([], False, 1).part1()
        DecoratedSolution([], True, 1).part1()

    def test_decorated_invalid(self):
        """Decorated solution returning unexpected value should throw"""
        # These calls should not raise an exception

        with self.assertRaises(InvalidSolutionError):
            DecoratedSolution([], False, 1).part2()

        with self.assertRaises(InvalidSolutionError):
            DecoratedSolution([], True, 1).part2()

    def test_undecorated_implemented(self):
        """Undecorated solution implemented method should never throw"""
        UnknownSolution([], False, 1).part1()
        UnknownSolution([], True, 1).part1()

    def test_undecorated_not_implemented(self):
        """Undecorated solution not implemented method should throw"""
        with self.assertRaises(NotImplementedError):
            UnknownSolution([], False, 1).part2()


if __name__ == "__main__":
    unittest.main(verbosity=2)
