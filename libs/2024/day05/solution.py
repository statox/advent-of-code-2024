from functools import cmp_to_key
from typing import NamedTuple

from ...base import BaseSolution, answer


class ParsedInput(NamedTuple):
    rules: dict[int, set[int]]
    updates: list[list[int]]


class Solution(BaseSolution[ParsedInput]):
    def parseInput(self):
        rules: dict[int, set[int]] = {}
        updates: list[list[int]] = []

        for line in self.lines:
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

        return ParsedInput(rules, updates)

    def updateIsInOrder(self, update: list[int], rules: dict[int, set[int]]):
        for i in range(len(update) - 1):
            a = update[i]
            rulesForA = rules.get(a, [])
            for j in range(i + 1, len(update)):
                b = update[j]
                if b in rulesForA:
                    return False
        return True

    @answer(143, 6242)
    def part1(self):
        (rules, updates) = self.parsedInput
        return sum(
            update[int(len(update) / 2)]
            for update in updates
            if self.updateIsInOrder(update, rules)
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

        (rules, updates) = self.parsedInput
        return sum(
            update[int(len(update) / 2)]
            for update in [
                sorted(
                    update,
                    key=cmp_to_key(lambda a, b: 1 if b in rules.get(a, []) else -1),
                )
                for update in updates
                if not self.updateIsInOrder(update, rules)
            ]
        )
