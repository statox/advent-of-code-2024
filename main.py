#!/usr/bin/env python3

import sys
from argparse import ArgumentParser
from importlib import import_module
from typing import Type, cast

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
    required=True,
    type=int,
    choices=[1, 2],
    help="The question to run",
)
parser.add_argument(
    "-l",
    "--livemode",
    dest="livemode",
    action="store_true",
    help="True to use real input, False to use test input",
)

if __name__ == "__main__":
    args = parser.parse_args()

    try:
        path = f"libs.day{args.day:02}.solution"
        solution_class = cast(Type[BaseSolution], import_module(path).Solution)
    except ModuleNotFoundError:
        print(f"ERROR: Day {args.day} is not implemented")
        sys.exit(1)

    lines = read_input_file(args.day, args.livemode)
    solution = solution_class(lines)

    res = solution.part1() if args.part == 1 else solution.part2()

    print(
        f"Result for day {args.day} - part {args.part} - livemode {args.livemode}: {res}"
    )
