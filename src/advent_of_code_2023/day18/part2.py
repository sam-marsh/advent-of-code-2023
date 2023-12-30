from matplotlib import pyplot as plt
import numpy as np
from advent_of_code_2023.utils import read_input

dir_map = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1)
}

def hex_to_data(hex):
    map = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}
    return (dir_map[map[hex[-1]]], int(hex[1:-1], 16))


def solve(lines: list[str]) -> int:
    data = []
    for line in lines:
        split = line.strip().split(' ')
        # data.append((dir_map[split[0]], int(split[1])))
        data.append(hex_to_data(split[2][1:-1]))                    

    # data = [(dir_map['U'], 2), (dir_map['R'], 1), (dir_map['D'], 1), (dir_map['R'], 1),(dir_map['D'], 1),(dir_map['L'], 2)]

    fig, ax = plt.subplots()
    ##
    ###
    ###
    # (0, 0), (0, 3), (2, 3), (2, 2), (3, 2), (3, 0), (0, 0)

    coords = [(0, 0)]
    area = 0
    perimeter = 0
    for dir, num in data:
        x = coords[-1]
        y = (x[0] + num * dir[0], x[1] + num * dir[1])
        coords.append(y)
        perimeter += num
        area += x[0] * y[1] - x[1] * y[0]

    # for (x, y), (xp, yp) in zip(coords, coords[1:]):
    #     ax.plot([x, xp], [y, yp], marker='o', color='r')

    return abs(area // 2) + perimeter // 2  + 1

print(solve(read_input(day=18)))