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


class Solution(BaseSolution):
    _secret: int
    _cnt: int

    def parseInput(self):
        return [int(v) for v in self.lines]

    def gen_secret(self, initialSecret: int, sequence_size: int):
        self._secret = initialSecret
        self._cnt = sequence_size

        while self._cnt >= 0:
            self._cnt -= 1
            s = self._secret
            s1 = ((s * 64) ^ s) % 16777216
            s2 = ((s1 // 32) ^ s1) % 16777216
            self._secret = ((s2 * 2048) ^ s2) % 16777216
            yield self._secret

    def gen_sequence(self, initialSecret: int, sequence_size: int):
        self._secret = initialSecret
        self._cnt = sequence_size

        while self._cnt >= 0:
            self._cnt -= 1
            prev_last_digit = self._secret % 10

            s1 = ((self._secret * 64) ^ self._secret) % 16777216
            s2 = ((s1 // 32) ^ s1) % 16777216
            self._secret = ((s2 * 2048) ^ s2) % 16777216

            last_digit = self._secret % 10
            yield (last_digit, last_digit - prev_last_digit)

    @answer(37327623, 20506453102)
    def part1(self):
        return sum(
            [
                next(islice(self.gen_secret(s, 2000), 1999, None))
                for s in self.parsedInput
            ]
        )

    @answer(24, 2423)
    def part2(self):
        orders_gains: dict[tuple, int] = defaultdict(int)
        best_gain = 0

        for secret in self.parsedInput:
            sq = self.gen_sequence(secret, 2000)
            sub_sq = deque([next(sq)[1], next(sq)[1], next(sq)[1]], maxlen=4)

            seen_changes: set[tuple] = set()
            for digit, diff in sq:
                sub_sq.append(diff)
                changes = tuple(sub_sq)

                if changes in seen_changes:
                    continue

                seen_changes.add(changes)
                orders_gains[changes] += digit
                if best_gain < orders_gains[changes]:
                    best_gain = orders_gains[changes]

        return best_gain
