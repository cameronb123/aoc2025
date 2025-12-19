from pathlib import Path


def solution(file: Path) -> tuple[int, int]:
    with open(file) as f:
        input_values = f.read().split("\n")

    fresh_ranges = []
    fresh_count = 0

    line = input_values.pop(0)
    while line != "":
        a, b = line.split("-")
        fresh_ranges.append((int(a), int(b)))
        line = input_values.pop(0)

    fresh_ranges.sort(key=lambda x: x[0])
    for line in input_values:
        ingredient = int(line)
        for fresh_range in fresh_ranges:
            if fresh_range[0] <= ingredient <= fresh_range[1]:
                fresh_count += 1
                break

    total_ranges = []
    i = 0
    while i < len(fresh_ranges):
        curr_range = fresh_ranges[i]
        # Consider the next range and whether it overlaps the current one
        i += 1
        next_range = fresh_ranges[i]
        while next_range[0] <= curr_range[1]:
            curr_range = (curr_range[0], max(curr_range[1], next_range[1]))
            i += 1
            if i >= len(fresh_ranges):
                break
            next_range = fresh_ranges[i]
        total_ranges.append(curr_range)

    total_fresh = 0
    for r in total_ranges:
        total_fresh += r[1] - r[0] + 1

    return fresh_count, total_fresh


if __name__ == "__main__":
    test_file = Path(__file__).parent / "test.txt"
    input_file = Path(__file__).parent / "input.txt"
    test_1, test_2 = solution(test_file)
    assert test_1 == 3
    assert test_2 == 14
    part_1, part_2 = solution(input_file)
    print("Part 1:", part_1)
    print("Part 2:", part_2)
