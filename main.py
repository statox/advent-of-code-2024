#!/usr/bin/env python3

import sys
from argparse import ArgumentParser
from importlib import import_module
from typing import Optional, Type, cast

from common.io import read_input_file
from libs.base import BaseSolution

parser = ArgumentParser()
parser.add_argument(
    "-d",
    "--day",
    dest="day",
    required=True,
    type=int,
    choices=list(range(1, 26)),
    help="The day to execute",
)
parser.add_argument(
    "-p",
    "--part",
    dest="part",
    type=int,
    choices=[1, 2],
    help="The question to run",
)

# Make -l and -b mutually exclusive
modesGroup = parser.add_mutually_exclusive_group()
modesGroup.add_argument(
    "-l",
    "--livemode",
    dest="livemode",
    action="store_true",
    help="True to use real input, False to use test input",
)
modesGroup.add_argument(
    "-b",
    "--bothmode",
    dest="bothmode",
    action="store_true",
    help="True to run both livemode and testmode",
)


def getSolution(day: int, livemode: bool):
    try:
        path = f"libs.day{day:02}.solution"
        solution_class = cast(Type[BaseSolution], import_module(path).Solution)
    except ModuleNotFoundError:
        print(f"ERROR: Day {args.day} is not implemented")
        sys.exit(1)

    lines = read_input_file(day, livemode)
    return solution_class(lines, livemode, day)


def runMode(day: int, livemode: bool, part: Optional[int]):
    solution = getSolution(day, livemode)
    if part is None:
        solution.runPart("both")
    else:
        solution.runPart("one" if part == 1 else "two")


if __name__ == "__main__":
    args = parser.parse_args()

    if args.bothmode:
        runMode(args.day, False, args.part)
        runMode(args.day, True, args.part)
    else:
        runMode(args.day, args.livemode, args.part)
