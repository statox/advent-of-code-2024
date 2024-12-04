import shlex
import subprocess
import unittest
from pathlib import Path
from shutil import which

# commands


def pick_python() -> str:
    """Return the python cmd that can be found in PATH"""
    # For some reason python points to python2 on my setup
    # for cmd in ("python", "python3"):
    for cmd in ("python3", "python"):
        if which(cmd):
            return cmd

    raise RuntimeError("python not found")


ROOT_DIR = Path(__file__).parents[1]
PROCESS = f"{pick_python()} {ROOT_DIR / 'main.py'}"


def make_args(day: int, part: int, livemode: bool):
    return f"-d {day} -p {part} {'-l' if livemode else ''}"


def make_command(day: int, part: int, livemode: bool):
    return f"{PROCESS} {make_args(day, part, livemode)}"


def get_process(day: int, part: int, livemode: bool):
    return subprocess.run(
        shlex.split(make_command(day, part, livemode)),
        capture_output=True,
        text=True,
        check=False,
    )


# tests


class Wrapper_Tests(unittest.TestCase):
    def test_invalid_part(self):
        """Test for an invalid part"""
        process = get_process(1, 3, True)
        self.assertEqual(process.returncode, 2)

    def test_not_implemented_day(self):
        """Test for a not implemented day"""
        process = get_process(25, 1, False)
        self.assertEqual(process.returncode, 1)
        self.assertEqual(process.stdout.strip(), "ERROR: Day 25 is not implemented")


class Days_Tests(unittest.TestCase):
    def test_day1_part1_example(self):
        """Test day 1 part 1 sample data"""
        process = get_process(1, 1, False)
        expected_output = "Result for day 1 - part 1 - livemode False: 11"
        self.assertEqual(process.stdout.strip(), expected_output)

    def test_day1_part1_real(self):
        """Test day 1 part 1 real data"""
        process = get_process(1, 1, True)
        expected_output = "Result for day 1 - part 1 - livemode True: 2769675"
        self.assertEqual(process.stdout.strip(), expected_output)

    def test_day1_part2_example(self):
        """Test day 1 part 2 sample data"""
        process = get_process(1, 2, False)
        expected_output = "Result for day 1 - part 2 - livemode False: 31"
        self.assertEqual(process.stdout.strip(), expected_output)

    def test_day1_part2_real(self):
        """Test day 1 part 2 real data"""
        process = get_process(1, 2, True)
        expected_output = "Result for day 1 - part 2 - livemode True: 24643097"
        self.assertEqual(process.stdout.strip(), expected_output)

    def test_day2_part1_example(self):
        """Test day 2 part 1 sample data"""
        process = get_process(2, 1, False)
        expected_output = "Result for day 2 - part 1 - livemode False: 2"
        self.assertEqual(process.stdout.strip(), expected_output)

    def test_day2_part1_real(self):
        """Test day 2 part 1 real data"""
        process = get_process(2, 1, True)
        expected_output = "Result for day 2 - part 1 - livemode True: 559"
        self.assertEqual(process.stdout.strip(), expected_output)

    def test_day2_part2_example(self):
        """Test day 2 part 2 sample data"""
        process = get_process(2, 2, False)
        expected_output = "Result for day 2 - part 2 - livemode False: 4"
        self.assertEqual(process.stdout.strip(), expected_output)

    def test_day2_part2_real(self):
        """Test day 1 part 2 real data"""
        process = get_process(2, 2, True)
        expected_output = "Result for day 2 - part 2 - livemode True: 601"
        self.assertEqual(process.stdout.strip(), expected_output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
