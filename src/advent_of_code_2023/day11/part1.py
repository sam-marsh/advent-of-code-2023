from itertools import combinations
from matplotlib import pyplot as plt
import networkx as nx
import numpy as np
from advent_of_code_2023.utils import read_input
from bisect import bisect

def solve(lines: list[str]) -> int:
    lines = np.array([list(line.strip()) for line in lines])
    n = len(lines)
    m = len(lines[0])

    empty_rows = [i for i in range(n) if np.all(lines[i] == '.')]
    empty_columns = [j for j in range(m) if np.all(lines[:, j] == '.')]

    galaxies = set()
    real_i = 0
    for i in range(n):
        if i in empty_rows:
            real_i += 1
        real_j = 0
        for j in range(m):
            if j in empty_columns:
                real_j += 1
            if lines[i, j] == '#':
                galaxies.add((real_i, real_j))
            real_j += 1
        real_i += 1

    total = 0
    for g1, g2 in combinations(galaxies, 2):
        total += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
    
    return total

if __name__ == "__main__":
    print(solve(read_input(day=11)))