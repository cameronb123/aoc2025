from pathlib import Path


def solution(file: Path) -> tuple[int, int]:
    with open(file) as f:
        input_values = f.read().split("\n")

    sum_part_1 = 0
    sum_part_2 = 0

    for bank in input_values:
        bank_size = len(bank)
        max_joltages_part_1 = {i: 0 for i in range(1, 3)}
        max_joltages_part_2 = {i: 0 for i in range(1, 13)}
        for idx, battery in enumerate(bank):
            battery_int = int(battery)
            cont_1 = True
            cont_2 = True
            for i in range(1, 3):
                if cont_1 and battery_int > max_joltages_part_1[i] and bank_size - 2 + i > idx >= i - 1:
                    max_joltages_part_1[i] = battery_int
                    for j in range(i+1, 3):
                        max_joltages_part_1[j] = 0
                    cont_1 = False

            for i in range(1, 13):
                if cont_2 and battery_int > max_joltages_part_2[i] and bank_size - 12 + i > idx >= i - 1:
                    max_joltages_part_2[i] = battery_int
                    for j in range(i+1, 13):
                        max_joltages_part_2[j] = 0
                    cont_2 = False

        sum_part_1 += int("".join(str(max_joltages_part_1[i]) for i in range(1, 3)))
        sum_part_2 += int("".join(str(max_joltages_part_2[i]) for i in range(1, 13)))

    return sum_part_1, sum_part_2


if __name__ == "__main__":
    test_file = Path(__file__).parent / "test.txt"
    input_file = Path(__file__).parent / "input.txt"
    test_1, test_2 = solution(test_file)
    assert test_1 == 357
    assert test_2 == 3121910778619
    part_1, part_2 = solution(input_file)
    print("Part 1:", part_1)
    print("Part 2:", part_2)
