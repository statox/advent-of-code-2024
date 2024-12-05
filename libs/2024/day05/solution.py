from functools import cmp_to_key

from ...base import BaseSolution, answer


def parseLines(lines: list[str]):
    rules: dict[int, set[int]] = {}
    updates: list[list[int]] = []

    for line in lines:
        if len(line) == 0:
            continue

        if "|" in line:
            [a, b] = list(map(int, line.split("|")))

            if rules.get(b) is None:
                rules[b] = set()
            rules[b].add(a)
        else:
            update = list(map(int, line.split(",")))
            updates.append(update)

    return rules, updates


class Solution(BaseSolution):
    rules: dict[int, set[int]]
    updates: list[list[int]]

    def __init__(self, *args, **kwargs):
        super(Solution, self).__init__(*args, **kwargs)

        rules, updates = parseLines(self.lines)
        self.rules = rules
        self.updates = updates

    def updateIsInOrder(self, update: list[int]):
        for i in range(len(update) - 1):
            a = update[i]
            rulesForA = self.rules.get(a, [])
            for j in range(i + 1, len(update)):
                b = update[j]
                if b in rulesForA:
                    return False
        return True

    @answer(143, 6242)
    def part1(self):
        return sum(
            update[int(len(update) / 2)]
            for update in self.updates
            if self.updateIsInOrder(update)
        )

        # for update in updates:
        #     inOrder = updateIsInOrder(update, rules)
        #     if inOrder:
        #         total += update[int(len(update) / 2)]

        # return total

    @answer(123, 5169)
    def part2(self):
        # total = 0
        # def custom_sort(a, b):
        #     rulesForA = rules.get(a, [])
        #     if b in rulesForA:
        #         return 1
        #     return -1
        # for update in updates:
        #     inOrder = updateIsInOrder(update, rules)
        #     if inOrder:
        #         continue

        #     update.sort(key=cmp_to_key(custom_sort))
        #     total += update[int(len(update) / 2)]

        # return total

        return sum(
            update[int(len(update) / 2)]
            for update in [
                sorted(
                    update,
                    key=cmp_to_key(
                        lambda a, b: 1 if b in self.rules.get(a, []) else -1
                    ),
                )
                for update in self.updates
                if not self.updateIsInOrder(update)
            ]
        )
