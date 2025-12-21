from pathlib import Path


def solution(file: Path, n: int) -> tuple[int, int]:
    with open(file) as f:
        input_values = [
            tuple(int(d) for d in coords.split(","))
            for coords in f.read().split("\n")
            if coords
        ]

    distances: dict[tuple[int, int], int] = {}
    circuits: list[set] = []
    size = 1

    # Get the distances between all pairs
    for i in range(len(input_values)):
        coord = input_values[i]
        for j in range(i + 1, len(input_values)):
            comparison_coord = input_values[j]
            distance = sum(abs(coord[k] - comparison_coord[k]) ** 2 for k in range(3))
            distances[(i, j)] = distance
        circuits.append({i})

    i = 1
    a, b = 0, 0
    # Keep connecting until all the circuits are done
    while len(circuits) > 1:
        # Get the minimum distances
        pair = min(distances.items(), key=lambda x: x[1])
        distances.pop(pair[0])
        a, b = pair[0]

        # Check each circuit to find a and b
        a_circuit, b_circuit = set({}), set({})
        for circuit in circuits:
            if a in circuit:
                a_circuit = circuit
            if b in circuit:
                b_circuit = circuit
        # Add a or b to the correct circuit, or combine the two circuits
        if a_circuit != b_circuit:
            combined_circuit = a_circuit.union(b_circuit)
            circuits.remove(a_circuit)
            circuits.remove(b_circuit)
            circuits.append(combined_circuit)

        # Get the sizes after n iterations
        if i == n:
            circuit_lengths = [len(circuit) for circuit in circuits]
            circuit_lengths.sort(reverse=True)
            for j in circuit_lengths[:3]:
                size *= j
        i += 1

    a_coords, b_coords = input_values[a], input_values[b]

    return size, a_coords[0] * b_coords[0]


if __name__ == "__main__":
    test_file = Path(__file__).parent / "test.txt"
    input_file = Path(__file__).parent / "input.txt"
    test_1, test_2 = solution(test_file, 10)
    assert test_1 == 40
    assert test_2 == 25272
    part_1, part_2 = solution(input_file, 1000)
    print("Part 1:", part_1)
    print("Part 2:", part_2)
