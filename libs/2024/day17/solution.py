import math
from typing import NamedTuple

from ...base import BaseSolution, answer


class Computer:
    a: int
    b: int
    c: int
    pointer: int
    program: list[tuple[int, int]]
    output: list[int]
    code: list[str]

    def __init__(self, A: int, B: int, C: int, program: list[tuple[int, int]]):
        self.a = A
        self.b = B
        self.c = C
        self.pointer = 0
        self.program = program
        self.output = []
        self.code = []

    def __str__(self):
        r = f"A: {self.a} B: {self.b} C: {self.c} \n"
        r += f"{self.program} \n"
        r += f"pointer: {self.pointer}"

        return r

    def adv(self, literal_operand: int):
        self.code.append(
            f"a = a // (2 ** {self.get_combo_operand_str(literal_operand)})"
        )
        self.a = self.a // (2 ** self.get_combo_operand(literal_operand))
        return self.pointer + 1

    def bdv(self, literal_operand: int):
        self.code.append(
            f"b = a // (2 ** {self.get_combo_operand_str(literal_operand)})"
        )
        self.b = self.a // (2 ** self.get_combo_operand(literal_operand))
        return self.pointer + 1

    def cdv(self, literal_operand: int):
        self.code.append(
            f"c = a // (2 ** {self.get_combo_operand_str(literal_operand)})"
        )
        self.c = self.a // (2 ** self.get_combo_operand(literal_operand))
        return self.pointer + 1

    def bxl(self, literal_operand: int):
        self.code.append(f"b = b ^ {literal_operand}")
        self.b = self.b ^ literal_operand
        return self.pointer + 1

    def bst(self, literal_operand: int):
        self.code.append(f"b = {self.get_combo_operand_str(literal_operand)} % 8")
        self.b = self.get_combo_operand(literal_operand) % 8
        return self.pointer + 1

    def jnz(self, literal_operand: int):
        if self.a == 0:
            self.code.append("print('result:', output)")
            return self.pointer + 1

        self.code.append("# Loop")
        return literal_operand // 2

    def bxc(self, _: int):
        self.code.append("b = b ^ c")
        self.b = self.b ^ self.c
        return self.pointer + 1

    def out(self, literal_operand: int):
        self.code.append(
            f"output.append({self.get_combo_operand_str(literal_operand)} % 8)"
        )
        self.output.append(self.get_combo_operand(literal_operand) % 8)
        return self.pointer + 1

    def get_combo_operand(self, literal_operand: int):
        if literal_operand == 7:
            raise Exception("Unexpected lit. operand 7")
        if literal_operand > 7:
            raise Exception(f"Unexpected lit. operand {literal_operand}")

        return {
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: self.a,
            5: self.b,
            6: self.c,
        }[literal_operand]

    def get_combo_operand_str(self, literal_operand: int):
        if literal_operand == 7:
            raise Exception("Unexpected lit. operand 7")
        if literal_operand > 7:
            raise Exception(f"Unexpected lit. operand {literal_operand}")

        return {
            0: "0",
            1: "1",
            2: "2",
            3: "3",
            4: "a",
            5: "b",
            6: "c",
        }[literal_operand]

    def run(self):
        self.code.append(
            f"a = {self.a}",
        )
        self.code.append("b = 0")
        self.code.append("c = 0")
        self.code.append("output = []")

        max_pointer = len(self.program)
        while self.pointer < max_pointer:
            (opcode, literal_operand) = self.program[self.pointer]

            ops = {
                0: self.adv,
                1: self.bxl,
                2: self.bst,
                3: self.jnz,
                4: self.bxc,
                5: self.out,
                6: self.bdv,
                7: self.cdv,
            }

            op = ops[opcode]

            self.pointer = op(literal_operand)
            # print(self)

        self.code.append("print(output)")
        # [print(line) for line in self.code]
        return self.output


# Reimplementation of the computer in python
def generated(initA: int):
    a = initA
    b = 0
    c = 0
    output = []

    while True:
        b = a % 8
        b = b ^ 3
        c = a // (2**b)
        b = b ^ c
        a = a // (2**3)
        b = b ^ 5
        output.append(b % 8)
        if a == 0:
            break

    return output


class Input(NamedTuple):
    a: int
    b: int
    c: int
    code: list[tuple[int, int]]
    raw_program: list[int]


class Solution(BaseSolution[Input]):
    def parseInput(self):
        (a, b, c) = [int(line.split(" ")[2]) for line in self.lines[:3]]
        raw_program = self.lines[4].split(" ")[1]
        code_chunks = [int(v) for v in raw_program.split(",")]
        code = [
            (code_chunks[i], code_chunks[i + 1]) for i in range(0, len(code_chunks), 2)
        ]

        return Input(a, b, c, code, code_chunks)

    @answer("4,6,3,5,6,3,5,2,1,0", "1,3,5,1,7,2,5,1,6")
    def part1(self):
        (a, b, c, code, _) = self.parsedInput
        res = Computer(a, b, c, code).run()
        return ",".join([str(i) for i in res])

    @answer(None, 236555997372013)
    def part2(self):
        """
        Observation: When converting a to octal, the same prefix in a gives
                     the same sufix in res.
        So the idea is to incrementally find the prefixes which match the
        expected results until find the ones giving it completely

        Also note that Computer(a, 0, 0, code).run() and generated(a) give the
        same result because my translation worked well
        """
        (_, _, _, code, raw_program) = self.parsedInput

        digits = [str(e) for e in range(8)]
        candidates = [""]
        answer = math.inf

        for _ in range(len(raw_program)):
            newCandidates = []
            for candidate in candidates:
                for d in digits:
                    a = int(candidate + d, 8)
                    # res = Computer(a, 0, 0, code).run()
                    res = generated(a)

                    if res == raw_program[-len(res) :]:
                        newCandidates.append(candidate + d)

                    if res == raw_program:
                        answer = min(answer, a)
            candidates = newCandidates

        return int(answer) if answer != math.inf else 0
