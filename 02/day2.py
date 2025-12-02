import math
from pathlib import Path


def solution(file: Path) -> tuple[int, int]:
    with open(file) as f:
        input_values = f.read().split("\n")

    ranges = []
    for input_value in input_values:
        ranges.extend(input_value.split(","))

    invalid_sum = 0
    all_invalid_ids = set()

    for r in ranges:
        start, end = r.split("-")
        start, end = int(start), int(end)
        for id in range(start, end+1):
            id_string = str(id)
            for j in range(1, math.ceil(len(id_string) / 2) + 1):
                for k in range(2, math.ceil(len(id_string) / j) + 1):
                    if id_string[:j] * k == id_string:
                        all_invalid_ids.add(id)
                        if k == 2:
                            invalid_sum += id
                        break

    return invalid_sum, sum(all_invalid_ids)


if __name__ == "__main__":
    test_file = Path(__file__).parent / "test.txt"
    input_file = Path(__file__).parent / "input.txt"
    test_1, test_2 = solution(test_file)
    assert test_1 == 1227775554
    assert test_2 == 4174379265
    part_1, part_2 = solution(input_file)
    print("Part 1:", part_1)
    print("Part 2:", part_2)
