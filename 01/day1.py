import math
from pathlib import Path


def solution(file: Path) -> tuple[int, int]:
    with open(file) as f:
        input_values = f.read().split("\n")

    current = 50
    zero_count = 0
    zero_pass_count = 0

    for rotation in input_values:
        direction = rotation[0]
        distance = int(rotation[1:])
        # print(f"current: {current}, rotation: {rotation}")

        n_passes = math.floor(distance / 100)
        remainder = distance % 100

        if direction == "L":
            if 0 < current <= remainder:
                n_passes += 1
            zero_pass_count += n_passes
            current = (current - distance) % 100
            # zero_pass_count += math.floor((current - distance) / 100)
        else:
            if current >= 100 - remainder:
                n_passes += 1
            zero_pass_count += n_passes
            current = (current + distance) % 100
            # zero_pass_count += math.floor((current + distance) / 100)

        if current == 0:
            zero_count += 1

        # print(f"zero_pass_count: {zero_pass_count}, zero_count: {zero_count}")

    return zero_count, zero_pass_count


if __name__ == "__main__":
    test_file = Path(__file__).parent / "test.txt"
    input_file = Path(__file__).parent / "input.txt"
    test_1, test_2 = solution(test_file)
    assert test_1 == 3
    assert test_2 == 6
    part_1, part_2 = solution(input_file)
    print("Part 1:", part_1)
    print("Part 2:", part_2)
