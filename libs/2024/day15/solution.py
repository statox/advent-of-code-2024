from typing import NamedTuple

from ...base import BaseSolution, answer
from ...utils.point import Point


class Input(NamedTuple):
    g: list[list[str]]
    moves: list[Point]
    pos: Point


def parsePart1(lines: list[str]) -> Input:
    g: list[list[str]] = []
    moves: list[Point] = []
    pos: Point | None = None

    movesMap = {
        "^": Point(0, -1),
        "v": Point(0, 1),
        "<": Point(-1, 0),
        ">": Point(1, 0),
    }

    doGrid = True
    y = -1
    for line in lines:
        if len(line) == 0:
            doGrid = False
            continue

        if doGrid:
            y += 1
            g.append(list(line))
            if line.find("@") > -1:
                pos = Point(line.index("@"), y)
            continue

        for moveStr in list(line):
            move = movesMap.get(moveStr)
            if move is None:
                raise Exception("Unexpected move: " + moveStr)

            moves.append(move)
    if pos is None:
        raise Exception("Initial position not found")

    return Input(g, moves, pos)


def parsePart2(lines: list[str]) -> Input:
    g: list[list[str]] = []
    moves: list[Point] = []
    pos: Point | None = None

    movesMap = {
        "^": Point(0, -1),
        "v": Point(0, 1),
        "<": Point(-1, 0),
        ">": Point(1, 0),
    }

    doGrid = True
    y = -1
    for line in lines:
        if len(line) == 0:
            doGrid = False
            continue

        if doGrid:
            y += 1
            finalLine = line
            finalLine = finalLine.replace("#", "##")
            finalLine = finalLine.replace("O", "[]")
            finalLine = finalLine.replace(".", "..")
            finalLine = finalLine.replace("@", "@.")

            g.append(list(finalLine))
            if finalLine.find("@") > -1:
                pos = Point(finalLine.index("@"), y)
            continue

        for moveStr in list(line):
            move = movesMap.get(moveStr)
            if move is None:
                raise Exception("Unexpected move: " + moveStr)

            moves.append(move)
    if pos is None:
        raise Exception("Initial position not found")

    return Input(g, moves, pos)


def getScore(g: list[list[str]]):
    return sum(
        [
            100 * y + x
            for x in range(len(g[0]))
            for y in range(len(g))
            if g[y][x] in "[O"
        ]
    )


def makeMove(g: list[list[str]], move: Point, pos: Point):
    neighbor = pos + move
    if g[neighbor.y][neighbor.x] == ".":
        # Direct neighbor is free
        return pos + move

    if g[neighbor.y][neighbor.x] == "#":
        # Direct neighbor is a wall
        return pos

    if move.x != 0:
        # Horizontal move
        n = pos
        while n == pos or g[n.y][n.x] in "[]":
            n += move

        if g[n.y][n.x] == "#":
            return pos

        for x in range(n.x, pos.x, -move.x):
            g[n.y][x] = g[n.y][x - move.x]

        return pos + move

    if move.y != 0:
        # Vertical move
        s = []
        toMove = []
        dest = pos + move
        if g[dest.y][dest.x] == "[":
            s.append((dest, dest + Point(1, 0)))
        elif g[dest.y][dest.x] == "]":
            s.append((dest + Point(-1, 0), dest))

        while s:
            (left, right) = s.pop(0)
            if (left, right) not in toMove:
                toMove.append((left, right))

            afterLeftPos = left + move
            afterLeft = g[afterLeftPos.y][afterLeftPos.x]

            afterRightPos = right + move
            afterRight = g[afterRightPos.y][afterRightPos.x]

            if afterLeft == "#" or afterRight == "#":
                return pos

            if afterLeft == "[":
                # []
                # []
                s.append((afterLeftPos, afterLeftPos + Point(1, 0)))
            elif afterLeft == "]":
                # []
                #  []
                s.append((afterLeftPos + Point(-1, 0), afterLeftPos))

            if afterRight == "[":
                #  []
                # []
                s.append((afterRightPos, afterRightPos + Point(1, 0)))

        for left, right in reversed(toMove):
            destL = left + move
            g[destL.y][destL.x] = g[left.y][left.x]
            g[left.y][left.x] = "."
            destR = right + move
            g[destR.y][destR.x] = g[right.y][right.x]
            g[right.y][right.x] = "."

        return pos + move

    raise Exception("Invalid situation")


class Solution(BaseSolution[Input]):
    @answer(10092, 1414416)
    def part1(self):
        (g, moves, pos) = parsePart1(self.lines)

        for move in moves:
            n = pos
            while n == pos or g[n.y][n.x] == "O":
                n += move

            if g[n.y][n.x] == ".":
                if n == pos + move:
                    # No box
                    g[pos.y][pos.x] = "."
                    g[n.y][n.x] = "@"
                else:
                    g[pos.y][pos.x] = "."
                    g[(pos + move).y][(pos + move).x] = "@"
                    g[n.y][n.x] = "O"

                pos = pos + move

        return getScore(g)

    @answer(9021, 1386070)
    def part2(self):
        (g, moves, pos) = parsePart2(self.lines)

        for move in moves:
            newPos = makeMove(g, move, pos)
            g[pos.y][pos.x] = "."
            g[newPos.y][newPos.x] = "@"
            pos = newPos
            # [print("".join(line)) for line in g]

        return getScore(g)