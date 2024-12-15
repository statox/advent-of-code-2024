import unittest

from ..base import BaseSolution, SolutionOptions, InvalidSolutionError, answer


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


class FileSolution(BaseSolution):
    @answer(4, 3)
    def part1(self):
        return len(self.lines)

    @answer(0, 1)
    def part2(self):
        return len(self.lines)


class ParsingInputSolution(BaseSolution[list[int]]):
    def parseInput(self):
        return [1, 2, 3]

    def part1(self):
        return sum(self.parsedInput)


# tests


class Solution_Tests(unittest.TestCase):
    def test_decorated_valid(self):
        """Decorated solution returning the expected value should not throw"""
        DecoratedSolution(SolutionOptions(False, 1, 2024)).part1()
        DecoratedSolution(SolutionOptions(True, 1, 2024)).part1()

    def test_decorated_invalid(self):
        """Decorated solution returning unexpected value should throw"""
        # These calls should not raise an exception

        with self.assertRaises(InvalidSolutionError):
            DecoratedSolution(SolutionOptions(False, 1, 2024)).part2()

        with self.assertRaises(InvalidSolutionError):
            DecoratedSolution(SolutionOptions(True, 1, 2024)).part2()

    def test_undecorated_implemented(self):
        """Undecorated solution implemented method should never throw"""
        UnknownSolution(SolutionOptions(False, 1, 2024)).part1()
        UnknownSolution(SolutionOptions(True, 1, 2024)).part1()

    def test_undecorated_not_implemented(self):
        """Undecorated solution not implemented method should throw"""
        with self.assertRaises(NotImplementedError):
            UnknownSolution(SolutionOptions(False, 1, 2024)).part2()

    def test_solution_reads_input_file(self):
        """Solution reads its input file in both modes"""
        FileSolution(SolutionOptions(False, 1, 2024)).part1()
        FileSolution(SolutionOptions(True, 1, 2024)).part1()

    def test_solution_reads_forced_input(self):
        """Solution reads its forced input in both modes"""
        FileSolution(SolutionOptions(False, 1, 2024, lines=[])).part2()
        FileSolution(SolutionOptions(True, 1, 2024, lines=["foo"])).part2()

    def test_solution_uses_parseInput_method(self):
        """Solution uses parseInput() method and puts the result in parsedInput"""
        s = ParsingInputSolution(SolutionOptions(False, 1, 2024, lines=[]))
        self.assertEqual(s.parsedInput, [1, 2, 3])


if __name__ == "__main__":
    unittest.main(verbosity=2)
