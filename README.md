# Advent of code 2024

## Add a solution for a new day

1. Run the script `./newDay [day]` with `[day]` the day to implement (`1 <= day <= 25`)
1. Edit `libs/dayXX/input` and `libs/dayXX/input_test` with the input
1. Edit `libs/dayXX/solution.py` with the code implementing the methods `part1` and `part2`
1. Run the code for the day with

   ```bash
   ./main.py -d [day] -p [part] [-l or --livemode] [-b or --bothmode]
   ```

   where

   - `[day]` is the current day without the leading `0`
   - (Optional) `[part]` is `1` or `2`. If omitted both parts are run.
   - (Optional) `[--livemode]` if present reads the `input` file, if not reads the `input_test`. Mutually exclusive with `[--bothmode]`
   - (Optional) `[--bothmode]` if present runs the solution for both `input` and `input_test`. If absent, `[--livemode]` is evaluated. Mutually exclusive with `[--livemode]`

## Solution's input

By default, when creating a class extending `BaseSolution` the lines from the input file split on new line character will be available as a list in `self.lines`.

If more complex treatment of the input is needed it is possible to implement the method `parseInput()` of the `BaseSolution` class. In this case the class definition should provide a type for the parsed input object (e.g. `class Solution(BaseSolution[list[int]]):`) and the method `parseInput()` should return this object.

The result will then be available via `self.parsedInput` in the solution class.

## Iterate on a solution

To iterate on the solution after the expected result is known the functions `part1` and `part2` can be decorated with `@answer(a, b)` where `a` and `b` are the expected answers for the test input and the real input respectively.

When the decorator is present an exception will be thrown if the returned value of the function doesn't match the expected value.

## Run the tests

I created the tests to make sure my `BaseSolution` class and `main.py` were correct, they might not be useful in the future. They can be run with:

```shell
python -m unittest **/*_test.py
```
