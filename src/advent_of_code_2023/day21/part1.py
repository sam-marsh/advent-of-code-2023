from functools import lru_cache
import numpy as np
from advent_of_code_2023.utils import read_input

def valid(data, i, j):
    return 0 <= i < len(data) and 0 <= j < len(data[0]) and data[i, j] != '#'

def solve(lines: list[str]) -> int:
    data = np.array([list(x.strip()) for x in lines])
    first = tuple(np.array(np.where(data == 'S')).flatten())

    @lru_cache(maxsize=None)
    def n_steps_from(curr, n):
        if n == 0:
            return set([curr])
        result = set()
        for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            neighbour = curr[0] + di, curr[1] + dj
            if not valid(data, *neighbour):
                continue
            result.update(n_steps_from(neighbour, n - 1))
        return result
        
    # print(n_steps_from(first, 0))
    # print(n_steps_from(first, 1))
    # print(len(n_steps_from(first, 64)))

    return len(n_steps_from(first, 64))

print(solve(read_input(day=21)))