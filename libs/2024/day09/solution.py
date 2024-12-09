from ...base import BaseSolution, answer


class Solution(BaseSolution[list[int]]):
    def parseInput(self):
        return [int(v) for v in list(self.lines[0])]

    @answer(1928, 6471961544878)
    def part1(self):
        disk: list[str] = []
        for i, length in enumerate(self.parsedInput):
            if i % 2 == 0:
                disk += [str(int(i / 2))] * length
            else:
                disk += ["."] * length

        # print(disk)
        left = 0
        right = len(disk) - 1
        while right > left:
            # print(f"left {left} ({disk[left]}) right {right} ({disk[right]})")
            while disk[left] != ".":
                left += 1
            while disk[right] == ".":
                right -= 1

            # print(f"    left {left} ({disk[left]}) right {right} ({disk[right]})")

            if right < left:
                # print("STOP")
                break

            disk[left] = disk[right]
            disk[right] = "."

            # print("".join(disk))
        # print(disk)
        total = 0
        for i, fileId in enumerate(disk):
            if fileId == ".":
                break
            total += i * int(fileId)
        return total

    # 113063514094 too low
    # 113063506936 too low
    @answer(2858, 6511178035564)
    def part2(self):
        disk: list[tuple[int, str]] = []
        for i, length in enumerate(self.parsedInput):
            if length == 0:
                continue

            if i % 2 == 0:
                disk.append((length, str(int(i / 2))))
            else:
                disk.append((length, "."))

        right = len(disk) - 1

        seen: set[str] = set()
        while right > 0:
            # print(f"right {right} ({disk[right]})")
            right = len(disk) - 1
            while disk[right][1] == "." or disk[right][1] in seen:
                # print("  skip, move right")
                right -= 1

            left = 0
            while left < right and (
                disk[left][1] != "." or disk[left][0] < disk[right][0]
            ):
                left += 1
            # print(f"    left {left} ({disk[left]}) right {right} ({disk[right]})")

            seen.add(disk[right][1])
            if left >= right:
                # print("No place found")
                right -= 1
                continue

            diff = disk[left][0] - disk[right][0]

            # print(f"diff {diff}")

            # print(f"move {disk[right]} from {right} to {left}")
            vright = disk[right][1]
            lright = disk[right][0]
            disk[right] = (disk[right][0], ".")

            disk.pop(left)
            disk.insert(left, (lright, vright))
            if diff > 0:
                disk.insert(left + 1, (diff, "."))

            i = 1
            while i < len(disk):
                chunk = disk[i]
                if chunk[1] == "." and disk[i - 1][1] == ".":
                    disk[i] = (disk[i - 1][0] + disk[i][0], ".")
                    disk.pop(i - 1)
                else:
                    i += 1

            # print(disk)
            # printDisk(disk)

        total = 0
        i = 0
        for length, val in disk:
            if val == ".":
                i += length
                continue

            for j in range(1, length + 1):
                total += i * int(val)
                i += 1

        return total
