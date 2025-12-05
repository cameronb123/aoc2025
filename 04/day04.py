import copy
from pathlib import Path


def get_accessible_points(grid: list[list[str]]) -> list[tuple[int, int]]:
    accessible = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            point = grid[i][j]
            if point != "@":
                continue

            adjacent = 0
            for m in (-1, 0, 1):
                for n in (-1, 0, 1):
                    if 0 <= i + m < len(grid) and 0 <= j + n < len(grid[0]) and (m != 0 or n != 0):
                        if grid[i + m][j + n] == "@":
                            adjacent += 1

            if adjacent < 4:
                accessible.append((i, j))

    return accessible


def solution(file: Path) -> tuple[int, int]:
    with open(file) as f:
        grid_raw = f.read().split("\n")

    grid = [list(row) for row in grid_raw]
    new_grid = copy.deepcopy(grid)

    total_accessible_points = 0

    accessible_points = get_accessible_points(new_grid)
    while len(accessible_points) > 0:
        # Remove accessible points from the grid
        for point in accessible_points:
            i, j = point
            new_grid[i][j] = "."
            total_accessible_points += 1
        accessible_points = get_accessible_points(new_grid)

    return len(get_accessible_points(grid)), total_accessible_points


if __name__ == "__main__":
    test_file = Path(__file__).parent / "test.txt"
    input_file = Path(__file__).parent / "input.txt"
    test_1, test_2 = solution(test_file)
    assert test_1 == 13
    assert test_2 == 43
    part_1, part_2 = solution(input_file)
    print("Part 1:", part_1)
    print("Part 2:", part_2)
