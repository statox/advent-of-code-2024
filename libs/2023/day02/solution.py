from ...base import BaseSolution, answer


class Solution(BaseSolution):
    @answer(8, 2632)
    def part1(self):
        total = 0
        limits = {"red": 12, "green": 13, "blue": 14}

        for line in self.lines:
            [first, second] = line.split(":")
            gameId = int(first.split(" ")[1])

            grabs = [
                [c.strip().split(" ") for c in grab]
                for grab in [
                    grabStr.strip().split(",") for grabStr in second.split(";")
                ]
            ]

            gameIsValid = True
            for grab in grabs:
                for [nb, color] in grab:
                    if int(nb) > limits[color]:
                        gameIsValid = False
                        break

                if not gameIsValid:
                    break

            if gameIsValid:
                total += gameId

        return total

    @answer(2286, 69629)
    def part2(self):
        total = 0

        for line in self.lines:
            [_, second] = line.split(":")

            grabs = [
                [c.strip().split(" ") for c in grab]
                for grab in [
                    grabStr.strip().split(",") for grabStr in second.split(";")
                ]
            ]

            mins = {"red": 0, "green": 0, "blue": 0}
            for grab in grabs:
                for [nb, color] in grab:
                    mins[color] = max(mins[color], int(nb))
            power = mins["red"] * mins["green"] * mins["blue"]
            total += power

        return total
