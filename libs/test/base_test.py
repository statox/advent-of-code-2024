import unittest
from unittest.mock import MagicMock

from ..base import (
    BaseSolution,
    InvalidSolutionError,
    InvalidSolutionOptions,
    SolutionOptions,
    answer,
)

#
# Test Answer decorator
#


class WorkingDecoratedSolution(BaseSolution):
    @answer(1, 2)
    def part1(self):
        # part1 returns expected values in both modes
        return 2 if self.livemode else 1

    @answer(1, 2)
    def part2(self):
        # part2 returns expected values in both modes
        return 2 if self.livemode else 1


class NotWorkingDecoratedSolution(BaseSolution):
    @answer(1, 2)
    def part1(self):
        # part1 returns invalid values in both modes
        return -1

    @answer(1, 2)
    def part2(self):
        # part1 returns invalid values in both modes
        return -1


class DecoratedWithNoneSolution(BaseSolution):
    @answer(None, None)
    def part1(self):
        return 10


class DecoratedWithStrSolution(BaseSolution):
    @answer("foo", "bar")
    def part1(self):
        return "foo"


class NoAnswerDecoratorSolution(BaseSolution):
    def part1(self):
        return 1

    def part2(self):
        return 1


class AnswerDecorator_Tests(unittest.TestCase):
    def test_decorated_answer_match(self):
        """Decorated solution returning the expected value should not raise"""
        WorkingDecoratedSolution(SolutionOptions(False)).part1()
        WorkingDecoratedSolution(SolutionOptions(True)).part1()
        WorkingDecoratedSolution(SolutionOptions(False)).part2()
        WorkingDecoratedSolution(SolutionOptions(True)).part2()

    def test_decorated_answer_dont_match(self):
        """Decorated solution returning the unexpected value should raise"""
        with self.assertRaises(InvalidSolutionError):
            NotWorkingDecoratedSolution(SolutionOptions(False)).part1()
        with self.assertRaises(InvalidSolutionError):
            NotWorkingDecoratedSolution(SolutionOptions(True)).part1()
        with self.assertRaises(InvalidSolutionError):
            NotWorkingDecoratedSolution(SolutionOptions(False)).part2()
        with self.assertRaises(InvalidSolutionError):
            NotWorkingDecoratedSolution(SolutionOptions(True)).part2()

    def test_not_decorated_answer(self):
        """Not Decorated solution should never raise"""
        NoAnswerDecoratorSolution(SolutionOptions(False)).part1()
        NoAnswerDecoratorSolution(SolutionOptions(True)).part1()
        NoAnswerDecoratorSolution(SolutionOptions(False)).part2()
        NoAnswerDecoratorSolution(SolutionOptions(True)).part2()

    def test_decorated_with_none_answer(self):
        """Solution decorated with none should not throw"""
        DecoratedWithNoneSolution(SolutionOptions(False)).part1()
        DecoratedWithNoneSolution(SolutionOptions(True)).part1()

    def test_decoration_str_answer(self):
        """Solution should be able to return and validate string result"""
        DecoratedWithStrSolution(SolutionOptions(False)).part1()
        with self.assertRaises(InvalidSolutionError):
            DecoratedWithStrSolution(SolutionOptions(True)).part1()


#
# Test Running parts
#
class UnimplementedSolution(BaseSolution):
    pass


class BothPartsImplementedSolution(BaseSolution):
    def part1(self):
        return 1

    def part2(self):
        return 1


