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
python -m unittest tests/test_cli.py
```
