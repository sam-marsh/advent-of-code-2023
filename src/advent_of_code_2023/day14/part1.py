import numpy as np
from advent_of_code_2023.utils import read_input


def solve(lines: list[str]):
    grid = np.array([list(line.strip()) for line in lines], dtype=str)
    grid = grid.T
    lines = [''.join(x) for x in grid]
    remapped = np.array([
        list('#'.join(''.join(sorted(part, key=lambda x: 0 if x == 'O' else 1)) for part in line.split('#')))
        for line in lines
    ], dtype=str).T
    s = 0
    for i in range(len(remapped)):
        for j in range(len(remapped)):
            if remapped[i, j] == 'O':
                s += (len(remapped) - i)
    print(s)

    print(remapped)

if __name__ == "__main__":
    print(solve(read_input(day=14)))