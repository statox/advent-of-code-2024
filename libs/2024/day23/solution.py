from collections import defaultdict
from itertools import combinations

from ...base import BaseSolution, answer


class Solution(BaseSolution[dict[str, list[str]]]):
    def parseInput(self):
        g: dict[str, list[str]] = defaultdict(list)

        for line in self.lines:
            [a, b] = line.split("-")

            g[a].append(b)
            g[b].append(a)

        return g

    # 2398 too high
    @answer(7, 1284)
    def part1(self):
        g = self.parsedInput

        groups_of_three: set[tuple[str, str, str]] = set()
        [print(node, g[node]) for node in g]

        for node in g:
            print("Searching", node)

            for a, b in combinations(g[node], 2):
                if b in g[a] and "t" in node[0] + a[0] + b[0]:
                    group = tuple(sorted([node, a, b]))
                    groups_of_three.add(group)

        return len(groups_of_three)

    # @answer("co,de,ka,ta", None)
    def part2(self):
        g = self.parsedInput

        h = {}
        for node in g:
            h[node] = set(g[node]).union([node])

        print("g and h")
        [print(node, g[node], h[node]) for node in g]

        for node in g:
            # node = list(h.keys())[0]
            group: set[str] = h[node]

            print("Searching group for", node)
            print("Initial group", group)

            for n in h[node]:
                print("  adding", n, h[n])
                group = group.intersection(h[n])
                print("    =>", group)

            [print(i) for i in group]

        return 0
