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

    # Used some optimizations to speed up the code (some of them probably aren't useful/are plain out bad)
    # - Avoided calling len(disk) as much as possible (looks like it iterates through the whole list)
    # - Keep track of where is the right pointer when splitting the empty slot into moved word+smaller empty slot
    #   and when packing contiguous empty slots
    # - When moving a file to empty slot, modify the empty slot tuple instead of removing/adding the tuple
    @answer(2858, 6511178035564)
    def part2(self):
        # Transform the parsed input into a list of tuples representing the length of the file and its id
        # or the length of the empty slot and "."
        disk: list[tuple[int, str]] = []
        for i, length in enumerate(self.parsedInput):
            if length == 0:
                continue

            if i % 2 == 0:
                disk.append((length, str(int(i / 2))))
            else:
                disk.append((length, "."))

        diskLen = len(disk)
        right = diskLen - 1
        while right > 0:
            # Search the next file id to move
            while disk[right][1] == ".":
                right -= 1

            # Search an available slot starting from the begining of the disk
            left = 0
            while left < right and (
                disk[left][1] != "." or disk[left][0] < disk[right][0]
            ):
                left += 1

            # No available slot for the file id, move to the next one
            if left >= right:
                right -= 1
                continue

            # Remaining space in the slot after we'll have moved the file
            diff = disk[left][0] - disk[right][0]

            # Replace the current file by empty slots
            vright = disk[right][1]
            lright = disk[right][0]
            disk[right] = (disk[right][0], ".")

            # Move the file id to the empty slot
            disk[left] = (lright, vright)
            if diff > 0:
                # If the slot is bigger than the file id, insert a new empty spot after the moved file
                disk.insert(left + 1, (diff, "."))
                diskLen += 1
                right += 1

            # The operations can create several continuous empty slots, packs them
            # Here we are tempted of not removing the empty slot of length 0 to avoid mutating the list
            # But that makes much more slots to iterate over and so would be slower
            while right < diskLen - 2 and disk[right + 1][1] == ".":
                disk[right] = (disk[right + 1][0] + disk[right][0], ".")
                disk.pop(right + 1)
                diskLen -= 1

            while right > 0 and disk[right - 1][1] == ".":
                disk[right - 1] = (disk[right - 1][0] + disk[right][0], ".")
                disk.pop(right)
                right -= 1
                diskLen -= 1

        # Moves are all done, compute the result
        total = 0
        i = 0
        for length, val in disk:
            if val == ".":
                i += length
                continue

            for _ in range(1, length + 1):
                total += i * int(val)
                i += 1

        return total
