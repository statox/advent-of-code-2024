from ...base import BaseSolution, answer


def parseLines(lines: list[str]):
    ls = []

    for line in lines:
        [first, second] = line.split(":")
        res = int(first)
        vals = [int(v) for v in second.strip().split(" ") if len(v)]
        ls.append((res, vals))

    return ls


def canWork(result: int, current: int, vals: list[int]):
    print("  ", result, current, vals)
    if current > result:
        return False

    if len(vals) == 0:
        return current == result

    v = vals[0]
    return canWork(result, current * v, vals[1:]) or canWork(
        result, current + v, vals[1:]
    )


def canWork2(result: int, current: int, vals: list[int]):
    # print("  ", result, current, vals)
    if current > result:
        return False

    if len(vals) == 0:
        return current == result

    v = vals[0]
    return (
        canWork2(result, current * v, vals[1:])
        or canWork2(result, current + v, vals[1:])
        or canWork2(result, int(str(current) + str(v)), vals[1:])
    )


class Solution(BaseSolution):
    @answer(3749, 465126289353)
    def part1(self):
        ls = parseLines(self.lines)
        total = 0

        for res, vals in ls:
            r = canWork(res, vals[0], vals[1:])
            if r:
                total += res
        return total

    @answer(11387, 0)
    def part2(self):
        ls = parseLines(self.lines)
        total = 0

        for res, vals in ls:
            print()
            print("--------")
            print(res, vals)
            r = canWork2(res, vals[0], vals[1:])
            print("work", r)
            if r:
                total += res
        return total
