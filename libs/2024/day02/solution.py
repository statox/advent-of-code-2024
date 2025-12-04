from ...base import BaseSolution, answer


def isValidReport(report):
    sortedReport = sorted(report)
    if report != sortedReport and report != list(reversed(sortedReport)):
        # print('not sorted', report)
        return False

    diffs = [abs(report[i] - report[i + 1]) for i in range(len(report) - 1)]

    if max(diffs) > 3:
        # print('diff more than 3', report)
        return False

    return min(diffs) >= 1


class Solution(BaseSolution):
    @answer(2, 559)
    def part1(self):
        safe_reports = 0

        for report in [[int(n) for n in line.split()] for line in self.lines]:
            if isValidReport(report):
                safe_reports += 1

        return safe_reports

    @answer(4, 601)
    def part2(self):
        safe_reports = 0

        for report in [[int(n) for n in line.split()] for line in self.lines]:
            # print('report', report)
            if isValidReport(report):
                # print('  is valid, skip')
                safe_reports += 1
                continue

            for i in range(len(report)):
                smallerReport = list(report)
                del smallerReport[i]
                # print('  smaller report', smallerReport)

                if isValidReport(smallerReport):
                    # print('    is valid')
                    safe_reports += 1
                    break

        return safe_reports
