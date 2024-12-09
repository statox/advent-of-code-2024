#!/usr/bin/env python3

import cProfile
import sys
from argparse import ArgumentParser
from datetime import datetime
from importlib import import_module
from typing import Optional, Type, cast

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
    "-y",
    "--year",
    dest="year",
    required=False,
    type=str,
    help="The year of the day to execute",
    default=datetime.now().year,
)
parser.add_argument(
    "-p",
    "--part",
    dest="part",
    type=int,
    choices=[1, 2],
    help="The question to run",
)
parser.add_argument(
    "--profile",
    dest="profile",
    action="store_true",
    help="Profile the code to run",
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


def getSolution(year: str, day: int, livemode: bool):
    try:
        path = f"libs.{year}.day{day:02}.solution"
        solution_class = cast(Type[BaseSolution], import_module(path).Solution)
    except ModuleNotFoundError:
        print(f"ERROR: Day {args.day}/{year} is not implemented")
        sys.exit(1)

    return solution_class(livemode, day, int(year))


def runMode(year: str, day: int, livemode: bool, part: Optional[int]):
    solution = getSolution(year, day, livemode)
    if part is None:
        solution.runPart("both")
    else:
        solution.runPart("one" if part == 1 else "two")


if __name__ == "__main__":
    args = parser.parse_args()

    if args.profile:
        if args.part is None:
            print("Can't profile several parts at once. --profile must come with -p")
            sys.exit(1)
        if args.bothmode:
            print(
                "Can't profile several inputs at once. --profile must not come with -b"
            )
            sys.exit(1)

        cProfile.run(
            "runMode(args.year, args.day, args.livemode, args.part)",
            # sort="tottime",
            sort="ncalls",
        )
    elif args.bothmode:
        runMode(args.year, args.day, False, args.part)
        runMode(args.year, args.day, True, args.part)
    else:
        runMode(args.year, args.day, args.livemode, args.part)
