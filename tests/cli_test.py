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


def make_args(
    day: int, bothmodes: bool = False, livemode: bool = False, part: int = -1
):
    d = f"-d {day}"
    p = f"-p {part}" if part > -1 else ""
    l = "-l" if livemode else ""
    b = "-b" if bothmodes else ""
    return f"{d} {p} {l} {b}"


def make_command(
    day: int, bothmodes: bool = False, livemode: bool = False, part: int = -1
):
    return f"{PROCESS} {make_args(day, bothmodes, livemode, part)}"


def get_process(
    day: int, bothmodes: bool = False, livemode: bool = False, part: int = -1
):
    return subprocess.run(
        shlex.split(make_command(day, bothmodes, livemode, part)),
        capture_output=True,
        text=True,
        check=False,
    )


# tests


class Wrapper_Tests(unittest.TestCase):
    def test_invalid_part(self):
        """Test for an invalid part"""
        process = get_process(day=1, livemode=True, part=3)
        self.assertEqual(process.returncode, 2)

    def test_not_implemented_day(self):
        """Test for a not implemented day"""
        process = get_process(day=25, livemode=False, part=1)
        self.assertEqual(process.returncode, 1)
        self.assertEqual(process.stdout.strip(), "ERROR: Day 25 is not implemented")


class Part_Tests(unittest.TestCase):
    def test_day1_part1(self):
        """Test day 1 part 1 sample data"""
        process = get_process(day=1, livemode=False, part=1)
        expected_output = "Result for day 1 - part 1 - livemode False: 11"
        self.assertEqual(process.stdout.strip(), expected_output)

    def test_day1_part2(self):
        """Test day 1 part 1 sample data"""
        process = get_process(day=1, livemode=False, part=2)
        expected_output = "Result for day 1 - part 2 - livemode False: 31"
        self.assertEqual(process.stdout.strip(), expected_output)

    def test_day1_allparts(self):
        """Test day 1 both sample data"""
        process = get_process(day=1, livemode=False)
        expected_output = "Result for day 1 - part 1 - livemode False: 11\nResult for day 1 - part 2 - livemode False: 31"

        self.assertEqual(process.stdout.strip(), expected_output)


class Mode_Tests(unittest.TestCase):
    def test_forbid_bothmodes_and_livemode(self):
        process = get_process(day=1, bothmodes=True, livemode=True, part=1)
        expected_output = "ERROR: Can't define both -b and -l"
        self.assertEqual(process.stdout.strip(), expected_output)

    def test_day1_part1_bothmodes(self):
        process = get_process(day=1, bothmodes=True, part=1)
        expected_output = "Result for day 1 - part 1 - livemode False: 11\nResult for day 1 - part 1 - livemode True: 2769675"
        self.assertEqual(process.stdout.strip(), expected_output)

    def test_day1_part1_livemode(self):
        process = get_process(day=1, livemode=True, part=1)
        expected_output = "Result for day 1 - part 1 - livemode True: 2769675"
        self.assertEqual(process.stdout.strip(), expected_output)

    def test_day1_part1_not_livemode(self):
        process = get_process(day=1, part=1)
        expected_output = "Result for day 1 - part 1 - livemode False: 11"
        self.assertEqual(process.stdout.strip(), expected_output)


class Days_Tests(unittest.TestCase):
    def test_day1_part1_example(self):
        """Test day 1 part 1 sample data"""
        process = get_process(day=1, livemode=False, part=1)
        expected_output = "Result for day 1 - part 1 - livemode False: 11"
        self.assertEqual(process.stdout.strip(), expected_output)

    def test_day1_part1_real(self):
        """Test day 1 part 1 real data"""
        process = get_process(day=1, livemode=True, part=1)
        expected_output = "Result for day 1 - part 1 - livemode True: 2769675"
        self.assertEqual(process.stdout.strip(), expected_output)

    def test_day1_part2_example(self):
        """Test day 1 part 2 sample data"""
        process = get_process(day=1, livemode=False, part=2)
        expected_output = "Result for day 1 - part 2 - livemode False: 31"
        self.assertEqual(process.stdout.strip(), expected_output)

    def test_day1_part2_real(self):
        """Test day 1 part 2 real data"""
        process = get_process(day=1, livemode=True, part=2)
        expected_output = "Result for day 1 - part 2 - livemode True: 24643097"
        self.assertEqual(process.stdout.strip(), expected_output)

    def test_day2_part1_example(self):
        """Test day 2 part 1 sample data"""
        process = get_process(day=2, livemode=False, part=1)
        expected_output = "Result for day 2 - part 1 - livemode False: 2"
        self.assertEqual(process.stdout.strip(), expected_output)

    def test_day2_part1_real(self):
        """Test day 2 part 1 real data"""
        process = get_process(day=2, livemode=True, part=1)
        expected_output = "Result for day 2 - part 1 - livemode True: 559"
        self.assertEqual(process.stdout.strip(), expected_output)

    def test_day2_part2_example(self):
        """Test day 2 part 2 sample data"""
        process = get_process(day=2, livemode=False, part=2)
        expected_output = "Result for day 2 - part 2 - livemode False: 4"
        self.assertEqual(process.stdout.strip(), expected_output)

    def test_day2_part2_real(self):
        """Test day 1 part 2 real data"""
        process = get_process(day=2, livemode=True, part=2)
        expected_output = "Result for day 2 - part 2 - livemode True: 601"
        self.assertEqual(process.stdout.strip(), expected_output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
