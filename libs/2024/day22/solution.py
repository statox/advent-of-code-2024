from collections import defaultdict, deque
from itertools import islice

from ...base import BaseSolution, answer

# To mix a value into the secret number:
#   calculate the bitwise XOR of the given value and the secret number.
#   Then, the secret number becomes the result of that operation.
#   (If the secret number is 42 and you were to mix 15 into the secret number, the secret number would become 37.)
# To prune the secret number:
#   calculate the value of the secret number modulo 16777216.
#   Then, the secret number becomes the result of that operation.
#   (If the secret number is 100000000 and you were to prune the secret number, the secret number would become 16113920.)


# 1. Calculate the result of multiplying the secret number by 64.
#    Then, mix this result into the secret number.
#    Finally, prune the secret number.
# 2. Calculate the result of dividing the secret number by 32.
#    Round the result down to the nearest integer.
#    Then, mix this result into the secret number.
#    Finally, prune the secret number.
# 3. Calculate the result of multiplying the secret number by 2048.
#    Then, mix this result into the secret number.
#    Finally, prune the secret number.
# @cache
class Monkey:
    _secret: int

    def __init__(self, initialSecret: int):
        self._secret = initialSecret

    def resetTo(self, initialSecret: int):
        self._secret = initialSecret

    def gen_secret(self):
        while True:
            s = self._secret
            s1 = ((s * 64) ^ s) % 16777216
            s2 = ((s1 // 32) ^ s1) % 16777216
            self._secret = ((s2 * 2048) ^ s2) % 16777216
            yield self._secret

    def gen_sequence(self):
        while True:
            prev_last_digit = self._secret % 10

            s = self._secret
            s1 = ((s * 64) ^ s) % 16777216
            s2 = ((s1 // 32) ^ s1) % 16777216
            self._secret = ((s2 * 2048) ^ s2) % 16777216

            last_digit = self._secret % 10
            last_digit_diff = last_digit - prev_last_digit
            yield (last_digit, last_digit_diff)


def get_sequence_orders_and_gains(start: int):
    r: dict[tuple, int] = {}

    sq = Monkey(start).gen_sequence()
    sub_sq = deque(maxlen=4)
    sub_sq.append(next(sq))
    sub_sq.append(next(sq))
    sub_sq.append(next(sq))

    for _ in range(4, 2000 + 1):
        last = next(sq)
        sub_sq.append(last)
        changes = tuple([v[1] for v in sub_sq])

        if changes not in r:
            r[changes] = last[0]

    return r


class Solution(BaseSolution):
    def parseInput(self):
        return [int(v) for v in self.lines]

    @answer(37327623, 20506453102)
    def part1(self):
        return sum(
            [next(islice(Monkey(s).gen_secret(), 1999, None)) for s in self.parsedInput]
        )

    @answer(24, 2423)
    def part2(self):
        orders_gains: dict[tuple, int] = defaultdict(int)
        best_gain = 0

        for secret in self.parsedInput:
            sub_orders_gains = get_sequence_orders_and_gains(secret)

            for changes in sub_orders_gains:
                orders_gains[changes] += sub_orders_gains[changes]
                best_gain = max(orders_gains[changes], best_gain)

        return best_gain
