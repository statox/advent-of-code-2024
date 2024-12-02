class BaseSolution():
    lines: list[str]

    def __init__(self, lines: list[str]):
        self.lines = lines

    def part1(self) -> int:
        raise NotImplementedError()

    def part2(self) -> int:
        raise NotImplementedError()
