# Advent of code 2024

To add a solution for a new day

- Create `data/dayXX/input` and `data/dayXX/input_test`
- Create `libs/dayXX/solution.py` containing:

  ```python
  from ..base import BaseSolution


  class Solution(BaseSolution):
      def part1(self):
          raise NotImplementedError()

      def part2(self):
          raise NotImplementedError()
  ```

- Run the code for the day with

  ```bash
  ./main.py -d [day] -p [part] [-l or --livemode]
  ```

  where

  - `[day]` is the current day without the leading `0`
  - `[part]` is `1` or `2`
  - `[--livemode]` if present reads the `input` file, if not reads the `input_test`

Run the tests with (I created them to make sure my structure and `main.py` were correct, they might not be useful in the future)

```shell
python -m unittest **/*_test.py
```

To iterate on the solution after the expected result is known the functions `part1` and `part2` can be decorated with `@answer(a, b)` where `a` and `b` are the expected answers for the test input and the real input respectively.

When the decorator is present an exception will be thrown if the returned value of the function doesn't match the expected value.
