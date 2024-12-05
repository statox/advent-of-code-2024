from ...base import BaseSolution, answer


def countWinningNumbers(line: str):
    [first, second] = line.split("|")
    [_, winningStr] = first.split(":")

    winning = {int(v) for v in winningStr.strip().split(" ") if len(v)}
    mines = [int(v) for v in second.strip().split(" ") if len(v)]

    return len([c for c in mines if c in winning])


class Solution(BaseSolution):
    @answer(13, 24542)
    def part1(self):
        total = 0
        for line in self.lines:
            winningNbs = countWinningNumbers(line)
            total += 2 ** (winningNbs - 1) if winningNbs > 0 else 0

        return total

    @answer(30, 8736438)
    def part2(self):
        cardCopies = [1 for l in self.lines]

        for i, line in enumerate(self.lines):
            winningNbs = countWinningNumbers(line)

            for j in range(winningNbs):
                cardCopies[i + 1 + j] += cardCopies[i]

        return sum(cardCopies)
