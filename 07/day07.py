from pathlib import Path


def solution(file: Path) -> tuple[int, int]:
    with open(file) as f:
        input_values = f.read().split("\n")

    split_count = 0
    timelines_count = 0
    beam_locs = {}
    beam_timelines = {}
    max_len = len(input_values[0])
    max_row = len(input_values)

    for i, row in enumerate(input_values):
        if i == 0:
            beam_locs[i] = {input_values[0].index("S")}
            beam_timelines[i] = {input_values[0].index("S"): 1}
        else:
            this_beam_locs = set()
            for beam_loc in beam_locs[i - 1]:
                if row[beam_loc] == "^":
                    # Get the current beam locations after splitting
                    if beam_loc - 1 >= 0:
                        this_beam_locs.add(beam_loc - 1)
                    if beam_loc + 1 < max_len:
                        this_beam_locs.add(beam_loc + 1)
                    split_count += 1
                else:
                    this_beam_locs.add(beam_loc)

            this_beam_timelines: dict[int, int] = {}
            for beam_timeline, count in beam_timelines[i - 1].items():
                if row[beam_timeline] == "^":
                    if beam_timeline - 1 >= 0:
                        this_beam_timelines[beam_timeline - 1] = (
                            this_beam_timelines.get(beam_timeline - 1, 0) + count
                        )
                    if beam_timeline + 1 < max_len:
                        this_beam_timelines[beam_timeline + 1] = (
                            this_beam_timelines.get(beam_timeline + 1, 0) + count
                        )
                else:
                    this_beam_timelines[beam_timeline] = (
                        this_beam_timelines.get(beam_timeline, 0) + count
                    )
            beam_locs[i] = this_beam_locs
            beam_timelines[i] = this_beam_timelines

    for count in beam_timelines[max_row - 1].values():
        timelines_count += count

    return split_count, timelines_count


if __name__ == "__main__":
    test_file = Path(__file__).parent / "test.txt"
    input_file = Path(__file__).parent / "input.txt"
    test_1, test_2 = solution(test_file)
    assert test_1 == 21
    assert test_2 == 40
    part_1, part_2 = solution(input_file)
    print("Part 1:", part_1)
    print("Part 2:", part_2)
