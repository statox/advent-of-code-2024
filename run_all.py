#!/usr/bin/env python3

import os
import sys
from datetime import datetime
from importlib import import_module
from pathlib import Path
from typing import Optional, Type, cast

from libs.base import BaseSolution, InvalidSolutionError, SolutionOptions


def getSolution(year: str, day: int, livemode: bool):
    path = f"libs.{year}.day{day:02}.solution"
    solution_class = cast("Type[BaseSolution]", import_module(path).Solution)
    return solution_class(SolutionOptions(livemode, day, int(year)))


def runMode(year: str, day: int, livemode: bool, part: Optional[int], inputFile: Optional[int]):
    solution = getSolution(year, day, livemode, inputFile)
    if part is None:
        solution.runPart("both")
    else:
        solution.runPart("one" if part == 1 else "two")


if __name__ == "__main__":
    failures = []
    for year in range(datetime.now().year, 2022, -1):
        for day in range(26):
            print(f"{year} - {day} Running")
            if day == 21 and year == 2024:
                continue

            solution = None
            try:
                solution = getSolution(str(year), day, False)
            except ModuleNotFoundError:
                continue

            try:
                # Redirect output, we are only interested in success/failure
                # Use main to get logs if needed
                with Path.open(os.devnull, "w") as devnull:
                    old_stdout = sys.stdout
                    sys.stdout = devnull
                    try:
                        solution.runPart("both")
                        print(f"{year} - {day} OK")
                    except InvalidSolutionError as invalidSolutionError:
                        failures.append((day, year, "invalidSolution", invalidSolutionError))
                    except NotImplementedError as notImplementedError:
                        failures.append((day, year, "not implemented", notImplementedError))
                    sys.stdout = old_stdout
            except Exception as e:  # noqa: BLE001
                failures.append((day, year, "unexpected error", e))

    print("Got the following failures:")
    for day, year, message, error in failures:
        print(f"{year} - {day} - {message}")
        print(error)
