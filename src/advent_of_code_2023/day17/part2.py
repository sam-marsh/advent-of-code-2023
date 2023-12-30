from functools import lru_cache
from heapq import heapify, heappop, heappush

import numpy as np
from advent_of_code_2023.utils import read_input

LEFT = (0, -1)
RIGHT = (0, 1)
UP = (-1, 0)
DOWN = (1, 0)

def valid(data, i, j):
    return 0 <= i < len(data) and 0 <= j < len(data[0])

def diff(a, b):
    return a[0] - b[0], a[1] - b[1]
    
def solve(lines: list[str]) -> int:
    data = np.array([[int(x) for x in x.strip()] for x in lines])

    heap = [(0, (0, 0), None)] # cost, loc, dir
    heapify(heap)
    min_cost = {(0, 0): 0}
    visited = set()
    
    sol = np.inf
    while heap:
        cost, loc, dir = heappop(heap)
        if loc[0] == len(data) - 1 and loc[1] == len(data[0]) - 1:
            sol = cost
            break
        if (loc, dir) in visited: continue
        visited.add((loc, dir))
        for next_dir in [LEFT, RIGHT, UP, DOWN]:
            if dir is not None and next_dir[0] == -dir[0] and next_dir[1] == -dir[1]: # 180 turn
                continue
            if dir is not None and next_dir[0] == dir[0] and next_dir[1] == dir[1]:
                continue
            next_cost = cost
            for i in range(10):
                next_pos = (loc[0] + (i + 1) * next_dir[0], loc[1] + (i + 1) * next_dir[1])
                if not valid(data, *next_pos):
                    continue
                next_cost += data[*next_pos]
                if i < 3:
                    continue
                next_node = (next_pos, next_dir)
                if next_cost < min_cost.get(next_node, np.inf):
                    min_cost[next_node] = next_cost
                    heappush(heap, (next_cost, next_pos, next_dir))

    return sol


print(solve(read_input(day=17)))