from matplotlib import pyplot as plt
import numpy as np
from advent_of_code_2023.utils import read_input


def solve(lines: list[str], cycles: int):
    # for line in lines:
    #     print(len(line.strip()))
    grid = np.array([list(line.strip()) for line in lines], dtype=str)
    cyclestart = None
    
    ok = []
    for j in range(cycles):
        for i in range(4):
            grid = np.rot90(grid, -i)
            lines = [''.join(x) for x in grid.T]
            grid = np.array([
                list('#'.join(''.join(sorted(part, key=lambda x: 0 if x == 'O' else 1)) for part in line.split('#')))
                for line in lines
            ], dtype=str).T
            grid = np.rot90(grid, i)
        flat = ''.join(''.join(x) for line in grid for x in line)
        if flat in ok:
            found = ok.index(flat)
            cyclestart = found
            print(cyclestart, j)
            break
        ok.append(flat)
    
    left = cycles - len(ok) - 1
    period = len(ok) - cyclestart
    final = ok[cyclestart + (left % period)]

    grid = np.array(list(final), dtype=str).reshape((len(lines), -1))
    print(grid)

    s = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i, j] == 'O':
                s += (len(grid) - i)

    return s

if __name__ == "__main__":
    print(solve(read_input(day=14), 1000000000))