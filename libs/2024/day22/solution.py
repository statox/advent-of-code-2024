from collections import defaultdict

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
def gen_next(s: int):
    s1 = ((s * 64) ^ s) % 16777216
    s2 = ((s1 // 32) ^ s1) % 16777216
    return ((s2 * 2048) ^ s2) % 16777216


def get_sequence(start: int, steps: int):
    secret = start
    last_digit = start % 10

    prev_secret = secret
    prev_last_digit = last_digit
    last_digit_diff = None

    seq: list[tuple[int, None | int]] = []

    for _ in range(steps):
        secret = gen_next(prev_secret)
        last_digit = secret % 10
        last_digit_diff = last_digit - prev_last_digit
        seq.append((last_digit, last_digit_diff))

        prev_secret = secret
        prev_last_digit = last_digit
    return seq


def get_sequence_orders_and_gains(sq: list[tuple[int, None | int]]):
    r: dict[tuple, int] = {}

    for i in range(4, len(sq) + 1):
        sub_sq = sq[i - 4 : i]
        changes = tuple([v[1] for v in sub_sq])

        if changes not in r:
            r[changes] = sq[i - 1][0]

    return r


class Solution(BaseSolution):
    def parseInput(self):
        return [int(v) for v in self.lines]

    @answer(37327623, 20506453102)
    def part1(self):
        total = 0
        for s in self.parsedInput:
            r = s
            for _ in range(2000):
                r = gen_next(r)
            total += r

        return total

    @answer(24, 2423)
    def part2(self):
        orders_gains: dict[tuple, int] = defaultdict(int)
        best_gain = 0
        for secret in self.parsedInput:
            sq = get_sequence(secret, 2000)
            sub_orders_gains = get_sequence_orders_and_gains(sq)

            for changes in sub_orders_gains:
                orders_gains[changes] += sub_orders_gains[changes]
                best_gain = max(orders_gains[changes], best_gain)

        return best_gain
