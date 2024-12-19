#!/usr/bin/env python3

import cProfile
import sys
from argparse import ArgumentParser, Namespace
from collections.abc import Sequence
from datetime import datetime
from importlib import import_module
from typing import Optional, Type, cast

from libs.base import BaseSolution, SolutionOptions


class CustomArgumentParser(ArgumentParser):
    def __init__(self):
        super().__init__()

        self.add_argument(
            "-d",
            "--day",
            dest="day",
            required=True,
            type=int,
            choices=list(range(1, 26)),
            help="The day to execute",
        )
        self.add_argument(
            "-y",
            "--year",
            dest="year",
            required=False,
            type=str,
            help="The year of the day to execute",
            default=datetime.now().year,
        )
        self.add_argument(
            "-p",
            "--part",
            dest="part",
            type=int,
            choices=[1, 2],
            help="The question to run",
        )
        self.add_argument(
            "-i",
            "--inputFile",
            dest="inputFile",
            type=int,
            help="The alternative input file to use",
        )
        self.add_argument(
            "--profile",
            dest="profile",
            action="store_true",
            help="Profile the code to run",
        )
        self.add_argument(
            "-pm",
            "--profile-metric",
            dest="profile_metric",
            type=str,
            choices=["tottime", "ncalls", "cumtime"],
            help="Metric to use to sort the profiler's results",
        )

        # Make -l and -b mutually exclusive
        modesGroup = self.add_mutually_exclusive_group()
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

    def parse_args(  # type: ignore TODO Find our why this didn't solve the issue https://github.com/microsoft/pyright/discussions/6739
        self, args: Sequence[str] | None = None
    ) -> Namespace:
        parsed = super().parse_args(args)

        if parsed.profile_metric and not parsed.profile:
            self.error(
                "--profile must be provided if --profile-metric (--pm) is provided"
            )

        if parsed.profile:
            if parsed.part is None:
                self.error(
                    "Can't profile several parts at once. --profile must come with -p"
                )
            if parsed.bothmode:
                self.error(
                    "Can't profile several inputs at once. --profile must not come with -b"
                )

        return parsed


def getSolution(year: str, day: int, livemode: bool, inputFile: int | None):
    try:
        path = f"libs.{year}.day{day:02}.solution"
        solution_class = cast(Type[BaseSolution], import_module(path).Solution)
    except ModuleNotFoundError:
        print(f"ERROR: Day {args.day}/{year} is not implemented")
        sys.exit(1)

    return solution_class(
        SolutionOptions(livemode, day, int(year), alternativeInputFile=inputFile)
    )


def runMode(
    year: str, day: int, livemode: bool, part: Optional[int], inputFile: Optional[int]
):
    solution = getSolution(year, day, livemode, inputFile)
    if part is None:
        solution.runPart("both")
    else:
        solution.runPart("one" if part == 1 else "two")


if __name__ == "__main__":
    args = CustomArgumentParser().parse_args()

    if args.profile:
        cProfile.run(
            "runMode(args.year, args.day, args.livemode, args.part, args.inputFile)",
            sort=args.profile_metric or "tottime",
        )
    elif args.bothmode:
        runMode(args.year, args.day, False, args.part, args.inputFile)
        runMode(args.year, args.day, True, args.part, args.inputFile)
    else:
        runMode(args.year, args.day, args.livemode, args.part, args.inputFile)
