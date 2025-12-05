# Advent of code 2024/2025

## Add a solution for a new day

1. Run the script `./newDay [-d day] [-y year]` with `[day]` the day to implement (`1 <= day <= 25`)
   - `[day]` is optional in December and will be replaced by the current day (_only in december_)
   - `[year]` is optional and will default to the current year
1. Edit `libs/dayXX/input` and `libs/dayXX/input_test` with the input
   1. If needed also add `libs/dayXX/input_test_1`, `libs/dayXX/input_test_2`, etc with alternative inputs (See `-i` option)
1. Edit `libs/dayXX/solution.py` with the code implementing the methods `part1` and `part2`
1. Run the code for the day with the `main.py` script

```bash
./main.py -d [day] -p [part] [-y year] [-i input file] [-l or --livemode] [-b or --bothmode]
```

Usage:

| Parameter                  | Optional | Value    | Comment                                                                                                                                        |
| -------------------------- | -------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `-d [day]`                 | No       | `{1,24}` | The day to run without the leading `0` e.g. `-d4`                                                                                              |
| `-y [year]`                | Yes      | `[1-9]`  | The year of the day to run e.g `-y2023`                                                                                                        |
| `-p [part]`                | Yes      | `1,2`    | If omitted both parts are run.                                                                                                                 |
| `-i [input file]`          | Yes      | `[1-9]`  | A number corresponding to the filename of an alternative input file e.g `-i1` to parse `input_test_1`                                          |
| `[--livemode]` (or `-l`)   | Yes      |          | If present reads the `input` file, if not reads the `input_test`. Mutually exclusive with `[--bothmode]`and `-i`                               |
| `[--bothmode]` (or `-b`)   | Yes      |          | If present runs the solution for both `input` and `input_test`. If absent, `[--livemode]` is evaluated. Mutually exclusive with `[--livemode]` |

## Solution's input

By default, when creating a class extending `BaseSolution` the lines from the input file split on new line character will be available as a list in `self.lines`.

If more complex treatment of the input is needed it is possible to implement the method `parseInput()` of the `BaseSolution` class. In this case the class definition should provide a type for the parsed input object (e.g. `class Solution(BaseSolution[list[int]]):`) and the method `parseInput()` should return this object.

The result will then be available via `self.parsedInput` in the solution class.

## Iterate on a solution

To iterate on the solution after the expected result is known the functions `part1` and `part2` can be decorated with `@answer(a, b)` where `a` and `b` are the expected answers for the test input and the real input respectively.

When the decorator is present an exception will be thrown if the returned value of the function doesn't match the expected value.

## Run the tests

I created the tests to make sure my `BaseSolution` class and `main.py` were correct. They can be run with:

```shell
python -m unittest **/*_test.py
```

## Run all solutions in the repo

```shell
run_all.py
```

This will run part 1 and 2 of all solutions, displaying at the end which part are potentially broken or not implemented. That will skip days which haven't been created at all.

## Lints and checks


```
# Formating
uv run ruff format .
# Linting
uv run ruff check .
# Types
uv run pyright
```
