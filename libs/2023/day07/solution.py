from functools import cmp_to_key
from typing import NamedTuple

from ...base import BaseSolution, answer

cardValues = "AKQJT98765432"
handValues = "54F3210"


class Hand(NamedTuple):
    cards: list[str]
    bid: int
    handValue: str


def handsComparison(a: Hand, b: Hand):
    valueA = handValues.index(a.handValue)
    valueB = handValues.index(b.handValue)

    if valueA != valueB:
        return valueA - valueB

    for i, card in enumerate(a.cards):
        if card != b.cards[i]:
            return cardValues.index(card) - cardValues.index(b.cards[i])

    return 0


handsComparison_key = cmp_to_key(handsComparison)


class Solution(BaseSolution[list[Hand]]):
    def parseInput(self):
        hands = []
        for line in self.lines:
            [cardsStr, bidStr] = line.split(" ")
            counts = {}
            for card in cardsStr:
                counts[card] = counts.get(card, 0) + 1
            countsVals = counts.values()
            handValue = "0"
            if 5 in countsVals:
                handValue = "5"
            elif 4 in countsVals:
                handValue = "4"
            elif 3 in countsVals and 2 in countsVals:
                handValue = "F"
            elif 3 in countsVals:
                handValue = "3"
            elif len([1 for v in countsVals if v == 2]) == 2:
                handValue = "2"
            elif 2 in countsVals:
                handValue = "1"

            hands.append(Hand(list(cardsStr), int(bidStr), handValue))

        return hands

    @answer(6440, 253910319)
    def part1(self):
        self.parsedInput.sort(key=handsComparison_key)

        total = 0
        for i, hand in enumerate(self.parsedInput):
            mult = len(self.parsedInput) - i
            total += hand.bid * mult

        return total

    # @answer(0, 0)
    # def part2(self):
    # return 1