class RunningParts_Tests(unittest.TestCase):
    def test_unimplemented_solution(self):
        """Solution with an unimplemented part should raise"""
        with self.assertRaises(NotImplementedError):
            UnimplementedSolution(SolutionOptions(False)).part1()
        with self.assertRaises(NotImplementedError):
            UnimplementedSolution(SolutionOptions(True)).part1()
        with self.assertRaises(NotImplementedError):
            UnimplementedSolution(SolutionOptions(False)).part2()
        with self.assertRaises(NotImplementedError):
            UnimplementedSolution(SolutionOptions(True)).part2()

    def test_runParts_one_method(self):
        """The runParts() method should call part1"""
        s = BothPartsImplementedSolution(SolutionOptions(False))
        s.part1 = MagicMock()
        s.part2 = MagicMock()

        s.runPart("one")
        s.part1.assert_called_once()
        s.part2.assert_not_called()

    def test_runParts_two_method(self):
        """The runParts() method should call part2"""
        s = BothPartsImplementedSolution(SolutionOptions(False))
        s.part1 = MagicMock()
        s.part2 = MagicMock()

        s.runPart("two")
        s.part1.assert_not_called()
        s.part2.assert_called_once()

    def test_runParts_both_method(self):
        """The runParts() method should call both parts"""
        s = BothPartsImplementedSolution(SolutionOptions(False))
        s.part1 = MagicMock()
        s.part2 = MagicMock()

        s.runPart("both")
        s.part1.assert_called_once()
        s.part2.assert_called_once()


#
# Test Input specification
#
class DontTreatInputSolution(BaseSolution):
    def part1(self):
        return 1

    def part2(self):
        return 1


class InputSpecifications_Tests(unittest.TestCase):
    def test_unimplemented_solution(self):
        """Providing both forced input and alternative input file should raise"""
        with self.assertRaises(InvalidSolutionOptions):
            DontTreatInputSolution(
                SolutionOptions(False, lines=["foo"], alternativeInputFile=2)
            )

        with self.assertRaises(InvalidSolutionOptions):
            DontTreatInputSolution(
                SolutionOptions(True, lines=["foo"], alternativeInputFile=2)
            )

    def test_input_file_livemode_true_selection(self):
        """Livemode True should read the input file"""
        s = DontTreatInputSolution(SolutionOptions(True))
        self.assertEqual(s.lines, ["a", "livemode", "input"])

    def test_input_file_livemode_false_selection(self):
        """Livemode False should read the input file"""
        s = DontTreatInputSolution(SolutionOptions(False))
        self.assertEqual(s.lines, ["a", "non", "livemode", "input"])

    def test_forced_file__selection(self):
        """Livemode True should raise if forced input is passed"""
        with self.assertRaises(InvalidSolutionOptions):
            DontTreatInputSolution(SolutionOptions(True, lines=["foo"]))

        """Livemode False should read the forced input"""
        s = DontTreatInputSolution(
            SolutionOptions(False, lines=["a", "forced", "input"])
        )
        self.assertEqual(s.lines, ["a", "forced", "input"])

    def test_alternative_input(self):
        """Livemode True given an alternative input file should raise"""
        with self.assertRaises(InvalidSolutionOptions):
            DontTreatInputSolution(SolutionOptions(True, alternativeInputFile=1))

        """Livemode False given a non existing alternative input file should raise"""
        with self.assertRaises(InvalidSolutionOptions):
            DontTreatInputSolution(SolutionOptions(False, alternativeInputFile=2))

        """Livemode False should read the alternative input file"""
        s = DontTreatInputSolution(SolutionOptions(False, alternativeInputFile=1))
        self.assertEqual(s.lines, ["an", "alternative", "input", "file"])


#
# Test Parse input
#
class ParsingInputSolution(BaseSolution[list[int]]):
    def parseInput(self):
        return [int(x) * 2 for x in self.lines]


class NotParsingInputSolution(BaseSolution):
    pass


class InputParsing_Tests(unittest.TestCase):
    def test_not_parsing_input_solution(self):
        """Solution with no input parsing should work"""
        s = NotParsingInputSolution(SolutionOptions(True))
        self.assertEqual(s.lines, ["a", "livemode", "input"])
        self.assertIsNone(s.parsedInput)

    def test_parsing_input_solution(self):
        """Solution with input parsing should populate self.parsedInput"""
        s = ParsingInputSolution(SolutionOptions(False, lines=["1", "2", "3"]))
        self.assertEqual(s.parsedInput, [2, 4, 6])


if __name__ == "__main__":
    unittest.main(verbosity=2)
